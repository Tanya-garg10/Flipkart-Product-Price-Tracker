#!/bin/bash

apt-get update
apt-get install -y chromium-browser chromium-driver

export CHROME_BIN=/usr/bin/chromium-browser
export PATH=$PATH:/usr/bin
