import pandas as pd
import numpy as np

data = pd.read_csv('Dados_Estatisticos.csv', delimiter=';')

# Filter rows
data = data[data['EMPRESA_SIGLA'] == 'GLO']
data = data[data['GRUPO_DE_VOO'] == 'REGULAR']
data = data[data['NATUREZA'] == 'DOMÉSTICA']

# Add MERCADO column
# Mercado is origin + destination airport, in alphabetical order
data['MERCADO'] = np.where(
    data['AEROPORTO_DE_ORIGEM_SIGLA'] > data['AEROPORTO_DE_DESTINO_SIGLA'],
    data['AEROPORTO_DE_DESTINO_SIGLA'] + data['AEROPORTO_DE_ORIGEM_SIGLA'],
    data['AEROPORTO_DE_ORIGEM_SIGLA'] + data['AEROPORTO_DE_DESTINO_SIGLA']
)

# Filter columns
data = data[['EMPRESA_SIGLA', 'ANO', 'MES','MERCADO', 'RPK']]

# Replace RPK NaN values with NULL
data['RPK'] = data['RPK'].replace(np.nan, 'NULL')

data.to_csv('Dados_Estatisticos_Filtered.csv')