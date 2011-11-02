

How to upgrade the XMenu:
>>>> Warning! All data on the MK5 will lose after you start the upgrade! Please backup it first!! <<<<
1. Use MK5 USB Linker connect PC , and enter USB data exchange mode , PC will detect one removable disk (MK5) have inserted
2. Copy "MK5_Menu_V1.39_AUTO_Upgrade.nds" to MK5
3. Restart NDS, enter MK5 menu, choose "MK5_Menu_V1.39_AUTO_Upgrade.nds" and run it,and restart NDS.
4. When NDS power on, hold L+R+A+B+DOWN to fast format whole MK5, or you can use A+B+START+SELECT+UP to make a low-level format ,then copy all data (include folder) from this uncompressed file.
5. Now new system is ready ,restart NDS and enjoy it!



MK5 8G/16G GIGA cart upgrade core V1.45 + 2.56 XMenu [07-14-2008]
* fixed the rumble pak support for these roms:
#0136, #0340, #0511, #0540, #0580, #0595, #0604, #0606, #0635, #0645, #0655, #0731, #0743, #0766, #0777, #0817, #0823, #0830, #0831, #0832, #0836, #0866, #0873, #0876, #0934, #1000, #1081, #1097, #1116



MK5 8G/16G GIGA cart upgrade core V1.45 + 2.55 XMenu [04-08-2008]
* fixed #2107 and #2207 bugs
* can show the balance memory on the top screen



MK5 8G/16G GIGA cart upgrade core V1.45 + 2.54 XMenu [01-01-2008]
* fixed FF4 bug
* fixed some DLDI bugs


MK5 8G/16G GIGA cart upgrade core V1.45 + 2.53 XMenu [08-20-2007]
* fixed some bugs
* Game save data update to #1323


MK5 8G/16G GIGA cart upgrade core V1.45 + 2.52 XMenu [07-20-2007]
* Optimized the flash low-level core, need re-format the MK5 first,please backup your game save file to PC in advance
* Added 3 format mode to the format page when boot up your NDS and hold SELECT+START
* Fixed one game save bug
* Changed the "wait to loading" screen, and can set the color in global.ini



MK5 8G/16G GIGA cart upgrade core V1.44 + 2.50 XMenu [07-05-2007]

* Fixed the bug of when #1044 use soft reset return to menu cause menu hang
* Fixed #0697 and #0963 white screen issue
* Game save data update to #1167



MK5 8G/16G GIGA cart upgrade core V1.43 + 2.48 XMenu [07-01-2007]
* Added soft-reset function
how to use the soft reset: L+R+A+B+X+Y
when select the current game save type to AUTO, then enable this soft reset function, otherwise will disable it.
* Fixed the #1101 white screen bug



MK5 8G/16G GIGA cart upgrade core V1.42 + 2.47 XMenu [07-01-2007]
* Added one extra ECC checking for ARM7&ARM9 bin 
* Improved the 4M save support, "The Legend of Zelda" working perfect now
* Improved some code for the core, more stable now.



MK5 8G/16G GIGA cart upgrade core V1.41 + 2.45 XMenu [06-27-2007]
* Modified the menu MFTL structure, please format your MK5 to upgrade it.
* Added the function for auto select save type
* Added 4M save support, for support the "The Legend of Zelda"



MK5 8G/16G GIGA cart upgrade core V1.40 + 2.43 XMenu Stable Version [06-26-2007]
* Modified some export message
* Modified use top screen to show message under the U-DISK mode
* Fixed some bugs, like the date display
* The Game save database update to #1138





MK5 8G/16G GIGA cart upgrade core V1.39 + 2.42 XMenu Stable Version [06-05-2007]
history:
* Fixed one bug of date
* Fixed one bug of global.ini setup





MK5 8G/16G GIGA cart upgrade core V1.39 + 2.41 XMenu  [06-05-2007]
history:
* Fixed the bug of can't create BMP file
* Added some DC_FlushRange()
* Support nitro fat 
* The BMP and global.ini / savetype.sdb files put to nitro fat , can use ndstool to modify
* Fixed the bug of without sound on the old nds console
* Fixed the FAT sector size to 64K
* Fixed the bug of upside screen can't display correct
* Upgrade the 2M SRAM test APP --- "MK5_2Mbit_test_V5.nds" , thanks cory1492 :)
* Fixed the function of _FAT_fat_linkFreeClusterCleared , increase the folder create speed
* The Game save database update to #1126
* Added the menu version verify
* Added the third read/write index, solved the moonshell hand up with some video format
* Rewrite the flash bad block manager function
* Support DLDI auto patch , and support DLDI write mdoe







