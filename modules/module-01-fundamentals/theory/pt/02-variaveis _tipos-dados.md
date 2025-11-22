# Variáveis e Tipos de Dados

## Por Que Precisamos de Variáveis

Imagine que você está calculando o preço final de um produto que custa cinquenta euros e tem vinte e três por cento de IVA aplicado. Você poderia fazer este cálculo diretamente: `50 + (50 * 0.23)`, que resultaria em 61.5 euros. Mas e se você precisar fazer este mesmo cálculo para múltiplos produtos com preços diferentes? E se precisar usar o preço original em vários lugares do seu programa? E se quiser tornar seu código compreensível para outras pessoas que o lerão mais tarde?

Variáveis resolvem todos estes problemas. Uma variável é essencialmente um nome significativo que você atribui a um valor, permitindo que você se refira a esse valor pelo nome em vez de repetir o número literal constantemente. Mais importante, variáveis representam abstração, a habilidade de trabalhar com conceitos em vez de apenas valores específicos.

Vamos ver como ficaria o mesmo cálculo usando variáveis:

```python
preco_original = 50
taxa_iva = 0.23
iva = preco_original * taxa_iva
preco_final = preco_original + iva
print(preco_final)
```

Este código faz exatamente o mesmo cálculo, mas observe como é muito mais claro o que cada número representa e o que cada operação está fazendo. Se você precisar mudar o preço original mais tarde, muda apenas em um lugar. Se quiser aplicar a mesma taxa de IVA a múltiplos produtos, pode reutilizar a variável `taxa_iva` sem repetir o valor 0.23 em vários lugares.

Variáveis também permitem que programas sejam dinâmicos, funcionando com valores diferentes em cada execução. No exemplo acima, o preço está fixado em cinquenta no código. Mais tarde neste módulo, você aprenderá como ler valores que usuários fornecem, permitindo que o mesmo programa calcule IVA para qualquer produto que qualquer pessoa queira usar.

## Criando e Usando Variáveis em Python

Em Python, criar uma variável é surpreendentemente simples. Você apenas escolhe um nome e atribui um valor usando o sinal de igual:

```python
idade = 25
nome = "Ana"
altura = 1.75
```

Estas três linhas criam três variáveis diferentes com valores diferentes. A primeira armazena um número inteiro, a segunda uma string de texto, e a terceira um número com casas decimais. Python automaticamente determina que tipo de dado cada variável contém baseado no valor atribuído, processo chamado tipagem dinâmica. Isto torna Python mais flexível e fácil de começar comparado a linguagens onde você precisa declarar explicitamente o tipo de cada variável.

O sinal de igual em programação não significa igualdade matemática como em equações. Significa atribuição, copiar o valor do lado direito para a variável do lado esquerdo. Esta distinção é crucial. Quando você escreve `idade = 25`, está dizendo ao Python para criar uma variável chamada `idade` e colocar o valor 25 dentro dela. O fluxo é sempre da direita para a esquerda.

Isto se torna mais claro quando você vê algo como:

```python
contador = 0
contador = contador + 1
```

A segunda linha não é equação matemática dizendo que contador é igual a si mesmo mais um, o que seria contradição matemática. É instrução dizendo pegue o valor atual de contador, adicione um a ele, e armazene o resultado de volta na variável contador, substituindo o valor anterior. Depois destas duas linhas, contador contém 1.

## Regras e Convenções Para Nomear Variáveis

Python tem regras estritas sobre que caracteres podem aparecer em nomes de variáveis. Nomes devem começar com uma letra (maiúscula ou minúscula) ou sublinhado, e podem conter letras, números e sublinhados, mas não espaços ou símbolos especiais. Nomes são sensíveis a caso, significando que `idade`, `Idade` e `IDADE` são três variáveis completamente diferentes.

Alguns exemplos de nomes válidos e inválidos:

```python
# Nomes válidos
nome = "João"
idade_em_anos = 25
peso2 = 75.5
_privado = 100

# Nomes inválidos que causariam erros
2preco = 50  # Não pode começar com número
nome-completo = "Ana Silva"  # Hífens não são permitidos
preço = 100  # Acentos não são recomendados
class = "A"  # 'class' é palavra reservada do Python
```

Além das regras sintáticas, há convenções culturais importantes na comunidade Python. A convenção mais estabelecida é usar snake_case para nomes de variáveis, onde palavras são separadas por sublinhados e todas as letras são minúsculas. Compare `idadeEmAnos` (estilo camelCase usado em outras linguagens) com `idade_em_anos` (estilo snake_case preferido em Python). A segunda é considerada mais pythonica, termo usado para código que segue o estilo e filosofia de Python.

