# COCKPIT — Australia-first SEO & first-drop launch plan
Updated: 18 November 2026

## The goal
Build an Australian audience searching for men's underwear and men's undies, convert that audience to COCKPIT Members Club registrations while the store is pre-launch, and convert an owned email audience into profitable first-drop orders once products and checkout exist. Expand globally only after the Australian product and fulfilment experience is validated.

**Preserve the brand:** Do not replace “BALLS DEEP IN COMFORT.”, “KEEP YOUR PANTS ON.”, “COCKPIT IS COMING. KEEP YOUR PANTS ON.”, “GOOD UNDERWEAR. BAD ATTITUDE.” or other approved text, art, links, colours or responsive layouts without explicit approval.

**Reality check:** No legitimate SEO work can guarantee first position for broad phrases like “men's underwear”. The site is pre-launch, and high-ranking retail competitors already have catalogues, reviews, backlinks and years of authority. Technical SEO enables discovery, not guaranteed rankings.

## What has been implemented in GitHub
- Keyword-relevant unique homepage and Members Club page titles and meta descriptions.
- Canonical URLs, Open Graph / Twitter sharing metadata, and schema.org Organization, WebSite and WebPage / BreadcrumbList data where appropriate.
- `robots.txt` and `sitemap.xml` with actual published pages.
- Helpful content on the homepage and a standalone `mens-underwear-guide.html`, covering styles, sizing, fit and fabric considerations without inventing COCKPIT product specifications.
- A `privacy.html` launch signup information page, visible from form and footer.
- Internal links between homepage, Members Club, fit guide and privacy page.
- The user-approved slogans, homepage layout, Members Club hero and signup form retained.

## Critical tasks that still require an account owner
1. **Verify the signup backend**: confirm `hello@cockpitau.com` works, approve FormSubmit's email activation message, and perform a consented test signup end-to-end. A form submitting successfully is not the same as a deliverable marketing subscriber.
2. **Choose an email marketing platform** (for example a service that supports Australian consent and unsubscribe rules). The current FormSubmit email relay is not a full subscriber database or email campaign service. Migrate to a verified ESP / CRM before paid promotion.
3. **Google Search Console**: add the Domain property `cockpitau.com`, complete DNS TXT ownership verification, submit `https://cockpitau.com/sitemap.xml`, then inspect/request indexing for homepage, Members Club and underwear guide. DNS verification token must come from Google; never invent it.
4. **Google Analytics 4**: create a property and share the measurement ID only when ready. Implement and verify events `view_item_list` when products exist, `club_form_start`, `club_signup_success`, `click_join_club`, and future `purchase`. Count actual accepted signups, not just button clicks.
5. **Meta tracking**: configure Pixel / Conversions API with consent controls before deploying paid conversion campaigns. Ensure lead confirmation represents accepted registrations.
6. **Product specifications**: confirm exact materials, style, sizing, stock, colours, price, shipping regions and consumer-return terms before product pages, Merchant Center, Product schema or advertisements claim them.
7. **Asset independence**: some existing live visuals/audio are still hosted from the public Cockpit-Preview repository; copy original binary assets to the production repository when upload support is available and update links without altering design.
8. **Performance audit**: run real mobile Lighthouse / PageSpeed Insights and fix measured Core Web Vitals issues; current tool access cannot prove the site's live browser scores.

## Search keywords and intent
| Priority | Search intent | Target |
| --- | --- | --- |
| Immediate | COCKPIT underwear, COCKPIT men's underwear, COCKPIT Members Club | Homepage / Members Club |
| Immediate | men's underwear Australia, mens undies Australia | Homepage + meaningful category wording |
| Build authority | choosing men's underwear, trunks vs boxer briefs, comfortable fit | Men's underwear guide and future helpful articles |
| After launch | premium men's underwear Australia, men's trunks Australia, high quality boxer briefs | Verified product and collection pages |
| Longer term | men's underwear, luxury underwear, global shipping underwear | Quality product experience + earned coverage + international logistics |

Don't create doorway pages or invent reviews, pricing, products, performance claims or stock. Use natural language and real search intents.

