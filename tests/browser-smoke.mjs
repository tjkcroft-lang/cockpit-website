import assert from 'node:assert/strict';
import { chromium } from 'playwright';

const origin='http://127.0.0.1:8765/';
const browser=await chromium.launch({headless:true,args:['--no-sandbox']});
const fail=[];
const requiredImage=async(page,selector)=>{
  await page.locator(selector).first().waitFor({state:'attached',timeout:15000});
  const ok=await page.locator(selector).first().evaluate(async(img)=>{
    if(!img.complete){await new Promise(resolve=>{img.addEventListener('load',resolve,{once:true});img.addEventListener('error',resolve,{once:true});setTimeout(resolve,10000)})}
    return img.complete&&img.naturalWidth>0;
  });
  assert.ok(ok,selector+' did not load');
};

async function checkViewport(name,width,height,isMobile) {
  const context=await browser.newContext({viewport:{width,height},deviceScaleFactor:1,isMobile,hasTouch:isMobile});
  const page=await context.newPage();
  page.on('pageerror',e=>fail.push(name+': uncaught page error: '+e.message));
  const response=await page.goto(origin,{waitUntil:'domcontentloaded',timeout:20000});
  assert.equal(response.status(),200,name+': homepage unavailable');
  await requiredImage(page,'.nav .brand img');
  await requiredImage(page,'.nav .rooster-button img');
  await requiredImage(page,'.club-popup-art');
  assert.equal(await page.locator('#club-signup-form').count(),1,name+': missing signup form');
  await page.screenshot({path:'screenshots/'+name+'-home.png',fullPage:true});
  const nav=page.locator('header.nav');
  if(isMobile){
    const rooster=await page.locator('.nav .rooster-button').boundingBox();
    assert.ok(rooster&&Math.abs(rooster.x+rooster.width/2-width/2)<8,name+': rooster not centred');
    const toggle=page.locator('.mobile-menu-toggle');
    await toggle.click();
    await page.locator('#mobile-navigation').waitFor({state:'visible'});
    const [headerBox,panelBox]=await Promise.all([nav.boundingBox(),page.locator('#mobile-navigation').boundingBox()]);
    assert.ok(panelBox.y>=headerBox.y+headerBox.height-2,name+': menu overlaps header');
    await page.screenshot({path:'screenshots/'+name+'-menu.png',fullPage:false});
    await page.locator('#mobile-navigation .mobile-join-link').click();
    await page.locator('#club-popup').waitFor({state:'visible'});
    assert.ok(await page.locator('#club-mobile').isVisible(),name+': mobile field missing');
    await page.locator('.club-popup-close').click();
    assert.equal(await page.locator('#club-popup').isVisible(),false);
    await toggle.click();
    await page.locator('#open-search').click();
    await page.locator('#search-overlay').waitFor({state:'visible'});
    await requiredImage(page,'.search-art img');
    await page.locator('#search-club-link').click();
    await page.locator('#club-popup').waitFor({state:'visible'});
    await page.locator('.club-popup-close').click();
    for(const modal of ['account','bag']){
      await toggle.click();
      await page.locator('[data-modal="'+modal+'"]').click();
      await page.locator('#info-modal').waitFor({state:'visible'});
      await page.locator('#modal-cta').click();
      await page.locator('#club-popup').waitFor({state:'visible'});
      await page.locator('.club-popup-close').click();
    }
  } else {
    assert.equal(await page.locator('.mobile-menu-toggle').isVisible(),false,'desktop hamburger should be hidden');
    await page.locator('#open-search').click();
    await page.locator('#search-club-link').click();
    await page.locator('#club-popup').waitFor({state:'visible'});
    await page.locator('.club-popup-close').click();
  }
  await page.evaluate(()=>window.scrollTo(0,1600));
  await page.waitForTimeout(200);
  const sticky=await nav.boundingBox();
  assert.ok(sticky&&Math.abs(sticky.y)<3,name+': navigation not sticky');
  if(isMobile){
    await page.locator('.mobile-menu-toggle').click();
    const [h,p]=await Promise.all([nav.boundingBox(),page.locator('#mobile-navigation').boundingBox()]);
    assert.ok(p.y>=h.y+h.height-2,name+': menu overlaps scrolled header');
  }
  await context.close();
  console.log(name+': homepage, navigation, brand assets, signup flows and sticky header passed');
}

try{
  await checkViewport('desktop',1440,900,false);
  await checkViewport('iphone',390,844,true);
  const context=await browser.newContext({viewport:{width:390,height:844},isMobile:true,hasTouch:true});
  const page=await context.newPage();
  await page.goto(origin+'members-club.html',{waitUntil:'domcontentloaded'});
  assert.ok((await page.locator('h1').innerText()).includes('PANTS ON.'),'Members Club heading changed');
  await page.locator('.cta').click();
  await page.locator('#club-popup').waitFor({state:'visible'});
  assert.equal(await page.locator('#club-email').isVisible(),true,'Members Club CTA did not open signup');
  await context.close();
  assert.equal(fail.length,0,fail.join('\n'));
  console.log('PASS — desktop, iPhone and Members Club smoke test');
}finally{await browser.close()}
