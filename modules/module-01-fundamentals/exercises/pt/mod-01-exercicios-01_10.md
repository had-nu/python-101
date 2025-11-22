# Exercícios do Módulo 01 - Fundamentos e Pensamento Computacional

## Exercício 01: Produto de Dois Números Inteiros

### Contexto
Você está criando uma calculadora simples para ajudar estudantes que estão aprendendo multiplicação. O programa deve pedir ao usuário dois números inteiros e apresentar o produto (resultado da multiplicação) deles.

### Objetivo de Aprendizado
Este exercício desenvolve sua habilidade de receber entrada do usuário, converter strings para números, realizar operações aritméticas básicas, e apresentar resultados formatados.

### Especificação
Crie um programa que:
1. Solicite ao usuário o primeiro número inteiro
2. Solicite ao usuário o segundo número inteiro
3. Calcule o produto dos dois números
4. Apresente o resultado de forma clara

### Exemplo de Execução
```
Digite o primeiro número: 7
Digite o segundo número: 8
O produto de 7 e 8 é: 56
```

### Dicas
- Use `input()` para receber os valores
- Lembre-se de converter a entrada para `int` usando `int()`
- Use f-strings para formatar a saída de forma legível

---

## Exercício 02: Média de Três Números

### Contexto
Você é um professor e precisa calcular rapidamente a média de três avaliações de um aluno. Este programa automatiza esse cálculo, permitindo que você insira as três notas e obtenha imediatamente a média aritmética.

### Objetivo de Aprendizado
Este exercício pratica trabalhar com múltiplas entradas, realizar operações que combinam múltiplos valores, e apresentar resultados numéricos com formatação apropriada (casas decimais para notas).

### Especificação
Crie um programa que:
1. Solicite três notas ao usuário
2. Calcule a média aritmética (soma dividida por três)
3. Apresente o resultado com uma casa decimal

### Exemplo de Execução
```
Digite a primeira nota: 15.5
Digite a segunda nota: 17.0
Digite a terceira nota: 16.5
A média das três notas é: 16.3
```

### Dicas
- Use `float()` para converter as entradas, pois notas podem ter decimais
- A média aritmética é (nota1 + nota2 + nota3) / 3
- Use `:.1f` na f-string para mostrar uma casa decimal

---

## Exercício 03: Antecedente e Sucessor

### Contexto
Você está desenvolvendo um sistema que trabalha com sequências numéricas e precisa, dado um número, identificar tanto o número que vem imediatamente antes (antecedente) quanto o que vem imediatamente depois (sucessor).

### Objetivo de Aprendizado
Este exercício, embora simples, desenvolve compreensão de operações incrementais e decrementais, padrões que você usará constantemente em algoritmos mais complexos.

### Especificação
Crie um programa que:
1. Solicite um número inteiro ao usuário
2. Calcule e apresente o antecedente (número - 1)
3. Calcule e apresente o sucessor (número + 1)

### Exemplo de Execução
```
Digite um número inteiro: 42
Número digitado: 42
Antecedente: 41
Sucessor: 43
```

### Dicas
- O antecedente é simplesmente o número menos 1
- O sucessor é o número mais 1
- Organize a saída de forma clara mostrando os três valores

---

## Exercício 04: Área de um Triângulo

### Contexto
Você trabalha em uma empresa de construção e precisa calcular frequentemente a área de terrenos triangulares para determinar quantidade de material necessário para cobertura ou pavimentação.

### Objetivo de Aprendizado
Este exercício pratica aplicação de fórmulas matemáticas em contexto prático, trabalhando com números decimais e apresentando resultados com unidades de medida apropriadas.

### Especificação
Crie um programa que:
1. Solicite a base do triângulo (em metros)
2. Solicite a altura do triângulo (em metros)
3. Calcule a área usando a fórmula: área = (base × altura) / 2
4. Apresente o resultado com duas casas decimais e a unidade m²

### Exemplo de Execução
```
Digite a base do triângulo (em metros): 12.5
Digite a altura do triângulo (em metros): 8.0
A área do triângulo é: 50.00 m²
```

### Dicas
- Use `float()` para aceitar valores decimais
- A fórmula é (base * altura) / 2
- Use `:.2f` para mostrar duas casas decimais
- Inclua a unidade m² na saída para clareza

---

## Exercício 05: Cálculo de IVA

