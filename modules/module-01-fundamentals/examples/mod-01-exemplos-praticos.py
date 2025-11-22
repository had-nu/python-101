# ============================================================================
# MÓDULO 01 - EXEMPLOS PRÁTICOS
# Fundamentos e Pensamento Computacional
# ============================================================================

# ----------------------------------------------------------------------------
# EXEMPLO 1: Calculadora de Preço com IVA
# Contexto: Você trabalha em uma loja e precisa calcular o preço final
# de produtos após adicionar o IVA (Imposto sobre Valor Acrescentado)
# ----------------------------------------------------------------------------

print("=== EXEMPLO 1: Calculadora de Preço com IVA ===\n")

# Primeiro, definimos o preço base do produto
# Usamos float porque preços podem ter centavos
preco_base = 50.00

# A taxa de IVA em Portugal é 23%, que expressamos como 0.23 em decimal
# Usar uma variável em vez de repetir 0.23 por todo código torna
# fácil mudar a taxa se necessário (por exemplo, para produtos com taxa reduzida)
TAXA_IVA = 0.23

# Calculamos quanto de IVA será adicionado ao preço
# Isto é simplesmente uma percentagem do preço base
valor_iva = preco_base * TAXA_IVA

# O preço final é o preço base mais o valor do IVA
preco_final = preco_base + valor_iva

# Apresentamos os resultados de forma clara e organizada
# Note o uso de :.2f para mostrar exatamente 2 casas decimais (padrão para dinheiro)
print(f"Preço base: {preco_base:.2f} €")
print(f"IVA (23%): {valor_iva:.2f} €")
print(f"Preço final: {preco_final:.2f} €")

# Observe que também poderíamos ter calculado o preço final diretamente:
# preco_final = preco_base * (1 + TAXA_IVA)
# Mas dividir em etapas torna o código mais legível e permite mostrar valores intermediários

print("\n" + "="*50 + "\n")

# ----------------------------------------------------------------------------
# EXEMPLO 2: Calculadora de Média de Notas
# Contexto: Você é professor e precisa calcular a média de três provas
# de um aluno
# ----------------------------------------------------------------------------

print("=== EXEMPLO 2: Calculadora de Média de Notas ===\n")

# Definimos as três notas do aluno
# Em um programa real, estas viriam de input() do usuário
nota_prova1 = 15.5
nota_prova2 = 17.0
nota_prova3 = 16.5

# Calculamos a média aritmética somando todas as notas e dividindo pela quantidade
# A média aritmética é a soma de todos os valores dividida pelo número de valores
media = (nota_prova1 + nota_prova2 + nota_prova3) / 3

# Apresentamos o resultado com uma casa decimal (comum para notas)
print(f"Nota da Prova 1: {nota_prova1:.1f}")
print(f"Nota da Prova 2: {nota_prova2:.1f}")
print(f"Nota da Prova 3: {nota_prova3:.1f}")
print(f"Média Final: {media:.1f}")

# Poderíamos também verificar se o aluno passou (média >= 10 em Portugal)
# Mas isso requer estruturas condicionais que aprenderemos no próximo módulo

print("\n" + "="*50 + "\n")

# ----------------------------------------------------------------------------
# EXEMPLO 3: Calculadora de Troco com Gorjeta
# Contexto: Você está em um restaurante e quer calcular quanto dar de troco
# ao cliente, considerando que ele quer dar 10% de gorjeta ao funcionário
# ----------------------------------------------------------------------------

print("=== EXEMPLO 3: Calculadora de Troco com Gorjeta ===\n")

# Valor da conta que o cliente deve pagar
valor_conta = 45.80

# Valor que o cliente entregou para pagamento (nota de 50 euros)
valor_pago = 50.00

# Calculamos o troco inicial (antes de considerar gorjeta)
# Isto é simplesmente o que foi pago menos o que era devido
troco_inicial = valor_pago - valor_conta

# O cliente quer dar 10% do troco como gorjeta
# Expressamos 10% como 0.10 em decimal
percentual_gorjeta = 0.10

# Calculamos o valor da gorjeta
valor_gorjeta = troco_inicial * percentual_gorjeta

# O troco efetivo que volta ao cliente é o troco inicial menos a gorjeta
troco_efetivo = troco_inicial - valor_gorjeta

# Apresentamos todos os valores de forma organizada
print(f"Valor da conta: {valor_conta:.2f} €")
print(f"Valor pago: {valor_pago:.2f} €")
print(f"Troco inicial: {troco_inicial:.2f} €")
print(f"Gorjeta (10%): {valor_gorjeta:.2f} €")
print(f"Troco efetivo ao cliente: {troco_efetivo:.2f} €")

# Este exemplo mostra como um cálculo aparentemente simples pode ter várias etapas
# Decompor em passos claros torna o código mais fácil de entender e verificar

print("\n" + "="*50 + "\n")

# ----------------------------------------------------------------------------
# EXEMPLO 4: Calculadora de Área de Triângulo
# Contexto: Você precisa calcular a área de um terreno triangular
# para determinar quanto material de cobertura comprar
# ----------------------------------------------------------------------------

