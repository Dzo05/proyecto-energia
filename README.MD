# 🏗️ Base de Datos para Modelo Predictivo de Demanda Energética  
**Automatización con PostgreSQL, FastAPI y Docker**  

---

## 📋 Descripción  
Este proyecto gestiona datos energéticos de XM (Colombia) para entrenar un modelo predictivo de demanda. Incluye:  
- **Base de datos PostgreSQL** en Docker para almacenar datos horarios, diarios y mensuales.  
- **Esquema estrella** optimizado para consultas analíticas.  
- **ETL automatizado** desde un archivo Excel (`datos_API.xlsx`).  
- **API REST** con FastAPI para acceder a los datos.  
- **Colección de Postman** preconfigurada para pruebas.  

---

## ⚙️ Requisitos Previos  
1. [Docker y Docker Compose](https://docs.docker.com/get-docker/) instalados.  
2. [Python 3.10+](https://www.python.org/downloads/) para ejecutar el ETL y la API.  
3. [Postman](https://www.postman.com/) para probar los endpoints de la API.  

---

## 🚀 Instalación Paso a Paso  

## 1. Clonar el Repositorio  
git clone https://github.com/tu-usuario/proyecto-energia.git  
cd proyecto-energia  

## 2. Iniciar PostgreSQL con Docker
docker-compose up -d  
Esto crea un contenedor de PostgreSQL en el puerto 5432 con las credenciales:

Usuario: admin

Contraseña: Password

Base de datos: energia_db

## 3. Crear las Tablas en la Base de Datos
bash
docker exec -i proyecto-energia-db-1 psql -U admin -d energia_db -a -f schema.sql  

## 4. Importar Datos desde Excel (ETL)
pip install pandas sqlalchemy openpyxl  # Instalar dependencias  
python etl.py  

## 5. Iniciar la API con FastAPI
pip install fastapi uvicorn  
uvicorn api:app --reload  La API estará disponible en: http://localhost:8000.

## 🔍 Cómo Usar el Sistema
### ▶️ Consultar Datos con Postman
Importar la colección:

Abre Postman > File > Import > Selecciona MX.postman_collection.json.

Configurar variables de entorno:

Crea un entorno llamado XM con la variable URL = http://localhost:8000.

Ejemplo de solicitud (POST a /hourly):
{  
  "MetricId": "DemaReal",  
  "StartDate": "2025-02-01",  
  "EndDate": "2025-02-28"  
}  
## ▶️ Consultar Datos con cURL
curl -X POST http://localhost:8000/consultar -H "Content-Type: application/json" -d '{  
  "metric_id": "DemaReal",  
  "start_date": "2025-02-01",  
  "end_date": "2025-02-28"  
}'  
## 📂 Estructura del Proyecto
proyecto-energia/  
├── docker-compose.yml       # Configuración de Docker para PostgreSQL  
├── schema.sql              # Script SQL del modelo de datos (tablas y relaciones)  
├── datos_API.xlsx          # Dataset fuente de XM (métricas energéticas)  
├── MX.postman_collection.json  # Colección de Postman con ejemplos de consultas  
├── etl.py                  # Script ETL para importar datos desde Excel  
├── api.py                  # Endpoints de la API (FastAPI)  
└── README.md               # Este archivo  

## 🚨 Solución de Problemas Comunes
❌ Error: psql no se reconoce como comando
Causa: El sistema no encuentra el ejecutable psql.
Solución: Ejecuta psql desde el contenedor de Docker:
docker exec -it proyecto-energia-db-1 psql -U admin -d energia_db  
❌ La API no responde
Pasos para resolverlo:

1. Verifica que la API esté en ejecución:
    uvicorn api:app --reload  
2. Asegúrate de que el puerto 8000 no esté bloqueado por otro programa.

❌ Datos no se cargan desde Excel
Pasos para resolverlo:

1. Coloca el archivo datos_API.xlsx en la raíz del proyecto.
2. Ejecuta el ETL nuevamente:
   python etl.py  