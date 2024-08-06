from tkinter import *
from tkinter import ttk
from download import dwnload
import webbrowser
print("Статус скачивания:")
root = Tk()

root.title('Gozerent Download Manager')
root.geometry('350x350')

def select():
    result = "Выбрано: "
    if anydesk.get() ==1: result += "Anydesk "
    if aact.get() == 1: result += "AAct "
    if chrome.get() == 1: result += "Google Chrome "
    if firefox.get() == 1: result += "Firefox "
    if yandex.get() == 1: result += "Yandex "
    if opera.get() == 1: result += "Opera "
    if klite.get() == 1: result += "K-Lite Codec Pack "
    languages.set(result)

def start_download():
    dwnload(anydesk.get(), aact.get(), chrome.get(), firefox.get(), yandex.get(), opera.get(), klite.get())

def office():
    webbrowser.open("https://repack.me/software/repacks/office/300-microsoft-office-2013-c2r.html", new=0)

position = {"padx": 6, "pady": 6, "anchor": NW}

languages = StringVar()
languages_label = ttk.Label(textvariable=languages)
languages_label.pack(**position)

anydesk = IntVar()
anydesk_checkbutton = ttk.Checkbutton(text='Anydesk', variable=anydesk, command=select)
anydesk_checkbutton.pack(**position)

aact = IntVar()
aact_checkbutton = ttk.Checkbutton(text='AAct', variable=aact, command=select)
aact_checkbutton.pack(**position)

chrome = IntVar()
chrome_checkbutton = ttk.Checkbutton(text='Google Chrome', variable=chrome, command=select)
chrome_checkbutton.pack(**position)

firefox = IntVar()
firefox_checkbutton = ttk.Checkbutton(text='Firefox', variable=firefox, command=select)
firefox_checkbutton.pack(**position)

yandex = IntVar()
yandex_checkbutton = ttk.Checkbutton(text='Yandex', variable=yandex, command=select)
yandex_checkbutton.pack(**position)

opera = IntVar()
opera_checkbutton = ttk.Checkbutton(text='Opera', variable=opera, command=select)
opera_checkbutton.pack(**position)

klite = IntVar()
klite_checkbutton = ttk.Checkbutton(text='K-Lite Codec Pack', variable=klite, command=select)
klite_checkbutton.pack(**position)

officebtn = ttk.Button(text='Office 2013', command=office)
officebtn.pack(**position)

confirmbtn = ttk.Button(text='Начать скачивание', command=start_download)
confirmbtn.pack()

root.mainloop()