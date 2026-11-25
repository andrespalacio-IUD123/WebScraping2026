import os
import logging

# Crear carpeta logs si no existe
os.makedirs("logs", exist_ok=True)

# Configuración de observabilidad
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("logs/pipeline.log", encoding="utf-8"),
        logging.StreamHandler()  # También muestra logs en consola/Docker
    ]
)
