import requests

def get_data_from_api(url):
    try:
        response = requests.get(url)
        # Comprueba si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            # Devuelve los datos en formato JSON si la solicitud fue exitosa
            return response.json()
        else:
            # Si la solicitud no fue exitosa, imprime el código de estado
            print("Error al realizar la solicitud. Código de estado:", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        # Maneja cualquier error de solicitud
        print("Error de solicitud:", e)
        return None

# URL de la API pública
api_url = "https://jsonplaceholder.typicode.com/posts"

# Llama a la función para obtener datos de la API
data = get_data_from_api(api_url)

# Imprime los datos obtenidos
if data:
    print("Datos de la API:")
    for item in data:
        print(item)
else:
    print("No se pudieron obtener datos de la API.")
