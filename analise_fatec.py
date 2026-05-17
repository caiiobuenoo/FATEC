import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# 1. Configurando o estilo visual limpo e corporativo do Seaborn
sns.set_theme(style="whitegrid")

# --- Banco de Dados Exato do Dashboard de 54 Questões ---
alternatives = ['A', 'B', 'C', 'D', 'E']
ideal_counts = [11, 12, 10, 12, 9]

semesters = [
    '2010.1', '2010.2', '2011.2', '2012.1', '2012.2', '2013.1', '2013.2', 
    '2014.1', '2014.2', '2015.1', '2015.2', '2016.1', '2016.2', '2017.1', 
    '2017.2', '2018.1', '2024.1', '2024.2', '2025.1_A', '2025.1_B'
]

# Distribuição empilhada real por alternativa (Mapeada de baixo para cima: A, B, C, D, E)
stacked_data = {
    'A': [9, 7, 11, 10, 11, 11, 9, 7, 9, 11, 11, 9, 10, 7, 9, 8, 11, 8, 11, 9],
    'B': [12, 11, 11, 12, 10, 12, 12, 9, 11, 9, 12, 8, 11, 15, 12, 15, 5, 5, 11, 11],
    'C': [10, 11, 14, 12, 10, 9, 10, 14, 10, 13, 10, 17, 13, 10, 10, 9, 9, 10, 11, 10],
    'D': [9, 11, 10, 9, 13, 12, 15, 17, 10, 12, 12, 12, 11, 8, 11, 12, 17, 17, 11, 12],
    'E': [14, 14, 8, 11, 10, 10, 8, 7, 14, 9, 9, 8, 9, 14, 12, 10, 12, 14, 10, 12]
}

# Paleta oficial e padronizada de cores hexadecimais do FATEC Analytics
colors = {
    'A': '#2b7bba', # Azul
    'B': '#ef8a24', # Laranja
    'C': '#34a047', # Verde
    'D': '#c93637', # Vermelho
    'E': '#987db7'  # Roxo
}

# 2. Estruturando a Proporção de Telas (Proporção assimétrica ideal para o Raio-X horizontal)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7), facecolor='#f8f9fa', 
                               gridspec_kw={'width_ratios': [1, 1.8]})
ax1.set_facecolor('#f8f9fa')
ax2.set_facecolor('#f8f9fa')

# 3. Cabeçalho Centralizado do Dashboard (Título + Subtítulo)
fig.suptitle('FATEC Analytics: O Gabarito Estatístico Definitivo (Matriz Histórica de 54Q)', 
             fontsize=14, weight='bold', color='#111111', ha='center')
fig.text(0.5, 0.93, 'Distribuição ideal consolidada versus evolução histórica dos exames.', 
         fontsize=11, ha='center', color='#444444', style='italic')

# ==========================================
# PAINEL 1: O Gabarito Estatístico Ideal
# ==========================================
ax1.set_title('O Gabarito Estatístico Ideal (Consolidado 54 Q.)', fontsize=12, weight='bold', pad=15)
ax1.set_ylabel('Quantidade de Respostas', fontsize=11, weight='bold', labelpad=8)
ax1.set_ylim(0, 14.5)

bars1 = ax1.bar(alternatives, ideal_counts, color=[colors[alt] for alt in alternatives], 
                edgecolor='#222222', linewidth=0.8, width=0.7)

# Adicionando rótulos de dados em cima das barras pretas do painel ideal
for bar in bars1:
    height = bar.get_height()
    ax1.annotate(f'{int(height)}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 4), textcoords="offset points",
                ha='center', va='bottom', fontsize=10, weight='bold', color='#111111')

# ==========================================
# PAINEL 2: Raio-X - Evolução Proporcional Empilhada
# ==========================================
ax2.set_title('Raio-X: Gabarito Exato de Cada Vestibular (54 Q.)', fontsize=12, weight='bold', pad=15)
ax2.set_ylabel('Total de Questões (0 a 54)', fontsize=11, weight='bold', labelpad=8)
ax2.set_ylim(0, 56)

x_indices = np.arange(len(semesters))
ax2.set_xticks(x_indices)
ax2.set_xticklabels(semesters, rotation=45, ha='right', fontsize=9, weight='bold')

# Construindo as barras empilhadas e acumulando a base de apoio vertical
bottom_vector = np.zeros(len(semesters))

for alt in alternatives:
    y_vals = np.array(stacked_data[alt])
    bars2 = ax2.bar(x_indices, y_vals, bottom=bottom_vector, color=colors[alt], 
                    edgecolor='#ffffff', linewidth=0.5, width=0.65)
    
    # Inserindo os rótulos brancos de dados DENTRO de cada bloco empilhado
    for idx, bar in enumerate(bars2):
        height = bar.get_height()
        if height > 0:
            # Calcula o ponto central do bloco atual para ancorar o texto
            y_position = bottom_vector[idx] + height / 2
            ax2.annotate(f'{int(height)}',
                        xy=(bar.get_x() + bar.get_width() / 2, y_position),
                        xytext=(0, 0), textcoords="offset points",
                        ha='center', va='center', fontsize=8, weight='bold', color='#ffffff')
            
    bottom_vector += y_vals

# ==========================================
# 4. NOVA LEGENDA HORIZONTAL UNIFICADA NA BASE
# ==========================================
legend_elements = [plt.Line2D([0], [0], color=colors[alt], lw=6, label=f'Letra {alt}') for alt in alternatives]

fig.legend(handles=legend_elements, loc='lower center', bbox_to_anchor=(0.5, -0.04), ncol=5, 
           frameon=True, facecolor='#ffffff', edgecolor='#e0e0e0', fontsize=10)

# Ajuste fino das margens para consolidar o design sem cortes
plt.tight_layout(rect=[0, 0.04, 1, 0.91])

# 5. Exportando o painel final com alta densidade de pixels (300 DPI)
output_filename = 'gabarito_fatec_definitivo_recriado.png'
plt.savefig(output_filename, dpi=300, bbox_inches='tight')

print(f"Sucesso! Código executado e salvo como: {output_filename}")