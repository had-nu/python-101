# ============================================================================
# MÓDULO 01 - SOLUÇÕES COMENTADAS DOS EXERCÍCIOS
# Fundamentos e Pensamento Computacional
# ============================================================================

# IMPORTANTE: Estas soluções são uma das muitas formas possíveis de resolver
# cada problema. Se você resolveu de forma diferente mas seu código funciona
# corretamente, sua solução é igualmente válida!

# ============================================================================
# SOLUÇÃO 01: Produto de Dois Números Inteiros
# ============================================================================

print("=== EXERCÍCIO 01: Produto de Dois Números ===\n")

# Recebemos o primeiro número do usuário
# input() sempre retorna string, então usamos int() para converter
primeiro_numero = int(input("Digite o primeiro número: "))

# Recebemos o segundo número, também convertendo para inteiro
segundo_numero = int(input("Digite o segundo número: "))

# Calculamos o produto (multiplicação) dos dois números
# O operador * realiza multiplicação em Python
produto = primeiro_numero * segundo_numero

# Apresentamos o resultado de forma clara e compreensível
# Usamos f-string para incorporar os valores na mensagem
print(f"O produto de {primeiro_numero} e {segundo_numero} é: {produto}")

print("\n" + "="*60 + "\n")

# ============================================================================
# SOLUÇÃO 02: Média de Três Números
# ============================================================================

print("=== EXERCÍCIO 02: Média de Três Números ===\n")

# Recebemos as três notas do usuário
# Usamos float() porque notas podem ter casas decimais
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# A média aritmética é a soma de todos os valores dividida pela quantidade
# Somamos as três notas e dividimos por 3
media = (nota1 + nota2 + nota3) / 3

# Apresentamos o resultado com uma casa decimal (:.1f)
# Uma casa decimal é comum para notas acadêmicas
print(f"A média das três notas é: {media:.1f}")

# OBSERVAÇÃO PEDAGÓGICA:
# Poderíamos ter escrito: media = nota1/3 + nota2/3 + nota3/3
# Mas a forma mostrada (soma primeiro, depois divide) é mais clara e
# corresponde melhor à definição matemática de média

print("\n" + "="*60 + "\n")

# ============================================================================
# SOLUÇÃO 03: Antecedente e Sucessor
# ============================================================================

print("=== EXERCÍCIO 03: Antecedente e Sucessor ===\n")

# Recebemos um número inteiro do usuário
numero = int(input("Digite um número inteiro: "))

# O antecedente é simplesmente o número menos 1
# É o número que vem imediatamente antes na sequência numérica
antecedente = numero - 1

# O sucessor é o número mais 1
# É o número que vem imediatamente depois na sequência numérica
sucessor = numero + 1

# Apresentamos os três valores de forma organizada
print(f"Número digitado: {numero}")
print(f"Antecedente: {antecedente}")
print(f"Sucessor: {sucessor}")

# OBSERVAÇÃO PEDAGÓGICA:
# Embora pareça simples, este padrão de incremento/decremento
# é fundamental em muitos algoritmos, especialmente em loops
# e navegação em sequências que você aprenderá em módulos futuros

print("\n" + "="*60 + "\n")

# ============================================================================
# SOLUÇÃO 04: Área de um Triângulo
# ============================================================================

print("=== EXERCÍCIO 04: Área de um Triângulo ===\n")

# Recebemos as dimensões do triângulo em metros
# Usamos float() porque medidas podem ter casas decimais
base = float(input("Digite a base do triângulo (em metros): "))
altura = float(input("Digite a altura do triângulo (em metros): "))

# A fórmula da área do triângulo é (base × altura) / 2
# Os parênteses são tecnicamente desnecessários devido à precedência,
# mas tornam a intenção explícita e o código mais legível
area = (base * altura) / 2

# Apresentamos o resultado com duas casas decimais
# Incluímos a unidade m² para deixar claro que é área
print(f"A área do triângulo é: {area:.2f} m²")

