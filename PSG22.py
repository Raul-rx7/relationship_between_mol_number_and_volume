def massa(x, y):
    return x * y


def vol(x, y):
    return x / y


print('\033[1;7mRELAÇÃO NÚMERO DE MOL E VOLUME DE UM COMPOSTO: \033[m')
print()
dens = float(input('\033[1mDensidade(g/mL): d = '))
mm = float(input('Massa molar(g/mol): MM = '))
sv = 0
while sv != 4:
    sv = int(input('[1] para continuar, [2] alterar o composto ou [3] sair do programa: '))
    if sv == 1:
        n = float(input('Número de mol:\033[1;33m n = \033[m'))
        print()
        print('\033[1;34m( {:.2f} ) mol    >>>>    ( {:.2f} ) mL.\033[m'.format(n, vol(massa(n, mm), dens)))
        print()
    elif sv == 2:
        print('Voltando . . . ')
        print()
        dens = float(input('\033[1mDensidade(g/mL): d = '))
        mm = float(input('Massa molar(g/mol): MM = '))
    elif sv == 3:
        print('OK . . .')
        exit()
    else:
        print('Opção inválida. Tente novamente!')
