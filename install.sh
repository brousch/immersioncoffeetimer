#!/bin/bash
virtualenv -p python2.7 venv
source venv/bin/activate
pip install --upgrade cython
hg clone https://bitbucket.org/pygame/pygame
cd pygame
python setup.py build
sudo python setup.py install
cd ..
rm -rf pygame
pip install --upgrade kivy
git clone https://github.com/brousch/buildozer.git
cd buildozer
python setup.py install
cd ..
rm -rf buildozer

