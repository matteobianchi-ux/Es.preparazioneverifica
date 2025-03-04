oreP = [10,11,13,15,17]
oreA = [12,14,16,18,20]
destinazioni = ["Roma", "Milano", "Torino", "Napoli", "Firenze"]
citta=str(input("Inserisci una città "))
boolean=False
indice=0
for i in range(len(oreP)):
    if(citta==destinazioni[i]):
        boolean=True
        indice=i
        break
if(boolean):
  print(f"Gli orari di partenza sono: {oreP[indice]}")
else:
  print("Città non valida")
intervallo1=int(input("Inserisci un orario "))
intervallo2=int(input("Inserisci un altro orario "))
for i in range(len(oreP)):
    if(oreP[i]>=intervallo1 and oreP[i]<=intervallo2):
        durata=oreA[i]-oreP[i]
        print(f"La corsa per {destinazioni[i]} parte alle ore: {oreP[i]} e arriva alle ore: {oreA[i]}, per una durata di: {durata} ore")

