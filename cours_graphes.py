import random
from pprint import pprint

class Graphes(object):
    """docstring for Graphes"""
    def __init__(self, __l_adj = None):
        self.__l_adj = __l_adj

    def arret(self, liste, s):
        for item in liste:
            if item[-1] is not s:
                return False
        return True

    def __str__(self):
        return str(self.__l_adj)

    def adjs(self, a):
        if self.__l_adj is not None:
            if a in self.__l_adj:
                return self.__l_adj[a]
        return []

    def est_adjs(self, a, b):
        return (b in self.__l_adj(a))

    def liste_adja(self):
        return self.__l_adj

    def sommets(self):
        if self.__l_adj is None:
            return []

        else:
            t = list(self.__l_adj.keys())
            t.sort()
            return t

    def nm_sommets(self):
        return len(self.sommets())

    def degre(self):
        return len(self.__l_adj)

    def comp_connex(self,s):
        p = [ ] # p liste vide
        if s in self.sommets(): # si s fait partie des sommets
            q = [] # q liste vide
            q.append(s) # on ajoute s à q
            vus = [] # vus liste vide
            vus.append(s) # on ajoute s à vus
            while len(vus) > 0: # tant que q n"est pas vide
                print("len(q)", len(q))
                x = q.pop() # on retire le premier élément de q noté x
                p.append(x) # on met x dans p
                for t in self.adjs(x): # pour t panni les adjacents du sommet visité
                    if t not in vus: # sitn"estpas dans vus
                        q.append(t)
                        vus.append(t)
        p.sort()
        return p

    def comp(self):
        c = []
        for s in self.sommets():
            t = self.comp_connex(s)
            t.sort()
            if t not in c:
                c.append(t)
        return c

    def liaison(self, a, b):
        return (b in self.comp_connex(a))

    def chaines(self, a, b):
        chai = []
        chai.append([a])
        while not self.arret(chai, b):
            q = []
            for p in chai:
                u = p[-1]
                if u == b:
                    q.append(p)
            else:
                s = self.adjs(u)
                for t in s:
                    if not (t in p):
                        v = [i for i in p]
                        v.append(t)
                        q.append(v)
            chai = q
        return chai

    def re_chai(self, a, b):
        p = []
        if a != b and self.liaison(a, b):
            p = self.chaines(a, b)

        return p

    def re_cycl(self, a):
        p = []
        c = self.adjs(a)
        for s in c:
            t = self.re_chai(s, a)
            for k in t:
                u = [a]
                for v in k:
                    u.append(v)
                if len(u) < 3:
                    p.append(u)
        return p

    def degre_sommet(self, a):
        deg = 0
        if self.__l_adj is not None:
            if a in self.__l_adj:
                deg = len(self.__l_adj[a])
        return deg

    def ex_ch_eu(self):
        som_deg_impair = 0
        for s in self.sommet():
            if self.degre_sommet(s) % 2 == 1:
                som_deg_impair += 1
        return (som_deg_impair == 0 or som_deg_impair == 2)

    def ex_cy_eu(self):
        som_deg_impair = 0
        for s in self.sommet():
            if self.degre_sommet(s) % 2 == 1:
                som_deg_impair += 1
        return (som_deg_impair)

    def nb_aretes(self):
        n = 0
        for s in self.sommets():
            n += len(self.adjs(s))
        return (n/2)

    def graphe_reduit(self, a, b):
        h = dict()
        for s in self.sommets():
            l = []
            for t in self.adjs(s):
                if (s != a or t != b) and (t != a or s != b):
                    l.append(t)
            if len(l) != 0:
                h[s] = l
        return Graphes(h)

    def pont(self, a, b):
        if not (b in self.adjs(a)):
            return False
        r = self.graphe_reduit(a, b)
        return (len(r.comp()) != 0)

    def rech_Euler(self):
        fin = self.nb_aretes() == 1
        if fin:
            return self.sommets()
        p = []
        choix = []
        for s in self.sommets():
            if self.degre_sommet(s) % 2 == 1:
                choix.append(s)
        if len(choix) == 0:
            choix = self.sommets()
        a = choix[random.randrange(0, len(choix))]
        while not fin:
            u = self.adjs(a)
            v = []
            for s in u:
                if not self.pont(a, s) and len(self.liste_adja()[s]) != 1:
                    v.append(s)
            b = v[random.randrange(0, len(v))]
            p.append(a)
            self = self.graphe_reduit(a, b)
            a = b
            fin = (self.nb_aretes() == 1)
        p.append(a)
        p.append(self.adjs(a)[0])

        return p


dicti1 =  {"A": ["G", "H"], "B": ["L", "K"], "C": ["J", "I"], "D": ["K", "J"], "E": ["L", "G"], "F": ["H", "I"], "G": ["A", "E", "L", "H"], "H": ["A", "F", "I", "G"], "I": ["F", "C", "J", "H"], "J": ["D", "C", "K", "I"], "K": ["B", "D", "L", "J"], "L": ["E", "B", "G", "K"]}
dicti2 = {"A": ["G", "H"], "B": ["L", "K"], "C": ["J", "I"], "D": ["K", "J"], "E": ["L", "G"], "F": ["H", "I"], "G": ["A", "E", "L", "H"], "H": ["A", "F", "I", "G", "K"], "I": ["F", "C", "J", "H"], "J": ["D", "C", "K", "I"], "K": ["B", "D", "L", "J", "H"], "L": ["E", "B", "G", "K"]}
dicti3 = {"A": ["G", "H"], "B": ["L", "K"], "C": ["J", "I"], "D": ["K", "J"], "E": ["L", "G"], "F": ["H", "I"], "G": ["A", "E", "L", "H", "J"], "H": ["A", "F", "I", "G", "K"], "I": ["F", "C", "J", "H"], "J": ["D", "C", "K", "I", "G"], "K": ["B", "D", "L", "J", "H"], "L": ["E", "B", "G", "K"]}
dicti4 = {"A": ["G", "H"], "B": ["L", "K"], "C": ["J", "I"], "D": ["K", "J"], "E": ["L", "G"], "F": ["H", "I"], "M": ["N", "O"], "O": ["M", "N"], "N": ["M", "O"], "G": ["A", "E", "L", "H"], "H": ["A", "F", "I", "G"], "I": ["F", "C", "J", "H"], "J": ["D", "C", "K", "I"], "K": ["B", "D", "L", "J"], "L": ["E", "B", "G", "K"]}
pprint(dicti1)
pprint(dicti2)
pprint(dicti3)
pprint(dicti4)
g1 = Graphes(dicti1)
print(g1.rech_Euler())