def map_tab( liste , fonction):
    for i in range(len(liste)) :
        liste[i]=fonction(liste[i])
    return liste

ma_liste = [ 8,1,4,6,7,9]
def ma_fonction (x):
    return 3*x+2

map_tab(ma_liste,ma_fonction)
