# Powerprofilesctl-daemon
This script is ugly and was a quick hack solution to get power-profiles-daemon automated P-state switching to work.

I recommmend you try and write a Udev rule first before using this but If you run into issues getting that to work then you might want to use this until you can get a working solution.

I have a Lenovo ThinkPad X1 carbon 6th gen. For whatever reason writing udev rules barely work as certain attributes aren't being detected properly (I should research more on Udev but there was obviously something strange going on). As a result I decided to write a python script and systemd service, my first attempt to write this script used linux filesystem api "inotify" to detect changes in files handling hardware but it didn't work because files handling devices are handled differently enough this doesn't work right. leading to issues detecting modifications. 

So thats why it has that ugly waiting 1 second timer stuff that I really don't like but will work until I can write a proper working udev rule. 