### Contexto
Você trabalha em uma loja e precisa calcular rapidamente o valor total que um cliente pagará por uma mercadoria, incluindo o IVA (Imposto sobre Valor Acrescentado) de 23%. Este programa automatiza esse cálculo diário.

### Objetivo de Aprendizado
Este exercício desenvolve habilidade essencial de calcular acréscimos percentuais, padrão extremamente comum em aplicações comerciais e financeiras.

### Especificação
Crie um programa que:
1. Solicite o valor da mercadoria (sem IVA)
2. Calcule o valor do IVA (23% do valor original)
3. Calcule o valor total (valor original + IVA)
4. Apresente todos os valores formatados como dinheiro (duas casas decimais)

### Exemplo de Execução
```
Digite o valor da mercadoria: 50.00
Valor da mercadoria: 50.00 €
IVA (23%): 11.50 €
Valor total a pagar: 61.50 €
```

### Dicas
- 23% em decimal é 0.23
- IVA = valor × 0.23
- Valor total = valor + IVA
- Alternativamente: valor_total = valor × 1.23
- Mostre o cálculo em etapas para clareza

---

## Exercício 06: Preço Final de Carro Novo

### Contexto
Você trabalha em uma concessionária de automóveis. O preço final que um cliente paga por um carro novo inclui o custo de fábrica, mais a margem do distribuidor (15%), mais os impostos (35% sobre o custo de fábrica). Este programa calcula o preço final ao consumidor.

### Objetivo de Aprendizado
Este exercício pratica cálculos com múltiplos acréscimos percentuais sobre a mesma base, situação comum em cálculos comerciais complexos.

### Especificação
Crie um programa que:
1. Solicite o custo de fábrica do carro
2. Calcule a margem do distribuidor (15% do custo de fábrica)
3. Calcule os impostos (35% do custo de fábrica)
4. Calcule o preço final (custo + distribuidor + impostos)
5. Apresente todos os valores de forma organizada

### Exemplo de Execução
```
Digite o custo de fábrica do carro: 20000.00
Custo de fábrica: 20000.00 €
Margem do distribuidor (15%): 3000.00 €
Impostos (35%): 7000.00 €
Preço final ao consumidor: 30000.00 €
```

### Dicas
- Distribuidor = custo × 0.15
- Impostos = custo × 0.35
- Preço final = custo + distribuidor + impostos
- Alternativamente: preço_final = custo × (1 + 0.15 + 0.35) = custo × 1.50
- Decomponha em etapas para mostrar todos os valores intermediários

---

## Exercício 07: Troco Efetivo com Gorjeta

### Contexto
Você está desenvolvendo um sistema para restaurantes. Quando um cliente paga sua conta, ele pode decidir dar parte do troco como gorjeta ao funcionário. Se o cliente decide dar 10% do troco como gorjeta, quanto efetivamente retorna para o cliente?

### Objetivo de Aprendizado
Este exercício combina operações de subtração e cálculo percentual, desenvolvendo habilidade de encadear múltiplas operações lógicas.

### Especificação
Crie um programa que:
1. Solicite o valor a pagar
2. Solicite o valor dado para pagamento (assumir que é maior que o valor a pagar)
3. Calcule o troco inicial
4. Calcule 10% do troco como gorjeta
5. Calcule o troco efetivo (troco inicial - gorjeta)
6. Apresente todos os valores claramente

### Exemplo de Execução
```
Digite o valor a pagar: 45.80
Digite o valor dado para pagamento: 50.00
Valor a pagar: 45.80 €
Valor dado: 50.00 €
Troco inicial: 4.20 €
Gorjeta (10%): 0.42 €
Troco efetivo ao cliente: 3.78 €
```

### Dicas
- Troco inicial = valor_dado - valor_a_pagar
- Gorjeta = troco_inicial × 0.10
- Troco efetivo = troco_inicial - gorjeta
- Mostre todos os valores intermediários para clareza

---

## Exercício 08: Percentagem de Votos em Eleições

### Contexto
Você está desenvolvendo um sistema de apuração de votos para um município. Dado o total de eleitores e a contagem de votos brancos, nulos e válidos, o sistema deve calcular que percentagem cada categoria representa do total de eleitores.

### Objetivo de Aprendizado
Este exercício desenvolve habilidade de calcular múltiplas percentagens a partir de um mesmo total, padrão comum em análises estatísticas e relatórios.

### Especificação
Crie um programa que:
1. Solicite o número total de eleitores
2. Solicite o número de votos brancos
3. Solicite o número de votos nulos
4. Solicite o número de votos válidos
5. Calcule a percentagem que cada categoria representa
6. Apresente os resultados com duas casas decimais

