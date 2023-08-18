colores = ["rojo", "verde", "amarillo", "negro", "blanco"]


class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if color in colores:
            self.color = color


class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        if tipo in ("electrico", "gasolina"):
            self.tipo = tipo


class Auto:
    cantidadCreados = 0

    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        cantidad = 0
        for asiento in self.asientos:
            if asiento is not None:
                cantidad += 1
        return cantidad

    def verificarIntegridad(self):
        if self._es_integro():
            return "Auto original"
        else:
            return "Las piezas no son originales"

    def _es_integro(self):
        if self.registro != self.motor.registro:
            return False

        for asiento in self.asientos:
            if asiento is not None and asiento.registro != self.registro:
                return False

        return True
