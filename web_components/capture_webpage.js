const puppeteer = require('puppeteer');
const os = require('os');
const fs = require('fs-extra');

let config = {
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox'],
    defaultViewport: { width: 480, height: 800, deviceScaleFactor: 1 }
}

// Check if raspberrypi
if(os.cpus()[0] && os.cpus()[0].model == "ARMv7 Processor rev 4 (v7l)"){
    config["executablePath"] = '/usr/bin/chromium-browser';
}

(async () => {
  const browser = await puppeteer.launch(config);
  const page = await browser.newPage();
  await page.goto('https://www.aahlad.dev');
  const path = `screenshots/`;
  fs.mkdirp(path);
  await page.screenshot({path: `${path}/image.png`});

  await browser.close();
})();