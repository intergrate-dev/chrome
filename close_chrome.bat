@echo off
echo "chrome quite"
start F:\install\autoit-v3.3.14.0\AutoIt3_x64.exe "E:\work-dir\project-python\Smart-Assist\byAutoit\close_chrome.au3"
ping -n 5 127.0.0.1 > null

exit
