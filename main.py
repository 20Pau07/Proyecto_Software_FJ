# PROYECTO: SOFTWARE FJ
# ARCHIVO PRINCIPAL: SIMULACIÓN DE 10 OPERACIONES
# COLABORADORES: Persona 1: Karen Juliana Rocha, Persona 2: Andres Julian Tellez, Persona 3: Paula Andrea Briñez

from clientes import Cliente
from servicios import ReservaSala, AlquilerEquipos, AsesoriaEspecializada
from reservas_modulo import Reserva
from excepciones import ErrorSoftwareFJ
from logs_sistema import registrar_evento, registrar_error, registrar_advertencia

def ejecutar_simulacion():
    clientes = []
    servicios = []
    reservas = []

    print("=== INICIANDO SIMULACIÓN SISTEMA SOFTWARE FJ ===\n")
    registrar_evento("=== INICIO DE SIMULACIÓN DE 10 OPERACIONES ===")

    # Simulacion 1
    try:
        c1 = Cliente("C001", "Daniela Ruiz", "daniela@correo.com", "3021547869")
        clientes.append(c1)
    except ErrorSoftwareFJ as e:
        registrar_error(e)
    else:
        print(f"[Op 1 - Éxito] Cliente registrado: {c1.nombre}")
        registrar_evento(f"Cliente registrado: {c1.codigo}")

    # Simulacion 2
    try:
        c2 = Cliente("C002", "Camilo Ramírez", "camilocorreo.com", "3009874531")
        clientes.append(c2)
    except ErrorSoftwareFJ as e:
        print(f"[Op 2 - Error Controlado] No se creó cliente: {e}")
        registrar_error(f"Op 2 fallida: {e}")

    # Simulacion 3
    try:
        c3 = Cliente("C003", "Laura Gómez", "laura@empresa.com", "3112223344")
        clientes.append(c3)
    except ErrorSoftwareFJ as e:
        registrar_error(e)
    else:
        print(f"[Op 3 - Éxito] Cliente registrado: {c3.nombre}")

    # Simulacion 4  
    try:
        s1 = ReservaSala("S001", "Sala Juntas Norte", 50000, 2, 10)
        servicios.append(s1)
    except ErrorSoftwareFJ as e:
        registrar_error(e)
    else:
        print(f"[Op 4 - Éxito] Servicio creado: {s1.describir_servicio()}")

    # Simulacion 5.
    try:
        s_error = AlquilerEquipos("S002", "Portátil Gamer", -15000, 2, 3)
        servicios.append(s_error)
    except ErrorSoftwareFJ as e:
        print(f"[Op 5 - Error Controlado] Servicio rechazado: {e}")
        registrar_error(f"Op 5 fallida: {e}")

    # Simulacion 6.
    try:
        s2 = AlquilerEquipos("S003", "Kit Proyector HD", 30000, 2, 1)
        s3 = AsesoriaEspecializada("S004", "Consultoría Cloud", 80000, "Arquitectura AWS", 3)
        servicios.extend([s2, s3])
    except ErrorSoftwareFJ as e:
        registrar_error(e)
    else:
        print(f"[Op 6 - Éxito] Servicios adicionales creados correctamente.")

    # Simulacion 7.
    try:
        r1 = Reserva(c1, s1, duracion=4)
        r1.confirmar()
        costo_final = r1.calcular_costo(impuesto=19, descuento=10)
        r1.procesar()
        reservas.append(r1)
    except ErrorSoftwareFJ as e:
        print(f"[Op 7 - Error] {e}")
        registrar_error(e)
    else:
        print(f"[Op 7 - Éxito] Reserva confirmada y procesada. Total con IVA/Descuento: ${costo_final}")
    finally:
        registrar_evento("Finalizó verificación de Operación 7.")

    # Simulacion 8.
    try:
        r_error = Reserva(c3, s2, duracion=0)
        reservas.append(r_error)
    except ErrorSoftwareFJ as e:
        print(f"[Op 8 - Error Controlado] Reserva rechazada: {e}")
        registrar_error(f"Op 8 fallida: {e}")

    # Simulacion 9. 
    try:
        r2 = Reserva(c3, s3, duracion=2)
        r2.procesar()  # Debe fallar porque está en estado "Pendiente"
    except ErrorSoftwareFJ as e:
        print(f"[Op 9 - Error Controlado] Flujo de estado inválido: {e}")
        registrar_error(f"Op 9 fallida: {e}")

    # Simulacion 10.
    try:
        r2.confirmar()
        mensaje_cancelacion = r2.cancelar()
        reservas.append(r2)
    except ErrorSoftwareFJ as e:
        print(f"[Op 10 - Error] {e}")
        registrar_error(e)
    else:
        print(f"[Op 10 - Éxito] {mensaje_cancelacion} (Estado actual: {r2.estado})")
    finally:
        print("\n=== SIMULACIÓN FINALIZADA SIN INTERRUPCIONES ===")
        registrar_evento("=== FIN DE SIMULACIÓN ===")

if __name__ == "__main__":
    ejecutar_simulacion()