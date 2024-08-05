import wget

def downloadanydesk():
    wget.download('https://download.anydesk.com/AnyDesk.exe')

def downloadaact():
    wget.download('http://gozerent.ru/filesforprog/AAct_x64.exe')

def downloadchrome():
    wget.download('http://gozerent.ru/filesforprog/ChromeSetup.exe')

def downloadfirefox():
    wget.download('http://gozerent.ru/filesforprog/Firefox Installer.exe')

def downloadopera():
    wget.download('http://gozerent.ru/filesforprog/OperaSetup.exe')

def downloadyandex():
    wget.download('http://gozerent.ru/filesforprog/Yandex.exe')

def downloadklite():
    wget.download('https://files2.codecguide.com/K-Lite_Codec_Pack_1848_Full.exe')

def dwnload(anydesk, aact, chrome, firefox, yandex, opera, klite):
    if anydesk:
        print("Загрузка Anydesk...")
        downloadanydesk()
        print("Anydesk загружен.")
    if aact:
        print("Загрузка AAct...")
        downloadaact()
        print("AAct загружен.")
    if chrome:
        print("Загрузка Google Chrome...")
        downloadchrome()
        print("Google Chrome загружен.")
    if firefox:
        print("Загрузка Firefox...")
        downloadfirefox()
        print("Firefox загружен.")
    if yandex:
        print("Загрузка Yandex...")
        downloadyandex()
        print("Yandex загружен.")
    if opera:
        print("Загрузка Opera...")
        downloadopera()
        print("Opera загружен.")
    if klite:
        print("Загрузка K-Lite Codec Pack...")
        downloadklite()
        print("K-Lite Codec Pack загружен.")
    if not (anydesk or aact or chrome or firefox or yandex or opera or klite):
        print("Ничего не выбрано")