# Projeto Integrador - Módulo 01
## Sistema de Orçamento para Construção Civil

### Introdução ao Projeto

Parabéns por chegar ao projeto integrador do Módulo 01! Este projeto foi cuidadosamente desenhado para consolidar todos os conceitos que você aprendeu nos exercícios individuais, combinando-os numa aplicação mais complexa e realista que simula um problema do mundo real.

Diferente dos exercícios anteriores que focavam em habilidades específicas, este projeto requer que você integre múltiplas competências simultaneamente, decida como estruturar o código, e crie uma experiência completa para o usuário final. É sua oportunidade de demonstrar maestria do material do módulo e preparar-se com confiança para o Módulo 02.

### Contexto do Problema

Você foi contratado para desenvolver um sistema de orçamento automatizado para uma pequena empresa de construção civil. A empresa frequentemente precisa calcular orçamentos para projetos de cobertura de terrenos retangulares e triangulares com diferentes materiais.

O processo manual atual é trabalhoso e propenso a erros. O gerente explica que cada orçamento requer múltiplos cálculos encadeados: primeiro determinar a área total a cobrir, depois calcular quantidade de material necessário considerando desperdício típico, aplicar margem de lucro e impostos ao custo de materiais, e finalmente apresentar proposta completa ao cliente com todos os valores discriminados.

Seu sistema deve automatizar completamente este processo, pedindo apenas as informações essenciais ao usuário e calculando todos os valores derivados automaticamente, apresentando resultado final profissional e completo.

### Especificação Funcional

Seu programa deve implementar as seguintes funcionalidades integradas:

**Fase 1: Coleta de Informações Básicas**

O sistema deve iniciar exibindo um título claro e acolhedor identificando-se como Sistema de Orçamento para Construção. Depois deve solicitar informações sobre o terreno, incluindo qual formato geométrico descreve a área a cobrir, podendo ser retangular ou triangular, exigindo medidas apropriadas dependendo da escolha.

Se o terreno for retangular, o sistema pede comprimento e largura em metros. Se for triangular, pede base e altura em metros. Todos estes valores devem aceitar decimais para permitir medidas precisas.

O sistema deve também perguntar qual material será usado na cobertura, oferecendo três opções: concreto que custa 45 euros por metro quadrado, pavimento que custa 32 euros por metro quadrado, ou grama artificial que custa 18 euros por metro quadrado.

**Fase 2: Cálculos de Área e Material**

Com base no formato escolhido e nas medidas fornecidas, o sistema calcula a área total a ser coberta, usando a fórmula apropriada. Para terrenos retangulares a área é comprimento multiplicado por largura. Para terrenos triangulares a área é base multiplicada por altura dividido por dois.

O sistema deve então aplicar uma margem de desperdício de quinze por cento sobre a área calculada, pois em construção sempre há perda de material durante aplicação, cortes e ajustes. A área total de material a comprar é portanto a área calculada multiplicada por um vírgula quinze.

Com a área final de material necessário e o preço por metro quadrado do material escolhido, o sistema calcula o custo bruto de materiais.

**Fase 3: Cálculos Financeiros e Formação do Preço Final**

Sobre o custo de materiais, a empresa aplica margem de lucro de vinte e cinco por cento. Este valor representa o lucro operacional da empresa e deve ser calculado como percentagem do custo de materiais.

Adicionalmente, há impostos de dezoito por cento que incidem sobre a soma do custo de materiais e da margem de lucro. Estes impostos incluem contribuições fiscais diversas e devem ser calculados sobre o subtotal que já inclui a margem.

O preço final apresentado ao cliente é a soma de todos estes componentes: custo de materiais, margem de lucro da empresa, e impostos.

**Fase 4: Apresentação do Orçamento**

O sistema deve apresentar um orçamento completo e profissional discriminando todos os valores calculados. A apresentação deve incluir título indicando que é o orçamento final, seguido de informações sobre o terreno especificando formato e dimensões fornecidas.

Depois deve mostrar área calculada do terreno, área total de material necessário incluindo o desperdício, e tipo de material selecionado com seu preço unitário.

