import sys, os, platform
from setuptools import setup

dependencies = ['Pillow', 'numpy']

# If raspberrypi install waveshare module
if os.uname().sysname == "Linux" and os.uname().nodename == "raspberrypi":
    if os.path.exists('/sys/bus/platform/drivers/gpiomem-bcm2835'):
        dependencies += ['RPi.GPIO', 'spidev']
    else:
        dependencies += ['Jetson.GPIO']

setup(
    name='my-dash-paper',
    description='My desktop gadget',
    author='Aahlad',
    package_dir={'': 'lib'},
    packages=['my_dash_paper'],
    install_requires=dependencies,
)

