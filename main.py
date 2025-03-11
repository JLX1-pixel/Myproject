
def forma_pago(n_piezas, precio_unitario):
    monto_total = n_piezas * precio_unitario
    if monto_total > 500000:
        inversion_empresa = (monto_total * 0.55)
        prestamo_banco = (monto_total * 0.30)
        credito_fabricante = (monto_total * 0.15)
    else:
        inversion_empresa = (monto_total * 0.70)
        credito_fabricante = (monto_total * 0.30)

    interes_fabricante = credito_fabricante * 0.20
    total_credito_fabricante = credito_fabricante + interes_fabricante

    # Mostrar resultados
    print(f"\n- Número de piezas a comprar: {n_piezas} - Precio unitario de cada pieza: {precio_unitario}")
    print(f"- Monto total de la compra: {monto_total} - Inversión de la compra: {inversion_empresa}")
    if monto_total > 500000:
        print(f"- Préstamo al banco: {prestamo_banco} - Crédito al fabricante: {credito_fabricante}")
    print(f"- Crédito al fabricante sumando el interés del 20%: {total_credito_fabricante}\n")

while True:
    print("\n1. Agregar la cantidad y el valor unitario de la pieza que desea comprar.")
    print("2. Salir del programa.")
    opcion = input("Ingrese la opción que desea: ")
    
    if opcion == "1":
        try:
            n_piezas = int(input("\nIngrese el número de piezas a comprar: "))
            precio_unitario = float(input("Ingrese el precio unitario de la pieza: "))
            forma_pago(n_piezas, precio_unitario)
        except ValueError:
            print("\nPor favor, ingrese un número válido.")
    elif opcion == "2":
        break
    else:
        print("\nIngrese una opción válida.")
