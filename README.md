# 📊 FATEC Exam Analytics: Reverse Engineering & Predictive Modeling

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Manipulation-150458.svg)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Low%20Level%20Rendering-brightgreen.svg)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20API-4C72B0.svg)
![Status](https://img.shields.io/badge/Status-Deployed-success.svg)
![Domain](https://img.shields.io/badge/Domain-Data%20Science%20%26%20Analytics-black.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

> **TL;DR (Executive Summary):**
> * 🎯 **O Problema:** Identificar padrões ocultos (Assimetria Controlada) na distribuição de alternativas dos gabaritos da FATEC.
> * 🛠️ **A Solução:** Análise estatística de variância e desvio padrão sobre 15 anos de dados (Data Wrangling & EDA).
> * 📈 **O Resultado:** Descoberta empírica de *alternativas-âncora* (baixo risco) e *alternativas-gatilho* (alta volatilidade), permitindo otimizar a tomada de decisão sob pressão de tempo (Forecasting).

## 🛠️ Stack Tecnológico
**Linguagens & Bibliotecas:** Python, Pandas, NumPy, Matplotlib, Seaborn.
**Ambiente & Deploy:** Jupyter Notebook, Google Colab, VS Code, Git/GitHub.
**Conceitos Aplicados:** Data Analytics, Engenharia Reversa, Estatística Descritiva, Teoria dos Jogos.

---

## 📑 Índice
1. [Resumo Executivo e Problema de Negócio](#1-resumo-executivo-e-problema-de-negócio)
2. [Arquitetura de Dados e Pipeline ETL](#2-arquitetura-de-dados-e-pipeline-etl)
3. [Modelagem Estatística e Framework Matemático](#3-modelagem-estatística-e-framework-matemático)
4. [O Gênesis do Algoritmo: Cohort Legacy (48Q)](#4-o-gênesis-do-algoritmo-cohort-legacy-48q)
5. [Dashboard Analítico: Cohort Standard (54Q)](#5-dashboard-analítico-cohort-standard-54q)
6. [O Impacto da Transição: Cohort Expansion (60Q)](#6-o-impacto-da-transição-cohort-expansion-60q)
7. [A Linha do Tempo da Assimetria Controlada](#7-a-linha-do-tempo-da-assimetria-controlada)
8. [Forecasting e Otimização de Risco](#8-forecasting-e-otimização-de-risco)
9. [Estrutura do Projeto e Reprodutibilidade](#9-estrutura-do-projeto-e-reprodutibilidade)
10. [Roadmap e Próximos Passos](#10-roadmap-e-próximos-passos)

---

## 📌 1. Resumo Executivo e Problema de Negócio
Testes padronizados de múltipla escolha não são avaliações puramente de conhecimento; eles são sistemas probabilísticos complexos estruturados para medir proficiência sob pressão. Para garantir a integridade do exame e mitigar o ROI (Return on Investment) de técnicas baseadas em probabilidade cega (o "chute" estatístico), bancas examinadoras desenvolvem algoritmos proprietários de distribuição de alternativas.

Este projeto aplica técnicas de **Data Analytics, Engenharia Reversa e Estatística Descritiva** sobre o histórico longitudinal (2007 - 2026) do Vestibular da FATEC (Faculdade de Tecnologia de São Paulo). O objetivo primário é auditar a matriz de respostas da banca, identificar os vieses de "Assimetria Controlada" inseridos intencionalmente no sistema e desenvolver uma heurística preditiva para otimização de tomada de decisão.

---

## 🏗️ 2. Arquitetura de Dados e Pipeline ETL
Para garantir a confiabilidade matemática da análise, os dados brutos passaram por um pipeline rigoroso de *Extract, Transform, Load* (ETL), focado em governança e qualidade de dados:

* **Data Ingestion:** Extração orientada a lotes (batch processing) de espelhos de gabaritos oficiais das edições históricas da instituição.
* **Data Cleansing & Wrangling:** Normalização de dados não-estruturados em um esquema relacional (Tidy Data). O Dicionário de Dados consolidado encontra-se na pasta `/data`.
* **Feature Engineering:** Criação da dimensão categórica `Cohort` para segmentar os dados e evitar poluição estatística entre diferentes matrizes curriculares.
* **Integrity Checks:** Validação estrita garantindo que a soma das frequências absolutas seja perfeitamente igual ao Total de Questões do período investigado.

---

## 📐 3. Modelagem Estatística e Framework Matemático
Em um cenário de incerteza absoluta, a esperança matemática $E(X)$ de acertos em $n$ questões restantes com 5 alternativas é ditada por um modelo binomial clássico, onde a probabilidade natural é $p = 0.20$.

$$E(X) = n \cdot p$$

O objetivo da "Assimetria Controlada" da banca é manipular a variância $\sigma^2$ do exame para punir o chute ingênuo. O modelo de *scoring* deste projeto busca identificar alternativas com desvios positivos históricos consistentes, alterando o peso probabilístico para $p > 0.20$ e maximizando o Valor Esperado do candidato:

$$\sigma^2 = \frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N}$$

Através da análise da variância (dispersão em relação à média ideal $\mu$), isolamos o comportamento previsível de cada letra.

---

## 📉 4. O Gênesis do Algoritmo: Cohort Legacy (48Q)

![Dashboard FATEC 48 Questões](https://raw.githubusercontent.com/caiiobuenoo/FATEC/main/output/gabarito_fatec_48q.PNG)

A fase embrionária (2007.2 - 2009.2) revela o comportamento primitivo da banca. O "Muro Simétrico" demonstrava uma forte intenção de equilibrar a prova organicamente, mas com um viés estatístico de execução claro: as alternativas iniciais (A e B) frequentemente acumulavam desvios positivos por regras de arredondamento humano, enquanto a alternativa **E** absorvia o desvio negativo máximo, atuando como zona de descarte.

### 4.2. Cenários de Simulação Probabilística (Exame de 48Q)
Considerando a reexecução hipotética de uma prova sob as regras de automação desta cohort:

| Alternativa | Cenário 1 (Alta Variância) | Cenário 2 (Desvio Lateral) | Cenário 3 (Achatamento E) | Modelo "Certeiro" (Target) |
| :---: | :---: | :---: | :---: | :---: |
| **A** | 11 | 10 | 11 | **10** |
| **B** | 11 | 12 | 12 | **10** |
| **C** | 9 | 10 | 9 | **10** |
| **D** | 9 | 8 | 8 | **9** |
| **E** | 8 | 8 | 8 | **9** |
| **Total** | **48** | **48** | **48** | **48** |

* **Critério do Target:** O modelo ideal estabiliza no vetor $[10, 10, 10, 9, 9]$ devido à incapacidade estrutural do algoritmo primitivo em sustentar picos de volatilidade sem comprometer a restrição de simetria básica do período.

---

## 📈 5. Dashboard Analítico: Cohort Standard (54Q)

![Dashboard Executivo FATEC 54Q](https://raw.githubusercontent.com/caiiobuenoo/FATEC/main/output/gabarito_fatec_54q.PNG)

Na era de ouro da estabilidade (15 anos de dados consolidados), a visualização acima utiliza *barplots* para contrapor o **Modelo de Gabarito Ideal** contra o **Raio-X de Evolução Empilhada**, permitindo a detecção imediata de *outliers* na série temporal.

### 5.1. Deep Dive: A Psicologia do Algoritmo (54Q)
A Análise Exploratória de Dados (EDA) permitiu classificar o perfil de risco:

* 🔵 **Letra A (A "Baseline Silenciosa"):** Historicamente discreta, funciona como um preenchimento seguro e de baixa variância (canal entre 9 e 11).
* 🟠 **Letra B (O "Honeypot" Punitivo):** Sofreu um *Crash Point* algorítmico nas safras 2024.1 e 2024.2, caindo para apenas 5 respostas (circuit breaker punitivo da banca).
* 🟢 **Letra C (A "Âncora Estatística"):** Atua como o centro de gravidade. Possui o menor Desvio Padrão global, ancorando-se na marca de **10 respostas** na esmagadora maioria da série histórica.
* 🔴 **Letra D (O "Gatilho de Caos"):** O vetor primário de volatilidade. Registra picos anômalos de **15 a 17 ocorrências**.
* 🟣 **Letra E (O "Pêndulo de Compensação"):** Absorve o saldo residual das equações de distribuição.

### 5.2. Cenários de Simulação Probabilística (Exame de 54Q)
| Alternativa | Cenário 1 (Pico D) | Cenário 2 (Retorno do Honeypot) | Cenário 3 (Saturação E) | Modelo "Certeiro" (Target) |
| :---: | :---: | :---: | :---: | :---: |
| **A** | 10 | 11 | 9 | **11** |
| **B** | 9 | 13 | 11 | **12** |
| **C** | 10 | 10 | 10 | **10** |
| **D** | 16 | 11 | 10 | **12** |
| **E** | 9 | 9 | 14 | **9** |
| **Total** | **54** | **54** | **54** | **54** |

* **Critério do Target:** Representa o *Steady State* (Estado Estacionário). A Letra C atua como restrição rígida em 10. As variáveis de ataque (B e D) operam em equilíbrio na fronteira máxima (12), forçando a Letra E a atuar como folga sistêmica na base inferior (9).

---

## 🚀 6. O Impacto da Transição: Cohort Expansion (60Q)

![Comparativo Transição 60Q](https://raw.githubusercontent.com/caiiobuenoo/FATEC/main/output/gabarito_fatec_60q.PNG)

A partir do semestre 2025.2, a carga do exame aumentou para 60 questões. A Análise de Divergência comprova que a banca rejeitou o modelo igualitário (12 precisas por letra). As 6 novas alocações foram injetadas estrategicamente nos polos. O miolo conteve sua expansão, enquanto as Letras **A (+2.5)** e **E (+2.8)** explodiram em dominância.

### 6.2. Cenários de Simulação Probabilística (Exame de 60Q)
| Alternativa | Cenário 1 (Polarização) | Cenário 2 (Instabilidade Central) | Cenário 3 (Hiper-Volume A) | Modelo "Certeiro" (Target) |
| :---: | :---: | :---: | :---: | :---: |
| **A** | 14 | 13 | 15 | **13** |
| **B** | 11 | 12 | 11 | **11** |
| **C** | 11 | 10 | 11 | **11** |
| **D** | 10 | 11 | 11 | **11** |
| **E** | 14 | 14 | 12 | **14** |
| **Total** | **60** | **60** | **60** | **60** |

* **Critério do Target:** Determinado pela nova política de *Achatamento de Miolo por Proteção Algorítmica*. Congelar as alternativas $[B, C, D]$ em 11 ocorrências obriga os polos $[A, E]$ a operar em regime de saturação simétrica desbalanceada (13 e 14).

---

## 🔄 7. A Linha do Tempo da "Assimetria Controlada"

![Evolução Cronológica FATEC](https://raw.githubusercontent.com/caiiobuenoo/FATEC/main/output/gabarito_fatec_evolucao_matrizes.PNG)

* **Matriz 48Q:** Simetria rudimentar, linear e vulnerável.
* **Matriz 54Q:** Introdução do caos controlado. Uso de variâncias extremas (D) e âncoras (C) para ofuscar o padrão subjacente.
* **Nova Matriz 60Q:** Modelo algorítmico definitivo. Congelamento exato do "miolo" e alocação maciça de peso nas margens (A e E).

---

## 🔮 8. Forecasting e Otimização de Risco
Transformando *Data Analysis* em *Actionable Insights*:

1. **A Nova Fronteira de Segurança (Polos A e E):** No cenário atual (60Q), as alternativas A (13) e E (14) concentram 45% do gabarito. Compõem o portfólio de chute estatístico com o maior Índice de Sharpe (Retorno sobre Risco).
2. **Restrição de Miolo (Limites B, C, D):** O algoritmo fixa um teto rígido em 11 ocorrências para o centro. Marcações excessivas (ex: 13+ opções na letra C) são um Sinal de Alerta de captura por distratores linguísticos.

---

## 📂 9. Estrutura do Projeto e Reprodutibilidade

### ☁️ Validação Estatística (Ambiente Cloud)
Você pode auditar a matemática e os desvios padrões deste projeto diretamente no seu navegador, sem instalar nada:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/caiiobuenoo/FATEC/blob/main/notebooks/01_eda_fatec.ipynb)

### 💻 Setup de Ambiente (Local)
A taxonomia do repositório segue os padrões da comunidade de Ciência de Dados.

```bash
# ==========================================
# 1. VISÃO GERAL DO REPOSITÓRIO
# ==========================================
# FATEC/
# ├── data/
# │   ├── processed/          # DataFrames consolidados em CSV (Tidy Data)
# │   └── DATA_DICTIONARY.md  # Governança e metadados
# ├── notebooks/              # Jupyter Notebooks de EDA e Validação
# ├── output/                 # Renderizações de painéis em alta resolução
# ├── src/
# │   └── visualization/      # Scripts focados na geração via Seaborn/Matplotlib
# ├── LICENSE                 # Licença MIT
# └── README.md               # Documentação principal

# ==========================================
# 2. EXECUÇÃO
# ==========================================
git clone [https://github.com/caiiobuenoo/FATEC.git](https://github.com/caiiobuenoo/FATEC.git)
cd FATEC
python src/visualization/dashboard_fatec_matriz_54q.py
