import this
import Exercicio_01
import Exercicio_02
import Exercicio_03
import Exercicio_04
import Exercicio_05

this.opcao = 0

num = 0
def coletarNum():#exercicio 2
    print('Informe o número para ver o seu antecessor')
    this.num = int(input())


base = 0
altura = 0
def coletarBase():
    print('Informe a Base do triângulo: ')
    this.base = float(input())

def coletarAltura():
    print('Informe a Altura do triângulo: ')
    this.altura = float(input())


anos = 0
meses = 0
dias = 0
def coletarAnos():
    print('Informe quantos anos você tem: ')
    this.anos = int(input())

def coletarMeses():
    print('Informe quantos meses você tem: ')
    this.meses = int(input())

def coletarDias():
    print('Informe quantos dias você tem: ')
    this.dias = int(input())


votosNulos = 0
votosBrancos = 0
votosValidos = 0
eleitores = 0
def coletarEleitores():
    print('Informe o número de eleitores do município: ')
    this.eleitores = int(input())

def coletarValidos():
    print('Informe o número de votos válidos: ')
    this.votosValidos = int(input())

def coletarBrancos():
    print('Informe o número de votos brancos: ')
    this.votosBrancos = int(input())

def coletarNulos():
    print('Informe o número de votos nulos: ')
    this.votosNulos = int(input())




def Menu():
    print('Escolha uma das opções abaixo:\n\n'+
          '\n1. Exercício 1'+
          '\n2. Exercício 2'+
          '\n3. Exercício 3'+
          '\n4. Exercício 4'+
          '\n5. Exercício 5'+
          '\n6. Sair')
    this.opcao = int(input())

def operacao():
    #Mostrar o menu em tela
    while this.opcao != 6:
        Menu()
        #realizar operações
        if this.opcao == 1:
            #operacao para exerc1
            Exercicio_02.exibir()
        elif this.opcao == 2:
            #operacao para exerc2
            coletarNum()
            print('Seu antecessor é: ' + str(Exercicio_02.exibir(this.num)))
        elif this.opcao == 3:
            #operacao para exerc3
            coletarBase()
            coletarAltura()
            print('Sua área é: ' + str(Exercicio_03.calcularArea(this.base, this.altura)))
        elif this.opcao == 4:
            #operacao para exerc4
            coletarAnos()
            coletarMeses()
            coletarDias()
            print('Seu ano em dias é: ' + str(Exercicio_04.retorne()))
        elif this.opcao == 5:
            #operacao para exerc5
            coletarEleitores()
            coletarValidos()
            coletarBrancos()
            coletarNulos()
            print('O percentual de votos válidos é: ' + Exercicio_05.percentualValidos())
            print('O percentual de votos brancos é: ' + Exercicio_05.percentualBrancos())
            print('O percentual de votos nulos é: ' + Exercicio_05.percentualNulos())
        elif this.opcao == 6:
            print('Obrigado!')
        else:
            print('Opcao escolhida inválida! Tente novamente com as opções fornecidas.')
