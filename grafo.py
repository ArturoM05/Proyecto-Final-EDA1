class Nodo:
  # Constructor de la clase Nodo.
  # Inicializa un nodo con un ID y un nombre.
  def __init__(self, id, nombre):
    self.id = id
    self.nombre = nombre

  # Representación en cadena del nodo.
  def __str__(self):
    return f'({self.id}) | '


class Arista:
  # Constructor de la clase Arista.
  # Inicializa una arista con un nodo de inicio, un nodo de destino y un peso.
  def __init__(self, nodo_inicio, nodo_destino, peso):
    self.nodo_inicio = nodo_inicio
    self.nodo_destino = nodo_destino
    self.peso = peso

  # Representación en cadena de la arista.
  def __str__(self):
    return f'ARISTA [{self.nodo_inicio} --> {self.nodo_destino}:: w:{self.peso}]'


class GrafoDirigido:
  # Constructor de la clase Arista.
  # Inicializa una arista con un nodo de inicio, un nodo de destino y un peso.
  def __init__(self, data):
    self.nodos = {}  # Diccionario para almacenar nodos con su ID como clave.
    self.aristas = []  # Lista para almacenar las aristas del grafo.
    self.lista = data["lista_adyacencia"]  # Lista para almacenar los datos del grafo.

  # Agrega un nodo al grafo.
  def agregar_nodo(self, nodo):
    self.nodos[nodo.id] = nodo

  # Agrega una arista al grafo, si los nodos de inicio y destino existen en el grafo.
  def agregar_arista(self, nodo_inicio, nodo_destino, peso):
    if nodo_inicio.id in self.nodos and nodo_destino.id in self.nodos:
      arista = Arista(nodo_inicio, nodo_destino, peso)
      self.aristas.append(arista)
      return arista


  # Muestra el grafo en forma de lista de adyacencia y matriz de adyacencia.
  def mostrar_grafo(self):
    print(
        f"\n==================================LISTA-ADYACENCIA=================================="
    )
    for origen in self.lista:
      print(f"{self.nodos.get(origen).nombre}|(origen: {origen})|{self.lista.get(origen)}")
    
  #Buscar el usuario con mas amigos
  def buscar_mayor(self):
    print(f"\n==================================USUARIO-MAX-AMIGOS=================================="
         )
    usuario_max = None
    max_elementos = 0
  
    for clave, lista in self.lista.items():
        cantidad_elementos = len(lista)
  
        if cantidad_elementos > max_elementos:
            max_elementos = cantidad_elementos
            usuario_max = clave
    print(f"El usuario con más conexiones es {self.nodos.get(usuario_max).nombre} con {max_elementos} amigos/contactos.")

  #Buscar los mejores amigos
  def mejores_amigos(self):
    print(f"\n==================================MEJORES-AMIGOS=================================="
       )
    arista_mayor_peso = None
    peso_maximo = float('-inf')  # Inicializar con un valor muy bajo
  
    for arista in self.aristas:
        peso_arista = arista.peso
        if peso_arista > peso_maximo:
            peso_maximo = peso_arista
            arista_mayor_peso = arista
    print(f"Los usuarios mejores amigos son {arista_mayor_peso.nodo_inicio.nombre} y {arista_mayor_peso.nodo_destino.nombre} peso {arista_mayor_peso.peso}")


