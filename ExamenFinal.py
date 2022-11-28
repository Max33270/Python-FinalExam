# Dans cet exercice, vous allez coder des fonctions.
# Des tests sont fournis, vous disant si votre code
# fonctionne correctement.
#
# Il y a 20 tests, chacun étant sur 1 point.
# Il y a une question bonus, avec un 21ème test.
#
# Vous pouvez utiliser print pour vous aider à débugger,
# car sys.stdout est ignoré par les tests.

# Ignorez ces deux lignes, elles servent pour la fin
# du programme.

import hashlib
import unittest

# Définir une fonction nommée count_ones.
# Elle prend un paramètre :
#  * un nombre binaire sous forme de chaine
#    de caractères composée uniquement de
#    1 et de 0
#
# Cette fonction doit renvoyer le nombre de
# 1 présents dans le nombre binaire passé en
# paramètre.

def count_ones(myBin): 
    counter = 0
    for _ in range(len(myBin)): 
        counter = myBin.count("1")
    return counter 

# Définir une fonction nommée invert_bit.
# Elle prend un paramètre :
#  * un nombre binaire sous forme de chaine
#    de caractère composée uniquement de
#    1 et de 0. Cette chaine représente
#    un bit, et est donc de longeur 1.
#
# Cette fonction doit inverser le bit :
#  * Si la chaine vaut '0', il faut retourner '1'.
#  * Si la chaine vaut '1', il faut retourner '0'

def invert_bit(myBin): 
    if myBin == '0': 
        myBin = '1' 
    elif myBin == '1': 
        myBin = '0'
    return myBin

# Définir une fonction nommée index_of_last_one.
# Elle prend un paramètre :
#  * un nombre binaire sous forme de chaine
#    de caractères composée uniquement de
#    1 et de 0
#
# Cette fonction doit renvoyer l'index du dernier bit à 1,
# c'est à dire la position du bit à 1 le plus à
# droite. Il est évident que les index commencent
# à 0.

def index_of_last_one(myBin): 
    lastIndex = 0
    for _ in range(len(myBin)):  
        lastIndex = myBin.rfind("1")
    return lastIndex 

# Définir une fonction nommée invert_bit_n.
# Elle prend deux paramètres :
#  * un nombre binaire sous forme de chaine
#    de caractères composée uniquement de
#    1 et de 0
#  * un entier l'index du bit à inverser
#
# Cette fonction doit renvoyer le nombre
# fourni, mais dans lequel le bit à l'index
# fourni a été inversé.

def invert_bit_n(myBin, myInt): 

    newList = list(myBin)
    if newList[myInt] == '0': 
        newList[myInt] = '1'
    else : 
        newList[myInt] = '0'
    return "".join(newList)

# Définir une fonction nommée result.
# Elle prend deux paramètres :
#  * un nombre binaire sous forme de chaine
#    de caractères composée uniquement de
#    1 et de 0
#  * un entier représentant le nombre d'étapes
#
# Cette fonction renvoie une liste, contenant
# n éléments, n étant le nombre d'étapes.
#
# Le premier élément de la liste est le nombre
# binaire passé en paramètre de la fonction.
#
# Chaque élément suivant dans la liste est
# ensuite calculé à partir du précédent.
#
# Lorsqu'il y a un nombre pair de 1 dans le nombre
# précédent, on inverse le dernier bit (celui de
# droite).
#
# Lorsqu'il y a un nombre impair de 1 dans le
# nombre précédent, on inverse le bit directement à
# gauche du 1 le plus à droite.
#
# Ce nouveau nombre est ajouté dans la liste
# des résultats.

        
def index_of_first_one(myBin): 
    lastIndex = 0
    for _ in range(len(myBin)):  
        lastIndex = myBin.rfind("1")
    return lastIndex 

