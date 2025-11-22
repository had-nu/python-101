# Operações Aritméticas, Entrada e Saída de Dados

## Operações Aritméticas Fundamentais

Python oferece os operadores aritméticos que você espera de matemática básica, mas com algumas peculiaridades e capacidades adicionais que vale entender profundamente. Cada operador tem propósito específico e comportamento que precisa ser compreendido para usar corretamente.

A adição usa o símbolo de mais e funciona exatamente como esperado:

```python
total = 10 + 5  # Resultado: 15
```

A subtração usa o símbolo de menos:

```python
diferenca = 10 - 3  # Resultado: 7
```

A multiplicação usa o asterisco, não o x que você pode estar acostumado de matemática escrita:

```python
produto = 6 * 7  # Resultado: 42
```

Para divisão, Python oferece dois operadores distintos que você precisa entender claramente porque fazem coisas diferentes. A barra simples realiza divisão decimal, sempre retornando um float mesmo quando divide números inteiros que são perfeitamente divisíveis:

```python
resultado = 10 / 2  # Resultado: 5.0 (note que é float, não inteiro)
resultado2 = 10 / 3  # Resultado: 3.3333333333333335
```

A barra dupla realiza divisão inteira, também chamada divisão de piso, que descarta qualquer parte fracionária e retorna apenas o quociente inteiro:

```python
resultado = 10 // 3  # Resultado: 3 (descarta o resto)
resultado2 = 17 // 5  # Resultado: 3 (17 dividido por 5 é 3 com resto 2)
```

Esta distinção será crucial quando você tiver problemas onde precisa saber quantas vezes algo cabe completamente em outra coisa. Por exemplo, se você tem 17 euros e algo custa 5 euros, divisão inteira diz que você pode comprar 3 unidades, descartando o fato de que sobra 2 euros.

O módulo, representado pelo símbolo de percentagem, retorna exatamente esse resto que a divisão inteira descarta:

```python
resto = 17 % 5  # Resultado: 2 (o resto quando 17 é dividido por 5)
```

Finalmente, a exponenciação usa dois asteriscos para representar potência:

```python
quadrado = 5 ** 2  # Resultado: 25 (5 ao quadrado)
cubo = 2 ** 3  # Resultado: 8 (2 ao cubo)
raiz = 9 ** 0.5  # Resultado: 3.0 (raiz quadrada, porque elevar a 0.5 é raiz)
```

## Precedência de Operadores: A Ordem Importa

Quando você combina múltiplas operações em uma única expressão, Python precisa saber em que ordem executá-las. Assim como em matemática, Python segue regras de precedência onde certas operações acontecem antes de outras:

```python
resultado = 2 + 3 * 4  # Resultado: 14, não 20
```

A multiplicação acontece antes da adição, exatamente como você aprendeu em matemática escolar. Python multiplica 3 por 4 obtendo 12, depois adiciona 2 obtendo 14. Se você quiser que a adição aconteça primeiro, usa parênteses para controlar ordem explicitamente:

```python
resultado = (2 + 3) * 4  # Resultado: 20
```

A ordem completa de precedência, da mais alta (executa primeiro) para mais baixa é exponenciação, multiplicação e divisão (mesma precedência, executam da esquerda para direita), depois adição e subtração (mesma precedência, executam da esquerda para direita).

No entanto, a melhor prática não é memorizar tabelas complexas de precedência, mas usar parênteses liberalmente para tornar intenção explícita. Compare estas duas expressões que calculam a mesma coisa:

```python
# Confiando em precedência implícita
resultado = preco_base + preco_base * taxa_imposto

# Tornando intenção explícita com parênteses
resultado = preco_base + (preco_base * taxa_imposto)
```

A segunda versão é mais clara mesmo que os parênteses sejam tecnicamente redundantes. Código é lido muito mais vezes do que é escrito, então clareza sempre vale o esforço extra de adicionar parênteses que tornam intenção óbvia.

## Operadores de Atribuição Compostos: Atalhos Convenientes

Você frequentemente precisará modificar o valor de uma variável baseado em seu valor atual. Por exemplo, adicionar algo a um acumulador ou incrementar um contador. Python oferece operadores compostos que combinam operação aritmética com atribuição:

```python
# Forma longa
contador = 0
contador = contador + 1  # Incrementa contador

# Forma curta equivalente
contador = 0
contador += 1  # Faz exatamente a mesma coisa
```

O operador `+=` é atalho que significa pegue o valor atual da variável, adicione o valor da direita, e armazene o resultado de volta na variável. Python oferece versões compostas para todas as operações principais:

