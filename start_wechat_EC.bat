@echo off
call E:

set auto_path = E:\work-dir\project-python\Smart-Assist\byAutoit\
cd %auto_path%
ping -n 1 127.0.0.1 > null
echo "1"



start F:\install\autoit-v3.3.14.0\AutoIt3_x64.exe "E:\work-dir\project-python\Smart-Assist\byAutoit\start_wechat.au3"
ping -n 6 127.0.0.1 > null
echo "wechat"

start F:\install\autoit-v3.3.14.0\AutoIt3_x64.exe "E:\work-dir\project-python\Smart-Assist\byAutoit\start_EC.au3"
ping -n 2 127.0.0.1 > null
echo "EC"


exit

