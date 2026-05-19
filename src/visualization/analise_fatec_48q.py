import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.lines import Line2D

sns.set_theme(style="whitegrid", font_scale=1.1)

# Dados Simulated/Exemplo com base na sua imagem antiga de 48Q
edicoes = ['2007.2', '2008.1', '2009.1']
alternativas = ['A', 'B', 'C', 'D', 'E']
cores = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Matriz de dados fake baseada no comportamento do seu gráfico antigo de 48Q
dados_edicoes = {
    'A': [10, 10, 10],
    'B': [10, 10, 11],
    'C': [10, 9, 9],
    'D': [9, 10, 9],
    'E': [9, 9, 9]
}
desvio_acumulado = np.array([1.2, 2.2, -0.8, -0.8, -1.8]) # Valores exatos da sua imagem
media_periodo = np.array([10.0, 10.3, 9.3, 9.3, 9.0])

fig = plt.figure(figsize=(22, 8), facecolor='#f4f5f7')

plt.suptitle('FATEC Analytics: Comportamento da Matriz de 48 Questões (Histórico)', 
             fontsize=22, fontweight='bold', color='#1a1a1a', y=1.02)
fig.text(0.5, 0.95, 'Análise de simetria, desvios acumulados e comportamento geométrico médio.', 
         ha='center', fontsize=16, color='#4a4a4a')

# PAINEL 1: Frequência Agrupada por Edição
ax1 = fig.add_subplot(131)
ax1.set_facecolor('white')
x = np.arange(len(edicoes))
width = 0.15

for i, alt in enumerate(alternativas):
    ax1.bar(x + i*width, dados_edicoes[alt], width, label=f'Letra {alt}', color=cores[i], edgecolor='black', linewidth=1)
ax1.axhline(9.6, color='black', linestyle='--', linewidth=1.5, label='Média Teórica (9.6)')
ax1.set_xticks(x + width * 2)
ax1.set_xticklabels(edicoes)
ax1.set_ylim(0, 14)
ax1.set_title('O Muro Simétrico (Frequência Absoluta)', fontsize=15, fontweight='bold', pad=15)
ax1.set_ylabel('Quantidade de Respostas', fontsize=13, fontweight='bold', labelpad=10)

# PAINEL 2: Desvio Acumulado (Convertido para Vertical para alinhar com o padrão!)
ax2 = fig.add_subplot(132)
ax2.set_facecolor('white')
sns.barplot(x=alternativas, y=desvio_acumulado, palette=cores, edgecolor='black', linewidth=1.2, ax=ax2)
ax2.axhline(0, color='black', linewidth=2)
for i, diff in enumerate(desvio_acumulado):
    sinal = "+" if diff > 0 else ""
    deslocamento = 0.1 if diff > 0 else -0.15
    ax2.text(i, diff + deslocamento, f"{sinal}{diff:.1f}", color=cores[i], fontweight='bold', ha='center', fontsize=13)
ax2.set_ylim(min(desvio_acumulado) - 0.8, max(desvio_acumulado) + 0.8)
ax2.set_title('O Viés Oculto da Banca: Desvio Acumulado', fontsize=15, fontweight='bold', pad=15)
ax2.set_ylabel('Pontos Acima/Abaixo da Média', fontsize=13, fontweight='bold', labelpad=10)

# PAINEL 3: Geometria do Exame (Substituindo o Radar por Barras Consistentes)
ax3 = fig.add_subplot(133)
ax3.set_facecolor('white')
sns.barplot(x=alternativas, y=media_periodo, palette=cores, edgecolor='black', linewidth=1.2, ax=ax3, alpha=0.9)
for i, freq in enumerate(media_periodo):
    ax3.text(i, freq + 0.3, f"{freq:.1f}", color='black', fontweight='bold', ha='center', fontsize=13)
ax3.set_ylim(0, 14)
ax3.set_title('A Geometria do Exame: Média do Período', fontsize=15, fontweight='bold', pad=15)
ax3.set_ylabel('Frequência Média', fontsize=13, fontweight='bold', labelpad=10)

# Legenda Global
legend_elements = [Line2D([0], [0], color=cores[i], lw=8, label=f'Letra {alternativas[i]}') for i in range(len(alternativas))]
fig.legend(handles=legend_elements, loc='lower center', bbox_to_anchor=(0.5, 0.02), ncol=5, frameon=True, fontsize=13, shadow=True)

sns.despine(ax=ax1)
sns.despine(ax=ax2, bottom=True, left=True)
sns.despine(ax=ax3)
plt.subplots_adjust(top=0.85, bottom=0.15, wspace=0.25)

plt.savefig('gabarito_fatec_48q_master.png', dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.show()
