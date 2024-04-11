LIMITE_SAQUES = 3

#Variáveis de controle
opcao = -1
conta_corrente = 0
extrato = ""
numero_saques = 0

#Loop principal 
while opcao != 0:

  #Menu usuário
  opcao = int(input("[1] Deposito\n[2] Saque\n[3] Extrato\n[0] Sair\n"))

  #Opção para depósito
  if opcao == 1:
    deposito = int(input("Digite o valor do depósito:\n"))

    #Testa se o depósito é maior que 0
    if deposito > 0:
      conta_corrente += deposito
      extrato += f"Depósito: R$ {deposito:.2f}\n"
    else:
      print("Valor inválido")

  #Opção para saque   
  elif opcao == 2:

    #Testa primeiro se o usuário não atingiu o limite de saques diários
    if numero_saques == LIMITE_SAQUES:
      print("Você ja atingiu o limite de 3 saques diários")
    else:
      saque = int(input("Qual o valor que deseja sacar?"))
      print(f"Você sacou {saque:.2f}")
      conta_corrente -= saque
      extrato += f"Saque: R$ {saque:.2f}"
      numero_saques += 1

      #Testa se o saque do usuário ultrapassa o limite de 500 reais por saque
      if saque > 500:
        print("Você só pode sacar 500 reais por vez")
      #Testa se o o usuário tem saldo suficiente na conta
      elif saque > conta_corrente:
        print(f"Você tem R$ {conta_corrente:.2f} na sua conta")

  #Opção para retirar o extrato
  elif opcao == 3:
    print(extrato)

#Opção para sair do sistema
else:
  print("Saindo")
  