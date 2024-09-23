#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 67
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

# Sistema experto simple para diagnóstico de fallas en un sistema eléctrico

def hacer_pregunta(pregunta):
    """Función que realiza una pregunta y espera una respuesta de 'sí' o 'no'."""
    respuesta = input(pregunta + " (sí/no): ").lower()
    while respuesta not in ['sí', 'no']:
        print("Por favor, responde 'sí' o 'no'.")
        respuesta = input(pregunta + " (sí/no): ").lower()
    return respuesta == 'sí'

def diagnosticar_falla():
    print("Sistema experto para diagnóstico de fallas en un sistema eléctrico.")
    
    # Primera pregunta: ¿Hay electricidad en toda la casa?
    electricidad_en_casa = hacer_pregunta("¿Hay electricidad en toda la casa?")
    
    if not electricidad_en_casa:
        print("Posible falla: Hay un problema con el suministro eléctrico externo.")
        return
    
    # Segunda pregunta: ¿El interruptor está en posición encendida?
    interruptor_encendido = hacer_pregunta("¿El interruptor está en posición encendida?")
    
    if not interruptor_encendido:
        print("Solución: Enciende el interruptor.")
        return
    
    # Tercera pregunta: ¿Hay luz en la habitación?
    luz_en_habitacion = hacer_pregunta("¿Hay luz en la habitación?")
    
    if not luz_en_habitacion:
        bombilla_fundida = hacer_pregunta("¿La bombilla está fundida?")
        
        if bombilla_fundida:
            print("Solución: Cambia la bombilla.")
        else:
            print("Posible falla: Revisa los fusibles o el sistema de cableado.")
        return
    
    # Cuarta pregunta: ¿Hay problemas con algún electrodoméstico?
    problema_electrodomestico = hacer_pregunta("¿Algún electrodoméstico no funciona?")
    
    if problema_electrodomestico:
        sobrecarga_circuito = hacer_pregunta("¿El sistema está sobrecargado?")
        
        if sobrecarga_circuito:
            print("Solución: Desconecta algunos electrodomésticos o instala un sistema de mayor capacidad.")
        else:
            print("Posible falla: El electrodoméstico puede estar dañado.")
    else:
        print("Todo parece estar en orden. Si el problema persiste, puede requerir una inspección más detallada.")
    
def main():
    while True:
        diagnosticar_falla()
        repetir = input("¿Quieres realizar otro diagnóstico? (sí/no): ").lower()
        if repetir != 'sí':
            print("Gracias por usar el sistema experto de diagnóstico.")
            break

if __name__ == "__main__":
    main()
