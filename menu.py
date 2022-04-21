import this
import Exercicio_01
import Exercicio_02
import Exercicio_03
import Exercicio_04
import Exercicio_05
import Exercicio_06
import Exercicio_07
import Exercicio_08
import Exercicio_09
import Exercicio_10
import Exercicio_11
import Exercicio_12
import Exercicio_13
import Exercicio_14

this.opcao = 0
this.numT = 0
this.contador = 0
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


salario = 0
percentualReajuste = 0
def coletarSalario():
    print('Informe o salário mensal atual do funcionário: ')
    this.salario = float(input())
def coletarPercentualReajuste():
    print('Informe o percentual de reajuste: ')
    this.percentualReajuste = float(input())


custoFabr = 0
percentualDistr = 0;
imposto = 0
def coletarCustoFabr():
    print('Informe o custo de fábrica do veículo: ')
    this.custoFabr = float(input())
def coletarPercentualDistr():
    print('Informe o percentual do distribuidor: ')
    this.percentualDistr = float(input())
def coletarImposto():
    print('Informe o percentual de imposto: ')
    this.imposto = float(input())


notaUm = 0
notaDois = 0
notaTres = 0
def coletarNotaUm():
    print('Informe a primeira nota do aluno: ')
    this.notaUm = float(input())
def coletarNotaDois():
    print('Informe a segunda nota do aluno: ')
    this.notaDois = float(input())
def coletarNotaTres():
    print('Informe a terceira nota do aluno: ')
    this.notaTres = float(input())


numMacas = 0
def coletarMacas():
    print('Informe o número de maçãs compradas: ')
    this.numMacas = float(input())


def coletarNum():
    for i in range(10):
        print('Informe o ' + (i+1) + 'º número:')


salario = 0
valorVendas = 0
def coletarSalario():
    print('Informe o salário fixo do funcionário: ')
    this.salario = float(input())
def coletarValorVenda():
    print('Informe o valor das vendas efetuadas pelo vendedor: ')
    this.valorVendas = float(input())


saldo = 0
debito = 0
credito = 0
def coletarSaldo():
    print('Informe o saldo da conta: ')
    this.saldo = float(input())
def coletarDebito():
    print('Informe o débito da conta: ')
    this.debito = float(input())
def coletarCredito():
    print('Informe o crédito da conta: ')
    this.credito = float(input())

def coletarNumT():
    print('Informe um número de 1 a 10: ')
    this.numT = int(input())

    while (this.numT < 0) or (this.numT > 10):
        if (this.numT < 1) or (this.numT > 10):
           print('Informe número de 1 a 10!')
           this.numT = int(input())

valor = 0
def coletarValor():
    print('Informe um número acima de 1')
    this.valor = int(input())

    while this.valor <= 1:
        if this.valor <= 1:
            print('ERRO! Informe um número acima de 1!')
            this.valor = int(input())

numero = 0
def coletarNumero():
    for i in range(10):
        print('Digite o {}'.format(i+1) + 'º número de 10: ')
        this.numero = int(input())
        if this.numero < 0:
            this.contador = this.contador + 1
    print('A quantidade de números negativos é: {}'.format(this.contador))



def Menu():
    print('\n\n\n -------------- Escolha uma das opções abaixo: --------------\n'+
          '1. Exercício 1'+
          '\n2. Exercício 2'+
          '\n3. Exercício 3'+
          '\n4. Exercício 4'+
          '\n5. Exercício 5'+
          '\n6. Exercício 6'+
          '\n7. Exercício 7'+
          '\n8. Exercício 8'+
          '\n9. Exercício 9'+
          '\n10. Exercício 10 (não feito)'+
          '\n11. Exercício 11'+
          '\n12. Exercício 12'+
          '\n13. Exercício 13' +
          '\n14. Exercício 14' +
          '\n15. Exercício 15' +
          '\n16. Exercício 16' +
          '\n17. Exercício 17' +
          '\n18. Exercício 18' +
          '\n19. Exercício 19' +
          '\n20. Exercício 20' +
          '\n21. Sair')
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
            print('O percentual de votos válidos é: ' + str(Exercicio_05.percentualValidos(this.votosValidos, this.eleitores)) + '%')
            print('O percentual de votos brancos é: ' + str(Exercicio_05.percentualBrancos(this.votosBrancos, this.eleitores)) + '%')
            print('O percentual de votos nulos é: ' + str(Exercicio_05.percentualNulos(this.votosNulos, this.eleitores)) + '%')
        elif this.opcao == 6:
            #operação para exerc6
            coletarSalario()
            coletarPercentualReajuste()
            print('O novo salário atualizado do funcionário é: '+str(Exercicio_06.Reajuste(this.salario, this.percentualReajuste))+' reais')
        elif this.opcao == 7:
            #operacao para exerc7
            coletarCustoFabr()
            coletarPercentualDistr()
            coletarImposto()
            print('O custo final do veículo é: '+str(Exercicio_07.ValorTotal(this.custoFabr, this.percentualDistr, this.imposto))+' reais')
        elif this.opcao == 8:
            #operacao para exerc8
            coletarNotaUm()
            coletarNotaDois()
            coletarNotaTres()
            print('A média do aluno é: '+str(Exercicio_08.Media(this.notaUm, this.notaDois, this.notaTres)))
        elif this.opcao == 9:
            #operacao para exerc9
            coletarMacas()
            print('O valor total em relação ao número de maçãs é: '+str(Exercicio_09.Valor(this.numMacas)))
        elif this.opcao == 10:
            #operacao para exerc10
            coletarNum()
            print('A ordem crescente dos 10 números é: ' +str(Exercicio_10.Ordem(this.i)))
        elif this.opcao == 11:
            #operacao para exerc11
            coletarSalario()
            coletarValorVenda()
            print('O valor de seu salário total é: '+str(Exercicio_11.Total(this.salario, this.valorVendas)))
        elif this.opcao == 12:
            #operacao para exerc12
            coletarSaldo()
            coletarDebito()
            coletarCredito()
            print(Exercicio_12.SaldoAtual(this.saldo, this.debito, this.credito))
        elif this.opcao == 13:
            #operacao para exerc13
            coletarNumT()
            print("Sua Tabuada é: ")
            Exercicio_13.Tabuada(this.numT)
        elif this.opcao == 14:
            #operação para exerc14
            coletarValor()
            print('Os números entre 0 e {} são: '.format(this.valor))
            Exercicio_14.Impressao(this.valor)
        elif this.opcao == 15:
            #operacao para exerc15
            coletarNumero()
        elif this.opcao == 21:
            print('Obrigado!')
        else:
            print('Opcao escolhida inválida! Tente novamente com as opções fornecidas.')
