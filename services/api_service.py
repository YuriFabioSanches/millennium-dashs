import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

API_URL = "https://192.168.34.28/rest/VendaProduto_DataProvider_Rest"
API_KEY = "n6zF2RYlaXlV4HNEhjJiCIDZ567MLy3G2X5Qy4/oiDg="

def get_vendas(data_inicial, data_final):
    params = {
        "ChaveApi": API_KEY,
        "DataInicial": data_inicial.strftime('%Y-%m-%d'),
        "DataFinal": data_final.strftime('%Y-%m-%d'),
        "Pagina": 1,
        "Tamanho": 100
    }
    try:
        response = requests.get(API_URL, params=params, verify=False, timeout=10)
        response.raise_for_status()
        logger.info("Consulta à API realizada com sucesso.")
        return response.json()
    except Exception as e:
        logger.error(f"Erro na consulta à API: {e}")
        return []
