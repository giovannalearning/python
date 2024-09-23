saldo = 1000
saque = 200
limite = 100 
conta_especial = True

# Tabela verdade    
print(True and True)
print(True and False)
print(True or True)
print(True or False)
print(False or False)
print(False and False)

saldo >= saque and saque <= limite or conta_especial and saldo >= saque
# True

(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
# True