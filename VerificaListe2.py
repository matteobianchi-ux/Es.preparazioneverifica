citta=["milano","roma","napoli"]
tmax=[28,31,34]
tmin=[18,21,24]
somma=0
somma2=0
min=tmin[0]
max=tmax[0]
minc=citta[0]
maxc=citta[0]
for i in range(len(tmin)):
    somma+=tmin[i]
    somma2+=tmax[i]
media=somma/len(tmin)
media2=somma2/len(tmax)
print(f"La media delle temperature minime è: {media}")
print(f"La media delle temperature massime è: {media2}")
citta2=[]
for i in range(len(tmin)):
    if(tmin[i]<media):
        citta2.append(citta[i])
print(f"Le città che hanno riportato una temperatura inferiore rispetto alla media sono: {citta2}")
c=str(input("Inserisci il nome di una città"))
boolean=False
for i in range(len(citta)):
    if(c==citta[i]):
        boolean=True
        break
    else:
        boolean=False
if(boolean):
    print(f"{c} è presente nell'array")
else:
    print(f"{c} non è presente nell'array")
for i in range(1, len(tmin)):
    if(tmin[i]<min):
        minc=citta[i]
    if(tmax[i]>max):
        maxc=citta[i]
print(f"La città più calda é: {maxc}")
print(f"La città più fredda é: {minc}")