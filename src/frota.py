class Carro:
    modelo : str
    marca : str
    cor : str
    odometro : 0.0
    motor_on : False
    tanque : float
    cm: float

    def __init__(self, modelo : str, marca : str, cor : str,
                       odometro : float, motor : bool, tanque: float, cm:float):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.odometro = odometro
        self.motor_on = motor
        self.tanque = tanque
        self.cm = cm

    def ligar(self):
        if not self.motor_on and self.tanque > 0:
            self.motor_on = True
        else:
            raise Exception("Erro: Motor já ligado!")

    def acelerar(self, velocidade : float, tempo : float):
        if self.motor_on:
            km = velocidade * tempo
            litros = km / self.cm
            if self.tanque >= litros:
                self.odometro += km
                self.tanque -= litros
            else:
                km = self.tanque * self.cm
                self.tanque = 0
                self.desligar()

            self.odometro += km

        else:
            raise Exception("Erro: Não é possível acelerar! Motor desligado!")

    def desligar(self):
        if self.motor_on:
            self.motor_on = False
        else:
            raise Exception("Erro: Motor já desligado!")

    def __str__(self):
        info = (f'Carro: {self.modelo}\n'
                f'Marca: {self.marca}\n'
                f'Cor: {self.cor}\n{self.odometro} Km, '
                f'Motor: {self.motor_on}\n'
                f'Consumo: {self.cm} Km/L\n'
                f'Nivel do tanque: {self.tanque} L\n')
        return info





