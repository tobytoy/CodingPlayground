#!/bin/bash

cd ~
mkdir playground
git config --global user.name "toby"
git config --global user.email tobywang2021@gmail.com
git clone https://github.com/tobytoy/CodingPlayground.git

ln -s /var/www/html  /home/toby/playground/html
