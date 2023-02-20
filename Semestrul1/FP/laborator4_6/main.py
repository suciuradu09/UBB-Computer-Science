"""
Se cere dezvoltarea unei aplicatii pentru gestiunea unui cont bancar.
Fiecare tranzactie are ziua (date), suma (float) si tipul(intrare/iesire).

Aplicatia are interfata tip consola si permite urmatoarele functionalitati:

1. Adaugare tranzactie (zi, suma, tip)
2. Actualizeaza tranzactie (zi, suma, tip)

3. Sterge cheltuielile pentru o zi specificata (se da ziua)
4. Sterge cheltuielile pentru o perioada data (se da ziua de inceput si sfarsit)
5. Sterge tranzactiile de un anumit tip

6. Tipareste tranzactiile cu sume mai mari decat o suma data
7. Tipareste tranzactiile efectualte inainte de o zi si mai mari decat o suma (se da suma si ziua)
8. Tipareste tranzactiile de un anumit tip

9. Suma totala a tranzactiilor de un anumit tip
10. Soldul contului la o data specificata
11. Tipareste tranzactiile de un anumit tip ordonate dupa suma

12. Elimina toate tranzactiile de un anumit tip
13. Elimina toate tranzactiile mai mici de o suma data care are tipul specificat

14. Reface ultima operatie

Se adauga o optiune pentru printarea listei curente
"""

from ui.console import start_2

start_2()
