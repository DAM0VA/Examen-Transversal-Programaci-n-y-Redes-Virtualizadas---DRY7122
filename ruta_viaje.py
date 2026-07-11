import requests

key = "07298fd1-c946-40cd-93e7-a255e121c6ec"


def buscar(ciudad):
    url = "https://graphhopper.com/api/1/geocode"
    datos = requests.get(url, params={"q": ciudad, "limit": 1, "key": key}).json()
    punto = datos["hits"][0]["point"]
    return punto["lat"], punto["lng"]


while True:
    origen = input("Ciudad de Origen (s para salir): ")
    if origen.lower() == "s":
        break
    destino = input("Ciudad de Destino: ")
    if destino.lower() == "s":
        break

    print("Medio de transporte:  1) Auto   2) Bicicleta   3) A pie")
    opcion = input("Opcion (1-3): ")
    if opcion.lower() == "s":
        break
    medios = {"1": "car", "2": "bike", "3": "foot"}
    medio = medios.get(opcion, "car")

    lat1, lng1 = buscar(origen)
    lat2, lng2 = buscar(destino)

    url = "https://graphhopper.com/api/1/route"
    params = {
        "point": [f"{lat1},{lng1}", f"{lat2},{lng2}"],
        "profile": medio,
        "locale": "es",
        "key": key
    }
    ruta = requests.get(url, params=params).json()["paths"][0]

    km = ruta["distance"] / 1000
    millas = km * 0.621371
    seg = ruta["time"] / 1000
    horas = int(seg // 3600)
    minutos = int((seg % 3600) // 60)
    segundos = int(seg % 60)

    print("Distancia: {:.2f} km".format(km))
    print("Distancia: {:.2f} millas".format(millas))
    print("Duracion: {:02d}:{:02d}:{:02d}".format(horas, minutos, segundos))
    print("Narrativa del viaje:")
    for paso in ruta["instructions"]:
        print("- " + paso["text"])
