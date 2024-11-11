from collections import Counter  # https://docs.python.org/3/library/collections.html
import random

class MAnSPANZUR:
    def __init__(self, cuvant):
        self.cuvant = cuvant
        self.ghici = set()
        self.inc = 32 #alfabetul ro are 31 de litere -inc-incercari

    def cauta_lit(self, lit):
        if lit in self.ghici:
            return False
        self.ghici.add(lit)
        if lit not in self.cuvant:
            self.inc = self.inc - 1
        return True

    def terminat(self):
        return all(lit in self.ghici for lit in self.cuvant)

##################################################################clasa-hangman
def cuv_fiser(filename):
    cuvs = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split(';')
                if len(parts) == 3:
                    pattern, cuv = parts[1], parts[2]
                    cuvs[pattern] = cuv
    return cuvs

def frecventa(lista_cuv, ghicit_litere):
    cuv_ramas = [cuv for cuv in lista_cuv.values() if not any(lit in cuv for lit in ghicit_litere)]
    lit_counts = Counter()

    for cuv in cuv_ramas:
        for lit in set(cuv):
            if lit not in ghicit_litere:
                lit_counts[lit] += 1

    return lit_counts.most_common()
########################################
def joc(lista_cuv):
    incercari_totale = 0 #counter pt litere incercate
    items = list(lista_cuv.items())
    random.shuffle(items) #random
    print(items) #doar sa vad ca functineaza

    for pattern, cuv in items:
        game = MAnSPANZUR(cuv)

        while not game.terminat():
            lit_freq = frecventa(lista_cuv, game.ghici)
            if not lit_freq:
                break
            next_lit = lit_freq[0][0]
            game.cauta_lit(next_lit)
            incercari_totale += 1

    print(f"S-a realizat : {incercari_totale} de incercari")
    print(" ________\n" 
          "/       |\n"
     "|     (x_x) \n"
     "|      \|/ \n"
     "|       | \n"
     "|      / \ \n"
     "| \n"
  "|______________ \n")


##################################################################run-u
filename = 'cuvinte_de_verificat.txt'
lista_cuv = cuv_fiser(filename)
joc(lista_cuv)