# OBSERVAÇÃO PEDAGÓGICA:
# A fórmula funciona porque um triângulo é "metade de um retângulo"
# Se você imaginar um retângulo com a mesma base e altura,
# o triângulo ocupa exatamente metade dessa área

print("\n" + "="*60 + "\n")

# ============================================================================
# SOLUÇÃO 05: Cálculo de IVA
# ============================================================================

print("=== EXERCÍCIO 05: Cálculo de IVA ===\n")

# Recebemos o valor da mercadoria sem IVA
valor_mercadoria = float(input("Digite o valor da mercadoria: "))

# Definimos a taxa de IVA como constante
# Em Portugal, a taxa normal é 23% (0.23 em decimal)
TAXA_IVA = 0.23

# Calculamos o valor do IVA (23% do valor da mercadoria)
valor_iva = valor_mercadoria * TAXA_IVA

# O valor total é a soma do valor original com o IVA
valor_total = valor_mercadoria + valor_iva

# Apresentamos todos os valores de forma organizada
# Mostramos sempre duas casas decimais para valores monetários
print(f"Valor da mercadoria: {valor_mercadoria:.2f} €")
print(f"IVA (23%): {valor_iva:.2f} €")
print(f"Valor total a pagar: {valor_total:.2f} €")

# OBSERVAÇÃO PEDAGÓGICA:
# Alternativamente, poderíamos calcular diretamente:
# valor_total = valor_mercadoria * 1.23
# Multiplicar por 1.23 é equivalente a somar 23%
# Mas mostrar o cálculo em etapas é mais didático e permite
# apresentar o valor do IVA separadamente

print("\n" + "="*60 + "\n")

# ============================================================================
# SOLUÇÃO 06: Preço Final de Carro Novo
# ============================================================================

print("=== EXERCÍCIO 06: Preço Final de Carro ===\n")

# Recebemos o custo de fábrica do carro
custo_fabrica = float(input("Digite o custo de fábrica do carro: "))

# Definimos as percentagens como constantes
# Distribuidor recebe 15% sobre o custo de fábrica
PERCENTUAL_DISTRIBUIDOR = 0.15
# Impostos são 35% sobre o custo de fábrica
PERCENTUAL_IMPOSTOS = 0.35

# Calculamos cada componente do preço final
margem_distribuidor = custo_fabrica * PERCENTUAL_DISTRIBUIDOR
impostos = custo_fabrica * PERCENTUAL_IMPOSTOS

# O preço final é a soma de todos os componentes
# Custo original + margem do distribuidor + impostos
preco_final = custo_fabrica + margem_distribuidor + impostos

# Apresentamos todos os valores de forma organizada
print(f"Custo de fábrica: {custo_fabrica:.2f} €")
print(f"Margem do distribuidor (15%): {margem_distribuidor:.2f} €")
print(f"Impostos (35%): {impostos:.2f} €")
print(f"Preço final ao consumidor: {preco_final:.2f} €")

# OBSERVAÇÃO PEDAGÓGICA:
# Note que tanto a margem quanto os impostos são calculados sobre
# o custo de fábrica (a base), não um sobre o outro
# Poderíamos ter usado a fórmula direta:
# preco_final = custo_fabrica * (1 + 0.15 + 0.35) = custo_fabrica * 1.50
# Mas decompor permite mostrar cada componente separadamente

print("\n" + "="*60 + "\n")

# ============================================================================
# SOLUÇÃO 07: Troco Efetivo com Gorjeta
# ============================================================================

print("=== EXERCÍCIO 07: Troco com Gorjeta ===\n")

# Recebemos o valor a pagar e o valor dado para pagamento
valor_a_pagar = float(input("Digite o valor a pagar: "))
valor_dado = float(input("Digite o valor dado para pagamento: "))

# Calculamos o troco inicial (antes da gorjeta)
# É simplesmente a diferença entre o que foi dado e o que era devido
troco_inicial = valor_dado - valor_a_pagar

