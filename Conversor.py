num = int(input('Digite um número: '))
c = True
print()

base = int(input('1 - Binário\n2 - Octal\n3 - hexadecimal\nQual a base que você quer que converta? '))
n = num
bin = ''
oct = ''
hex = ''

if base == 1:
    while n != 1:
        bin += str(n % 2)
        n = int(n / 2)

    bin += str(n)
    bin = bin[::-1]

    print('O número {} convertido para binário é {}'.format(num, bin))
    c == False
elif base == 2:
    while n > 8:
        oct += str(n % 8)
        n = int(n / 8)

    oct += str(n)
    oct = oct[::-1]

    print('O número {} convertido para octal é {}'.format(num, oct))
    c == False
elif base == 3:
    
    while n > 16:
        res = n % 16
        if res > 9:
            if res == 10:
                hex += 'A'
            elif res == 11:
                hex += 'B'
            elif res == 12:
                hex += 'C'
            elif res == 13:
                hex += 'D'
            elif res == 14:
                hex += 'E'
            else:
                hex += 'F'
        else:
            hex += str(n % 16)
            
        n = int(n / 16)

    if n > 9:
        if n == 10:
            hex += 'A'
        elif n == 11:
            hex += 'B'
        elif n == 12:
            hex += 'C'
        elif n == 13:
            hex += 'D'
        elif n == 14:
            hex += 'E'
        else:
            hex += 'F'
    else:
        hex += str(n)
    
    hex = hex[::-1]

    print('O número {} convertido para hexadecimal é {}'.format(num, hex))
    c == False
else:
    print('Opção selecionada inválida.\nTente novamente.')
