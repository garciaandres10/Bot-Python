# diccionario de contrarios
# clase informacion: esta clase contiene el diferentes diccionarios. entre conocimiento , saludo, despedidas
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
    # funcion nombre    
    # al iniciar el nombre la funcion saca el nombre de la persona que esta interactuando con el programa
    def setNombre(self,Nombre):
        """
        
        :param Nombre: Nombre de la persona 
        :return:  retorna el nombre de la persona 
        """
        self.Nombre = Nombre;
    #funcion añadir conocimeinto 
    # funcion que añade la palabra al diccionario conocimiento 
    def addConocimiento(self, pregunta, respuesta):
          """
        
        :param pregunta: pregunta ingresada por la persona 
        :param respuesta: respuesta mandada 
        :return: 
        """
        self.conocimiento[pregunta] = respuesta
# clase escritura
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
# funcion principal      
def main():
    lainfo = info()
    Saludo = input("Hola \n")
    if Saludo in lainfo.saludos:
        print(lainfo.saludos[Saludo])
    Nombre = input("¿como te llamas?\n")
    ortog = escritura()


    verbo = ortog.verbos
    conocimiento = lainfo.conocimiento
    despedida = lainfo.despedidas

    print("Hola " + Nombre
                         + " verás, te explico soy Pepito, un programa que te ayuda a saber los contrarios de las palabras")

    while True:
        pregunta = input(Nombre + "¿ de que palabra buscas el contrario?\n")
        separarPregunta = pregunta.split()

        if pregunta in conocimiento:
            print("el contrario es " + conocimiento[pregunta] + "\n")
        elif pregunta in despedida:
            print(despedida[pregunta]+ " " + Nombre)
            break
        else:
            print("Oye, no tengo la respuesta, pero, hagamos una cosa, tu me vas a ayudar \n")
            respuesta = input("como podría responder a eso? \n")
            lainfo.addConocimiento(pregunta,respuesta)

        numseparar = len(separarPregunta)
        numverbos = len(verbo)
        verbosSon = []
        for i in range(0, numverbos):
            for j in range(0, numseparar):
                if verbo[i] == separarPregunta[j]:
                    verbosSon.append(separarPregunta[j])
        for i in verbosSon:
            print(i)

        if len(verbosSon) == 0:
            print("tu frase no tiene verbos\n")
        aprenderVerbos = input("o acaso ¿me faltó alguno?\n")
        if aprenderVerbos.lower() == 'si':
            verboAprender = input("¿podrías indicarme cuál fué?\n")
            verbo.append(verboAprender)
            print("gracias por tu ayuda")

main()
        
