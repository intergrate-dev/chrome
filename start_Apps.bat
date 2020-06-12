@echo off
start /d "F:\Program Files\Snipaste-2.3-Beta-x64\" Snipaste.exe
ping -n 5 127.0.0.1 > null
echo "1"

start /d "C:\Program Files (x86)\Google\Chrome\Application\" chrome.exe --profile-directory="Default" --remote-debugging-port=9222
ping -n 6 127.0.0.1 > null
echo "2"

start /d "F:\Program Files\Notepad++\" notepad++.exe
ping -n 3 127.0.0.1 > null
echo "3"


exit