## 4-stage organic and social launch sequence (schedule relative to confirmed launch date)
### Stage 1: Build anticipation
- Publish brand-first short videos: original rooster mascot/audio; show packaging silhouette, product textures only if real footage; “COCKPIT IS COMING. KEEP YOUR PANTS ON.”
- Content pillars: comfort/fit education, founder/product-making story, rooster personality, first-drop previews, community feedback.
- Link in every social bio to the Members Club with trackable campaign parameters.
- Encourage signups by email only after the signup service is validated.

### Stage 2: Earn attention
- Approach Australian men's lifestyle, fashion, fitness and humour creators with an honest early look once actual samples exist.
- Ask for real opinions and licensed user-generated material, not fake testimonials or forced positive reviews.
- Pitch real Australian brand-founder and product-design stories to relevant publishers and podcasts. Seek earned links from genuine mentions, not paid link networks.
- Use non-spammy audience polls on cuts, colours or packing preferences; do not imply products are already in stock.

### Stage 3: The countdown
- Once a real release date is confirmed, announce it consistently on site and social. Only then add a countdown.
- Send consented subscribers a confirmed launch reminder and a “tomorrow” reminder. If genuine early access is offered, ensure it is technically honoured and inventory is sufficient.
- Prepare checkout, payment methods, delivery estimates, returns pages, email confirmations and support response process before switching to open-orders language.

### Stage 4: The first drop and beyond
- Launch product/collection pages with accurate price, availability, fabrics, sizing, images and policies; add valid Product/Offer structured data and Google Merchant Center feed.
- Run launch email to opted-in contacts with working unsubscribe. Use owned short clips, creator assets and clear calls to action.
- Publish buyer-appropriate size and care guides and real post-purchase reviews when received and permission is granted.
- Monitor checkout conversion, refund/return rate, order contribution margin and new customer acquisition cost weekly.

## Paid traffic — plan only, no spending approved
- **Meta / Instagram & TikTok:** test 3 original angles: rooster humour, fit and comfort education, and transparent first-drop development. Optimize first for verified qualified leads, later for purchases once checkout exists.
- **Google Search:** prioritise branded terms and specific high-intent product terms only when a product page exists and user approves budget; broad generic “men's underwear” clicks may be expensive without a store.
- **Retargeting:** only after consent, conversion tracking and platform configuration are in place.
- Calculate break-even cost per acquired purchaser as **order revenue − product cost − pick/pack − shipping subsidy − payment fees − returns allowance − required profit contribution**; do not invent a CPA target without the real unit economics.
- Do not activate campaigns or make charges without explicit launch approval.

## Weekly dashboard
- Search Console: impressions, indexed URLs, CTR, average position **by actual query** and Australia vs other markets.
- GA4: acquisition channel, engagement, visits to Members Club, qualified signup rate and verified successful signups.
- ESP: new confirmed contacts, unsubscribes, open/click rates, launch revenue per recipient (when available).
- After launch: add-to-cart rate, checkout completion, purchase conversion rate, AOV, gross margin, contribution margin, CAC, returns and repeat purchase rate.
- Choose a baseline for every metric before publishing targets. Review fortnightly pre-launch and weekly at launch.

## Compliance and trust
- Australian marketing email/SMS rules require consent, sender identification and functional unsubscribe; see Australian Communications and Media Authority (ACMA): https://www.acma.gov.au/avoid-sending-spam
- Show accurate collection/use/privacy details and make contact and correction requests possible. Refer to the Office of the Australian Information Commissioner: https://www.oaic.gov.au/privacy/australian-privacy-principles/australian-privacy-principles-guidelines
- Avoid implying the underwear is “Australian-made”, medically beneficial, certified, environmentally superior or independently reviewed unless those facts are independently supported.
- Preserve the currently approved “FREE SHIPPING ON ORDERS OVER $100” banner; confirm terms/operational feasibility before launch.

## Trusted SEO guidance
- https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap
- https://developers.google.com/search/docs/specialty/ecommerce/how-to-launch-an-ecommerce-website
- https://developers.google.com/search/docs/specialty/ecommerce/help-google-understand-your-ecommerce-site-structure
