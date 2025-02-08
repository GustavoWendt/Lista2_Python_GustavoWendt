#Escreva um programa que pergunte o valor total da conta em seguida pergunte quantos clientes existem, divida a conta pelos clientes e exiba o quanto cada cliente deve pagar seguida mensagem "Cada cliente deve pagar" x valor.
contatotal=float(input("Digite a conta total:"))
numerodeclientes=float(input("Quantos clientes foram?"))
print("Cada cliente deve pagar", contatotal/numerodeclientes)