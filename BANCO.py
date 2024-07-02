menu = """
       MENU

 [1] DEPOSITAR
 [2] SACAR
 [3] EXTRATO
 [4] SAIR

 """
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limites_saques = 3

while True:

    opcao = input(menu)
    
    if opcao == "1":

        valor =float(input("Informe o valor do Deposito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito:  R$ {valor:.2f}\n"

        else:
            print("Opção invalida, informe um valor real !")
    
    elif opcao == "2":
      
      valor= float(input("Informe o valor do saque: "))

      excedeu_saldo = valor > saldo

      excedeu_limite = valor > limite

      excedeu_saques = numero_saques >= limites_saques

      if excedeu_saldo:
          print("Você não tem saldo suficiente. ")
        
      elif excedeu_limite:
          print("O valor do saque excedeu limite permitido por saque. ")        
      
      elif excedeu_saques:
          print("Você excedeu o limite de saques diarios!")
        
      elif valor > 0:
          saldo -= valor
          extrato += f"Saque: R${valor:.2f}\n"
          numero_saques += 1
      
      else:
          print("Operação falhou, o valor informado é invalido!")
      
        

    
    elif opcao == "3":
        print ("\n================Extrato================")
        print("Não foram realizados movimentações. " if not extrato else extrato)
        print(f"\n Saldo:  R$ {saldo:.2f}")
        print("==========================================")
    
    elif opcao == "4":
        break
    
    else:
        print("Operação invalida, por favor selecione novamente a opção desejada !")