A discriminação financeira deve mostrar custo bruto de materiais, margem de lucro aplicada com sua percentagem, impostos com sua percentagem, e finalmente o valor total do orçamento de forma destacada.

Todos os valores monetários devem ser formatados com exatamente duas casas decimais e o símbolo do euro. Valores de área devem mostrar duas casas decimais seguidas da unidade m².

### Requisitos Técnicos

Seu código deve demonstrar as melhores práticas aprendidas durante o módulo. Use nomes de variáveis descritivos que comuniquem claramente o que cada valor representa. Por exemplo, use `area_terreno` em vez de apenas `a`, ou `custo_materiais` em vez de `c`.

Defina todas as percentagens, taxas e preços de materiais como constantes no início do programa, escritas em maiúsculas para indicar que são valores configuráveis que não mudam durante execução. Isto facilita ajustar estes valores no futuro sem precisar procurá-los no meio do código.

Organize seu código em seções lógicas claramente separadas, com comentários indicando o propósito de cada seção. As seções naturais são: coleta de entrada, cálculos de área, cálculos de material, cálculos financeiros, e apresentação de resultados.

Adicione comentários explicativos antes de cálculos complexos ou não óbvios, explicando a lógica por trás da operação. Não comente coisas óbvias como "incrementa contador", mas sim raciocínios como "aplicamos margem de desperdício porque em construção há sempre perda de material".

Formate toda saída de forma profissional e legível, usando linhas de separação visual onde apropriado, alinhando valores monetários corretamente, e garantindo que o orçamento final pareça um documento que poderia ser apresentado a um cliente real.

### Exemplo de Execução Completa

Para ilustrar como o sistema completo deve funcionar, aqui está uma execução exemplo com terreno retangular:

```
==========================================================
        SISTEMA DE ORÇAMENTO - CONSTRUÇÃO CIVIL
==========================================================

INFORMAÇÕES DO TERRENO
Digite o formato do terreno (retangular/triangular): retangular
Digite o comprimento do terreno em metros: 15.5
Digite a largura do terreno em metros: 8.0

ESCOLHA DO MATERIAL
Materiais disponíveis:
  1. Concreto - 45.00 €/m²
  2. Pavimento - 32.00 €/m²
  3. Grama artificial - 18.00 €/m²
Digite o número do material escolhido: 2

Calculando orçamento...

==========================================================
                  ORÇAMENTO FINAL
==========================================================

DADOS DO TERRENO:
Formato: Retangular
Dimensões: 15.50m x 8.00m
Área do terreno: 124.00 m²
Área de material (com 15% desperdício): 142.60 m²

MATERIAL SELECIONADO:
Pavimento - 32.00 €/m²

DISCRIMINAÇÃO DE CUSTOS:
Custo de materiais: 4563.20 €
Margem de lucro (25%): 1140.80 €
Subtotal: 5704.00 €
Impostos (18%): 1026.72 €

----------------------------------------------------------
VALOR TOTAL DO ORÇAMENTO: 6730.72 €
----------------------------------------------------------

Orçamento válido por 30 dias.
Obrigado por consultar nossos serviços!
```

### Orientações Para Desenvolvimento

Aborde este projeto de forma incremental, não tentando construir tudo de uma vez. Comece implementando apenas a coleta de informações do terreno retangular e cálculo de sua área, testando que funciona antes de adicionar mais complexidade.

Depois adicione o cálculo de material com margem de desperdício. Teste novamente. Depois adicione os cálculos financeiros. Teste cada etapa independentemente antes de integrar a próxima. Esta abordagem incremental facilita identificar exatamente onde está qualquer problema, pois você sabe que tudo que funcionava antes continua funcionando.

Quando tiver o fluxo básico funcionando para terreno retangular, adicione suporte para terrenos triangulares. Você precisará usar estrutura condicional para distinguir entre os dois casos, mas isto é mais simples do que parece. Pense em cada formato como um caminho diferente através do mesmo programa.

Para a escolha de material, você pode usar uma abordagem similar, onde baseado na escolha do usuário você seleciona o preço apropriado. Novamente, pense em cada material como um caminho diferente que eventualmente chega ao mesmo lugar, o cálculo final.

