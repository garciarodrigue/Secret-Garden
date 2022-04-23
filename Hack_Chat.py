#comezamos a programar 3l codigo
import os

print('''               HACH_CHAT.COM 
''')

canal = input('ingresa el nombre de tu chat secreto: \n [+]')
print()
print("tu canal es")
print('¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥')
url = print(f'https://hack.chat/?{canal}')
print('¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥')
print()
opc = input('Quieres dirigirte a el chat?\n [+]')
if opc == 'si':
    print('habriendo chat')
    os.system(f'termux-open-url https://hack.chat/?{canal}')
else:
        print('nos vemos')
        os.system('clear')


