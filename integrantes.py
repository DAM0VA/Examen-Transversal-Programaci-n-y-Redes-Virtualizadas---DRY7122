from tabulate import tabulate

integrantes = [
    ("Daniel", "Morales Valenzuela"),
    ("Manuel", "Gonzalez Cona"),
]

def main():
    print("Integrantes del grupo - Examen Transversal DRY7122\n")
    tabla = [(i + 1, nom, ape) for i, (nom, ape) in enumerate(integrantes)]
    print(tabulate(tabla, headers=["#", "Nombre", "Apellido"], tablefmt="grid"))

if __name__ == "__main__":
    main()