Dedique atenção especial à formatação da saída. Um orçamento bem apresentado não é apenas esteticamente agradável, mas comunica profissionalismo e inspira confiança. Use linhas de separação, espaçamento adequado, e alinhamento consistente.

Teste seu programa com múltiplos cenários diferentes. Teste com terreno retangular e triangular. Teste com cada tipo de material. Teste com dimensões pequenas e grandes. Teste com valores que resultam em números decimais complexos para verificar que a formatação está correta. Cada teste aumenta sua confiança de que o sistema funciona robustamente.

### Critérios de Avaliação

Seu projeto será considerado completo e bem-sucedido quando atender todos estes critérios. Funcionalidade significa que o programa executa sem erros, aceita todas as entradas especificadas, realiza todos os cálculos corretamente, e produz orçamento completo e preciso. Teste rigorosamente para garantir isto.

Qualidade de código significa uso consistente de nomes descritivos, organização lógica em seções claras, comentários úteis que explicam raciocínio, e ausência de código redundante ou confuso. Revise seu código como se outra pessoa fosse lê-lo e mantê-lo.

Apresentação profissional significa que a saída é formatada de forma limpa e organizada, todos os valores monetários usam formato apropriado com duas casas decimais, há alinhamento e espaçamento visual adequados, e o documento final poderia ser apresentado a um cliente real.

Compreensão profunda significa que você pode explicar claramente cada parte do código, justificar decisões de design que tomou, e modificar o programa para adicionar novas funcionalidades se solicitado. Este entendimento é mais importante que simplesmente fazer funcionar.

### Extensões Opcionais Para Aprendizado Adicional

Se você completou o projeto básico e quer desafios adicionais para aprofundar aprendizado, considere estas extensões opcionais que não são obrigatórias mas oferecem prática valiosa.

Você poderia adicionar validação de entrada verificando que dimensões são positivas, que formato digitado é válido, e que escolha de material é uma das opções disponíveis. Embora você ainda não tenha aprendido estruturas condicionais formalmente no Módulo 02, pode começar a pensar sobre estas verificações.

Poderia adicionar cálculo de tempo estimado de execução baseado na área, assumindo que uma equipe consegue cobrir certa quantidade de metros quadrados por dia. Isto oferece informação adicional valiosa ao cliente sobre prazo do projeto.

Poderia criar uma versão que calcula orçamentos para múltiplos terrenos em uma única execução, acumulando área total e custo total do projeto completo. Isto simula projetos com múltiplas áreas a serem cobertas.

Poderia adicionar opção de desconto para projetos grandes, aplicando percentagem de desconto reduzida quando área total ultrapassa determinado limite. Isto simula práticas comerciais reais de incentivo a projetos maiores.

### Reflexão Final

Este projeto integrador representa culminação do seu aprendizado no Módulo 01. Ao completá-lo com sucesso, você demonstrou não apenas conhecimento de sintaxe Python, mas compreensão profunda de como decompor problemas complexos, como estruturar código de forma lógica e legível, e como criar aplicações que resolvem necessidades reais de forma profissional.

Mais importante, você desenvolveu pensamento computacional, a capacidade de olhar situações do mundo real e reconhecer como modelá-las usando abstrações e operações computacionais. Esta habilidade transcende Python ou qualquer linguagem específica, sendo a essência verdadeira de programação.

Quando você completar este projeto, pause e reflita sobre sua jornada desde o início do módulo quando talvez não soubesse nada sobre programação. Observe quanto progresso fez, quantos conceitos dominou, e quão capaz você se tornou de resolver problemas complexos através de código.

Este é apenas o começo. O Módulo 02 construirá sobre estas fundações, introduzindo estruturas de decisão que tornarão seus programas muito mais inteligentes e capazes. Mas tudo que você aprenderá lá depende do domínio sólido destes fundamentos que você desenvolveu aqui.

Boa sorte com seu projeto, e lembre-se que a comunidade está aqui para apoiar você caso encontre dificuldades. Quando completar, considere compartilhar sua solução para que outros estudantes possam aprender com sua abordagem, e veja soluções de outros para expandir sua perspectiva sobre diferentes formas de resolver o mesmo problema.

Você chegou longe, e tem todos os motivos para se orgulhar do que conquistou!