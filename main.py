import nltk
import re


def RE():
    #Email
    #ex = r"(^[a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    #cadena = "correo.prueba@dominio.com"

    #Numero de telefono valido
    #ex = r"(^3[0-9]{9}$)"
    #cadena = "3215030353"

    # Fechas DD/MM/AAAA
    ex = r"([0-2][0-9]|3[0-1])(\/|-)(0[1-9]|1[0-2])\2(\d{4})"
    cadena = "27-12-2002"


    if re.match(ex, cadena) is None:
        print("NO es una cadena valida")
    else:
        print("Es una cadena valida")

def REFullMatch():
    exp = re.compile(r'ab*')
    res = exp.fullmatch('abbb')
    if res is None:
        print("No es una cadena valida")
    else:
        print("Es una cadena valida")

def GIC():
    try:
        g1 = """
            S -> NP VP
            NP -> Det N | Det N PP | 'I'
            VP -> V NP | VP PP
            PP -> P NP
            Det -> 'an' | 'my'
            N -> 'elephant' | 'pajamas'
            V -> 'shot'
            P -> 'in'
            """

        grammar1 = nltk.CFG.fromstring(g1)
        oracion = "I shot an elephant in my pajamas".split()
        # guardamos todos los posibles análisis sintácticos en trees
        rdParser = nltk.RecursiveDescentParser(grammar1)
        for tree in rdParser.parse(oracion):
            print(tree)
            tree.draw()
            aux = True
        if not aux:
            print("Fnished")
        else:
            print(len(rdParser.parse((oracion))))
    except:
        print("Esta cadena no se encuentra en la gramatica")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #GIC()
    RE()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
