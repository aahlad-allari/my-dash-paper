const puppeteer = require('puppeteer');
const os = require('os');
const fs = require('fs-extra');

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

exports.generate_image = (url='https://www.aahlad.dev', orientation="L") => {

  let config = {
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox'],
    defaultViewport: { width: 800, height: 480, deviceScaleFactor: 2 }
  }
  
  // Check if raspberrypi
  if (os.cpus()[0] && os.cpus()[0].model == "ARMv7 Processor rev 4 (v7l)") {
    config["executablePath"] = '/usr/bin/chromium-browser';
  }

  (async () => {
    if(orientation == "P"){
      config.defaultViewport.width = 480
      config.defaultViewport.height = 800
    }
    const browser = await puppeteer.launch(config);
    const page = await browser.newPage();
    await page.goto(url, {"waitUntil" : "networkidle0", timeout: 0});
    const path = `screenshots/`;
    fs.mkdirp(path);
    await page.evaluate(() => document.body.style.background = 'transparent');
    resp = await page.screenshot({ path: `${path}/image.png`, omitBackground: true, });
    
    
    await browser.close();
    await sleep(2000);

    return resp;
    
  })();

}
