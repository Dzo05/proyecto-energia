from fastapi import FastAPI
from sqlalchemy import create_engine
import pandas as pd

app = FastAPI()
engine = create_engine('postgresql://admin:password@localhost:5432/energia_db')

@app.get("/metricas")
def listar_metricas():
    df = pd.read_sql("SELECT * FROM Metrica", engine)
    return df.to_dict(orient="records")

@app.post("/consultar")
def consultar_datos(metric_id: str, start_date: str, end_date: str):
    query = f"""
    SELECT * FROM HechosDemanda
    JOIN Metrica ON HechosDemanda.id_metrica = Metrica.id_metrica
    WHERE Metrica.metric_id = '{metric_id}'
    """
    df = pd.read_sql(query, engine)
    return df.to_dict(orient="records")