#!/usr/bin/env bash
# delete fcitx
sudo apt-get remove fcitx*
sudo apt-get autoremove
# install sougou pinyin
sudo add-apt-repository ppa:fcitx-team/nightly
sudo apt-get update
sudo apt-get install fcitx-sogoupinyin
