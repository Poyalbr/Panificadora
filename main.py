import os

######## MENU #########
while(True): # loop infinito  
  # Imprime na tela o menu
  print("1 - Nova Venda")
  print("2 - Gerar relatório")
  print("3 - Sobre")
  print("4 - Sair")

  # Pegar a opção do usuário
  opcao = input("Digite a opção desejada: ")

  # Verificar qual opção o usuário escolheu
  if (opcao == "1"): #se 
    os.system('clear') #limpa a tela
    print("Nova venda")
    sal_qt = int(input("Digite a quantidade Pães de Sal: "))
    leite_qt = int(input("Digite a quantidade Pães de Leite: "))
    milho_qt = int(input("Digite a quantidade Pães de Milho: "))
    total = sal_qt + leite_qt + milho_qt
    print("Total de pães: %.0f deu R$ %.2f" % (total, total*0.25))

    input("\n\nPressione ENTER para continuar: ")
    os.system('clear') #limpa a tela
  elif(opcao == "2"): #senao se
    print("Relatório")
  elif(opcao == "3"):
    print("Sobre")
  elif(opcao == "4"):
    print("Sair")
    break #interrompe a executação do laço
  else:
    print("Opção inválida, tente novamente!")  
  
print("Programa finalizado!")
