#!/usr/bin/env sh
cd ~
mv 公共 Public
mv 模板 Templetes
mv 视频 Videos
mv 图片 Pictures
mv 文档 Documents
mv 下载 Downloads
mv 音乐 Music
mv 桌面 Desktop

sed -i "s/HOME\/公共/HOME\/Public/" ~/.config/user-dirs.dirs
sed -i "s/HOME\/模板/HOME\/Templetes/" ~/.config/user-dirs.dirs
sed -i "s/HOME\/视频/HOME\/Videos/" ~/.config/user-dirs.dirs
sed -i "s/HOME\/图片/HOME\/Pictures/" ~/.config/user-dirs.dirs
sed -i "s/HOME\/文档/HOME\/Documents/" ~/.config/user-dirs.dirs
sed -i "s/HOME\/下载/HOME\/Downloads/" ~/.config/user-dirs.dirs
sed -i "s/HOME\/音乐/HOME\/Music/" ~/.config/user-dirs.dirs
sed -i "s/HOME\/桌面/HOME\/Desktop/" ~/.config/user-dirs.dirs
