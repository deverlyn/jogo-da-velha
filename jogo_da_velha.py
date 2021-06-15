import os

#função de montar menu
def menu():
  print("\n \n")
  print("****************** MENU ******************")
  print("*   1 - Criar novo Jogador               *")
  print("*   2 - Exibir histórico de um jogador   *")
  print("*   3 - Excluir um Jogador               *")
  print("*   4 - Iniciar uma Partida              *")
  print("******************************************")
  opcao = input("\nEscolha uma das Opções acima: ")
  main(opcao)


#função principai ou main
#verifica o caminh0o que o usuário deseja seguir durante o jogo
#separada da funão menu apenas para encurtar o codigo desta
def main(escolha):
 
  if(escolha == "1"):
    criaNovoJogador()
 
  elif(escolha == "2"):
    apresentaHistorico()
 
  elif(escolha == "3"):
    excluiJogador()
 
  elif(escolha == "4"):
    jogadores()
 
  else:
    print("\nOpção Inválida!!\n") 
    menu()

#função que cria um novo jogador 
def criaNovoJogador():
  nome = input("Digite o nome do Jogador: ")

  nome = nome.strip()
   
  if os.path.isfile("./usuarios/"+nome+".txt"):
    print("Usuário já exixtente! \n Tente novamente!!")
    criaNovoJogador()

  elif nome == '':
    print("O nome não pode ser vazio! \n Tente novamente!!")
    criaNovoJogador()
  
  else:
    arquivo = open("./usuarios/"+nome+".txt", "w")
    arquivo.write("0\n")
    arquivo.write("0")
    arquivo.close()
    print("Usuário "+nome+" criado.")
    menu()

#função que apresenta o historico dos jogadores
def apresentaHistorico(jogador = ''):
  if jogador == '':
    nome = input("Digite o nome do jogador: ")
  else:
    nome = jogador
 
  if os.path.isfile("./usuarios/"+nome+".txt"):
    arquivo = open("./usuarios/"+nome+".txt")
    historico = arquivo.readlines()
    print("Vitórias "+historico[0])
    print("Derrotas "+historico[1])
    menu()

  else:
    print(nome+" não é um usuário cadastrado!")
    apresentaHistorico()

#função que exclui um jogador
def excluiJogador():
  nome = input("Digite o nome do jogador a ser excluído: ")
 
  if os.path.isfile("./usuarios/"+nome+".txt"):
    validacao = input("Tem certeza desta ação? \nEla é permanente e não poderá ser desfeita!\n Didite s para sim e n para não: ")
 
    if validacao.lower() == "s":
      os.remove("./usuarios/"+nome+".txt")
      print("Usuário "+nome+" excluído!")
      menu()
 
    else:
      menu()
 
  else:
    print(nome+" não é um usuário cadastrado!")
    excluiJogador()

