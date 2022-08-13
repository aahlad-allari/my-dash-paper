const puppeteer = require('puppeteer');
const os = require('os');
const fs = require('fs-extra');

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

let config = {
  headless: true,
  args: ['--no-sandbox', '--disable-setuid-sandbox'],
  defaultViewport: { width: 480, height: 800, deviceScaleFactor: 1 }
}

// Check if raspberrypi
if (os.cpus()[0] && os.cpus()[0].model == "ARMv7 Processor rev 4 (v7l)") {
  config["executablePath"] = '/usr/bin/chromium-browser';
}

exports.generate_image = (url='https://www.aahlad.dev') => {

  (async () => {
    const browser = await puppeteer.launch(config);
    const page = await browser.newPage();
    await page.goto(url);
    const path = `screenshots/`;
    fs.mkdirp(path);

    await sleep(2000);

    resp = await page.screenshot({ path: `${path}/image.png` });
    
    await sleep(2000);
    
    await browser.close();

    return resp;
    
  })();

}
