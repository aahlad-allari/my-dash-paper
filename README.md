# My Dash Paper
E-paper Dashboard on top of your work desk.

# I've used
- RaspberryPi-3(But, works with 4)
- EPaper(Black&White) 7.5 inch

# Resources
- [Waveshare](https://github.com/waveshare/e-Paper)
- [zx](https://github.com/google/zx)
- Python3
- Nodejs
- [Puppeteer](https://github.com/puppeteer/puppeteer)

## Install

```bash
npm i -g zx
```

```bash
zx setup.mjs
```

## You might need to run these in Raspberrypi
```bash
sudo pip3 install spidev
sudo apt-get install python-imaging
sudo pip3 install spidev
sudo pip3 install RPi.GPIO
sudo pip3 install Pillow

# Install pip on RaspberryPi
sudo python3 -m pip install -U pip
sudo python3 -m pip install -U matplotlib
sudo python3 -m pip install -U numpy 

#I raninto issue with numpy (ImportError: libcblas.so.3: cannot open shared object file: No such file or directory)
sudo apt-get install libjasper-dev
```


```bash
npm install -g sass
npm install -g http-server
```