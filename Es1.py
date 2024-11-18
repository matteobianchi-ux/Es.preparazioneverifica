print("Input: ")
fascine=int(input("Inserisci il numero di fascine acquistate "))
sacchi=int(input("Inserisci il numero di sacchi acquistati "))
bancali=int(input("Inserisci il numero di bancali acquistati "))
peso=(fascine*5)+(sacchi*20)+(bancali*50)
print(f"Il peso totale della legna è di: {peso} kg")
if(peso<100):
  print("Output: ")
  prezzo=peso*0.8
  print(f"Il prezzo della legna è di:  {prezzo} €")
else:
  print("Output: ")
  prezzo=peso*0.8
  print(f"Il prezzo della legna senza sconto è di:  {prezzo} €")
  sconto=(peso*0.8)/100*15
  print(f"Lo sconto è di: {sconto} €")
spesetrasporto=3
print(f"Le spese di trasporto sono di: {spesetrasporto} €")
prezzofinale=prezzo+spesetrasporto
print(f"Il prezzo finale su scontrino è di: {prezzofinale:.2f} €")