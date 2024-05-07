#!/bin/bash

colprint () {
    echo -e "$1$2\033[0m"
}

colprint "\033[0;36m" "[II] Update ubuntu"
sudo apt update
sudo apt install python3 -y

colprint "\033[0;36m" "[II] Chrome install"
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -q
sudo apt install ./google-chrome-stable_current_amd64.deb

colprint "\033[0;36m" "[II] Install pip requirements"
pip3 install -r requirements.txt