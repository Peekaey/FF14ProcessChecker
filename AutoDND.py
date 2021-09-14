import os

processname = 'ffxiv_dx11.exe'
tmp = os.popen("ps -Af").read()
proccount = tmp.count(processname)

if proccount > 0:
    os.system("gsettings set org.gnome.desktop.notifications show-banners false")
else:
     os.system("gsettings set org.gnome.desktop.notifications show-banners true")


