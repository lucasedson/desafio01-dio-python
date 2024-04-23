import os

menu = """
1 - Depositar
2 - Sacar
3 - Extrato
4 - Sair
"""

conta_bancaria = {
    "Saldo": 0,
    "Extrato": [],
    "numero_saques": 0
}


def depositar(valor):
    conta_bancaria["Saldo"] += valor
    conta_bancaria["Extrato"].append(f"Deposito de {valor}")
    print("Deposito realizado com sucesso")
    

def sacar(valor):
    if conta_bancaria["numero_saques"] > 3:
        print("Limite de saques excedido")
        return
    
    if conta_bancaria["Saldo"] - valor > 0:
        conta_bancaria["Saldo"] -= valor
        conta_bancaria["Extrato"].append(f"Saque de {valor}")
        conta_bancaria["numero_saques"] += 1
        print("Saque realizado com sucesso")
        return 

    print("Saldo insuficiente")
def extrato():
    print(f"Saldo: {conta_bancaria['Saldo']}")
    print("Extrato:")
    for movimentacao in conta_bancaria["Extrato"]:
        print(movimentacao)

os.system("clear")
while True:
    print("#"*25,"BANCO","#"*25)
    opcao = input(menu)
    print("#"*25,"#####","#"*25)

    if opcao == "1":
        valor = float(input("Quanto deseja depositar? "))
        depositar(valor)
    elif opcao == "2":
        valor = float(input("Quanto deseja sacar? "))
        sacar(valor)
    elif opcao == "3":
        extrato()
    elif opcao == "4":
        break
    else:
        print("Opção inválida")

    input("Pressione qualquer tecla para continuar...")
    os.system("clear")
