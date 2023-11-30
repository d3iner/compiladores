import nltk
import re


def RE():
    #Email
    ex = r"(^[a-zA-Z0-9_.-]+@[a-zA-Z0-9]+\.[a-zA-Z]+$)"
    cadena = "moises.cantillo_@dominio.com"

    #Numero de celular COLOMBIANO valido
    #ex = r"(^3[0-9]{9}$)"
    #cadena = "3000000000"

    # Fechas DD/MM/AAAA
    #ex = r"([0-2][0-9]|3[0-1])(\/|-)(0[1-9]|1[0-2])\2(\d{4})"
    #cadena = "101-11-2002"


    if re.match(ex, cadena) is None:
        print("NO es una cadena valida")
    else:
        print("Es una cadena valida")

def REFullMatch():
    exp = re.compile(r'(a|b)+')
    res = exp.fullmatch('')
    if res is None:
        print("No es una cadena valida")
    else:
        print("Es una cadena valida")

def GIC():
    try:
        g1 = """
            H -> 'while' C R 'end'
            C -> F W P | P W F | F W Q | Q W F
            F -> V L
            L -> V L | Z L | I L | 
            I -> _ M
            M -> V | Z | V M | Z M
            P -> Z P | Z
            Q -> P '.' P
            R -> R '+' S | R '-' S | S
            S -> S '*' T | S '/' T | T 
            T -> T '^' U | U
            U -> P | Q | F | '(' R ')'
            W -> '>' | '>=' | '<=' | '<' | '==' | '!='
            X -> 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z'
            Y -> 'A' | 'B' | 'C' | 'D' | 'E' | 'F' | 'G' | 'H' | 'I' | 'J' | 'K' | 'L' | 'M' | 'N' | 'O' | 'P' | 'Q' | 'R' | 'S' | 'T' | 'U' | 'V' | 'W' | 'X' | 'Y' | 'Z'
            Z -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
            V -> X | Y
            """

        grammar1 = nltk.CFG.fromstring(g1)
        oracion = "while a > 1 1 + 1 end".split()
        # guardamos todos los posibles análisis sintácticos en trees
        rdParser = nltk.ChartParser(grammar1)
        for tree in rdParser.parse(oracion):
            print(tree)
            tree.draw()
            aux = True
        if not aux:
            print("Fnished")
        else:
            print(len(rdParser.parse((oracion))))

    except Exception as e:
        print(e)
        print("Esta cadena no se encuentra en la gramatica")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    GIC()
    #REFullMatch()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
