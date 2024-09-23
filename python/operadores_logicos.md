## Operadores Lógicos
- São operadores utilizados em conjunto com os operadores de comparação, para montar uma expressão lógica. Quando um operador de comparação é utilizado, o resultado retornado é um booleano.

- Exemplo: op_comparacao + op_logico + op_comparacao... N

```Python
saldo = 1000
saque = 200
limite = 100

saldo >= saque
# True

saque <= limite
# False
```

### Operador E
- Todos precisam ser verdadeiro

```python
saldo = 1000
saque = 200
limite = 100 

saldo >= saque and saque <= limite
# False

```

### Operador OU
- Apenas um precisa ser verdadeiro

```python
saldo = 1000
saque = 200
limite = 100 

saldo >= saque or saque <= limite
# False

```

### Operador Negação
- Inverso

```python
contatos_emergencia = []

not 1000 > 1500
# True

not contatos_emergencia
# True

not "saque 1500
# False

not ""
# True
```

<!-- Lista vazia em python é falso-->

### Parênteses
- Precedência de comparação

```python
saldo = 1000
saque = 200
limite = 100 
conta_especial = True

saldo >= saque and saque <= limite or conta_especial and saldo >= saque
# True

(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
# True
```

