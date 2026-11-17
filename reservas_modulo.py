# PROYECTO: SOFTWARE FJ
# MODULO: GESTION DE RESERVAS
# Persona 3: Paula Andrea Briñez

from excepciones import (
    ReservaInvalidaError,
    ServicioNoDisponibleError,
    EstadoReservaError,
    CalculoCostoError
)
from logs_sistema import registrar_evento, registrar_error


class Reserva:

    def __init__(self, cliente, servicio, duracion):
        if cliente is None:
            raise ReservaInvalidaError("No se puede crear una reserva sin cliente.")

        if servicio is None:
            raise ReservaInvalidaError("No se puede crear una reserva sin servicio.")

        if isinstance(duracion, bool) or not isinstance(duracion, (int, float)):
            raise ReservaInvalidaError("La duración debe ser un número.")

        if duracion <= 0:
            raise ReservaInvalidaError("La duración debe ser mayor a cero.")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"
        self.costo = None

        registrar_evento("Se creó una nueva reserva.")

    def validar_servicio(self):
        try:
            if not callable(getattr(self.servicio, "validar_parametros", None)):
                raise ServicioNoDisponibleError(
                    "El servicio no tiene el método de validación requerido."
                )

            resultado = self.servicio.validar_parametros(self.duracion)
            if resultado is False:
                raise ServicioNoDisponibleError(
                    "El servicio no está disponible para esta reserva."
                )

            return True

        except ServicioNoDisponibleError:
            raise
        except Exception as error:
            raise ServicioNoDisponibleError(
                "No fue posible validar el servicio."
            ) from error

    def confirmar(self):
        if self.estado != "Pendiente":
            raise EstadoReservaError("Solo se pueden confirmar reservas pendientes.")

        try:
            self.validar_servicio()
            self.estado = "Confirmada"
            registrar_evento("Reserva confirmada correctamente.")
            return "La reserva fue confirmada."
        except Exception as error:
            registrar_error(error)
            raise

    def cancelar(self):
        if self.estado not in ("Pendiente", "Confirmada"):
            raise EstadoReservaError(
                "No se puede cancelar una reserva en este estado."
            )

        self.estado = "Cancelada"
        registrar_evento("Reserva cancelada correctamente.")
        return "La reserva fue cancelada."

    def procesar(self):
        if self.estado != "Confirmada":
            raise EstadoReservaError(
                "La reserva debe estar confirmada para procesarse."
            )

        try:
            if not callable(getattr(self.servicio, "calcular_costo", None)):
                raise CalculoCostoError(
                    "El servicio no tiene un método de cálculo de costos."
                )

            costo = self.servicio.calcular_costo(self.duracion)

            if isinstance(costo, bool) or not isinstance(costo, (int, float)):
                raise CalculoCostoError("El costo calculado no es válido.")

            if costo < 0:
                raise CalculoCostoError("El costo no puede ser negativo.")

            self.costo = costo
            self.estado = "Procesada"
            registrar_evento(f"Reserva procesada. Costo: {self.costo}")
            return self.costo

        except CalculoCostoError:
            raise
        except Exception as error:
            registrar_error(error)
            raise ReservaInvalidaError(
                "No fue posible procesar la reserva."
            ) from error

    def calcular_costo(self, impuesto=0, descuento=0):
        if self.estado not in ("Confirmada", "Procesada"):
            raise EstadoReservaError(
                "La reserva debe estar confirmada o procesada."
            )

        if (
            isinstance(impuesto, bool)
            or not isinstance(impuesto, (int, float))
            or isinstance(descuento, bool)
            or not isinstance(descuento, (int, float))
        ):
            raise CalculoCostoError(
                "El impuesto y el descuento deben ser numéricos."
            )

        if not 0 <= impuesto <= 100:
            raise CalculoCostoError("El impuesto debe estar entre 0 y 100.")

        if not 0 <= descuento <= 100:
            raise CalculoCostoError("El descuento debe estar entre 0 y 100.")

        try:
            if self.costo is None:
                if not callable(getattr(self.servicio, "calcular_costo", None)):
                    raise CalculoCostoError(
                        "El servicio no permite calcular costos."
                    )

                costo_base = self.servicio.calcular_costo(self.duracion)
                if isinstance(costo_base, bool) or not isinstance(costo_base, (int, float)) or costo_base < 0:
                    raise CalculoCostoError("El costo base calculado no es válido.")
            else:
                costo_base = self.costo

            total = costo_base * (1 - descuento / 100)
            total = total * (1 + impuesto / 100)

            registrar_evento(f"Se calculó el costo final: {total}")
            return round(total, 2)

        except CalculoCostoError:
            raise
        except Exception as error:
            registrar_error(error)
            raise CalculoCostoError(
                "Ocurrió un problema al calcular el costo."
            ) from error

    def mostrar_informacion(self):
        return {
            "cliente": self.cliente,
            "servicio": self.servicio,
            "duracion": self.duracion,
            "estado": self.estado,
            "costo": self.costo
        }