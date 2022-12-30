import tkinter as tk; import os, platform; import tkinter.messagebox as mb; import requests, socket
from tkinter import *; from tkinter.ttk import *; import random, time, sys

print(os.path.abspath("."))

psv=['d']
def probe():
    def step3():
        paths=[f'{sys._MEIPASS}\\files\\', f'{sys._MEIPASS}\\files\\wp.png', f'{sys._MEIPASS}\\files\\icon.ico', f'{sys._MEIPASS}\\files\\enable.vbs', f'{sys._MEIPASS}\\files\\disable.vbs']
        for i in paths:
            if os.path.exists(i):
                pass
            else:
                mb.showerror("Файл не найден", f'При запуске CSECProxy нам не удалось найти файл {i}. Переустановите программу.')
                return sys.exit()
        main()

    def step2():
        if os.system('netsh help') == 0:
            step3()
        else:
            mb.showerror("Неподдерживаемая система", 'CSECProxy не обнаружил в вашей системе netsh winhttp, погуглите эту проблему в сети, или свяжитесь с нами в Telegram: @csecsupbot')
            return sys.exit()
    def step1():
        if "Win" or 'win' in platform.system():
            if '10' in platform.version():
                step2()
            else:
                mb.showwarning("Неподдерживаемая ОС", 'CSECProxy стабильно работает на Windows 10, однако может не работать или вызвывать ошибки на других версиях ОС.')
                pass
        else:
            mb.showerror("Неподдерживаемая система", 'CSECProxy поддерживает только ОС Windows NT.')
            return sys.exit()
    step1()



def main():
    def connect():
        win = Tk()
        win.title('Netbar')
        win.geometry('300x200')
        win.iconbitmap(f'{sys._MEIPASS}\\files\\icon.ico')
        win.resizable(width=False, height=False)
        def err(content):
            os.system('reg add "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings" /v ProxyEnable /t REG_DWORD /d 0 /f')
            Label(win, text=content).pack()
            cbtn['state']=tk.NORMAL
            cbtn.config(text='CONNECT')
        if not os.path.exists(f'{sys._MEIPASS}\\files\\lock'):
            cbtn['state']=tk.DISABLED
            cbtn.config(text='CONNECTING')
            Label(win, text='Checking windows netsh...').pack()
            if os.system('netsh help') == 0:
                Label(win, text='Done.').pack()
            else:
                err("netsh can't be launched")
                return
            Label(win, text='Launching with script...').pack()
            try:
                os.startfile(f'{sys._MEIPASS}\\files\\enable.vbs')
            except:
                err("Can't start files/enable.vbs")
                return
            Label(win, text='Done. Checking connection...').pack()
            proxy='proxy.crypton.ga:8443'
            try:
                try:
                    proxydomain, port=proxy.split(':')
                except:
                    err('Unckown error')
                    return
                cpr = {'http': f'https://{proxy}'}
                cip=requests.get('http://ifconfig.ru', proxies=cpr).text.replace('\n', '')
                pname=socket.gethostbyname(proxydomain).replace('\n', '')
                if cip == pname:
                    open(f'{sys._MEIPASS}\\files\\lock', 'w').close()
                    Label(win, text='Connected!').pack()
                    cbtn['state']=tk.NORMAL
                    cbtn.config(text='DISCONNECT')
                else:
                    Label(win, text='Hostname error').pack()
                    cbtn['state']=tk.NORMAL
                    cbtn.config(text='CONNECT')
                    return
            except Exception as EE:
                err(f'Connection error')
                print(EE)
                return
        else:
            cbtn['state']=tk.DISABLED
            cbtn.config(text='DISABLING')
            Label(win, text='Disabling...').pack()
            try:
                os.startfile(f'{sys._MEIPASS}\\files\\disable.vbs')
                os.remove(f'{sys._MEIPASS}\\files\\lock')
            except:
                err('Error while disabling')
                return
            err('Disconnected successfully!')

    root = Tk()
    root.title('CSECProxy')
    root.geometry('640x420')
    background_image=tk.PhotoImage(file=f'{sys._MEIPASS}\\files\\wp.png')
    root.iconbitmap(f'{sys._MEIPASS}\\files\\icon.ico')
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    #style
    style = Style()
    style.configure('TButton', font =
               ('calibri', 20, 'bold'),
                    borderwidth = '4')
    style.map('TButton', foreground = [('active', '!disabled', 'green')],
                     background = [('active', 'black')])
    #
    #Connect button
    if os.path.exists(f'{sys._MEIPASS}\\files\\lock'):
        cbtn=Button(root, text = 'DISCONNECT', command = connect)
    else:
        cbtn=Button(root, text = 'CONNECT', command = connect)
    cbtn.place(x=460, y=360)
    #

    root.resizable(width=False, height=False)
    root.mainloop()

#Launch
probe()
main()
