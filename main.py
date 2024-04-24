menu = """\n
#########MENU##########
[n]\tNova Conta
[l]\tListar contas

[d]\tDepositar
[s]\tSacar
[sa]\tSaldo
[e]\tExtrato

[q]\tSair

#######################
"""

lista_contas = [0]

bd = [

]

class Conta:
    def __init__(self, nome):

        self.numero = lista_contas[-1] + 1
        self.nome = nome
        self.saldo = 0
        self.qtd_saque = 0
        self.extrato = []

        lista_contas.append(self.numero)
    def  depositar(self, valor):
        self.saldo += valor
        self.extrato.append({"deposito": valor})
        print("Deposito realizado com sucesso!")
        return True

    def sacar(self, valor):
        if self.qtd_saque > 3:
            print("Operação falhou! Número máximo de saques excedido.")
            return False
        
        if self.saldo >= valor:
            self.saldo -= valor
            self.extrato.append({"saque": valor})
            self.qtd_saque += 1
            print("Saque realizado com sucesso!")
            return True
        
        else:
            print("Operação falhou! Saldo insuficiente.")
            return False


    def ler_extrato(self):
        print("Extrato:")
        if self.ler_extrato == []:
            print("Sem movimentações")
            return False
        
        for extrato in self.extrato:
            print(extrato)
        return True
    

    def ler_saldo(self):
        print(str(self.saldo))
        return True

    
    

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)


    if opcao == "n":
        print("Criando uma nova conta...")
        nome = input("Infome o nome do cliente: ")
        conta = Conta(nome)
        bd.append(conta)
        print(f"Conta criada com sucesso!\nNumero da conta: {conta.numero}\nNome do cliente: {conta.nome}")


    if opcao == "l":
        print(bd)
        print("Listando contas...")
        for conta in lista_contas:
            print(conta)

    if opcao == "d":
        numero = input("Infome o numero da conta: ")

        for conta in bd:
            if conta.numero == int(numero):
                conta.depositar(int(input("Infome o valor a ser depositado: ")))

            else:
                print("Conta inexistente!")

    elif opcao == "s":
        numero = int(input("Infome o numero da conta: "))
        
        for conta in bd:
            if int(conta.numero) == int(numero):
                valor = int(input("Infome o valor a ser sacado: "))
                conta.sacar(valor)

            else:
                print("Conta inexistente!")

    elif opcao == "sa":
        numero = input("Infome o numero da conta: ")
        
        for conta in bd:
            if int(conta.numero) == int(numero):
                conta.ler_saldo()

            else:
                print("Conta inexistente!")


    elif opcao == "e":
        numero = input("Infome o numero da conta: ")
        
        for conta in bd:
            if conta.numero == int(numero):
                conta.ler_extrato()

            else:
                print("Conta inexistente!")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")