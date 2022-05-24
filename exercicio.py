#1-----------------------------------------------
"""
n1,n2,n3,n4,n5,n6=2,3,4,5,10,12
result=(n6/n1)+n3+n5+n2-n4
print(result)
"""

#2-----------------------------------------------
"""
#fazer a soma, substituição, multiplicação, divisão e pegar o resto da divisão de dois números

n1=int(input("Digite o primeiro numero:"))
n2=int(input("Digite o segundo numero:"))

if n1>=n2:
          n3=n1
          n4=n2
else:
          n3=n2
          n4=n1

soma=n3+n4
sub=n3-n4
mult=n3*n4
div=n3/n4
res=n3%n4

print("soma:",n1,"+",n2,"=",soma)
print("subtração:",n1,"-",n2,"=",sub)
print("multiplicação:",n1,"x",n2,"=",mult)
print("divisão:",n1,"/",n2,"=",div)
print("resto:",n3,"%",n4,"=",res)
"""
#3------------------------------------------------
"""
#fazer a média das notas de um aluno

n1=int(input("entre com a nota:"))
n2=int(input("entre com a nota:"))
n3=int(input("entre com a nota:"))
n4=int(input("entre com a nota:"))
qtd=int(input("digite a quantidade de notas:"))

media=(n1+n2+n3+n4)/qtd

print("Média:",media)
"""
#4------------------------------------------------
"""
#fazer o cálculo de quanto alguém ganha no mês

ganho=int(input("entre com quanto vc ganha por hora:"))
hr=int(input("entre com a quantidade de horas q vc trabalha no dia:"))
d=int(input("entre com a quantidade de dias q vc trabalha no mes:"))

Tt=ganho*hr*d

print("no mes vc ganha:",Tt)
"""
#5------------------------------------------------
"""
#fazer uma mensagem de boas vindas para o usuário

nome=input("digite seu nome:")
print("seja bem vindo,",nome)
"""
#6------------------------------------------------
"""
#fazer um programa que armazene e mostre o dia, mês e ano

di=int(input("Dia:"))
while di<=0 or di>=32:
          print("Erro! tente novamente")
          di=int(input("Dia:"))
if di>0 and di<32:
          do=di
          
mi=int(input("Mes:"))
while mi<=0 or mi>=13:
          print("Erro! tente novamente")
          mi=int(input("Mes:"))
if mi>0 and mi<13:
          mo=mi
          
a=int(input("Ano:"))

print(do,"/",mo,"/",a)
"""
#7------------------------------------------------
"""
#mostrar o antecessor e o sucessor de um número 

n=int(input("Digite um numero:"))
ant=n-1
dps=n+1
print("antecessor:",ant)
print("sucessor:",dps)
"""
#8------------------------------------------------
"""
#fazer o dobro, o triplo, e a raiz quadrada de um número

n=int(input("digite um numero:"))
dobro=n*2
triplo=n*3
import math
rqz=math.sqrt(n)

print(dobro,triplo,rqz)
"""
#9-----------------------------------------------
"""
#fazer um programa que converta metros em centimetros e milimetros

m=float(input("digite quantos metros deseja converter:"))
cent=m*100
mili=cent*10

print("centimetros:",cent,"milimetros:",mili)
"""
#10----------------------------------------------
"""
#fazer a tabuada de um numero

n=int(input("digite um numero:"))
n0=n*0
n1=n*1
n2=n*2
n3=n*3
n4=n*4
n5=n*5
n6=n*6
n7=n*7
n8=n*8
n9=n*9
print(n,"x 0 = ",n0)
print(n,"x 1 = ",n1)
print(n,"x 2 = ",n2)
print(n,"x 3 = ",n3)
print(n,"x 4 = ",n4)
print(n,"x 5 = ",n5)
print(n,"x 6 = ",n6)
print(n,"x 7 = ",n7)
print(n,"x 8 = ",n8)
print(n,"x 9 = ",n9)
"""
#11--------------------------------------------
"""
#fazer um conversor para dolar

n=float(input("digite quanto vc tem na carteira:"))
dol=4.2
conv=n/dol

print("vc tem:",n,"$, q corresponde a:",conv,"dolares")
"""
#12--------------------------------------------
"""
#fazer um programa que calcule a quantidade de tinta necessária para pintar uma parede

h=float(input("digite a altura:"))
l=float(input("digite a largura:"))
S=h*l
qtd=S/2

print("serão necessários:",qtd,"litros de tinta")
"""
#13--------------------------------------------
"""
#fazer um programa que aplica 5% de desconto 

preco=float(input("digite o preço:"))
predi=(5*preco)/100
predio=preco-predi
print("preço com desconto:",predio)
"""
#14---------------------------------------------
"""
#fazer um programar que mostre o salário de alguem com um aumento de 15%

salario=float(input("digite o salario:"))
sali=(15*salario)/100
salio=sali+salario
print("salario com aumento:",salio)
"""
#15----------------------------------------------
"""
#fazer um conversor de celsius para fahrenheit

c=float(input("digite a temperatura em celsius:"))
f=c+32
print(f,"F")
"""













      
