## Conversão de Tipos: 

- Inteiro para Float

```Python
preco = 10
print(preco)
# 10
```

```Python
preco = float(preco)
print(preco)
# 10.0
```

```Python
preco = 10/2
print(preco)
# 5.0
```

- Float para Inteiro

```Python
preco = 10.30
print(preco)
# 10.30
```

```Python
preco = int(preco)
print(preco)
# 10
```

- Conversão por divisão

```Python
preco = 10
print(preco)
# 10
```

```Python
preco = (preco/2)
print(preco)
# 5.0
```

```Python
preco = (preco//2)
print(preco)
# 5 
```

- Número para String

```python
preco = 10.50
idade = 28

print(str(preco))
#10.5

print(str(idade))
#28

texto = f"idade {idade} preco {preco}" # f = formatar
print texto
#idade 28 ´reco 10.5
```

- String para Número

```python
preco = 10.50
idade = 28

print(float(preco))
#10.5

print(float(idade))
#28
```

• Adicionar type no print faz com que ele devolva o tipo da variável
• // para preservar o número inteiro
