## Input e Output

### Função Input
- Receber dados via buffer
<!--Builtin: já está enraizada na linguagem e não há necessidade de baixar ou declarar -->

Recebe _string_

```python
nome = input("Informe o seu nome:")
```

### Função Print
- Exibição de dados na saída padrão (tela);
- Ela recebe um argumento obrigatório do tipo varargs de objetos e 4 argumentos opcionais (sep, end, file, flush);
- Todos os objetos são convertidos para string, separados por sep e terminados por end.

```python
nome = Giovanna
sobrenome = Menezes

print(nome, sobrenome)
print(nome, sobrenome, end="...\n")
print(nome, sobrenome, sep="#")

# Giovanna Menezes
# Giovanna Menezes...
# Giovanna#Menezes (#menezes mais claro)
```