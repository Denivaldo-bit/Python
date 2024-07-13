
#desafio 2
# TODO: Crie uma Lista 'itens' para armazenar os equipamentos:
itens = []

# TODO: Crie um loop para solicita os itens ao usuário:
for i in range(3):
# TODO: Solicite o item e armazena na variável "item":
  item = input("Insira o equipamento {}: ".format(i + 1))
# TODO: Adicione o item à lista "itens":
  itens.append(item)

# Exibe a lista de itens
  print("Lista de Equipamentos:")  
  for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")

#ou
#Em Python existe várias formas de implementar o STDIN e STDOUT recomendamos utilizar sys.stdin.readline para o STDIN e o print para o STDOUT.
#Exemplo:
#import sys
#a = int(sys.stdin.readline()) // Lê a linha de entrada
#print(a); // Imprime o dado

#import sys
# Crie uma Lista 'itens' para armazenar os equipamentos:

#itens = []

# Crie um loop para solicitar os itens ao usuário:
#for i in range(3):
    # Solicite o item e armazena na variável "item":
#   item = sys.stdin.readline().strip()
    
    # Adicione o item à lista "itens":
#    itens.append(item)

# Exibe a lista de itens
#print("Lista de Equipamentos:")
#for item in itens:
    # Loop que percorre cada item na lista "itens"
 #   print(f"- {item}")