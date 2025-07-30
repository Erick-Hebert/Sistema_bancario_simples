def Saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if(numero_saques < limite_saques):
        if(valor < 1):
            print('o valor deve ser maior ou igual a 1');
            return saldo, extrato, numero_saques;
        if(valor <= 500 and valor <= saldo):
            saldo -= valor;
            print('Saque realizado!');
            extrato += f'{"Saque":<10} | valor: R$ {valor}\n';
            numero_saques += 1;
            return saldo, extrato, numero_saques;
        else:
            print('O valor informado excede o saldo ou o limite de 500 reais!\n');
    else:
        print('Limite de saques atingido!\n');
    return saldo, extrato, numero_saques;  

def Depositar(saldo, valor, extrato, /):
    if(deposito < 1):
        print('o valor deve ser maior ou igual a 1');
        return saldo, extrato;
    saldo += deposito;
    print('Depósito realizado!')
    extrato += f'{"Deposito":<10} | valor: R$ {deposito}\n';  
    return saldo, extrato;

def Extrato(saldo, /, *, extrato):
    print('Extrato: \n');
    print(extrato);
    print(f'Saldo restante: R$ {saldo:.2f}');

def Cadastra_usuario():
    nome = input('\nInforme o nome do Usuário: ');
    data_nascimento = input('\nInforme o data de nascimento do Usuário: ');
    cpf = input('\nInforme o CPF do Usuário: ');
    endereco = input('\nInforme o endereço do Usuário: ');

    for usuario in usuarios:
        if cpf in usuario['cpf']:
            print('Este usuário já foi cadastrado!');
            return;

    usuario = {'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco};
    usuarios.append(usuario);

def Cadastra_conta(numero_conta, agencia):
    cpf = input('\nInforme o cpf do Usuário: ');
    for usuario in usuarios:
        if cpf in usuario['cpf']: 
            print(f'Sua conta é {numero_conta}');
            print(f'A agência é 0001')
            conta = {'cpf': cpf, 'numero_conta': numero_conta, 'agencia': agencia};
            contas.append(conta);
            return numero_conta + 1;

    print('Usuário não encontrado')
    return numero_conta

def Listar_usuarios():
    print('-'*30);
    for usuario in usuarios:
        print(f'Nome: {usuario['nome']}\nData de nascimento: {usuario['data_nascimento']}\nCpf: {usuario['cpf']}\nendereço: {usuario['endereco']}\n{'-'*30}');


def Listar_contas():
    print('-'*30);
    for conta in contas:
        print(f'Cpf: {conta['cpf']}\nNumero de conta: {conta['numero_conta']}\nAgência: {conta['agencia']}\n{'-'*30}');

def Menu():
    print('''\n
      ---------------MENU--------------
        1 - Depositar
        2 - Saque
        3 - Extrato
        4 - Cadastrar Usuário
        5 - Cadastrar Conta
        6 - Listar Usuários
        7 - Listar Contas
        8 - Sair
      ''');

saque = 0;
deposito = 0;
saldo = 1400;
extrato = '';
numero_saques = 0;
LIMITE_SAQUES = 3;
AGENCIA = '0001';

numero_conta = 1;
usuarios = [];
contas = [];

while True:
    Menu();
    opcao = input('\nInforme a opção desejada: ');
    print();
    match opcao:
        case '1':
            deposito = float(input('\nInforme o valor do depósito: '));    
            saldo, extrato = Depositar(saldo, deposito, extrato)  ;
        case '2':
           saque = float(input('\nInforme o valor do saque: '));
           saldo, extrato, numero_saques = Saque(saldo=saldo, valor=saque, extrato=extrato, limite=500, numero_saques=numero_saques, limite_saques=3);
        case '3':
            Extrato(saldo, extrato=extrato);   
        case '4':
            Cadastra_usuario();
        
        case '5':
            numero_conta = Cadastra_conta(numero_conta, AGENCIA);

        case '6':
            Listar_usuarios();
        
        case '7':
            Listar_contas();
        
        case '8':
            break;
        
        case _:
            print('Informe uma opção válida!');