```python
x = 10
x += 5  # x agora vale 15 (equivalente a x = x + 5)
x -= 3  # x agora vale 12 (equivalente a x = x - 3)
x *= 2  # x agora vale 24 (equivalente a x = x * 2)
x /= 4  # x agora vale 6.0 (equivalente a x = x / 4)
x //= 2  # x agora vale 3.0 (equivalente a x = x // 2)
x %= 2  # x agora vale 1.0 (equivalente a x = x % 2)
x **= 3  # x agora vale 1.0 (equivalente a x = x ** 3)
```

Estes operadores compostos não apenas economizam digitação, mas também comunicam intenção mais claramente. Quando você vê `total += preco`, imediatamente reconhece o padrão de acumular valores, enquanto `total = total + preco` requer um momento mental extra para processar.

## Entrada de Dados: Conversando com Usuários

Até agora, todos os valores nos exemplos foram codificados diretamente no programa, tornando-o estático. Programas úteis precisam ser dinâmicos, aceitando entrada de usuários para processar dados diferentes em cada execução. Python oferece a função `input()` para ler texto que o usuário digita:

```python
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")
```

Quando este programa executa, ele exibe a mensagem dentro dos parênteses, pausa esperando que o usuário digite algo e pressione Enter, e então armazena o que foi digitado na variável nome. A função `input()` sempre retorna string de texto, mesmo se o usuário digitar números.

Esta é fonte comum de confusão para iniciantes. Observe este código problemático:

```python
idade = input("Digite sua idade: ")
anos_ate_aposentadoria = 65 - idade  # ERRO! Não pode subtrair string de número
```

Este código falhará porque `input()` retorna string, e você não pode fazer operações aritméticas com strings como se fossem números. A solução é converter a entrada para o tipo apropriado:

```python
idade_texto = input("Digite sua idade: ")
idade = int(idade_texto)  # Converte string para inteiro
anos_ate_aposentadoria = 65 - idade  # Agora funciona
```

Você pode encurtar isso fazendo a conversão diretamente:

```python
idade = int(input("Digite sua idade: "))
```

Esta linha lê entrada do usuário, converte para inteiro, e armazena na variável idade, tudo em uma única instrução. Os parênteses aninhados podem parecer confusos no início, mas você rapidamente se acostumará com este padrão extremamente comum.

Para números com casas decimais, usa `float()` em vez de `int()`:

```python
altura = float(input("Digite sua altura em metros: "))
```

## Saída Formatada: Apresentando Resultados Claramente

Fazer cálculos é apenas metade da história, você também precisa comunicar resultados de forma que sejam compreensíveis para humanos. A função `print()` que você já viu aceita múltiplos valores separados por vírgulas, automaticamente inserindo espaços entre eles:

```python
nome = "Ana"
idade = 25
print("Nome:", nome, "Idade:", idade)  # Nome: Ana Idade: 25
```

No entanto, a maneira mais moderna e flexível de formatar saída em Python é usar f-strings, que você viu brevemente antes. F-strings permitem incorporar expressões Python diretamente dentro de strings:

```python
nome = "João"
idade = 30
print(f"{nome} tem {idade} anos")  # João tem 30 anos
```

Você pode usar qualquer expressão dentro das chaves, não apenas nomes de variáveis:

```python
preco = 50
taxa_iva = 0.23
print(f"Preço final: {preco * (1 + taxa_iva)} euros")
```

F-strings também permitem controlar precisão de números decimais, crucial quando você trabalha com valores monetários:

```python
valor = 10 / 3
print(f"Resultado: {valor}")  # Resultado: 3.3333333333333335
print(f"Resultado: {valor:.2f}")  # Resultado: 3.33
```

O `:.2f` dentro das chaves significa formatar como float com duas casas decimais. Você pode mudar o número para qualquer precisão desejada. Este formato é especialmente importante para dinheiro, onde convenção universal é mostrar exatamente duas casas decimais.

Você também pode controlar largura de campos para alinhar saída tabulada:

```python
produtos = [("Pão", 1.5), ("Leite", 2.8), ("Café", 4.75)]
for produto, preco in produtos:
    print(f"{produto:<10} {preco:>6.2f} €")
# Pão            1.50 €
# Leite          2.80 €
# Café           4.75 €
```

O `:<10` significa alinhar à esquerda em campo de largura 10, e `:>6.2f` significa alinhar à direita em campo de largura 6 com 2 casas decimais. Não se preocupe se isso parecer complexo agora, você usará formatação simples na maioria dos casos e aprenderá opções avançadas conforme necessário.

## Colocando Tudo Junto: Um Programa Interativo Completo

Vamos ver como entrada, processamento e saída funcionam juntos em um programa completo que resolve problema real. Imagine um programa que calcula o preço final de um produto após adicionar IVA:

```python
# Entrada: recebe informações do usuário
preco_base = float(input("Digite o preço base do produto: "))
taxa_iva = float(input("Digite a taxa de IVA (como decimal, ex: 0.23): "))

# Processamento: calcula valores intermediários e resultado final
valor_iva = preco_base * taxa_iva
preco_final = preco_base + valor_iva

# Saída: apresenta resultados de forma clara e formatada
print(f"\nResumo do cálculo:")
print(f"Preço base: {preco_base:.2f} €")
print(f"IVA ({taxa_iva * 100:.0f}%): {valor_iva:.2f} €")
print(f"Preço final: {preco_final:.2f} €")
```

Este programa segue padrão clássico de entrada-processamento-saída que você verá repetidamente. Primeiro coleta todas as informações necessárias do usuário, depois realiza cálculos necessários sem interromper usuário para mais entrada, finalmente apresenta todos os resultados formatados apropriadamente.

Note o uso de linha em branco na saída através de `\n` no início da string de print. O `\n` é caractere especial que representa quebra de linha, criando espaço visual que torna saída mais legível. Pequenos detalhes de formatação como este fazem enorme diferença na experiência do usuário com seus programas.

## Lidando com Erros de Entrada

Quando você usa `input()` e converte para número, assume que o usuário digitará entrada válida. Mas usuários cometem erros, e programas robustos precisam lidar com isso graciosamente. Por enquanto, você não tem ferramentas para tratar erros sofisticadamente, isso vem em módulos futuros. Mas pode e deve validar entrada de formas simples.

Por exemplo, se você pede um número positivo, pode verificar que o valor é realmente positivo:

```python
preco = float(input("Digite o preço: "))
if preco < 0:
    print("Erro: preço não pode ser negativo!")
else:
    # Continua processamento normal
    print(f"Preço válido: {preco:.2f}")
```

Você aprenderá sobre estruturas condicionais como `if` no próximo módulo, mas a ideia básica é verificar condições e reagir apropriadamente. Programas que validam entrada e comunicam erros claramente são infinitamente mais agradáveis de usar que programas que simplesmente quebram com mensagens crípticas quando algo inesperado acontece.

## Trabalhando com Múltiplas Entradas

Frequentemente você precisa coletar múltiplos valores do usuário. Organize isto de forma que seja claro para o usuário o que está sendo pedido:

```python
print("Sistema de Cálculo de Média")
print("=" * 30)  # Imprime linha de separação

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print("\nResultado:")
print(f"Média: {media:.2f}")
```

Este programa demonstra boa prática de interface usuário. Tem título claro, separa visualmente entrada de saída, usa prompts descritivos que dizem exatamente o que é esperado, e formata saída de maneira organizada.

## Operações Aritméticas em Contexto Real

Todas essas operações e técnicas de entrada e saída existem para resolver problemas reais. Vamos ver alguns contextos onde você aplicará estes conceitos nos exercícios:

Quando você calcula preço final de produto incluindo impostos, está usando multiplicação para calcular o valor do imposto e adição para somar ao preço base. Quando determina quantos itens completos cabem dentro de um orçamento, está usando divisão inteira. Quando calcula o troco de uma transação comercial, está usando subtração. Quando determina área de um triângulo, está usando multiplicação e divisão em combinação específica.

Cada operação aritmética que Python oferece existe porque resolve classes inteiras de problemas práticos. Exponenciação não está lá apenas porque é matematicamente interessante, mas porque você precisa dela para calcular juros compostos, crescimento populacional, ou área de formas que escalam quadraticamente. Módulo não é curiosidade obscura, mas ferramenta essencial para problemas cíclicos como determinar dia da semana ou verificar paridade.

Conforme você trabalha os exercícios deste módulo, preste atenção não apenas em fazer o código funcionar, mas em reconhecer o padrão geral do problema que cada exercício representa. Quando você vê além do problema específico de calcular preço de um carro incluindo taxas de distribuidor e impostos para reconhecer o padrão geral de calcular preço final com múltiplos acréscimos percentuais, você desenvolveu pensamento computacional que pode aplicar em contextos totalmente diferentes.

Esta habilidade de abstração, ver o padrão geral através de instâncias específicas, é possivelmente a competência mais valiosa que programação desenvolve. Você não está apenas aprendendo como somar números em Python, está aprendendo como identificar quando um problema requer acumulação de valores, como quando um problema requer transformação percentual, como decompor problemas complexos em sequências de operações mais simples.

Com a teoria coberta, você está pronto para ver estes conceitos em ação através de exemplos práticos, e depois aplicá-los você mesmo resolvendo exercícios contextualizados. Cada exemplo e exercício foi cuidadosamente escolhido para desenvolver não apenas competência técnica em Python, mas também intuição sobre quando e como aplicar cada conceito em situações reais.