import pandas as pd
from sqlalchemy import create_engine

# Conexión a PostgreSQL
engine = create_engine('postgresql://admin:password@localhost:5432/energia_db')

# Leer el Excel
df = pd.read_excel('datos_API.xlsx', sheet_name='SINERGOX')

# Poblar tabla Metrica
metricas = df[['MetricId', 'MetricName', 'Entity', 'MetricUnits', 'MetricDescription']]
metricas = metricas.rename(columns={
    'MetricId': 'metric_id',
    'MetricName': 'nombre',
    'Entity': 'entidad_relacionada',
    'MetricUnits': 'unidad',
    'MetricDescription': 'descripcion'
})
metricas.to_sql('Metrica', engine, if_exists='append', index=False)

# Poblar tabla Sistema (ejemplo)
sistemas = df[df['Entity'] == 'Sistema'][['Entity']].drop_duplicates()
sistemas['nombre'] = sistemas['Entity']
sistemas.to_sql('Sistema', engine, if_exists='append', index=False, columns=['nombre'])