menu = print('''
      --------MENU--------
        1 - Depositar
        2 - Saque
        3 - Extrato
        4 - Sair
      ''');

saque = 0;
deposito = 0;
saldo = 1400;
extrato = '';
numero_saques = 0;
LIMITE_SAQUES = 3;


# programa principal
while True:
    menu;
    opcao = input('\nInforme a opção desejada: ');
    print();
    match opcao:
        case '1':
            deposito = float(input('\nInforme o valor do depósito: '));
            if(deposito < 1):
                print('o valor deve ser maior ou igual a 1');
                continue;
            saldo += deposito;
            print('Depósito realizado!')
            extrato += f'{"Deposito":<10} | valor: R$ {deposito}\n';              
        case '2':
            if(numero_saques < LIMITE_SAQUES):
                saque = float(input('\nInforme o valor do saque: '));
                if(saque < 1):
                    print('o valor deve ser maior ou igual a 1');
                    continue;
                if(saque <= 500 and saque <= saldo):
                    saldo -= saque;
                    print('Saque realizado!')
                    extrato += f'{"Saque":<10} | valor: R$ {saque}\n';
                    numero_saques += 1;
                else:
                    print('O valor informado excede o saldo ou o limite de 500 reais!\n');
            else:
                print('Limite de saques atingido!\n');
        case '3':
            print('Extrato: \n');
            print(extrato);
            print(f'Saldo restante: R$ {saldo:.2f}');
        case '4':
            break;
        case _:
            print('Informe uma opção válida!');
            