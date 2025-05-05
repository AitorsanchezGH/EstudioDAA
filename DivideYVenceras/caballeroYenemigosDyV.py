
def DyV (enemigos, ini, fin, miFuerza):
    if(ini==fin):
        if(enemigos[ini]<=miFuerza):
            return ini
        else:
            return -1
    else:
        mitad = (ini+fin)//2
        if (enemigos[mitad]>miFuerza):
            return DyV(enemigos, ini, mitad, miFuerza)
        else:
            pos = DyV(enemigos,mitad+1,fin, miFuerza)
            if(pos==-1):
                return mitad
            else:
                return pos

nEnemigos=7
enemigos=[1,2,3,4,5,6,7]
miFuerza=3
ultimoIndiceAlQueGanamos= DyV (enemigos, 0, len(enemigos)-1, miFuerza)
print("Ganamos a", ultimoIndiceAlQueGanamos+1, "personajes")