def result(myBin, stepNum):
    myList = [] 
    myList.append(myBin)
    for i in range(stepNum-1):
        currentBinary = myList[i]
        newBinary = ""
        if currentBinary.count('1') % 2 == 0 :
            newBinary = invert_bit_n(currentBinary,-1)
        else : 
            newBinary = invert_bit_n(currentBinary,index_of_last_one(currentBinary)-1)
        myList.append(newBinary)
    return myList


# Définir une fonction nommée bonus.
# Cette fonction renvoie une chaine de caractères.
# Cette chaine de caractères doit contenir le
# nom du codage que nous venons de réaliser.
# Ce codage a été breveté il y a longtemps et
# il a un énorme avantage que je vous expliquerai
# plus tard.

def bonus(): 
    return "gray"


################################################################
################################################################
# La suite du programme est là pour tester ce que vous faites. #
# Vous n'avez pas à y toucher, et vous n'êtes pas obligés de   #
# la lire.                                                     #
################################################################
################################################################


class TestCountOnes(unittest.TestCase):
    def test_zero_bit_set_to_one(self):
        self.assertEqual(count_ones("0000"), 0)

    def test_one_bit_set_to_one(self):
        self.assertEqual(count_ones("001000"), 1)

    def test_two_bits_set_to_one(self):
        self.assertEqual(count_ones("0010001000"), 2)

    def test_three_bits_set_to_one(self):
        self.assertEqual(count_ones("00100010001"), 3)

    def test_four_bits_set_to_one(self):
        self.assertEqual(count_ones("100100010001"), 4)


class TestInvertBit(unittest.TestCase):
    def test_invert_zero(self):
        self.assertEqual(invert_bit("0"), "1")

    def test_invert_one(self):
        self.assertEqual(invert_bit("1"), "0")


class TestIndexOfLastOne(unittest.TestCase):
    def test_first_bit(self):
        self.assertEqual(index_of_last_one("1000000"), 0)

    def test_last_bit(self):
        self.assertEqual(index_of_last_one("00001"), 4)

    def test_middle_bit(self):
        self.assertEqual(index_of_last_one("0000100"), 4)

    def test_two_bits(self):
        self.assertEqual(index_of_last_one("0000100100"), 7)


class TestInvertBitN(unittest.TestCase):
    def test_invert_zero(self):
        self.assertEqual(invert_bit_n("0", 0), "1")

    def test_invert_one(self):
        self.assertEqual(invert_bit_n("1", 0), "0")

    def test_invert_first(self):
        self.assertEqual(invert_bit_n("01", 0), "11")

    def test_invert_last(self):
        self.assertEqual(invert_bit_n("01", 1), "00")

    def test_invert_middle(self):
        self.assertEqual(invert_bit_n("010", 1), "000")

    def test_invert_middle_2(self):
        self.assertEqual(invert_bit_n("00010", 1), "01010")


class TestResult(unittest.TestCase):
    @staticmethod
    def secret(a, b=0):
        a += b
        a ^= a >> 1
        return bin(a)[2:]

    def test_nb_steps(self):
        for nb_steps in range(3, 10):
            res = result("000" * (nb_steps // 2), nb_steps)
            self.assertEqual(len(res), nb_steps)

    def test_0000_16(self):
        res = result("0000", 16)
        for index in range(16):
            self.assertEqual(self.secret(index).zfill(4), res[index])

    def test_0000000_20(self):
        res = result("0000101", 20)
        for index in range(20):
            self.assertEqual(self.secret(index, 6).zfill(7), res[index])


class TestBonus(unittest.TestCase):
    def test_bonus(self):
        answer = bonus()
        answer = answer.strip().lower()
        self.assertEqual(
            len(answer), 4, "la réponse attendue fait 4 caractères"
        )
        hash = hashlib.sha256(answer.encode("utf-8")).hexdigest()
        hash = hashlib.sha256(hash.encode("utf-8")).hexdigest()
        self.assertEqual(
            hash,
            "bc06f3cf61dd436b8837fd63dbd17173a2347a5d109985e323d3cd65f5505f0a",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
