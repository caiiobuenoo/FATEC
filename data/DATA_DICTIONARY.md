# 📖 Dicionário de Dados (Data Dictionary)

Este documento descreve o esquema de metadados para os *DataFrames* consolidados na pasta `data/processed/`. Os conjuntos de dados representam o volume de respostas corretas extraídas dos gabaritos oficiais da FATEC.

## Arquivo: `fatec_gabaritos_historico.csv`
*(Cohort de 54 Questões: Edições 2010.1 a 2025.1)*

| Coluna | Tipo de Dado | Descrição | Restrição |
| :--- | :--- | :--- | :--- |
| `ano_semestre` | `String` / `Categorical` | Chave primária de identificação da prova. Formato YYYY.S (ex: 2024.1). Casos de desmembramento recebem sufixo `_A` ou `_B`. | Não Nulo, Único |
| `total_questoes` | `Integer` | Volume fixo de questões daquela Matriz Curricular (Cohort). | Constante = 54 |
| `freq_A` | `Integer` | Frequência absoluta de respostas corretas na Alternativa A. | $x \ge 0$ |
| `freq_B` | `Integer` | Frequência absoluta de respostas corretas na Alternativa B. | $x \ge 0$ |
| `freq_C` | `Integer` | Frequência absoluta de respostas corretas na Alternativa C. | $x \ge 0$ |
| `freq_D` | `Integer` | Frequência absoluta de respostas corretas na Alternativa D. | $x \ge 0$ |
| `freq_E` | `Integer` | Frequência absoluta de respostas corretas na Alternativa E. | $x \ge 0$ |

### 🛠️ Regra de Integridade (Integrity Check)
Para que o arquivo seja considerado íntegro (Tidy Data), a equação abaixo deve ser verdadeira para todas as linhas da matriz:
`freq_A + freq_B + freq_C + freq_D + freq_E = total_questoes`
