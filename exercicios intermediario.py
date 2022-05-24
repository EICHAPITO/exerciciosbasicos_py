#1----------------------------------------
"""
#saber se as sequencias digitadas sao identicas

seqA=float(input("digite uma sequencia de numeros:"))
seqB=float(input("digite uma sequencia de numeros:"))

if seqA == seqB:
          print("identicas")
else:
          print("diferentes")
"""
#__________________________________________________________
#2--------------------------------------------------
"""
#leia um arquivo

nome=input("digite o nome do arquivo que vc deseja abrir:")
arquivo=open(nome)
linhas=arquivo.readlines()
for linha in linhas:
          print(linha)
"""       
#____________________________________________________________
#3-------------------------------------------------
"""
#escrever em um arquivo de texto

seq=input("digite uma sequencia:")

arquivo=open("seq2.txt","w")
arquivo.write(seq)
arquivo.close()
"""
#___________________________________________________________
#4--------------------------------------------------
"""
#fazer um meno para ler um arquivo, ou para imprimir o conteudo do arquivo e depois para sair do programa

print("digite 1 para ler um arquivo txt")
print("digite 2 para imprimir o conteudo do arquivo")
print("digite 3 para sair do programa")

def abrir():
          nome=input("digite o nomedo arquivo:")
          arquivo=open(nome)
          return arquivo

def ler(arquivo):
          linhas=arquivo.readlines()
          for linha in linhas:
                    print(linha.strip())

choosen=int(input("digite o que voce quer fazer:[1/2/3]"))
while choosen>3:
          print("nao entendi, digite novamente")
          choosen=int(input("digite o que voce quer fazer:[1/2/3]"))

while choosen!=3:
          if choosen == 1:
                    arquivo=abrir()
          if choosen == 2:
                    ler(arquivo)
          choosen=int(input("digite o que voce quer fazer:[1/2/3]"))

if choosen == 3:
          exit()
"""
#__________________________________________________________________