Mais importante que regras sintáticas é escolher nomes descritivos que comunicam significado. Compare estes dois trechos de código que fazem exatamente a mesma coisa:

```python
# Código com nomes ruins
a = 50
b = 0.23
c = a * b
d = a + c

# Código com nomes bons
preco_base = 50
taxa_imposto = 0.23
valor_imposto = preco_base * taxa_imposto
preco_final = preco_base + valor_imposto
```

O segundo trecho é infinitamente mais compreensível mesmo para alguém que nunca viu o código antes. Bons nomes de variáveis são forma de documentação, tornando código auto explicativo. Você gastará muito mais tempo lendo código (seu próprio e de outros) do que escrevendo-o originalmente, então investir em nomes claros sempre compensa.

## Tipos de Dados Numéricos: Inteiros e Decimais

Python distingue entre dois tipos principais de números: inteiros, chamados `int`, e números com casas decimais, chamados `float` (abreviação de floating point, ponto flutuante). Esta distinção não é arbitrária, mas tem consequências práticas importantes sobre como seus programas funcionam.

Inteiros são números sem parte decimal: 0, 1, 42, -17, 1000000. São representados exatamente na memória do computador, sem qualquer aproximação. Quando você armazena o número 42 em uma variável int, é precisamente quarenta e dois, nem um pouco mais, nem um pouco menos.

Floats são números que têm ou podem ter casas decimais: 3.14, -0.5, 2.0, 1.23456789. São chamados ponto flutuante porque internamente o computador os representa usando notação científica, permitindo que o ponto decimal flutue para representar números muito grandes ou muito pequenos. Esta flexibilidade tem custo: floats são frequentemente aproximações, não valores exatos.

Esta diferença importa quando você faz cálculos. Observe:

```python
# Operações com inteiros
a = 10
b = 3
print(a + b)  # Resultado: 13 (inteiro)
print(a - b)  # Resultado: 7 (inteiro)
print(a * b)  # Resultado: 30 (inteiro)
print(a / b)  # Resultado: 3.3333333333333335 (float)
print(a // b)  # Resultado: 3 (inteiro, divisão inteira)

# Operações com floats
x = 10.0
y = 3.0
print(x / y)  # Resultado: 3.3333333333333335 (float)
```

Note que quando você divide dois inteiros usando barra simples, Python automaticamente converte o resultado para float. Se você quer divisão que mantém apenas a parte inteira, descartando qualquer resto, usa barra dupla. Esta distinção será crucial em problemas onde você precisa, por exemplo, calcular quantos pacotes completos de algo você pode comprar, descartando qualquer quantidade parcial.

## O Operador Módulo: Trabalhando com Restos

Um operador aritmético que talvez você não conheça de matemática escolar mas que é extremamente útil em programação é o módulo, representado pelo símbolo de percentagem. O operador módulo retorna o resto da divisão entre dois números:

```python
print(10 % 3)  # Resultado: 1 (porque 10 dividido por 3 é 3 com resto 1)
print(15 % 4)  # Resultado: 3 (porque 15 dividido por 4 é 3 com resto 3)
print(20 % 5)  # Resultado: 0 (porque 20 é divisível por 5, resto zero)
```

O módulo tem aplicações práticas surpreendentemente numerosas. Por exemplo, você pode usar módulo para determinar se um número é par ou ímpar: qualquer número cujo módulo por 2 é zero é par, qualquer número cujo módulo por 2 é um é ímpar. Você pode usar módulo para circular através de sequências, voltando ao início quando chegar ao fim. Veremos aplicações concretas do módulo nos exercícios.

## Conversão Entre Tipos: Quando Você Precisa Mudar Representação

Às vezes você precisa converter valores entre tipos diferentes. Python oferece funções para isso: `int()` converte para inteiro, `float()` converte para decimal, e `str()` converte para string de texto.

```python
# Convertendo para inteiro
numero_texto = "42"
numero_inteiro = int(numero_texto)  # Agora é o número 42, não texto

# Convertendo para float
inteiro = 10
decimal = float(inteiro)  # Agora é 10.0

# Convertendo para string
numero = 42
texto = str(numero)  # Agora é o texto "42"
```

Estas conversões são especialmente importantes quando você lê entrada de usuários, porque entrada vem sempre como string de texto. Se você pedir ao usuário para digitar um número mas não converter a entrada, operações matemáticas falharão porque Python não pode adicionar texto com números. Veremos isso em detalhe quando discutirmos entrada de dados.

