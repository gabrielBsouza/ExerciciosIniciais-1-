def Total(salario, valorVendas):
    if valorVendas <= 1500:
        return (salario*0.03)+salario
    else:
        return (salario*0.08)+salario