MK5 8G/16G GIGA cart upgrade core V1.23O  [04-29-2007]

history:

* Change the SMS working way:
  [1] if set the "FORCEBACKUP"=1 in \Dsystem\global.ini , then:
      (a) Will force backup the current game data to #1 memory slot;
      (b) Don't notice to backup the current save, show the SMS menu directly;
      (c) You can press START to call the SMS screen when you in the menu.
  [2] if set the "FORCEBACKUP"=0 in \Dsystem\global.ini , then:
      (a) Don't auto backup current save when turn on nds;
      (b) Will let you select backup the current game save to which memory slot when you start to run a rom;
      (c) You can press START to call the SMS screen when you in the menu.
* The game save type database update to #1023.



MK5 8G/16G GIGA cart upgrade core V1.23N+  [04-10-2007]

history:

* Support 4 different language:
	CHS	-	Chinese (simplified) version
	CHT	-	Chinese (traditional) version
	ENG	-	English version
	JAP	-	Japanese version
	you can choose which MK5 version you like, just run this upgrade ROM then can change to the different language;
* Allow keep all save files to one same sub-folder;
*	Support SMS multi-save system, when you start to run this rom,you can choose which save file you want to restore and start for current game;
*	You can specify your own skin now,just need to put the *.BMP to your MK5 "dsystem\skin" folder,
	c_file.bmp --- it's upside background picture,BMP format,256pix X 192pix , 24bit color
  desktop.bmp --- it's downside background picture,BMP format,256pix X 192pix , 24bit color
  save_bg.bmp --- it's the SMS background picture,BMP format,256pix X 192pix , 24bit color
  MK5 will show the default skin if the "dsystem\skin" folder is empty;
* Add one "passme2" mode,when the NDS turn on or in the MK5 menu, you can press the L+R+A+B 4 keys to enter MK5 passme2 mode , it'll boot GBA slot immediately;
* Add one traditional 2D display mode,you can change 2D or 3D style in the "global.ini" file;
* Add one MK5 USB linker boot loader,you can choose to enter the "Media Center" mode (MK5 mode) or the "Data Exchange" mode (PC mode) when you inset the MK5 GBA linker and turn on NDS.
* Fixed one data transfer CRC error;
* Add the folder auto create function,not need to create the folder which have defined in "global.ini" by manual;
* Add the force backup function in MK5 menu,when you select one rom and press "START" will force to backup current rom save;
* Fixed one reading error with global.ini file;
* the game save type database update to #987.



MK5 8G/16G GIGA cart upgrade core V1.23A+  [02-23-2007]

history:
* the save data upgrade to #947, game compatibility = 100%!
* change the MK5 skin, more colorful
* moonshell upgrade to V1.71, movie play speed up! And support TTA/AAC/OGG !
* dpgtools upgrade to V1.3 , more stable

more info check here: http://www.neoflash.com/forum/index.php/board,78.0.html
download: http://www.neoflash.com/download/mk5_1.23A_plus_upgrade.rar 

how to upgrade: (without format)
[1] link your MK5 to pc through the MK5 USB linker;
[2] unzip this rar pack,and enter the "Driver" folder ,copy all files to your MK5 and overwrite the old files,and stop the MK5 removeable disk when it's done;
[3] remove the MK5 USB linker,turn on nds and enter the menu,click and run "mk5_update_fat_new_V1.23A+.nds"
[4] turn off nds,now upgrade finish,enjoy it!


how to upgrade: (with format)
[1] If your MK5 can't enter the menu to upgrade,you can try to format it on NDS (warnning: this upgrade will format MK5 and all old data will be destory!), please follow me:
    <a> plug in the USB cart to GBA slot and link to PC,and plug in the MK5 to NDS slot;
    <b> hold the "L" + "R" + "DOWN" and turn on NDS till you see the mk5 logo appear (don't release these 3 keys), and press "A"+"B" (now 5 keys were hold) ,then you can see USB cart start to formatting MK5. When if finish(around 5 seconds),you can see "USB DISK PROGRAM(8G/16G_256K)" appear on the NDS screen, PC will appear one USB DISK too;
[2] Now you can follow the "how to upgrade: (without format)" to upgrade MK5 again.


-----------------------------------------------------------

MK5 8G/16G GIGA cart upgrade core V1.23A  [17-02-2007]

history:
* support the DLDI,and open the DLDI source code
* support CRC write checksum,read/write is more safety
* fix few roms running bug
* moonshell play movie more smooth now,and upgrade to V1.5
* support MK5 joypad and MK5 mouse,and open the source code
* dpgtools upgrade to v1.21 ,support more video format


-----------------------------------------------------------
NEOTEAM 2007
www.NEOFLASH.com