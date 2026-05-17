import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.lines import Line2D

# Configuração de Estilo Global
sns.set_theme(style="whitegrid", font_scale=1.1)

# Dados
alternativas = ['A', 'B', 'C', 'D', 'E']
cores = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
freq_60q = np.array([13, 11, 11, 11, 14])
freq_54q_mean = np.array([10.5, 10.6, 10.0, 11.7, 11.2])
diferenca = freq_60q - freq_54q_mean

# Estrutura do Canvas Corporativo
fig = plt.figure(figsize=(22, 8), facecolor='#f4f5f7')

plt.suptitle('FATEC Analytics: Comparativo e Impacto da Transição de Matriz (54Q ➔ 60Q)', 
             fontsize=22, fontweight='bold', color='#1a1a1a', y=1.02)
fig.text(0.5, 0.95, 'Análise da distribuição absoluta e alocação de questões extras.', 
         ha='center', fontsize=16, color='#4a4a4a')

# PAINEL 1
ax1 = fig.add_subplot(131)
ax1.set_facecolor('white')
sns.barplot(x=alternativas, y=freq_60q, palette=cores, edgecolor='black', linewidth=1.2, ax=ax1)
for i, freq in enumerate(freq_60q):
    ax1.text(i, freq + 0.3, str(freq), color='black', fontweight='bold', ha='center', fontsize=13)
ax1.set_ylim(0, max(freq_60q) + 2)
ax1.set_title('Distribuição Atual: Matriz de 60 Questões', fontsize=15, fontweight='bold', pad=15)
ax1.set_ylabel('Quantidade de Questões', fontsize=13, fontweight='bold', labelpad=10)

# PAINEL 2
ax2 = fig.add_subplot(132)
ax2.set_facecolor('white')
sns.barplot(x=alternativas, y=freq_54q_mean, palette=cores, edgecolor='black', linewidth=1.2, ax=ax2, alpha=0.85)
for i, freq in enumerate(freq_54q_mean):
    ax2.text(i, freq + 0.3, f"{freq:.1f}", color='black', fontweight='bold', ha='center', fontsize=13)
ax2.set_ylim(0, max(freq_54q_mean) + 2)
ax2.set_title('Média Histórica: Matriz de 54 Questões', fontsize=15, fontweight='bold', pad=15)
ax2.set_ylabel('Média Histórica (nº de questões)', fontsize=13, fontweight='bold', labelpad=10)

# PAINEL 3
ax3 = fig.add_subplot(133)
ax3.set_facecolor('white')
sns.barplot(x=alternativas, y=diferenca, palette=cores, edgecolor='black', linewidth=1.2, ax=ax3)
ax3.axhline(0, color='black', linewidth=2)
for i, diff in enumerate(diferenca):
    sinal = "+" if diff > 0 else ""
    deslocamento = 0.15 if diff > 0 else -0.3
    ax3.text(i, diff + deslocamento, f"{sinal}{diff:.1f}", color=cores[i], fontweight='bold', ha='center', fontsize=15)
ax3.set_ylim(min(diferenca) - 1, max(diferenca) + 1)
ax3.set_title('Análise da Divergência: Alocação das 6 Questões Extras', fontsize=15, fontweight='bold', pad=15)
ax3.set_ylabel('Diferença Absoluta', fontsize=13, fontweight='bold', labelpad=10)
ax3.tick_params(axis='x', length=0)

# Legenda Global e Acabamento
legend_elements = [Line2D([0], [0], color=cores[i], lw=8, label=f'Letra {alternativas[i]}') for i in range(len(alternativas))]
fig.legend(handles=legend_elements, loc='lower center', bbox_to_anchor=(0.5, 0.02), ncol=5, frameon=True, fontsize=13, shadow=True)

sns.despine(ax=ax1)
sns.despine(ax=ax2)
sns.despine(ax=ax3, bottom=True, left=True)
plt.subplots_adjust(top=0.85, bottom=0.15, wspace=0.25)

plt.savefig('gabarito_transicao_60q_premium.png', dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.show()