@echo off

echo "code quite"
taskkill /f /im code.exe
ping -n 5 127.0.0.1 > null

echo "chrome quite"
start F:\install\autoit-v3.3.14.0\AutoIt3_x64.exe "E:\work-dir\project-python\Smart-Assist\byAutoit\close_chrome.au3"
ping -n 5 127.0.0.1 > null

echo "wechat quite"
taskkill /f /im WeChat.exe
ping -n 5 127.0.0.1 > null

echo "snipaste quite"
taskkill /f /im Snipaste.exe
ping -n 3 127.0.0.1 > null

echo "notepad quite"
taskkill /f /im notepad++.exe
ping -n 3 127.0.0.1 > null

shutdown -s -t 5