# O cliente decide dar 10% do troco como gorjeta
PERCENTUAL_GORJETA = 0.10
valor_gorjeta = troco_inicial * PERCENTUAL_GORJETA

# O troco efetivo que volta ao cliente é o troco inicial menos a gorjeta
troco_efetivo = troco_inicial - valor_gorjeta

# Apresentamos todos os valores de forma clara e organizada
print(f"Valor a pagar: {valor_a_pagar:.2f} €")
print(f"Valor dado: {valor_dado:.2f} €")
print(f"Troco inicial: {troco_inicial:.2f} €")
print(f"Gorjeta (10%): {valor_gorjeta:.2f} €")
print(f"Troco efetivo ao cliente: {troco_efetivo:.2f} €")

# OBSERVAÇÃO PEDAGÓGICA:
# Este exercício combina subtração e cálculo percentual
# Note a sequência lógica: primeiro calculamos quanto sobra (troco),
# depois calculamos a percentagem desse valor (gorjeta),
# finalmente subtraímos para obter o resultado final

print("\n" + "="*60 + "\n")

# ============================================================================
# SOLUÇÃO 08: Percentagem de Votos
# ============================================================================

print("=== EXERCÍCIO 08: Percentagem de Votos ===\n")

# Recebemos o total de eleitores e cada categoria de votos
total_eleitores = int(input("Digite o total de eleitores: "))
votos_brancos = int(input("Digite o número de votos brancos: "))
votos_nulos = int(input("Digite o número de votos nulos: "))
votos_validos = int(input("Digite o número de votos válidos: "))

# Para calcular percentagem: (parte / total) × 100
# Cada categoria é dividida pelo total e multiplicada por 100
percentual_brancos = (votos_brancos / total_eleitores) * 100
percentual_nulos = (votos_nulos / total_eleitores) * 100
percentual_validos = (votos_validos / total_eleitores) * 100

# Apresentamos os resultados com duas casas decimais
print("\nResultados:")
print(f"Votos brancos: {percentual_brancos:.2f}%")
print(f"Votos nulos: {percentual_nulos:.2f}%")
print(f"Votos válidos: {percentual_validos:.2f}%")

# OBSERVAÇÃO PEDAGÓGICA:
# Note que as percentagens podem não somar exatamente 100%
# devido a arredondamentos nas casas decimais
# Em sistemas reais, você pode querer verificar se a soma dos votos
# corresponde ao total de eleitores antes de calcular percentagens

print("\n" + "="*60 + "\n")

# ============================================================================
# SOLUÇÃO 09: Custo de Pintura de Cubos
# ============================================================================

print("=== EXERCÍCIO 09: Custo de Pintura de Cubos ===\n")

# Recebemos a quantidade de cubos a produzir
quantidade_cubos = int(input("Digite o número de cubos: "))

# Constantes do problema
ARESTA_CUBO = 2  # cm
COBERTURA_POR_DL = 5  # cm² por dl
CAPACIDADE_LATA = 1.5  # dl por lata
PRECO_LATA = 2.75  # euros por lata

# ETAPA 1: Calcular a área de um cubo
# Um cubo tem 6 faces, cada face é um quadrado de aresta²
area_um_cubo = 6 * (ARESTA_CUBO ** 2)
print(f"Área de um cubo: {area_um_cubo} cm²")

# ETAPA 2: Calcular área total a pintar
area_total = area_um_cubo * quantidade_cubos
print(f"Área total a pintar: {area_total} cm²")

# ETAPA 3: Calcular quantos dl de tinta são necessários
# Se 1 dl cobre 5 cm², então precisamos de (área total / 5) dl
dl_necessarios = area_total / COBERTURA_POR_DL
print(f"Tinta necessária: {dl_necessarios:.2f} dl")

