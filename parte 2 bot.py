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
