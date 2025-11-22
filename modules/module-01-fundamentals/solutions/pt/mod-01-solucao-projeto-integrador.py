# ============================================================================
# PROJETO INTEGRADOR - MÓDULO 01
# Sistema de Orçamento para Construção Civil
# ============================================================================
# 
# Este programa calcula orçamentos automatizados para projetos de cobertura
# de terrenos retangulares ou triangulares com diferentes materiais.
#
# Autor: Python-101 Project
# Módulo: 01 - Fundamentos e Pensamento Computacional
# ============================================================================

# ----------------------------------------------------------------------------
# CONSTANTES DO SISTEMA
# ----------------------------------------------------------------------------
# Definimos todas as taxas, percentagens e preços como constantes no início
# Isto facilita manutenção e ajustes futuros sem alterar lógica do programa

# Margem de desperdício típica em construção civil (15%)
MARGEM_DESPERDICIO = 0.15

# Margem de lucro da empresa (25%)
MARGEM_LUCRO = 0.25

# Taxa de impostos aplicada (18%)
TAXA_IMPOSTOS = 0.18

# Preços dos materiais por metro quadrado
PRECO_CONCRETO = 45.00  # euros/m²
PRECO_PAVIMENTO = 32.00  # euros/m²
PRECO_GRAMA = 18.00  # euros/m²

# ----------------------------------------------------------------------------
# APRESENTAÇÃO DO SISTEMA
# ----------------------------------------------------------------------------
print("=" * 60)
print("        SISTEMA DE ORÇAMENTO - CONSTRUÇÃO CIVIL")
print("=" * 60)
print()

# ----------------------------------------------------------------------------
# FASE 1: COLETA DE INFORMAÇÕES DO TERRENO
# ----------------------------------------------------------------------------
print("INFORMAÇÕES DO TERRENO")
print("-" * 60)

# Perguntamos qual formato de terreno será coberto
# Esta informação determina que medidas pediremos e que fórmula usaremos
formato_terreno = input("Digite o formato do terreno (retangular/triangular): ").lower()

# Baseado no formato, coletamos medidas apropriadas e calculamos área
# Inicializamos a variável area_terreno que será usada independente do formato
area_terreno = 0

if formato_terreno == "retangular":
    # Para terreno retangular, precisamos de comprimento e largura
    comprimento = float(input("Digite o comprimento do terreno em metros: "))
    largura = float(input("Digite a largura do terreno em metros: "))
    
    # Área de retângulo é comprimento multiplicado por largura
    area_terreno = comprimento * largura
    
    # Armazenamos dimensões para exibir no orçamento final
    dimensoes_texto = f"{comprimento:.2f}m x {largura:.2f}m"
    formato_texto = "Retangular"
    
elif formato_terreno == "triangular":
    # Para terreno triangular, precisamos de base e altura
    base = float(input("Digite a base do triângulo em metros: "))
    altura = float(input("Digite a altura do triângulo em metros: "))
    
    # Área de triângulo é (base multiplicada por altura) dividido por 2
    area_terreno = (base * altura) / 2
    
    # Armazenamos dimensões para exibir no orçamento final
    dimensoes_texto = f"Base: {base:.2f}m, Altura: {altura:.2f}m"
    formato_texto = "Triangular"
else:
    # Se formato não for reconhecido, exibimos mensagem e encerramos
    # Em versão mais avançada, poderíamos pedir entrada novamente
    print("Formato não reconhecido. Encerrando programa.")
    exit()

print()

# ----------------------------------------------------------------------------
# FASE 2: ESCOLHA DO MATERIAL
# ----------------------------------------------------------------------------
print("ESCOLHA DO MATERIAL")
print("-" * 60)
print("Materiais disponíveis:")
print(f"  1. Concreto - {PRECO_CONCRETO:.2f} €/m²")
print(f"  2. Pavimento - {PRECO_PAVIMENTO:.2f} €/m²")
print(f"  3. Grama artificial - {PRECO_GRAMA:.2f} €/m²")

# Coletamos escolha do usuário
escolha_material = int(input("Digite o número do material escolhido: "))

# Baseado na escolha, definimos preço por metro quadrado e nome do material
if escolha_material == 1:
    preco_por_m2 = PRECO_CONCRETO
    nome_material = "Concreto"
elif escolha_material == 2:
    preco_por_m2 = PRECO_PAVIMENTO
    nome_material = "Pavimento"
elif escolha_material == 3:
    preco_por_m2 = PRECO_GRAMA
    nome_material = "Grama artificial"
else:
    print("Opção inválida. Encerrando programa.")
    exit()

print("\nCalculando orçamento...")
print()

# ----------------------------------------------------------------------------
# FASE 3: CÁLCULOS DE ÁREA E MATERIAL NECESSÁRIO
# ----------------------------------------------------------------------------
# Em construção, sempre há desperdício de material devido a cortes e ajustes
# Aplicamos margem de desperdício para calcular área real de material a comprar
area_material_necessario = area_terreno * (1 + MARGEM_DESPERDICIO)

# ----------------------------------------------------------------------------
# FASE 4: CÁLCULOS FINANCEIROS
# ----------------------------------------------------------------------------
# Custo bruto de materiais é área necessária vezes preço por metro quadrado
custo_materiais = area_material_necessario * preco_por_m2

