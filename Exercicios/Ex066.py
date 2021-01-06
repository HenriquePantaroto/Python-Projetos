n = s = q =0
while n != 999:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    s += n
    q += 1
print(f'A quantidade de números digitados foi de {q}, e sua soma total é de {s}.')
