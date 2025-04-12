# Usa una imagen base oficial de Python
FROM python:3.11-slim

# Setea el directorio de trabajo
WORKDIR /app

# Copia los archivos de requisitos e instala dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código
COPY . .

# Expone el puerto donde corre FastAPI
EXPOSE 8000

# Comando para iniciar Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]