class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            return
        self._ligado = True

    def desligar(self):
        if not self._ligado:
            return
        self._ligado = False


class LogMixin:

    @staticmethod
    def write(msg):
        with open('log.log', 'a+') as file:
            file.write(f'{msg}\n')

    def log_info(self, msg):
        self.write(f'[INFO] {msg}')

    def log_error(self, msg):
        self.write(f'[ERROR] {msg}')

    def log_warning(self, msg):
        self.write(f'[WARNING] {msg}')


class Smarthphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            warning = f'{self._nome} não está ligado.'
            self.log_warning(warning)
            return

        if self._conectado:
            error = f'{self._nome} já está conectado.'
            self.log_error(error)

        info = f'{self._nome} agora está conectado.'
        self.log_info(info)
        self._conectado = True

    def desconectar(self):
        if not self._conectado:
            error = f'{self._nome} não está conectado.'
            self.log_error(error)
            return

        info = f'{self._nome} agora está desconectado.'
        self.log_info(info)
        self._conectado = False


smartphone = Smarthphone('Pocophone F1')
smartphone.conectar()
smartphone.desligar()
smartphone.ligar()
smartphone.desconectar()
smartphone.conectar()
smartphone.conectar()
smartphone.conectar()
smartphone.desconectar()
smartphone.desligar()
smartphone.conectar()
smartphone.desligar()
smartphone.desligar()

