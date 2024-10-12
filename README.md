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
sudo pip3 install docopt==0.6.2

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

## Log rotation
```bash
pm2 install pm2-logrotate

pm2 set pm2-logrotate:max_size 10K

pm2 set pm2-logrotate:rotateInterval '*/10 * * * *'
```

## How to use

### If you want to use cli you and use the following commands
```bash
zx test.mjs --c=webpage --url=http://google.com --bg=<BLACK or WHITE> --o=<P or L>
zx test.mjs --c=web_calendar
zx test.mjs --c=py_calendar
zx test.mjs --c=write_text --text="Do it" --fontsize=60
zx test.mjs --c=hackernews
zx test.mjs --c=image --img_name=file_name.jpg  --bg=<BLACK or WHITE> --o=<P or L>
zx test.mjs --c=web_col --index=r --o=l
```

## If you want to run daemon which rotates all the widgets in 1 min interval

```bash
zx daemon.mjs --start
```

To Stop the daemon

```bash
zx daemon.mjs --stop
```

# MagicMirror
Magic mirror must be installed beside this proj directory

## Start Magic Mirror 

```bash
zx test.mjs --c=start_magic_mirror
```

## Stop Magic Mirror 

```bash
zx test.mjs --c=stop_magic_mirror
```