#Escreva um programa que pergunte quantos pedaços o bolo tem, em seguida pergunte ao usuario quantos pedaços ele comeu, calcule quantos pedaços ainda tem e exiba o resultado com uma mensagem de livre escolha.
pedacostotais=int(input("Quantos pedaços o bolo tem"))
pedacoscomidos=int(input("Quantos pedaços você comeu?"))
sobra=pedacostotais-pedacoscomidos
print("Restam:",sobra,"pedaços de bolo")