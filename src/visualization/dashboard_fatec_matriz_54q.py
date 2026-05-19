"""
Módulo de Visualização: FATEC Analytics (Cohort 54Q)
Gera o painel consolidado da matriz histórica de 54 questões (2010.1 a 2025.1).
"""

import logging
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, List

# Configuração do sistema de logs (Padrão Corporativo em vez de 'print')
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Constantes Globais de Identidade Visual
PALETA_CORES: Dict[str, str] = {
    'A': '#2b7bba',
    'B': '#ef8a24',
    'C': '#34a047',
    'D': '#c93637',
    'E': '#987db7'
}

def configurar_ambiente_visual() -> None:
    """Aplica as configurações globais de estilo do Seaborn."""
    sns.set_theme(style="whitegrid")
    logging.info("Ambiente visual Seaborn configurado.")

def gerar_dashboard_54q(caminho_saida: str) -> None:
    """
    Constrói e exporta o dashboard de barras e fatias empilhadas para a cohort de 54 questões.
    
    Args:
        caminho_saida (str): Caminho ou nome do arquivo onde a imagem será salva.
    """
    logging.info("Iniciando a geração do dashboard 54Q...")
    
    # Dados Simulados/Estruturados (Idealmente viriam de um DataFrame Pandas)
    alternativas: List[str] = ['A', 'B', 'C', 'D', 'E']
    contagem_ideal: List[int] = [11, 12, 10, 12, 9]
    
    semestres: List[str] = [
        '2010.1', '2010.2', '2011.2', '2012.1', '2012.2', '2013.1', '2013.2', 
        '2014.1', '2014.2', '2015.1', '2015.2', '2016.1', '2016.2', '2017.1', 
        '2017.2', '2018.1', '2024.1', '2024.2', '2025.1_A', '2025.1_B'
    ]
    
    dados_empilhados: Dict[str, List[int]] = {
        'A': [9, 7, 11, 10, 11, 11, 9, 7, 9, 11, 11, 9, 10, 7, 9, 8, 11, 8, 11, 9],
        'B': [12, 11, 11, 12, 10, 12, 12, 9, 11, 9, 12, 8, 11, 15, 12, 15, 5, 5, 11, 11],
        'C': [10, 11, 14, 12, 10, 9, 10, 14, 10, 13, 10, 17, 13, 10, 10, 9, 9, 10, 11, 10],
        'D': [9, 11, 10, 9, 13, 12, 15, 17, 10, 12, 12, 12, 11, 8, 11, 12, 17, 17, 11, 12],
        'E': [14, 14, 8, 11, 10, 10, 8, 7, 14, 9, 9, 8, 9, 14, 12, 10, 12, 14, 10, 12]
    }

    # Configuração da Figura
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7), facecolor='#f8f9fa', 
                                   gridspec_kw={'width_ratios': [1, 1.8]})
    ax1.set_facecolor('#f8f9fa')
    ax2.set_facecolor('#f8f9fa')

    fig.suptitle('FATEC Analytics: O Gabarito Estatístico Definitivo (Matriz Histórica de 54Q)', 
                 fontsize=14, weight='bold', color='#111111')
    fig.text(0.5, 0.93, 'Distribuição ideal consolidada versus evolução histórica dos exames.', 
             fontsize=11, ha='center', color='#444444', style='italic')

    # Painel 1: Gabarito Ideal
    ax1.set_title('O Gabarito Estatístico Ideal (Consolidado 54 Q.)', fontsize=12, weight='bold', pad=15)
    ax1.set_ylabel('Quantidade de Respostas', fontsize=11, weight='bold')
    ax1.set_ylim(0, 14.5)
    
    barras_ideais = ax1.bar(alternativas, contagem_ideal, 
                            color=[PALETA_CORES[alt] for alt in alternativas], 
                            edgecolor='#222222', linewidth=0.8, width=0.7)

    for bar in barras_ideais:
        altura = bar.get_height()
        ax1.annotate(f'{int(altura)}', xy=(bar.get_x() + bar.get_width() / 2, altura),
                     xytext=(0, 4), textcoords="offset points", ha='center', va='bottom', 
                     fontsize=10, weight='bold', color='#111111')

    # Painel 2: Raio-X Empilhado
    ax2.set_title('Raio-X: Gabarito Exato de Cada Vestibular (54 Q.)', fontsize=12, weight='bold', pad=15)
    ax2.set_ylabel('Total de Questões (0 a 54)', fontsize=11, weight='bold')
    ax2.set_ylim(0, 56)
    
    indices_x = np.arange(len(semestres))
    ax2.set_xticks(indices_x)
    ax2.set_xticklabels(semestres, rotation=45, ha='right', fontsize=9, weight='bold')

    vetor_base = np.zeros(len(semestres))

    for alt in alternativas:
        valores_y = np.array(dados_empilhados[alt])
        barras_empilhadas = ax2.bar(indices_x, valores_y, bottom=vetor_base, 
                                    color=PALETA_CORES[alt], edgecolor='#ffffff', 
                                    linewidth=0.5, width=0.65)
        
        for idx, bar in enumerate(barras_empilhadas):
            altura = bar.get_height()
            if altura > 0:
                posicao_y = vetor_base[idx] + altura / 2
                ax2.annotate(f'{int(altura)}', xy=(bar.get_x() + bar.get_width() / 2, posicao_y),
                             ha='center', va='center', fontsize=8, weight='bold', color='#ffffff')
        
        vetor_base += valores_y

    # Legenda Unificada
    elementos_legenda = [plt.Line2D([0], [0], color=PALETA_CORES[alt], lw=6, label=f'Letra {alt}') 
                         for alt in alternativas]
    fig.legend(handles=elementos_legenda, loc='lower center', bbox_to_anchor=(0.5, -0.04), ncol=5, 
               frameon=True, facecolor='#ffffff', edgecolor='#e0e0e0', fontsize=10)

    plt.tight_layout(rect=[0, 0.04, 1, 0.91])
    
    # Exportação
    plt.savefig(caminho_saida, dpi=300, bbox_inches='tight')
    logging.info(f"Dashboard gerado com sucesso em: {caminho_saida}")

if __name__ == "__main__":
    # Ponto de entrada oficial do script
    configurar_ambiente_visual()
    gerar_dashboard_54q(caminho_saida="output/gabarito_fatec_definitivo.png")
