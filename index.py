#- -*- coding: utf8; -*-
#recuperations des données (variables et fonctions)
import datas

def main():

    print("Base Converter ( x into y) (1-36)")

    print("Enter: ") 

    xBase,  yBase = datas.baseInput()

    print()
    
    while 1: 

        x = input(f" Grab world (of base {xBase}): ").upper()
        # Delete space(s)
        x = "".join( x.split() )

        if datas.itemCorrect(x, xBase):
            break
        else:
            print("Error: world syntaxe incorrect\n")
            print()

    y = datas.xToY(x, xBase, yBase)

    print()
    print(f" {x} ({xBase}) = {y} ({yBase})")

if __name__ == '__main__':
    main()
    import os; os.system('pause')