Tenha cuidado com conversões que descartam informação. Quando você converte float para int, a parte decimal é simplesmente cortada, não arredondada:

```python
numero = 3.9
inteiro = int(numero)  # Resultado é 3, não 4
print(inteiro)
```

Se você quer arredondar, use a função `round()`:

```python
numero = 3.9
arredondado = round(numero)  # Resultado é 4
print(arredondado)
```

## Strings: Trabalhando com Texto

Embora este módulo foque principalmente em operações numéricas, você inevitavelmente trabalhará com texto também, nem que seja apenas para comunicar resultados aos usuários. Em Python, texto é representado como strings, que são sequências de caracteres envoltas em aspas.

```python
nome = "Ana Silva"
mensagem = 'Olá, mundo!'
texto_longo = """Este é um texto
que ocupa múltiplas
linhas."""
```

Você pode usar aspas simples ou duplas para strings de uma linha, e ambas funcionam identicamente. Python também oferece aspas triplas (simples ou duplas) para strings que ocupam múltiplas linhas, preservando quebras de linha no texto.

Strings podem ser concatenadas, que significa unidas, usando o operador de adição:

```python
primeiro_nome = "Ana"
ultimo_nome = "Silva"
nome_completo = primeiro_nome + " " + ultimo_nome  # "Ana Silva"
```

Note que você precisa adicionar espaços explicitamente quando concatena. Python não adiciona espaços automaticamente.

Você também pode inserir valores de variáveis dentro de strings usando f-strings, recurso extremamente útil para formatar saída:

```python
nome = "João"
idade = 25
mensagem = f"{nome} tem {idade} anos"  # "João tem 25 anos"
print(mensagem)
```

O `f` antes das aspas indica que é uma f-string, e qualquer coisa dentro de chaves é avaliada como expressão Python e seu valor é inserido na string. Este será seu método principal para formatar saída de programas de forma legível.

## Múltiplas Atribuições e Trocas de Valores

Python permite atribuir valores a múltiplas variáveis em uma única linha, recurso conveniente que você usará frequentemente:

```python
x, y, z = 10, 20, 30
```

Isto é equivalente a escrever três linhas separadas, mas mais conciso. Python também permite algo particularmente elegante: trocar valores entre variáveis sem precisar de variável temporária:

```python
a = 5
b = 10
a, b = b, a  # Agora a vale 10 e b vale 5
```

Em linguagens mais verbosas, você precisaria de uma terceira variável temporária para realizar esta troca. Python permite fazer diretamente, tornando código mais limpo.

## Constantes: Valores Que Não Devem Mudar

Às vezes você tem valores que não devem ser modificados durante execução do programa, como taxa de IVA fixa ou valor de pi. Tecnicamente Python não impede que você modifique qualquer variável, mas por convenção, variáveis escritas completamente em maiúsculas são tratadas como constantes que não devem ser modificadas:

```python
TAXA_IVA = 0.23
PI = 3.14159
VELOCIDADE_LUZ = 299792458  # metros por segundo
```

Esta convenção de nomenclatura sinaliza visualmente que estes valores são constantes configuradas uma vez e usadas em múltiplos lugares. Se você precisar mudar o valor, muda apenas na definição da constante e todos os lugares que a usam automaticamente usarão o novo valor.

## Variáveis Como Abstrações: Pensando em Níveis Mais Altos

A habilidade mais importante que variáveis proporcionam não é técnica mas conceptual. Variáveis permitem que você pense sobre problemas em termos de conceitos abstratos em vez de valores específicos. Quando você escreve `preco_final = preco_base + imposto`, está expressando relacionamento entre conceitos que permanece verdadeiro independente dos valores numéricos específicos envolvidos.

Esta capacidade de abstração é o que permite que o mesmo código resolva infinitas instâncias específicas de um problema geral. Um programa que calcula preço final com imposto funciona para qualquer produto, qualquer preço, qualquer taxa de imposto. O código expressa o padrão geral, e variáveis capturam valores específicos que mudam de execução para execução.

Conforme você progride em programação, verá abstrações em níveis progressivamente mais altos. Variáveis são abstração no nível mais baixo, nomeando valores individuais. Mais tarde você verá estruturas de dados que são abstrações organizando coleções de valores, funções que são abstrações encapsulando sequências de operações, e classes que são abstrações modelando conceitos inteiros com tanto dados quanto comportamento.

Mas tudo começa aqui, com habilidade de usar nomes significativos em vez de valores literais, capturando em código não apenas mecânica de cálculos mas também semântica de o que esses cálculos representam no contexto do problema sendo resolvido.