import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# 1. Configurando o tema do Seaborn para um visual limpo e profissional
sns.set_theme(style="whitegrid")

# 2. Estruturação dos dados com base na linha do tempo corrigida (2010.1 a 2025.1)
cohorts = [
    'Matriz Histórica\n48Q (2007.2 - 2009.2)', 
    'Matriz Consolidada\n54Q (2010.1 - 2025.1)', 
    'Nova Matriz\n60Q (2025.2+)'
]
alternatives = ['A', 'B', 'C', 'D', 'E']

# Valores exatos/médios mapeados a partir dos gabaritos do projeto
data = {
    'A': [10.0, 11.0, 13.0],
    'B': [10.3, 12.0, 11.0],
    'C': [9.3, 10.0, 11.0],
    'D': [9.3, 12.0, 11.0],
    'E': [9.0, 9.0, 14.0]
}

# Paleta de cores oficial e idêntica à identidade visual do FATEC Analytics
colors = {
    'A': '#2b7bba', # Azul
    'B': '#ef8a24', # Laranja
    'C': '#34a047', # Verde
    'D': '#c93637', # Vermelho
    'E': '#987db7'  # Roxo
}

# 3. Criando a estrutura do gráfico (usando subplots para maior controle de layout)
fig, ax = plt.subplots(figsize=(11, 6), facecolor='#f8f9fa')
ax.set_facecolor('#f8f9fa')

x = np.arange(len(cohorts))
width = 0.15  # Largura individual de cada barra

# 4. Plotagem das barras agrupadas por alternativa
for i, alt in enumerate(alternatives):
    y_vals = data[alt]
    bars = ax.bar(
        x + (i - 2) * width, y_vals, width, 
        label=f'Letra {alt}', 
        color=colors[alt], 
        edgecolor='#333333', 
        linewidth=0.6
    )
    
    # Adicionando os rótulos numéricos no topo de cada barra de forma dinâmica
    for bar in bars:
        height = bar.get_height()
        # Formata como inteiro se não houver quebra decimal (ex: 11), senão mantém float (ex: 10.3)
        label_text = f'{height:.1f}' if height % 1 != 0 else f'{int(height)}'
        
        ax.annotate(
            label_text,
            xy=(bar.get_x() + bar.get_width() / 2, height),
            xytext=(0, 4),  # Descolamento de 4 pontos para cima da barra
            textcoords="offset points",
            ha='center', va='bottom', 
            fontsize=9.5, weight='bold', color='#222222'
        )

# 5. Customização e refinamento dos eixos e títulos
ax.set_title(
    'FATEC Analytics: Evolução Histórica da Estrutura de Gabaritos\n'
    'Alocação de alternativas e a consolidação da "Assimetria Controlada" ao longo das eras', 
    fontsize=13, pad=25, weight='bold', color='#111111', ha='center'
)

ax.set_xticks(x)
ax.set_xticklabels(cohorts, fontsize=11, weight='bold', color='#333333')
ax.set_ylabel('Quantidade de Questões (Ideal / Média)', fontsize=11, labelpad=10, weight='bold')
ax.set_ylim(0, 16)  # Margem superior para o texto não colidir com o topo do gráfico

# 6. Posicionamento perfeito da legenda na base horizontal (evita sobreposição)
ax.legend(
    loc='lower center', bbox_to_anchor=(0.5, -0.2), ncol=5, frameon=True, 
    facecolor='#ffffff', edgecolor='#e0e0e0', fontsize=10
)

# Ajuste automático de margens para garantir que nenhum rótulo seja cortado na exportação
plt.tight_layout()

# 7. Salvando a imagem final com alta resolução (300 DPI) para o repositório
output_filename = 'evolucao_cronologica_matrizes_fatec.png'
plt.savefig(output_filename, dpi=300, bbox_inches='tight')

print(f"Sucesso! Gráfico salvo como: {output_filename}")
