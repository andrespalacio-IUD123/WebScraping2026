import os
import logging
import requests
from bs4 import BeautifulSoup

# 1. Configuración inicial del logger (al inicio del archivo)
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("logs/pipeline.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

def ejecutar_scraping_multicanal(paginas=1):
    exitos_200 = 0
    errores_http = 0
    productos = []

    for pagina in range(1, paginas + 1):
        url = f"https://ejemplo.com/productos?page={pagina}"  # Tu URL real

        try:
            response = requests.get(url, timeout=15)

            # 2. Auditoría del código de estado HTTP
            if response.status_code == 200:
                exitos_200 += 1
                logging.info(f"HTTP 200 OK - Página {pagina} descargada ({url})")
                
                # --- AQUÍ VA TU LÓGICA DE EXTRACCIÓN CON BEAUTIFULSOUP ---
                soup = BeautifulSoup(response.text, "html.parser")
                # ... extraer productos ...

            elif response.status_code == 404:
                errores_http += 1
                logging.warning(f"HTTP 404 Not Found - La página {pagina} no existe ({url})")
            elif response.status_code >= 500:
                errores_http += 1
                logging.error(f"HTTP {response.status_code} Server Error - Caída en servidor ({url})")
            else:
                errores_http += 1
                logging.error(f"HTTP {response.status_code} - Respuesta inesperada en {url}")

        except requests.exceptions.RequestException as e:
            errores_http += 1
            logging.critical(f"Fallo de conexión en página {pagina}: {e}")

    # 3. Resumen de tasa de éxito al finalizar
    logging.info(f"Resumen HTTP -> Éxitos (200): {exitos_200} | Fallos: {errores_http}")
    return len(productos)
