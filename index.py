#- -*- coding: utf8; -*-
#recuperations des données (variables et fonctions)
import datas

def main():

    print("CONVERTISSEUR DE BASE X ( 1-35) EN BASE Y (1-35)\n")

    print("Saisir ") 

    xBase,  yBase = int(input(">> base x: ")) , int( input(">> base y: "))

    print()
    
    while 1: 
        """ Tant que les caracteres du mots ne correspondantent
        pas a la base...""" 

        x = input("Saisir le mots en base x: ").upper()
        # Eliminer les espaces s'il y a dans x
        x = "".join( x.split(" ") )

        if datas.itemCorrect(x, xBase):
            break
        else:
            print("Le mot est mal ecrit dans sa base\n")
            print()

    y = datas.xToY(x, xBase, yBase)

    print()
    print(f" {x} ({xBase}) = {y} ({yBase})")

if __name__ == '__main__':
    main()
    import os; os.system('pause')