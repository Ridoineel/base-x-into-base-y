from string import ascii_uppercase as as_up  
# ascii_uppercase is all upper letters "ABCD......Z"

#   CONSTANTS (Start)       #

charListe = list("0123456789" + as_up)  # ["1", "2",....., "A", ...... "Z"]

# under : charCorresp  {"0": 0 , 1":  1, .... "A":  10,  : B":  11, ...., "Z":  35} end him reverse
charCorresp = dict()

for index, el in enumerate(charListe):
  charCorresp[el] = index

charCorrespReverse = dict()

for el, index in charCorresp.items():
  charCorrespReverse[index] = el


#   CONSTANTS (End)         #

#    FUNCTIONS DECLARATION  #

def itemCorrect(mots, base):
    """ Return 
      - True if "mots" is right for "base"
      - else False 
    
    """

    correct = True

    global charListe

    valableElement = charListe[:base]

    # correct is False if one of "mot" characters not in "valableElement"
    for el in mots:
        if el not in valableElement: 
          correct = False
    
    return correct

def baseInput():

    xBase,  yBase = int(input(">> base x: ")) , int( input(">> base y: "))
    
    if (0 < xBase < 36 and 0 < yBase < 36) == False:
        print("base x or y not in range (1-35)\n") 
        return baseInput()
    
    return xBase,  yBase


def xToDec(x, xBase):
    """ return _x ( in base "xBase") to base 10_ """

    global charCorresp
      
    x = list(x)  #list of all characters of x

    x.reverse() # ex: [1, 2] into [2, 1]

    dec =0 

    for i, el in enumerate(x):

      dec += charCorresp[el]* (xBase**i)

    return dec
 

def decToY(dec, yBase):
    """ return _dec ( in base10) to base "yBase"_ """

    global charCorrespReverse
  
    y = ""
    while dec != 0:
        y = charCorrespReverse[dec % yBase] + y
        dec //= yBase
       
    return y


def xToY(x, xBase, yBase):
    """ return y of x (in base "xBase") into base "yBase """
    
    # x into base 10
    decimale = xToDec(x, xBase) 

    # Finish: "decimale" into base "yBase"
    y = decToY(decimale, yBase )
  
    return y