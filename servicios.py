# IMPORTACION CLASES ABSTRACTAS  
# Persona 2: Andres Julian Tellez

from abc import ABC, abstractmethod
from excepciones import DatosInvalidosError, ParametroFaltanteError

# Clase Abstracta Servicio
class Servicio(ABC):

    def __init__(self, codigo, nombre, precio):
        if not isinstance(codigo, str) or not codigo.strip():
            raise ParametroFaltanteError("El codigo del servicio es obligatorio.")
        if not isinstance(nombre, str) or not nombre.strip():
            raise ParametroFaltanteError("El nombre del servicio es obligatorio.")
        if isinstance(precio, bool) or not isinstance(precio, (int, float)) or precio <= 0:
            raise DatosInvalidosError("El precio del servicio debe ser mayor a cero.")

        self.codigo = codigo.strip()
        self.nombre = nombre.strip()
        self.precio = precio

    @abstractmethod
    def calcular_costo(self, duracion=None):
        pass

    @abstractmethod
    def describir_servicio(self):
        pass

    @abstractmethod
    def validar_parametros(self, duracion=None):
        pass

# Clase Reserva de Sala
class ReservaSala(Servicio):

    def __init__(self, codigo, nombre, precio, horas, capacidad):
        super().__init__(codigo, nombre, precio)

        self.horas = horas
        self.capacidad = capacidad

    def calcular_costo(self, duracion=None):
        tiempo = duracion if duracion is not None else self.horas
        return self.precio * tiempo

    def describir_servicio(self):
        return "Servicio de reserva de sala"

    def validar_parametros(self, duracion=None):
        tiempo = duracion if duracion is not None else self.horas
        return tiempo > 0 and self.capacidad > 0

# Clase Alquiler de Equipos
class AlquilerEquipos(Servicio):

    def __init__(self, codigo, nombre, precio, cantidad, dias):
        super().__init__(codigo, nombre, precio)

        self.cantidad = cantidad
        self.dias = dias

    def calcular_costo(self, duracion=None):
        tiempo = duracion if duracion is not None else self.dias
        return self.precio * self.cantidad * tiempo

    def describir_servicio(self):
        return "Servicio de alquiler de equipos"

    def validar_parametros(self, duracion=None):
        tiempo = duracion if duracion is not None else self.dias
        return self.cantidad > 0 and tiempo > 0

# Clase Asesoria Especializada
class AsesoriaEspecializada(Servicio):

    def __init__(self, codigo, nombre, precio, especialidad, horas):
        super().__init__(codigo, nombre, precio)

        self.especialidad = especialidad
        self.horas = horas

    def calcular_costo(self, duracion=None):
        tiempo = duracion if duracion is not None else self.horas
        return self.precio * tiempo

    def describir_servicio(self):
        return "Servicio de asesoria especializada"

    def validar_parametros(self, duracion=None):
        tiempo = duracion if duracion is not None else self.horas
        return tiempo > 0 and isinstance(self.especialidad, str) and self.especialidad.strip() != ""