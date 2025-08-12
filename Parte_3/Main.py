from abc import ABC, abstractmethod
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []
        
    def Realizar_transacao(self, conta, transacao):
        transacao.Registrar(conta)
        
    def Adicionar_conta(self, conta):
        self._contas.append(conta)
        
    @property
    def contas(self):
        return self._contas
        
class Pessoa_fisica(Cliente):
    def __init__(self, endereco, cpf, nome, nascimento):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._nascimento = nascimento
        
    def __str__(self):
        return f'\nNome: {self._nome}'
    
    @property
    def cpf(self):
        return self._cpf
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def nascimento(self):
        return self._nascimento
    
    @property
    def endereco(self):
        return self._endereco

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def Nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def Saldo(self):
        return self._saldo
    
    @property
    def Numero(self):
        return self._numero
    
    @property
    def Agencia(self):
        return self._agencia
    
    @property
    def Cliente(self):
        return self._cliente
    
    @property
    def Historico(self):
        return self._historico
    
    def Sacar(self, valor):
        saldo = self._saldo
        if valor > saldo:
            print('\nO valor excede o saldo atual')
        
        elif valor > 0:
            self._saldo -= valor
            print('\nSeu saque foi realizado com sucesso!')
            return True
        
        else:
            print('\nO Valor informado é inválido!')
            
        return False
    
    def Depositar(self, valor):
        if(valor < 1):
            print('o valor deve ser maior ou igual a 1');
            return False
        self._saldo += valor
        print('Depósito realizado!')
        return True
    
class Conta_Corrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques
        
    def Sacar(self, valor):
        numero_saques = len([transacao for transacao in self._historico.transacoes if transacao['tipo'] == 'Saque'])
        if valor > self._limite:
           print('\nO valor excede o limite!') 
        
        elif numero_saques >= self._limite_saques:
            print('\nO limite de saques foi atingido!')
      
        else:
            return super().Sacar(valor)
        
        return False
    
    def __str__(self):
        return f'\nNumero: {self._numero}\nAgência: {self._agencia}\nCliente: {self._cliente}'
                              
class Historico:
    
    def __init__(self):
        self._transacoes = []
        
    @property
    def Transacoes(self):
        return self._transacoes
        
    
    def Adicionar_transacao(self, transacao):
        self.transacoes.append({
            'tipo' : transacao.__class__.__name__,
            'valor' : transacao.valor,
            'data' : datetime.now().strftime('%d-%m-%Y %H:%M:%S')})
        
    @property
    def transacoes(self):
        return self._transacoes

class Transacao(ABC):
    
    @property
    @abstractmethod
    def valor(self):
        ...
    
    @abstractmethod
    def Registrar(self, Conta):
        ...
    
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor
    
    def Registrar(self, conta):
        transacao_efetuada = conta.Sacar(self.valor)
        
        if transacao_efetuada:
            conta.Historico.Adicionar_transacao(self)
            
class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor
    
    def Registrar(self, conta):
        transacao_efetuada = conta.Depositar(self.valor)
        
        if transacao_efetuada:
            conta.Historico.Adicionar_transacao(self)    

def Titulo(mensagem=''):
        print(f'\n{mensagem:=^30}')
    
def Menu():
    Titulo('Bem vindo');
    print('''
    1 - Depositar
    2 - Saque
    3 - Extrato
    4 - Cadastrar Usuário
    5 - Cadastrar Conta
    6 - Listar Contas
    7 - Sair
    ''');

def Buscar_cliente(cpf, clientes):
    cliente = [cliente for cliente in clientes if cliente.cpf == cpf]
    return cliente[0] if cliente else None
    
def Buscar_conta(cliente, numero):
    for conta in cliente.contas:
        if conta.Numero == numero:
            return conta
    print('\nO usuário não possui a conta informada')
    return None
         
def Depositar(clientes):
    cpf = input('Informe o cpf do cliente: ').strip()
    cliente = Buscar_cliente(cpf, clientes)
    
    if not cliente:
        print('\nCliente não encontrado')
        return
    
    conta_existe = int(input('Informe o número da conta: ').strip())
    conta = Buscar_conta(cliente, conta_existe)
    
    if not conta:
        return 'A conta informada não foi encontrada'
    
       
    valor = float(input('Informe o valor a ser depositado: '))
    transacao = Deposito(valor)
    
    cliente.Realizar_transacao(conta, transacao)
    
def Sacar(clientes):
    cpf = input('Informe o cpf do cliente: ').strip()
    cliente = Buscar_cliente(cpf, clientes)
    
    if not cliente:
        print('\nCliente não encontrado')
        return
    
    conta_existe = int(input('Informe o número da conta: ').strip())
    conta = Buscar_conta(cliente, conta_existe)
    
    if not conta:
        return 'A conta informada não foi encontrada'
    
    
    valor = float(input('Informe o valor a ser sacado: '))
    transacao = Saque(valor)
    
    cliente.Realizar_transacao(conta, transacao)
    
def Extrato(clientes):
    cpf = input('Informe o cpf do cliente: ').strip()
    cliente = Buscar_cliente(cpf, clientes)
    
    if not cliente:
        print('\nCliente não encontrado')
        return
    
    conta_existe = int(input('Informe o número da conta: ').strip())
    conta = Buscar_conta(cliente, conta_existe)
    
    if not conta:
        return 'A conta informada não foi encontrada'
    
    Titulo('Extrato')
    
    transacoes = conta.Historico.Transacoes
    extrato = ''
    if not transacoes:
        print('\nNão foram realizadas transações!')
    else:
        for transacao in transacoes:
            extrato += f'\n{transacao['tipo']}:\n\tR${transacao['valor']:.2f}'
    
    print(extrato)
    print(f'\nSaldo:\n\t{conta.Saldo:.2f}')
    Titulo()
    
def Criar_conta(numero, clientes, contas):
    cpf = input('Informe o cpf do cliente: ').strip()
    cliente = Buscar_cliente(cpf, clientes)
    
    if not cliente:
        print('\nCliente não encontrado')
        return
    
    conta = Conta_Corrente.Nova_conta(cliente, numero)
    contas.append(conta)
    cliente.contas.append(conta)
    print('\nConta criada com sucesso')
        
def Criar_cliente(clientes):
    cpf = input('Informe o cpf do cliente: ').strip()
    cliente = Buscar_cliente(cpf, clientes)  
    if cliente:
        print('\nO cliente já está cadastrado')
        return
    
    nome = input('Informe o nome do cliente: ').strip()
    nascimento = input('Informe o nascimento do cliente: ').strip()
    endereco = input('Informe o endereço do cliente: ').strip()
    
    cliente = Pessoa_fisica(endereco, cpf, nome, nascimento);
    clientes.append(cliente);
    
def Listar_contas(contas):
    Titulo('Listagem de Contas')
    for conta in contas:
        print(conta)
                        
class Main():
    clientes = []
    contas = []
    
    while True:
        Menu();
        opcao = input('\nInforme a opção desejada: ');
        print();
        match opcao:
            case '1':
                Depositar(clientes)
            case '2':
                Sacar(clientes)
            case '3':
                Extrato(clientes)
            case '4':
                Criar_cliente(clientes)
            case '5':
                Criar_conta(len(contas)+1, clientes, contas)
            case '6':
                Listar_contas(contas)    
            case '7':
                break
                