# ETAPA 4: Calcular quantas latas são necessárias
# Cada lata tem 1.5 dl, então dividimos os dl necessários por 1.5
# Como não podemos comprar fração de lata, arredondamos para cima
# Truque simples: adicionar 0.999 antes de converter para int arredonda para cima
latas_necessarias = int(dl_necessarios / CAPACIDADE_LATA + 0.999)
print(f"Latas necessárias: {latas_necessarias}")

# ETAPA 5: Calcular custo total
custo_total = latas_necessarias * PRECO_LATA
print(f"Custo total: {custo_total:.2f} €")

# OBSERVAÇÃO PEDAGÓGICA:
# Este exercício demonstra decomposição de problema complexo em etapas
# Cada etapa usa o resultado da anterior, criando uma sequência lógica
# Em Python moderno, usaríamos math.ceil() para arredondar para cima,
# mas o truque mostrado funciona bem para este contexto

print("\n" + "="*60 + "\n")

# ============================================================================
# SOLUÇÃO 10: Separação de Dígitos
# ============================================================================

print("=== EXERCÍCIO 10: Separação de Dígitos ===\n")

# Recebemos um número de 3 dígitos (entre 100 e 999)
numero = int(input("Digite um número de 3 dígitos: "))

# MÉTODO 1: Usando divisão inteira e módulo de forma sequencial

# Para extrair as centenas: dividimos por 100 e pegamos apenas a parte inteira
# Exemplo: 472 // 100 = 4
centenas = numero // 100

# Para extrair as dezenas: primeiro removemos as centenas,
# depois dividimos o resto por 10
# Exemplo: 472 % 100 = 72, depois 72 // 10 = 7
dezenas = (numero % 100) // 10

# Para extrair as unidades: usamos módulo por 10
# O resto da divisão por 10 é sempre o último dígito
# Exemplo: 472 % 10 = 2
unidades = numero % 10

# Apresentamos os dígitos separados por espaços
print(f"Dígitos separados: {centenas} {dezenas} {unidades}")

# OBSERVAÇÃO PEDAGÓGICA:
# Esta técnica de usar divisão inteira (//) e módulo (%)
# para extrair dígitos é fundamental em muitos algoritmos
# 
# Método alternativo para dezenas:
# dezenas = (numero // 10) % 10
# Primeiro removemos as unidades dividindo por 10,
# depois pegamos o resto da divisão por 10 para ter apenas as dezenas
#
# Para verificar se sua solução está correta, você pode
# reconstruir o número: centenas*100 + dezenas*10 + unidades
# Isso deve resultar no número original

print("\n" + "="*60 + "\n")

# ============================================================================
# REFLEXÕES FINAIS SOBRE AS SOLUÇÕES
# ============================================================================

print("""
PONTOS IMPORTANTES SOBRE ESTAS SOLUÇÕES:

1. DECOMPOSIÇÃO: Note como cada problema mais complexo foi quebrado
   em etapas menores e mais simples. Esta é habilidade fundamental.

2. NOMES DESCRITIVOS: Variáveis têm nomes que comunicam significado,
   não apenas x, y, z. Isso torna código auto-documentado.

3. CONSTANTES: Valores que não mudam (como TAXA_IVA) foram escritos
   em maiúsculas para indicar que são constantes configuráveis.

4. COMENTÁRIOS: Há explicações do raciocínio, não apenas do que o código faz.
   Bons comentários explicam o "porquê", não o "o quê".

5. FORMATAÇÃO: Valores monetários sempre mostram duas casas decimais,
   criando saída profissional e consistente.

6. MÚLTIPLAS ABORDAGENS: Muitos problemas têm várias soluções válidas.
   Se você resolveu diferente mas funciona, ótimo!

7. PROGRESSÃO: Os exercícios começaram simples e ficaram gradualmente
   mais complexos, desenvolvendo habilidades incrementalmente.

Parabéns por completar todos os exercícios do Módulo 01!
Você está pronto para o projeto integrador que consolida
todos estes conceitos em uma aplicação mais complexa.
""")