print("=== EXEMPLO 4: Calculadora de Área de Triângulo ===\n")

# Medidas do triângulo em metros
base = 12.5
altura = 8.0

# A fórmula da área de um triângulo é (base * altura) / 2
# Os parênteses são tecnicamente desnecessários devido à precedência de operadores,
# mas tornam a intenção explícita e o código mais legível
area = (base * altura) / 2

print(f"Base do triângulo: {base} m")
print(f"Altura do triângulo: {altura} m")
print(f"Área calculada: {area} m²")

# Se o material custa 15 euros por metro quadrado, podemos calcular o custo total
custo_por_metro = 15.00
custo_total = area * custo_por_metro

print(f"\nCusto do material (15€/m²): {custo_total:.2f} €")

print("\n" + "="*50 + "\n")

# ----------------------------------------------------------------------------
# EXEMPLO 5: Conversão de Temperatura (Celsius para Fahrenheit)
# Contexto: Você está planejando uma viagem aos EUA e quer converter
# temperaturas de Celsius (usado na Europa) para Fahrenheit
# ----------------------------------------------------------------------------

print("=== EXEMPLO 5: Conversão de Temperatura ===\n")

# Temperatura em Celsius (verão típico em Lisboa)
temperatura_celsius = 28.0

# A fórmula de conversão é: F = (C * 9/5) + 32
# Dividimos em etapas para claridade
temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32

print(f"Temperatura em Celsius: {temperatura_celsius:.1f}°C")
print(f"Temperatura em Fahrenheit: {temperatura_fahrenheit:.1f}°F")

# Podemos também fazer a conversão inversa (Fahrenheit para Celsius)
# Fórmula: C = (F - 32) * 5/9
temp_fahrenheit_referencia = 86.0
temp_celsius_convertida = (temp_fahrenheit_referencia - 32) * 5/9

print(f"\nConversão inversa:")
print(f"{temp_fahrenheit_referencia:.1f}°F = {temp_celsius_convertida:.1f}°C")

print("\n" + "="*50 + "\n")

# ----------------------------------------------------------------------------
# EXEMPLO 6: Programa Interativo - Calculadora de IMC
# Contexto: Este exemplo mostra como criar um programa que interage com o usuário
# calculando o Índice de Massa Corporal
# ----------------------------------------------------------------------------

print("=== EXEMPLO 6: Calculadora Interativa de IMC ===\n")

# Nota: Este exemplo está comentado para que você possa executar o arquivo completo
# sem precisar fornecer entrada. Descomente as linhas abaixo para testar interação.

"""
# Solicitamos o peso em quilogramas
peso = float(input("Digite seu peso em kg: "))

# Solicitamos a altura em metros
altura = float(input("Digite sua altura em metros (ex: 1.75): "))

# A fórmula do IMC é peso dividido pela altura ao quadrado
# Usamos o operador ** para exponenciação
imc = peso / (altura ** 2)

# Apresentamos o resultado com uma casa decimal
print(f"\nSeu IMC é: {imc:.1f}")

# Note que neste módulo ainda não aprendemos estruturas condicionais
# para classificar o IMC (abaixo do peso, normal, sobrepeso, etc.)
# Isso virá no Módulo 02
"""

# Para demonstração sem requerer input, usamos valores fixos
peso_exemplo = 70.0  # kg
altura_exemplo = 1.75  # metros

imc_exemplo = peso_exemplo / (altura_exemplo ** 2)

print(f"Exemplo de cálculo:")
print(f"Peso: {peso_exemplo} kg")
print(f"Altura: {altura_exemplo} m")
print(f"IMC: {imc_exemplo:.1f}")

print("\n" + "="*50 + "\n")

# ----------------------------------------------------------------------------
# EXEMPLO 7: Trabalhando com Múltiplas Operações
# Contexto: Cálculo do custo total de produção de cubos artísticos
# considerando material, quantidade e desperdício
# ----------------------------------------------------------------------------

print("=== EXEMPLO 7: Custo de Produção de Cubos ===\n")

# Um artista produz cubos de 2cm de aresta
aresta_cubo = 2  # cm

# Área de um cubo é 6 vezes a área de uma face (aresta²)
# O número 6 vem do fato de que um cubo tem 6 faces
area_cubo = aresta_cubo * aresta_cubo * 6
print(f"Área de um cubo: {area_cubo} cm²")

# Quantidade de cubos a produzir
quantidade_cubos = 10

# Área total a pintar
area_total = area_cubo * quantidade_cubos
print(f"Área total para {quantidade_cubos} cubos: {area_total} cm²")

# Tinta: 1 dl cobre 5 cm²
# Primeiro calculamos quantos dl são necessários
cobertura_por_dl = 5  # cm² por dl
dl_necessarios = area_total / cobertura_por_dl
print(f"Quantidade de tinta necessária: {dl_necessarios} dl")

# Tinta é vendida em latas de 1.5 dl a 2.75€
capacidade_lata = 1.5  # dl
preco_lata = 2.75  # euros

