# ||||||||||||||||||||||||||||||||||  DATI ||||||||||||||||||||||||||||||||||
"""
Depositare 10000 dollari in un conto bancario che fornisce il 5 per cento di interesse annuo. 
Quanti anni occorrono perché il saldo del conto arrivi al doppio del importo iniziale.
"""


# ||||||||||||||||||||||||||||||||||  CODE ||||||||||||||||||||||||||||||||||
# Definiamo una funzione per calcolare gli anni necessari per raggiungere il doppio dell'importo iniziale
def calcola_anni_doppio_saldo(importo_iniziale, tasso_interesse_annuo):
    saldo = importo_iniziale  # Inizializziamo il saldo con l'importo iniziale
    anni = 0  # Inizializziamo il contatore degli anni a 0

    # Continuiamo ad aumentare il saldo finché non raggiunge o supera il doppio dell'importo iniziale
    while saldo < 2 * importo_iniziale:
        saldo += saldo * (tasso_interesse_annuo / 100)  # Aggiorniamo il saldo applicando il tasso di interesse
        anni += 1  # Incrementiamo il contatore degli anni

    return anni  # Restituiamo il numero di anni necessari

# Impostiamo l'importo iniziale e il tasso di interesse annuo
importo_iniziale = 10000
tasso_interesse_annuo = 5

# Calcoliamo gli anni necessari utilizzando la funzione precedentemente definita
anni_necessari = calcola_anni_doppio_saldo(importo_iniziale, tasso_interesse_annuo)

# Stampiamo il risultato
print(f"Saranno necessari {anni_necessari} anni per raggiungere il doppio dell'importo iniziale.")


# ||||||||||||||||||||||||||||||||||  OUTPUT ||||||||||||||||||||||||||||||||||
"""
Saranno necessari 13 anni per raggiungere il doppio dell'importo iniziale.
"""