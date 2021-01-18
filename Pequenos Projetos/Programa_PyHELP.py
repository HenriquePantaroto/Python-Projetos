from time import sleep

print('\033[33m-=\033[m' * 25)
print('\033[33m            Sistema de ajuda PyHELP               \033[m')
print('\033[33m-=\033[m' * 25)
sleep(1)
while True:
    print('\033[34m-=\033[m' * 25)
    sis = str(input(('\033[34mFunção, ou Biblioteca (quit para sair): \033[m'))).strip()
    print('\033[34m-=\033[m' * 25)
    if sis.lower() == 'quit':
        break
    sleep(1.5)
    print('\033[33m-=\033[m' * 25)
    print(f'\033[33mAcessando o Manual do {sis}.\033[m')
    print('\033[33m-=\033[m' * 25)
    sleep(1.5)
    print('\033[36m')
    help(sis)
    print('\033[m')
print()
print('\033[35mFinalizando Programa PyHELP.\033[m')
sleep(1)
print('\033[35m...\033[m')
sleep(1)
print('\033[35m...\033[m')
sleep(1)
print('\033[35m-=-=-=-=-=-= FIM do PyHELP =-=-=-=-=-=-\033[m')
