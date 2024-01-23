# ||||||||||||||||||||||||||||||||||  DATI ||||||||||||||||||||||||||||||||||
"""
Dovete scegliere per l'acquisto tra due auto, una delle quali è piu efficiente dell'altra in merito al consumo di carburate, 
ma è più costosa. Sono noti il prezzo e efficienza ( in migliaia per gallone, mpg) di entrambe le vetture. 
Pianificate di usare l'auto per dieci anni, percorrendo 15000 migliaia all'anno, con un prezzo del carburante 
di 4 dollari al gallone. Quale è l'acquisto migliore?.
"""


# ||||||||||||||||||||||||||||||||||  CODE ||||||||||||||||||||||||||||||||||
# Funzione per calcolare i costi totali per un'auto in un dato periodo di tempo
def calcola_costi_totali(prezzo_auto, efficienza_auto, miglia_annue, prezzo_carburante, anni_utilizzo):
    # Calcolare le miglia totali in 10 anni
    miglia_totali = miglia_annue * anni_utilizzo
    
    # Calcolare i galloni totali utilizzati
    galloni_totali = miglia_totali / efficienza_auto
    
    # Calcolare i costi totali del carburante
    costo_carburante = galloni_totali * prezzo_carburante
    
    # Calcolare i costi totali, sommando il prezzo dell'auto e i costi del carburante
    costo_totale = prezzo_auto + costo_carburante
    
    return costo_totale

# Dati dell'auto 1
prezzo_auto_1 = 25000  # in dollari
efficienza_auto_1 = 30  # in miglia per gallone
miglia_annue = 15000  # in miglia
prezzo_carburante = 4  # in dollari per gallone
anni_utilizzo = 10  # numero di anni

# Calcolare i costi totali per l'auto 1
costo_totale_auto_1 = calcola_costi_totali(prezzo_auto_1, efficienza_auto_1, miglia_annue, prezzo_carburante, anni_utilizzo)

# Dati dell'auto 2
prezzo_auto_2 = 30000  # in dollari
efficienza_auto_2 = 25  # in miglia per gallone

# Calcolare i costi totali per l'auto 2
costo_totale_auto_2 = calcola_costi_totali(prezzo_auto_2, efficienza_auto_2, miglia_annue, prezzo_carburante, anni_utilizzo)

# Confrontare i costi totali e stampare il risultato
if costo_totale_auto_1 < costo_totale_auto_2:
    print("L'auto 1 è l'acquisto migliore.")
elif costo_totale_auto_1 > costo_totale_auto_2:
    print("L'auto 2 è l'acquisto migliore.")
else:
    print("Entrambe le auto hanno costi totali simili.")


# ||||||||||||||||||||||||||||||||||  OUTPUT ||||||||||||||||||||||||||||||||||
"""
L'auto 1 è l'acquisto migliore.

"""