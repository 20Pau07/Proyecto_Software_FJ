#Modulo 1: Entidades bases y datos
# Persona 1: Karen Juliana Rocha

from abc import ABC, abstractmethod

from excepciones import DatosInvalidosError

# 2. Clase abtracta de entidad

class Entidad(ABC):

    def __init__(self, codigo):

        if not isinstance(codigo, str) or not codigo.strip():
            raise DatosInvalidosError(
                "El codigo de la entidad es obligatorio.")

        self.__codigo = codigo.strip()

    @property
    def codigo(self):
        return self.__codigo

    @abstractmethod
    def mostrar_informacion(self):
        pass

# 3. Clase cliente

class Cliente(Entidad):

    def __init__(self, codigo, nombre, correo, telefono):

        super().__init__(codigo)

        self.__nombre = self._validar_texto(
            nombre, "nombre"
        )

        self.__correo = self._validar_correo(correo)

        self.__telefono = self._validar_telefono(
            telefono)

    # Validacion del nombre

    @staticmethod
    def _validar_texto(valor, campo):

        if not isinstance(valor, str) or not valor.strip():
            raise DatosInvalidosError(
                f"El {campo} no puede estar vacio.")

        return valor.strip()

    # Validacion del correo

    @staticmethod
    def _validar_correo(correo):

        if (
            not isinstance(correo, str)
            or "@" not in correo
            or "." not in correo
        ):
            raise DatosInvalidosError(
                "El correo electronico no es valido."
            )

        return correo.strip()

    # Validacion del telefono

    @staticmethod
    def _validar_telefono(telefono):

        telefono = str(telefono).strip()

        if not telefono.isdigit() or len(telefono) < 7:
            raise DatosInvalidosError(
                "El telefono debe tener minimo 7 digitos.")
        return telefono

    # Metodo para consultar los datos

    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    @property
    def telefono(self):
        return self.__telefono

    # Mostrar la informacion de los clientes

    def mostrar_informacion(self):

        return (
            f"Codigo: {self.codigo} | "
            f"Nombre: {self.nombre} | "
            f"Correo: {self.correo} | "
            f"Telefono: {self.telefono}")

    def __str__(self):
        return self.mostrar_informacion()

# 4. Prueba de entidades y bases

if __name__ == "__main__":

    print(" SOFTWARE FJ - REGISTRO DE CLIENTES")


    try:

        cliente1 = Cliente(
            "C001",
            "Daniela Ruiz",
            "danielaru@gmail.com",
            "3021547869" )

        print("\nCliente registrado correctamente:")
        print(cliente1.mostrar_informacion())

        # Prueba de un registro incorrecto
        print("Probando validacion de datos:")

        cliente2 = Cliente(
            "C002",
            "Camilo Ramirez",
            "camilocorreo",
            "3009874531")

    except DatosInvalidosError as error:

        print("Error controlado:", error)

    print("El sistema continua funcionando.")
