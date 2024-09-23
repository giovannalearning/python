# Variáveis e Constantes

## Variáveis: mutável

```python
age = 22
name = 'Giovanna'
print(f'meu nome é {name} e eu tenho {age} anos de idade.')
```
OU
``` python
age, name = (22,'Giovanna') #Parênnteses é opcional
print(f'meu nome é {name} e eu tenho {age} anos de idade.')
```
#### Pode declarar várias variáveis na mesma linha 

### Alterando o valor da variável:
basta atribuir um novo valor

```python
age = 22
name = 'Giovanna'
print(f'meu nome é {name} e eu tenho {age} anos de idade.')

```python
age = 19
name = 'Luisa'
print(f'meu nome é {name} e eu tenho {age} anos de idade.')
```

## Constantes: imutável
- Não existe uma palavra reservada para informar ao interpretador  que o valor é constante. Para declarar uma constante é necessário que o nome da variável seja totalmente escrito em letras maíusculas.

#### Exemplo:

```Python
ABS_PARTH = 'C:\Users\giovanna.silva\Desktop\python'
DEBUG = True
STATES={
    'SP'
    'RJ'
    'MG'
}
AMOUNT = 30.2
```

### Boas Práticas:
- O padrão de nomes deve ser snake case. Utilização de '_' em espaços em branco;
- Escolher nomes sugestivos;
- Nome de constantes todo em maíusculo. 