### Exemplo de Execução
```
Digite o total de eleitores: 10000
Digite o número de votos brancos: 500
Digite o número de votos nulos: 300
Digite o número de votos válidos: 9200

Resultados:
Votos brancos: 5.00%
Votos nulos: 3.00%
Votos válidos: 92.00%
```

### Dicas
- Percentagem = (valor / total) × 100
- Calcule cada percentagem separadamente
- Use `:.2f` para mostrar duas casas decimais
- Note que as percentagens podem não somar exatamente 100% devido a arredondamentos

---

## Exercício 09: Custo de Pintura de Cubos Artísticos

### Contexto
Um artista produz cubos de 2 cm de aresta que depois pinta completamente. A tinta é vendida em latas de 1,5 dl ao preço de 2,75€, e com 1 dl de tinta ele consegue pintar 5 cm² de superfície. Dado o número de cubos, calcule quanto custa pintar todos os cubos.

### Objetivo de Aprendizado
Este é um exercício de múltiplas etapas que desenvolve habilidade de decompor problemas complexos em cálculos sequenciais, onde cada resultado alimenta o próximo cálculo.

### Especificação
Crie um programa que:
1. Solicite o número de cubos a produzir
2. Calcule a área total a pintar (área de um cubo × número de cubos)
   - Área de um cubo = 6 × aresta²
   - Aresta = 2 cm
3. Calcule quantos dl de tinta são necessários
   - 1 dl cobre 5 cm²
4. Calcule quantas latas são necessárias
   - Cada lata tem 1,5 dl
   - Arredondar para cima (não se vendem frações de lata)
5. Calcule o custo total
   - Cada lata custa 2,75€

### Exemplo de Execução
```
Digite o número de cubos: 10
Área de um cubo: 24 cm²
Área total a pintar: 240 cm²
Tinta necessária: 48.00 dl
Latas necessárias: 32
Custo total: 88.00 €
```

### Dicas
- Área de um cubo com aresta 2cm = 2 × 2 × 6 = 24 cm²
- Decomponha o problema em etapas claras
- Para arredondar para cima, você pode usar int(valor + 0.999) como truque simples
- Mostre cálculos intermediários para facilitar verificação

---

## Exercício 10: Separação de Dígitos

### Contexto
Você está desenvolvendo um sistema que processa números de identificação. Dado um número de 3 dígitos (entre 100 e 999), você precisa separar e exibir cada dígito individualmente, o que será útil para validações e processamentos posteriores.

### Objetivo de Aprendizado
Este exercício ensina técnica fundamental de manipulação numérica usando divisão inteira e módulo, habilidades essenciais para muitos algoritmos de processamento.

### Especificação
Crie um programa que:
1. Solicite um número inteiro de 3 dígitos (entre 100 e 999)
2. Extraia o dígito das centenas
3. Extraia o dígito das dezenas
4. Extraia o dígito das unidades
5. Apresente os três dígitos separados por espaços

### Exemplo de Execução
```
Digite um número de 3 dígitos: 472
Dígitos separados: 4 7 2
```

### Dicas
- Para centenas: use divisão inteira por 100 (numero // 100)
- Para dezenas: remova as centenas primeiro, depois divida por 10
  - resto = numero % 100 (remove centenas)
  - dezenas = resto // 10
- Para unidades: use módulo por 10 (numero % 10)
- Alternativamente para dezenas: (numero // 10) % 10

---

## Critérios de Avaliação

Para cada exercício, sua solução será considerada completa quando:

1. **Funcionalidade**: O programa aceita entrada apropriada, realiza cálculos corretamente, e produz saída correta
2. **Código Limpo**: Variáveis têm nomes descritivos e significativos
3. **Comentários**: Há comentários explicando lógica quando não é óbvia
4. **Formatação**: A saída é apresentada de forma clara e profissional
5. **Compreensão**: Você pode explicar cada linha e por que funciona

## Próximos Passos

Depois de completar todos os exercícios, compare suas soluções com as fornecidas na pasta de soluções. Não se preocupe se sua abordagem foi diferente, frequentemente há múltiplas formas válidas de resolver o mesmo problema. O importante é que funcione corretamente e que você compreenda profundamente por que funciona.

Quando dominar todos estes exercícios, estará pronto para o projeto integrador do módulo, que combinará múltiplos conceitos em uma aplicação mais complexa e realista.