# Calculamos quantas latas precisamos (arredondando para cima)
# Usamos divisão normal e depois round() para arredondar
# Note: em produção real, usaríamos math.ceil() para sempre arredondar para cima
latas_necessarias = round(dl_necessarios / capacidade_lata + 0.5)  # truque simples para arredondar para cima

# Custo total
custo_total = latas_necessarias * preco_lata

print(f"Latas necessárias: {latas_necessarias}")
print(f"Custo total: {custo_total:.2f} €")
print(f"Custo por cubo: {custo_total / quantidade_cubos:.2f} €")

print("\n" + "="*50 + "\n")

# ----------------------------------------------------------------------------
# EXEMPLO 8: Extração de Dígitos de um Número
# Contexto: Dado um número de 3 dígitos, separar os dígitos individuais
# Técnica útil em muitos algoritmos de processamento numérico
# ----------------------------------------------------------------------------

print("=== EXEMPLO 8: Extração de Dígitos ===\n")

# Temos um número de três dígitos
numero = 472

# Para extrair o dígito das centenas: dividimos por 100 e pegamos só a parte inteira
centenas = numero // 100
print(f"Dígito das centenas: {centenas}")

# Para as dezenas: removemos as centenas, depois dividimos por 10
# Primeiro removemos as centenas multiplicando elas por 100 e subtraindo
resto_sem_centenas = numero - (centenas * 100)
dezenas = resto_sem_centenas // 10
print(f"Dígito das dezenas: {dezenas}")

# Para as unidades: usamos o operador módulo
# numero % 10 nos dá o resto da divisão por 10, que é exatamente o último dígito
unidades = numero % 10
print(f"Dígito das unidades: {unidades}")

# Verificação: reconstruir o número original
numero_reconstruido = (centenas * 100) + (dezenas * 10) + unidades
print(f"\nNúmero original: {numero}")
print(f"Número reconstruído: {numero_reconstruido}")
print(f"Dígitos separados: {centenas} {dezenas} {unidades}")

# Esta técnica de usar divisão inteira e módulo para extrair dígitos
# é fundamental em muitos algoritmos e será usada em vários exercícios

print("\n" + "="*50 + "\n")

# ----------------------------------------------------------------------------
# EXEMPLO 9: Cálculo de Sucessor e Antecedente
# Contexto: Operações simples mas fundamentais que aparecem em muitos algoritmos
# ----------------------------------------------------------------------------

print("=== EXEMPLO 9: Sucessor e Antecedente ===\n")

# Dado um número qualquer
numero = 42

# O antecedente (número anterior) é simplesmente o número menos 1
antecedente = numero - 1

# O sucessor (número posterior) é o número mais 1
sucessor = numero + 1

print(f"Número original: {numero}")
print(f"Antecedente: {antecedente}")
print(f"Sucessor: {sucessor}")

# Embora pareça trivial, este padrão é usado constantemente em algoritmos
# Por exemplo, ao navegar em sequências, ao gerar números consecutivos, etc.

print("\n" + "="*50 + "\n")

# ----------------------------------------------------------------------------
# EXEMPLO 10: Formatação Avançada de Saída
# Contexto: Demonstra diferentes formas de formatar números e texto
# para criar saídas profissionais e legíveis
# ----------------------------------------------------------------------------

print("=== EXEMPLO 10: Formatação Avançada ===\n")

# Valores para demonstração
produto = "Café Premium"
quantidade = 3
preco_unitario = 4.756
preco_total = quantidade * preco_unitario

# Formatação básica com duas casas decimais para dinheiro
print(f"Produto: {produto}")
print(f"Quantidade: {quantidade}")
print(f"Preço unitário: {preco_unitario:.2f} €")
print(f"Preço total: {preco_total:.2f} €")

print("\nFormatação alinhada para criar tabela:")

# Usando formatação com alinhamento e largura fixa
# :<20 significa alinhar à esquerda em campo de 20 caracteres
# :>8 significa alinhar à direita em campo de 8 caracteres
print(f"{'Descrição':<20} {'Qtd':>8} {'Preço':>10} {'Total':>10}")
print("-" * 58)
print(f"{produto:<20} {quantidade:>8} {preco_unitario:>10.2f} {preco_total:>10.2f}")

# Este tipo de formatação é essencial para criar interfaces de terminal
# profissionais e legíveis

print("\n" + "="*50 + "\n")

print("""
CONCLUSÃO DOS EXEMPLOS:

Estes exemplos demonstraram os conceitos fundamentais do Módulo 01:
- Variáveis para armazenar e nomear valores significativamente
- Operações aritméticas básicas e suas aplicações práticas
- Entrada de dados do usuário e conversão de tipos
- Formatação de saída para apresentação clara de resultados
- Decomposição de problemas em etapas lógicas e calculáveis

Cada exemplo mostrou não apenas COMO fazer algo tecnicamente,
mas QUANDO e POR QUE você faria dessa forma específica.

Agora você está pronto para aplicar estes conceitos nos exercícios,
onde terá chance de resolver problemas reais de forma independente,
consolidando seu entendimento através da prática ativa.
""")