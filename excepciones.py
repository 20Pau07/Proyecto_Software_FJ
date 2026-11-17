# PROYECTO: SOFTWARE FJ
# MODULO: EXCEPCIONES PERSONALIZADAS
# Persona 3: Paula Andrea Briñez

class ErrorSoftwareFJ(Exception):
    """Clase base para las excepciones del sistema."""

class DatosInvalidosError(ErrorSoftwareFJ):
    pass

class ClienteNoEncontradoError(ErrorSoftwareFJ):
    pass

class ServicioNoDisponibleError(ErrorSoftwareFJ):
    pass

class ReservaInvalidaError(ErrorSoftwareFJ):
    pass

class EstadoReservaError(ErrorSoftwareFJ):
    pass

class ParametroFaltanteError(ErrorSoftwareFJ):
    pass

class CalculoCostoError(ErrorSoftwareFJ):
    pass
