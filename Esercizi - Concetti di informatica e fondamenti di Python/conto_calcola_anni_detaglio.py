# ||||||||||||||||||||||||||||||||||  DATI ||||||||||||||||||||||||||||||||||
"""
Depositare 10000 dollari in un conto bancario che fornisce il 5 per cento di interesse annuo. 
Quanti anni occorrono perché il saldo del conto arrivi al doppio del importo iniziale.
"""


# ||||||||||||||||||||||||||||||||||  CODE ||||||||||||||||||||||||||||||||||
# Definiamo una funzione per calcolare gli anni necessari per raggiungere il doppio dell'importo iniziale
def calcola_anni_doppio_saldo(importo_iniziale, tasso_interesse_annuo):
    saldo = importo_iniziale
    anni = 0

    # Lista per memorizzare i dati per ogni anno
    dati_per_anni = []

    while saldo < 2 * importo_iniziale:
        interessi = saldo * (tasso_interesse_annuo / 100)
        saldo += interessi
        anni += 1

        # Aggiungiamo i dati per l'anno corrente alla lista
        dati_per_anni.append((anni, interessi, saldo))

    return dati_per_anni

# Impostiamo l'importo iniziale e il tasso di interesse annuo
importo_iniziale = 10000
tasso_interesse_annuo = 5

# Calcoliamo gli anni necessari e otteniamo i dati per ogni anno
dati_anni = calcola_anni_doppio_saldo(importo_iniziale, tasso_interesse_annuo)

# Stampiamo i dati per ogni anno in tre colonne
print("Anno\tInteressi\tSaldo")
for anno, interessi, saldo in dati_anni:
    print(f"{anno}\t{interessi:.2f}\t\t{saldo:.2f}")




# ||||||||||||||||||||||||||||||||||  OUTPUT ||||||||||||||||||||||||||||||||||
"""
Anno    Interessi       Saldo
1       500.00          10500.00
2       525.00          11025.00
3       551.25          11576.25
4       578.81          12155.06
5       607.75          12762.82
6       638.14          13400.96
7       670.05          14071.00
8       703.55          14774.55
9       738.73          15513.28
10      775.66          16288.95
11      814.45          17103.39
12      855.17          17958.56
13      897.93          18856.49
14      942.82          19799.32
15      989.97          20789.28

"""