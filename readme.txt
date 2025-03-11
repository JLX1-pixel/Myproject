Gestión de Compra de Piezas
Este proyecto calcula la distribución de financiamiento para la compra de piezas dependiendo del monto total de la inversión.
Descripción
El programa solicita al usuario dos datos:
Número de piezas a comprar
Precio unitario de cada pieza
Con esta información, se calcula el monto total de la compra y se distribuye el financiamiento de la siguiente manera:
Si el monto total supera los $500,000:
55% se financia con la inversión propia de la empresa.
30% se solicita como préstamo bancario.
15% se financia con crédito del fabricante, que incluye un 20% de interés.
Si el monto total es menor o igual a $500,000:
70% se financia con la inversión propia de la empresa.
30% se financia con crédito del fabricante, también con un 20% de interés.
Código
python
numero_piezas = int(input("Ingrese el número de piezas a comprar: "))
precio_unitario = float(input("Ingrese el precio unitario de cada pieza: "))

monto_total = numero_piezas * precio_unitario

inversion_empresa = 0
prestamo_banco = 0
credito_fabricante = 0

if monto_total > 500000:
    inversion_empresa = monto_total * 0.55
    prestamo_banco = monto_total * 0.30
    credito_fabricante = (monto_total * 0.15) * 1.20  
else:
    inversion_empresa = monto_total * 0.70
    credito_fabricante = (monto_total * 0.30) * 1.20  

print(f"Número de piezas a comprar: {numero_piezas}")
print(f"Precio unitario de cada pieza: ${precio_unitario:.2f}")
print(f"Monto total de la compra: ${monto_total:.2f}")
print(f"Inversión de la empresa: ${inversion_empresa:.2f}")
print(f"Préstamo al banco: ${prestamo_banco:.2f}")
print(f"Crédito al fabricante (incluyendo intereses): ${credito_fabricante:.2f}")
Instrucciones de ejecución
Asegúrate de tener Python 3.x instalado en tu equipo.
Guarda el código en un archivo llamado main.py dentro del directorio myProject.
Abre la terminal o consola de comandos y navega hasta la carpeta del proyecto usando el comando:
bash
cd ruta/del/proyecto/myProject
Ejecuta el siguiente comando para iniciar el programa:
css
python main.py
Ejemplo de salida
yaml
Ingrese el número de piezas a comprar: 2000
Ingrese el precio unitario de cada pieza: 300
Número de piezas a comprar: 2000
Precio unitario de cada pieza: $300.00
Monto total de la compra: $600000.00
Inversión de la empresa: $330000.00
Préstamo al banco: $180000.00
Crédito al fabricante (incluyendo intereses): $108000.00
Créditos
Desarrollado por Louis Sleyth Acuña Mulford
Contacto: Louissleyth12@gmail.com
