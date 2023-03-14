# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import requests

def obtener_palabra_aleatoria():

    #Pedimos una lista de 10 palabras aleatorias en español a la API mediante el método GET
    url = 'https://random-word-api.herokuapp.com/word?lang=es&number=10'
    response = requests.get(url)
    #Si la respuesta ha sido existosa imprimimos la lista de las 10 palabras y devolvemos
    #la que se encuentra en la cuarta popsición de la lista
    if response.status_code == 200:
        print(response.json())
        return response.json()[4]
    else:
        return None



if __name__ == '__main__':
    # Ejemplo de uso
    palabra_aleatoria = obtener_palabra_aleatoria()
    print('la palabra aleatoria es:', palabra_aleatoria)