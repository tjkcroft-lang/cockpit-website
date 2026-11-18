#!/usr/bin/env python3
"""COCKPIT static site regression checks (stdlib only). No network calls."""
import json
import re
import subprocess
import sys
import tempfile
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote

ROOT = Path(__file__).resolve().parents[1]
PAGES = ["index.html", "members-club.html", "mens-underwear-guide.html", "privacy.html"]
ERRORS = []


class Links(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.images = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])
        if tag in ("img", "audio", "source") and a.get("src"):
            self.images.append(a["src"])


def require(ok, message):
    if not ok:
        ERRORS.append(message)


def read(path):
    p = ROOT / path
    require(p.is_file(), f"Missing file: {path}")
    return p.read_text(encoding="utf-8") if p.is_file() else ""


def internal_resource(url, filename):
    if url.startswith(("mailto:", "tel:", "javascript:", "data:")):
        return None
    parsed = urlparse(url)
    if parsed.netloc and parsed.netloc not in ("cockpitau.com", "www.cockpitau.com"):
        return None
    target_path = unquote(parsed.path)
    if not target_path:
        target_path = filename
    elif target_path == "/":
        target_path = "index.html"
    elif target_path.startswith("/"):
        target_path = target_path.lstrip("/")
    if target_path.endswith("/"):
        target_path += "index.html"
    return target_path, parsed.fragment


def main():
    page_info = {}
    titles = []
    for filename in PAGES:
        html = read(filename)
        if not html:
            continue
        parser = Links()
        parser.feed(html)
        page_info[filename] = parser
        t = re.search(r"<title>(.*?)</title>", html, re.S | re.I)
        require(t is not None, f"{filename}: missing title")
        if t:
            titles.append(t.group(1))
            require(len(t.group(1).strip()) > 15, f"{filename}: title too short")
        require(re.search(r'<meta\s+name="description"\s+content="[^"]+"', html, re.I) is not None, f"{filename}: missing description")
        canonical = re.search(r'<link\s+rel="canonical"\s+href="([^"]+)"', html, re.I)
        expected = "https://cockpitau.com/" + ("" if filename == "index.html" else filename)
        require(canonical is not None and canonical.group(1) == expected, f"{filename}: wrong canonical URL")
        require(html.lower().count("<h1") == 1, f"{filename}: expected exactly one H1")
        require("<main" in html and "</main>" in html, f"{filename}: main landmark missing")
        require("<footer" in html and "</footer>" in html, f"{filename}: footer missing")
        for match in re.finditer(r"<script\b([^>]*)>(.*?)</script>", html, re.I | re.S):
            attrs, text = match.groups()
            if "application/ld+json" in attrs:
                try:
                    json.loads(text)
                except json.JSONDecodeError as err:
                    ERRORS.append(f"{filename}: invalid structured data: {err}")
                continue
            if text.strip():
                with tempfile.NamedTemporaryFile(suffix=".js", mode="w", encoding="utf-8", delete=True) as f:
                    f.write(text)
                    f.flush()
                    result = subprocess.run(["node", "--check", f.name], capture_output=True, text=True)
                    require(result.returncode == 0, f"{filename}: JavaScript syntax error: {result.stderr.strip()[:350]}")

    require(len(titles) == len(set(titles)), "Page titles are not unique")
    for filename, parser in page_info.items():
        for ref in parser.links + parser.images:
            target = internal_resource(ref, filename)
            if target is None:
                continue
            path, fragment = target
            require((ROOT / path).is_file(), f"{filename}: broken local link or image: {ref}")
            if fragment and path in page_info:
                require(fragment in page_info[path].ids, f"{filename}: missing anchor target: {ref}")

    home = read("index.html")
    members = read("members-club.html")
    require("BALLS<br>DEEP IN<br><span>COMFORT.</span>" in home, "Approved homepage slogan changed")
    require("GOOD<br>UNDERWEAR" in home, "Approved homepage section changed")
    require("id=\"club-signup-form\"" in home, "Signup form removed")
    require("id=\"mobile-navigation\"" in home, "Mobile menu removed")
    require("cockpit-rooster.mp3" in home, "Rooster audio reference removed")
    require("THE FRIST DROP IS COMING" in home, "Approved banner text changed")
    require("FREE SHIPPING ON ORDERS OVER $100" in home, "Approved shipping banner changed")
    require("KEEP</span><span>YOUR</span><span class=\"red\">PANTS ON." in members, "Members Club slogan changed")
    require('href="index.html?join=1"' in members, "Members Club signup route missing")
    require('name="marketing_consent"' in home, "Signup consent field missing")
    require("privacy.html" in home, "Privacy link missing")
    robots = read("robots.txt")
    sitemap = read("sitemap.xml")
    require("Sitemap: https://cockpitau.com/sitemap.xml" in robots, "robots.txt missing sitemap")
    for page in PAGES:
        url = "https://cockpitau.com/" + ("" if page == "index.html" else page)
        require(f"<loc>{url}</loc>" in sitemap, f"sitemap missing {page}")

    if ERRORS:
        print("FAILED — " + str(len(ERRORS)) + " website checks")
        for error in ERRORS:
            print("  - " + error)
        return 1
    print("PASS — HTML metadata, JS syntax, approved slogans, signup links, site links, sitemap and privacy checks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
