import json
import random
import datetime
import json
from grafo import *


# Función para generar una relación de forma aleatoria
def generar_relacion(id_emisor, id_receptor):
  nombres = ["Liam", "Olivia", "Noah", "Emma", "Sophia", "Jackson", "Ava", "Lucas",
      "Isabella", "Oliver", "Lily", "Ethan", "Mia", "Aiden", "Amelia", "Caden",
      "Harper", "Michael", "Evelyn", "James", "Abigail", "Benjamin", "Emily",
      "Alexander", "Charlotte", "Daniel", "Madison", "Henry", "Avery",
      "Sebastian", "Scarlett", "Matthew", "Aria", "Samuel", "Grace", "David",
      "Chloe", "Joseph", "Camila", "Carter", "Penelope", "Owen", "Luna",
      "Wyatt", "Sofia", "John", "Ella", "Jack", "Mila", "Luke", "Aubrey",
      "Jayden", "Scarlet", "Dylan", "Layla", "Grayson", "Ellie", "Levi",
      "Zoey", "Isaac", "Grace", "Gabriel", "Victoria"]
  mensaje = f"Hola {nombres[id_receptor]}, soy {nombres[id_emisor]}. Amigos!!!."
  relacion = {
      "id_emisor": id_emisor,
      "nombre_emisor": nombres[id_emisor],
      "id_receptor": id_receptor,
      "nombre_receptor": nombres[id_receptor],
      "mensaje": mensaje,
      "hora": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  }
  return relacion


# Función para crear la lista de adyacencia y la lista de nombres
def crear_lista_adyacencia_y_nombres(historial_mensajes):
    lista_adyacencia = {}
    lista_nombres_ordenada = []

    for mensaje in historial_mensajes:
        id_emisor = mensaje["id_emisor"]
        id_receptor = mensaje["id_receptor"]
        nombre_emisor = mensaje["nombre_emisor"]
        nombre_receptor = mensaje["nombre_receptor"]

        if id_emisor not in lista_adyacencia:
            lista_adyacencia[id_emisor] = {}
            lista_nombres_ordenada.append(nombre_emisor)
        if id_receptor not in lista_adyacencia:
            lista_adyacencia[id_receptor] = {}
            lista_nombres_ordenada.append(nombre_receptor)

        # Incrementar el peso de la conexión de emisor a receptor y viceversa
        lista_adyacencia[id_emisor][id_receptor] = lista_adyacencia[id_emisor].get(id_receptor, 0) + 1
        lista_adyacencia[id_receptor][id_emisor] = lista_adyacencia[id_receptor].get(id_emisor, 0) + 1

    # Convertir la representación interna a la estructura final
    for usuario, conexiones in lista_adyacencia.items():
        lista_adyacencia[usuario] = [{"destino": destino, "peso": peso} for destino, peso in conexiones.items()]

    return lista_adyacencia, lista_nombres_ordenada


def main(cantidad):
  # Número de relaciones que deseas generar
  n = cantidad

  # Lista para almacenar las relaciones
  relaciones = []

  # Generar n relaciones y agregarlas a la lista
  for x in range(n):
    id_emisor = random.randint(0, 4)
    id_receptor = random.randint(0, 4)
    while (id_emisor == id_receptor):
      id_receptor = random.randint(0, 4)
    relacion = generar_relacion(id_emisor, id_receptor)
    relaciones.append(relacion)

  # Crear la lista de adyacencia
  lista_adyacencia, lista_nombres = crear_lista_adyacencia_y_nombres(relaciones)

  # Guardar la lista de adyacencia y la lista de nombres en un archivo JSON
  with open("datos.json", "w") as json_file:
      json.dump({"lista_adyacencia": lista_adyacencia, "lista_nombres": lista_nombres}, json_file, indent=4)

  # Guardar la lista de relaciones en un archivo JSON
  with open("historial_comunicaciones.json", "w") as archivo_json:
    json.dump(relaciones, archivo_json, indent=2)
  print(
      f"Se han generado y guardado {n} relaciones en el archivo 'relaciones.json'."
  )


# Crear una instancia de la clase GrafoDirigido
if __name__ == "__main__":
  main(int(input("Cuantas interacciones desea generar?: ")))
  
  # Cargar datos desde un archivo JSON
  with open('datos.json', 'r') as file:
    data = json.load(file)

  lista_adyacencia = data["lista_adyacencia"]
  nombres = data["lista_nombres"]
  grafo = GrafoDirigido(data)

  # Agregar nodos al grafo a partir de los datos cargados
  x = 0
  for id  in lista_adyacencia:
    nombre = nombres[x]
    nodo = Nodo(id, nombre)
    grafo.agregar_nodo(nodo)
    x += 1
  # Agregar aristas al grafo a partir de la lista de adyacencia
  for origen, destinos_con_pesos in lista_adyacencia.items():
    for destino_info in destinos_con_pesos:
      destino = destino_info["destino"]
      peso = destino_info["peso"]
      arista = grafo.agregar_arista(grafo.nodos.get(origen),
                           grafo.nodos.get(str(destino)), peso)
      
  grafo.mostrar_grafo()
  grafo.buscar_mayor()
  grafo.mejores_amigos()
