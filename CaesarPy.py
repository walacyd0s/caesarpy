class Caesar:
    def __init__(self):
        self.texto_claro = ''
        self.posicao = 0
        self.texto_cifrado = ''
        self.sequencia = ''

    def cifrar(self):
        self.texto_claro = str(input('Informe a mensagem para criptografar: '))
        self.texto_claro = self.texto_claro.lower()
        self.posicao = int(input('Informe a posição(deslocamento): '))
        for x in self.texto_claro:
            if x == ' ':
                self.texto_cifrado += x
                continue
            self.sequencia = ord(x) + self.posicao
            if self.sequencia > 122:
                self.sequencia = (self.sequencia - 122) + 96
            x = chr(self.sequencia)
            self.texto_cifrado += x
        print(self.texto_cifrado)

    def decifrar(self):
        self.texto_cifrado = str(input('Informe a mensagem para descriptografar: '))
        self.texto_cifrado = self.texto_cifrado.lower()
        self.posicao = int(input('Informe a posição(deslocamento): '))
        for y in self.texto_cifrado:
            if y == ' ':
                self.texto_claro += y
                continue
            self.sequencia = ord(y) - self.posicao
            if self.sequencia < 97:
                self.sequencia = 123 - (97 - self.sequencia)
            y = chr(self.sequencia)
            self.texto_claro += y
        print(self.texto_claro)


mensagem = Caesar()
mensagem.decifrar()
