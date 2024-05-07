#!/bin/bash

sudo apt update
sudo apt install python3 -y

# install chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb

python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
echo "DONE!"