# A empresa aplica margem de lucro sobre o custo de materiais
# Esta margem representa lucro operacional e cobre custos indiretos
valor_margem_lucro = custo_materiais * MARGEM_LUCRO

# Subtotal é custo de materiais mais margem de lucro
# Sobre este subtotal que incidirão os impostos
subtotal = custo_materiais + valor_margem_lucro

# Impostos são calculados sobre o subtotal (materiais + lucro)
valor_impostos = subtotal * TAXA_IMPOSTOS

# Valor final do orçamento é soma de todos componentes
valor_total_orcamento = subtotal + valor_impostos

# ----------------------------------------------------------------------------
# FASE 5: APRESENTAÇÃO DO ORÇAMENTO FINAL
# ----------------------------------------------------------------------------
print("=" * 60)
print("                  ORÇAMENTO FINAL")
print("=" * 60)
print()

# Dados do terreno
print("DADOS DO TERRENO:")
print(f"Formato: {formato_texto}")
print(f"Dimensões: {dimensoes_texto}")
print(f"Área do terreno: {area_terreno:.2f} m²")
print(f"Área de material (com {MARGEM_DESPERDICIO * 100:.0f}% desperdício): {area_material_necessario:.2f} m²")
print()

# Material selecionado
print("MATERIAL SELECIONADO:")
print(f"{nome_material} - {preco_por_m2:.2f} €/m²")
print()

# Discriminação detalhada de custos
print("DISCRIMINAÇÃO DE CUSTOS:")
print(f"Custo de materiais: {custo_materiais:.2f} €")
print(f"Margem de lucro ({MARGEM_LUCRO * 100:.0f}%): {valor_margem_lucro:.2f} €")
print(f"Subtotal: {subtotal:.2f} €")
print(f"Impostos ({TAXA_IMPOSTOS * 100:.0f}%): {valor_impostos:.2f} €")
print()

# Valor total destacado
print("-" * 60)
print(f"VALOR TOTAL DO ORÇAMENTO: {valor_total_orcamento:.2f} €")
print("-" * 60)
print()

# Informações adicionais
print("Orçamento válido por 30 dias.")
print("Obrigado por consultar nossos serviços!")
print()

# ============================================================================
# OBSERVAÇÕES PEDAGÓGICAS SOBRE ESTA SOLUÇÃO
# ============================================================================
"""
Esta solução demonstra múltiplas melhores práticas aprendidas no Módulo 01:

1. ESTRUTURA CLARA:
   O programa está organizado em fases lógicas bem definidas, cada uma
   com propósito claro. Comentários de seção facilitam navegação no código.

2. CONSTANTES NO INÍCIO:
   Todas as taxas e preços são definidas como constantes no início,
   facilitando manutenção. Para mudar a margem de lucro, altera-se
   apenas uma linha no topo do arquivo.

3. NOMES DESCRITIVOS:
   Variáveis têm nomes que comunicam significado: area_terreno,
   custo_materiais, valor_margem_lucro. Isto torna código auto-documentado.

4. COMENTÁRIOS EXPLICATIVOS:
   Comentários explicam o raciocínio por trás de decisões e cálculos,
   não apenas repetem o que o código faz. Por exemplo, explicamos
   POR QUE aplicamos margem de desperdício.

5. FORMATAÇÃO PROFISSIONAL:
   Toda saída é formatada com duas casas decimais para valores monetários,
   usa linhas de separação visual, e está organizada de forma legível.

6. CÁLCULOS INTERMEDIÁRIOS VISÍVEIS:
   Em vez de calcular tudo em uma expressão complexa, decompomos em
   etapas que mostram valores intermediários, tornando verificação mais fácil.

7. DECOMPOSIÇÃO DE PROBLEMA:
   Problema complexo foi quebrado em componentes manejáveis: coletar entrada,
   calcular área, calcular material, calcular finanças, apresentar resultado.

8. USO APROPRIADO DE TIPOS:
   Usamos int() para escolhas de menu e contadores, float() para medidas
   e valores monetários que podem ter decimais.

9. VALIDAÇÃO BÁSICA:
   Embora não tenhamos aprendido tratamento de erros formalmente,
   verificamos se formato e material escolhidos são válidos.

10. PREPARAÇÃO PARA EXPANSÃO:
    O código está estruturado de forma que adicionar novos materiais
    ou formatos de terreno seria relativamente simples.

MELHORIAS POSSÍVEIS (que você aprenderá em módulos futuros):

- No Módulo 02, você aprenderá estruturas condicionais mais sofisticadas
  que tornariam a validação de entrada mais robusta e amigável.

- No Módulo 03, você aprenderá loops que permitiriam processar múltiplos
  terrenos em uma única execução ou solicitar entrada novamente se inválida.

- No Módulo 04, você aprenderá funções que permitiriam organizar este código
  em componentes reutilizáveis e mais fáceis de testar.

- No Módulo 07, você aprenderá a trabalhar com arquivos para salvar
  orçamentos em formato que pode ser impresso ou enviado por email.

Mas com apenas os fundamentos do Módulo 01, você já é capaz de criar
uma aplicação funcional e útil que resolve problema real de forma profissional!
"""