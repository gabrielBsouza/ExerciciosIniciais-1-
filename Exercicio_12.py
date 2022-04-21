def SaldoAtual(saldo, debito, credito):
    saldoAtual = float(saldo - debito + credito)
    if saldoAtual > 0:
        print('O Saldo se encontra Positivo! Seu saldo é: {}'.format(saldoAtual))
    else:
        print('O Saldo se encontra Negativo! Seu saldo é: {}'.format(saldoAtual))