class info:
    Nombre = ""
    conocimiento = {
        'perro': 'gato',
        'malo': 'bueno',
        'moverse': 'quieto',
        'noche': 'dia',
        'silencio': 'ruido',
        'feliz': 'triste',
        'negro': 'blanco',
        'mojado': 'seco',
        'dormido': 'despierto',
        'caliente': 'frio',
        'caro': 'varato'
    }
    saludos = {
        'quiuvo':'hola socio',
        'hola':'hola',
        'bien':'me alegro, ¿en que te puedo ayudar?',
        'que más': 'bien, y tu?',
        'buenos días':'muy buenos días, en que puedo ayudarte?'
    }
    despedidas = {
        'chao':'hasta luego, que estés bien',
        'nos vemos':'que le valla bien',
        'hasta luego':'adios',
        'adios':'no metas a Dios en esto'
    }

    def __init__(self):
        self

    def setNombre(self,Nombre):
        self.Nombre = Nombre;

    def addConocimiento(self, pregunta, respuesta):
        self.conocimiento[pregunta] = respuesta

class escritura:
    verbos = [
        'jugar',
        'correr',
        'dormir',
        'nadar',
        'pensar',
        'llorar',
        'pelear',
        'gritar',
        'barrer',
        'bailar'
    ]

    def __init__(self):
        self
