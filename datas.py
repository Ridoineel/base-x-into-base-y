
from string import ascii_uppercase, digits

# ["1", "2",....., "A", ...... "Z"]
charListe = list(digits + ascii_uppercase)  

# charCorresp  {"0": 0 , 1":  1, .... "A":  10,  : B":  11, ...., "Z":  35} end him reverse

charCorresp = dict()
charCorrespReverse = dict()

for index, el in enumerate(charListe):
    charCorresp[el] = index
    charCorrespReverse[index] = el

def itemCorrect(mots, base):
    """ Return 
      - True if "mots" is right for "base"
      - else False 
    
    """

    correct = True

    global charListe

    valable_elements = charListe[:base]

    # correct is False if one of "mot" characters not in "valableElement"
    for el in mots:
        if el  not in valable_elements:
            correct = False
            break
    
    return correct

def baseInput():

    xBase,  yBase = int(input(">> base x: ")) , int( input(">> base y: "))
    
    if not (0 < xBase <= 36 and 0 < yBase <= 36):
        print("base x or y not in range (1-36)\n") 
        return baseInput()
    
    return xBase,  yBase


def xToDec(x: str, xBase: int) -> int:
    """ return _x ( in base "xBase") to base 10_ """

    global charCorresp
      
    x_rev = reversed(x.upper())  #list of all characters of x in reverse form

    dec = sum(charCorresp[el] * (xBase**i) for i, el in enumerate(x_rev))

    return dec
 

def decToY(dec: int, yBase: int) -> str:
    """ return _dec ( in base10) to base {yBase}_ """

    global charCorrespReverse
  
    y = ""
    while dec != 0:
        y = charCorrespReverse[dec % yBase] + y
        dec //= yBase
       
    return y


def xToY(x: str, xBase: int, yBase: int) -> str:
    """ return y of x (in base "xBase") into base "yBase """
    
    # x into base 10
    decimale = xToDec(x, xBase) if xBase != 10 else int(x)

    # Finish: "decimale" into base "yBase"
    y = decToY(decimale, yBase ) if yBase != 10 else str(decimale)
  
    return y
