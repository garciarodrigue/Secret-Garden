#comezamos a programar 3l codigo
import os
import sys,time
from colorama import Style,  Back, Fore, init
init()

os.system('clear')

name = Fore.RED + "NINGUN SISTEMA ES SEGURO... "

for l in name:
    sys.stdout.flush()
    print(l,end="")
    time.sleep(0.1)
    #fin banner

print()
print(Style.BRIGHT + Fore.BLUE + '''      HACK_CHAT.COM 
''')
print(''' 
カカシ                                  

　　   　∧ﾍ∧ﾍ                                               　     　 　(ﾆニ@ﾆ
　　 .（ ﾐ｀∀´）
　　　.Ｕ__.||_iつ                                                     l__.ﾊ_i
　　　　∪. .∪

''')

canal = input(Fore.YELLOW + 'ingresa el nombre de tu chat secreto: \n [+]')
print()
print(Fore.BLUE + "tu canal es")

f = open ('hack.chat.txt', 'a+')

print(Fore.MAGENTA + '¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥')
url = print(Fore.GREEN + f'https://hack.chat/?{canal}')
print(Fore.MAGENTA + '¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥')
print()


opc1 = input(Fore.BLUE + 'Quieres Guardar el url Chat en txt?\n[+]')
if opc1 == 'si':
    url = str()
    f.write(f'https://hack.chat/?{canal}\n')
    
    f.close()

print()
print(Fore.YELLOW + "URL GUARDADO")
print()

opc = input(Fore.RED + 'Quieres dirigirte a el chat?\n [+]')
if opc == 'si':
    print('habriendo chat')
    os.system(f'termux-open-url https://hack.chat/?{canal}')
else:
        print('nos vemos')
        os.system('clear')
        
