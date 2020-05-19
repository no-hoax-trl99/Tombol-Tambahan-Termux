import os
from time import sleep


a ='\033[92m'
b ='\033[91m'
c ='\033[0m'

def setup():
    try:
        os.mkdir('/data/data/com.termux/files/home/.termux')
    except:
        pass
    key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
    open('/data/data/com.termux/files/home/.termux/termux.properties','w').write(key)
    os.system('termux-reload-settings')


def banner():
    os.system('clear')
    print(a+'Shortcut Tombol Tambahan Termux '.center(40))
    print(b+'(home)(end)(PGUP)(PGDN)(panah kanan dan kiri)'.center(40))
    print(c+'OTOMATIS AKAN MUNCUL '.center(40))
    print("".join([i for i in "\n"*3]))
    


if __name__=='__main__':
    banner()
    from threading import Thread as td
    t = td(target=setup)
    t.start()
    while t.is_alive():
        for i in "-\|/-\|/":
            print('\rPlease wait '+i+' ',end="",flush=True)
            sleep(0.1)
    banner()
    print(c+'Jangan lupa untuk SUBSCRIBE chanel YOUTUBE '+a+'no hoax trl99'+c+' KOMENTAR jika ada yang mau di bicarakan terkait tool ini, LIKE JIKA Teman-teman suka. :v\nTerimakasih/MATURSUWUN ^_^')

# ini cuma shortcut buat bantu para nub
# no-hoax-trl99