#tabuleiro 
matriz = [[' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' '], 
          [' ', ' ', ' ', ' ', ' '],
          [' ', ' ', ' ', ' ', ' ']]
#Jogada X ou O          
Jogada = ''
#indice linha
linha = 0
#indice coluna
coluna = 0
#lista que conterá o nome dos jogadores
jogadoresnome = []
#lista que conterá o histórico do jogador com a jogada X
historicoX = [0,0]
#lista que conterá o histórico do jogador com a jogada O
historicoO= [0,0]

#função que limpa o tabuleiro
def limpaMatriz():
 
  for x in range(5):
    for y in range(5):
      matriz[x][y] = " "

#fução para iniciar o jogo 
#recolhe os dados dos jogadores e preenche nas variáveis
def jogadores():

  jogadorX = input("Digite o nome do jogador X: ")
  jogadorX = jogadorX.strip()#retira os espaçoes do nome
  if os.path.isfile("./usuarios/"+jogadorX+".txt"):
    arquivoX = open("./usuarios/"+jogadorX+".txt", "r")
    hX = arquivoX.readlines()

  else:
   
    condicao = input("Jogador ainda não cadastrado \n Deseja cadastralo antes de começar? \n digite s para sim e n para não: ")
    
    if condicao.lower() == "s":
      criaNovoJogador()
    
    else:
      jogadores()
  
  jogadorO = input("Digite o nome do jogador O: ")
  jogadorO = jogadorO.strip()
  
  if os.path.isfile("./usuarios/"+jogadorO+".txt"):
    
    arquivoO = open("./usuarios/"+jogadorO+".txt", "r")
    hO = arquivoO.readlines()
  
  else:
    
    condicao = input("Jogador ainda não cadastrado \n Deseja cadastralo antes de começar? \n digite s para sim e n para não: ")
    
    if condicao.lower() == "s":
      criaNovoJogador()
   
    else:
      jogadores()
  
  i = 0
  
  for x in hO:
    historicoO[i] = int(x)
    i+=1
  
  i  = 0
  
  for y in hX:
    historicoX[i] = int(y)
    i+=1

  jogadoresnome.append(jogadorX)
  jogadoresnome.append(jogadorO)
  
  limpaMatriz()
  iniciaJogo(0)
  
#função principal do jogo
# - verifica o vencedor
# - retorna o placar
# - inicia a partida e determina a jogada
def iniciaJogo(jogador):
    
  montaTabuleiro()

  linha = int(input("\nDigite a linha desejada: "))

  if linha < 0 or linha > 5:
    
    print("Opção Indisponível!! \n Jogue novamente")
    iniciaJogo(jogador)

  coluna = int(input("\nDigite a coluna desejada: "))

  if coluna < 0 or coluna > 5 :
    
    print("Opção Indisponível!! \n Jogue novamente")
    iniciaJogo(jogador)

  if(jogador%2==0):
    
    jogada = "X"
    
  else:
    
    jogada = "O"

  if(matriz[linha][coluna]==" "):
    
    matriz[linha][coluna] = jogada
  
  else:
    
    print("Opção Indisponível!! \n Jogue novamente")
    iniciaJogo(jogador)

  if verificaLinha() or verificaColuna() or verificaDiagonal():
    vencedor = ''
    
    if jogador %2==0:
    
      print("Parabéns!! Vitória do Jogador "+ jogadoresnome[0])
      historicoX[0] +=1
      historicoO[1] +=1
      vencedor = jogadoresnome[0]
    
    else:
    
      print("Parabéns!! Vitória do Jogador "+jogadoresnome[1])
      historicoO[0]+=1
      historicoX[1]+=1
      vencedor = jogadoresnome[1]
      
    arqX = open("./usuarios/"+jogadoresnome[0]+".txt", "w")
    arqO = open("./usuarios/"+jogadoresnome[1]+".txt", "w")

    arqO.write(str(historicoO[0])+"\n")
    arqO.write(str(historicoO[1]))
    arqO.close()

    arqX.write(str(historicoX[0])+"\n")
    arqX.write(str(historicoX[1]))
    arqX.close()

    montaTabuleiro()
    apresentaHistorico(vencedor)
    menu()

  if verificaEmpate():
  
    print("Ah que pena!! deu velha \n Tente novamente ")
    menu() 
  
  iniciaJogo(jogador+1)

#função que verifica valores iguais em uma linha da matriz
#retorna a quantidade de valores iguais encontrados
def verificaLinha():
  
  for x in range(5):
    if matriz[x][0] == matriz[x][1] and matriz[x][1] == matriz[x][2] and matriz[x][2] == matriz[x][3] and matriz[x][0] != ' ' or matriz[x][1] == matriz[x][2] and matriz[x][2] == matriz[x][3] and matriz[x][3] == matriz[x][4] and matriz[x][1] != ' ':
      return True
  return False

#função que verifica vitória em coluna
def verificaColuna():

  for x in range(5):
    if matriz[0][x] == matriz[1][x] and matriz[1][x] == matriz[2][x] and matriz[2][x] == matriz[3][x] and matriz[0][x] != ' ' or matriz[1][x] == matriz[2][x] and matriz[2][x] == matriz[3][x] and matriz[3][x] == matriz[4][x] and matriz[1][x] != ' ':
      return True
  return False
  
#função que verifica valores iguais na diagonal 
#retorna 4 para seguir o mesmo padrão de verificação das funções anteriores
def verificaDiagonal():
  
  if matriz[0][0] != " " and matriz[0][0] == matriz[1][1] and matriz[1][1] == matriz[2][2] and matriz[2][2]== matriz[3][3]:
    return True
  
  elif matriz[1][0] !=" " and matriz[1][0] == matriz[2][1] and matriz[2][1] == matriz[3][2] and matriz[3][2] == matriz[4][3]:
    return True
  
  elif matriz[0][4] != " " and matriz[0][4] == matriz[1][3] and matriz[1][3] == matriz[2][2] and matriz[2][2] == matriz[3][1]:
    return True
  
  elif matriz[1][4] !=" " and matriz[1][4] == matriz[2][3] and matriz[2][3] == matriz[3][2] and matriz[3][2] == matriz[4][1] :
    return True
  

  if matriz[4][0] != " " and matriz[4][0] == matriz[3][1] and matriz[3][1] == matriz[2][2] and matriz[2][2]== matriz[1][3]:
    return True
  
  elif matriz[4][4] !=" " and matriz[4][4] == matriz[3][3] and matriz[3][3] == matriz[2][2] and matriz[2][2] == matriz[1][1]:
    return True
  
  elif matriz[3][4] != " " and matriz[3][4] == matriz[2][3] and matriz[2][3] == matriz[1][2] and matriz[1][2] == matriz[0][1]:
    return True
  
  elif matriz[0][3] !=" " and matriz[0][3] == matriz[1][2] and matriz[1][2] == matriz[2][1] and matriz[2][1] == matriz[3][0] :
    return True
  return False

#função que cria e monta o tabuleiro
def montaTabuleiro():
  print("\n--------------------------")
  
  for x in range(5):
    
    for y in range(5):
      print("| "+matriz[x][y]+"  ", end="")
    
    print("| %d"%x)
    print("--------------------------")
  
  print("   0    1    2    3    4  ")

#função que verifica empate
def verificaEmpate():
  contador = 0
  for x in range(5):
    if matriz[x][0] != ' ' and matriz[x][1] != ' ' and matriz[x][2] != ' ' and matriz[x][3] != ' ' and matriz[x][4] != ' ':
      contador +=1
      
  if contador == 5:
    return True
  return False

  
#chamada do menu para inicio do game
menu()