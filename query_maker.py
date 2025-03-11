import pandas as pd

data = pd.read_csv('Dados_Estatisticos_Filtered.csv')

mercados_data = sorted(data['MERCADO'].str.strip().unique())
mercados_dict = {mercado: i+1 for i, mercado in enumerate(mercados_data)}

# Generate mercados Insert SQL Queries
def generate_mercados_sql(mercados):
    filename = 'mercados.sql'
    columns = ['id', 'mercado']
    table = 'mercados'
    with open(filename, 'w') as f:
        for i, mercado in enumerate(mercados):
            f.write(f"INSERT INTO {table} ('{"', '".join(columns)}') VALUES ({i+1}, '{mercado}');\n")

# Generate voos Insert SQL Queries
def generate_voos_sql(df, mercado_mapping):
    filename = 'voos.sql'
    columns = ['ano', 'mes', 'mercado', 'rpk']
    table = 'voos'
    
    with open(filename, 'w') as f:
        for _, row in df.iterrows():
            values = [
                str(row['ANO']),
                str(row['MES']),
                str(mercado_mapping[row['MERCADO']]),
                'NULL' if pd.isna(row['RPK']) else str(row['RPK'])
            ]
            f.write(
                f"INSERT INTO {table} ('{"', '".join(columns)}') VALUES ({', '.join(values)});\n"
            )

generate_mercados_sql(mercados_data)
generate_voos_sql(data, mercados_dict)