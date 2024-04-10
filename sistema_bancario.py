LIMITE_SAQUES = 3

opcao = -1
conta_corrente = 0
extrato = ""
numero_saques = 0

while opcao != 0:
  opcao = int(input("[1] Deposito\n[2] Saque\n[3] Extrato\n[0] Sair\n"))
  if opcao == 1:
    deposito = int(input("Digite o valor do depósito:\n"))
    if deposito > 0:
      conta_corrente += deposito
      extrato += f"Deposito: R$ {deposito:.2f}\n"
    else:
      print("Não é aceito valor negativo")
  elif opcao == 2:
    if numero_saques == LIMITE_SAQUES:
      print("Você ja atingiu o limite de 3 saques")
    else:
      saque = int(input("Qual o valor que deseja sacar?"))
      print(f"Você sacou {saque:.2f}")
      conta_corrente -= saque
      extrato += f"Saque: R$ {saque:.2f}"
      numero_saques += 1
      if saque > 500:
        print("Você só pode sacar 500 reais por vez")
      elif saque > conta_corrente:
        print(f"Você tem R$ {conta_corrente:.2f} na sua conta")
  elif opcao == 3:
    print(extrato)
else:
  print("Saindo")
  