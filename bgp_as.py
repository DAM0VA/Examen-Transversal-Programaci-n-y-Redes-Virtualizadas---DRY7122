def clasificar_asn(asn: int) -> str:
    if asn in (0, 65535, 4294967295):
        return "Reservado (no asignable)"
    if asn == 23456:
        return "Reservado (AS_TRANS)"
    if 64496 <= asn <= 64511 or 65536 <= asn <= 65551:
        return "Reservado (documentacion)"
    if 64512 <= asn <= 65534:
        return "Privado (16 bits)"
    if 4200000000 <= asn <= 4294967294:
        return "Privado (32 bits)"
    if 1 <= asn <= 4294967295:
        return "Publico"
    return "Fuera de rango"

def main():
    print("Clasificador de ASN de BGP - DRY7122")
    print("Rango valido: 1 - 4294967295   (0 = salir)\n")
    while True:
        entrada = input("Ingrese numero de AS de BGP: ").strip()
        if not entrada.isdigit():
            print("  -> Debe ingresar un numero entero.\n")
            continue
        asn = int(entrada)
        if asn == 0:
            print("Saliendo...")
            break
        print(f"  -> ASN {asn}: {clasificar_asn(asn)}\n")

if __name__ == "__main__":
    main()
