from termcolor import colored
from domain.transaction import get_date, get_suma, get_type, create_transaction, validate_transaction, validate_undo, \
    validate_type
from domain.bank import add_to_transactions, update_transaction, filter_list, delete_transaction, \
    search_transaction_sum, search_transaction_type, search_transaction_sum_day, sum_of_transactions_type, \
    calculate_balance, ordered_by_sum_type, delete_transaction_sum_type, find_transaction, undo
from utils.operations import refresh_history


def print_current_list(list):
    """
    Functia afiseaza tranzactiile curente
                                                                :param list: lista curenta
                                                                :type list: list
    """
    if list == []:
        print(colored('Nicio tranzactie! - Pentru a adauga selectati 1', 'yellow'))
        return
    for i, transaction in enumerate(list):
        print(i, 'Ziua: ', colored(get_date(transaction), 'blue'),
              '- Suma:', colored(get_suma(transaction), 'blue'),
              '- Tip: ', colored(get_type(transaction), 'blue'))


def add_transaction_ui(list, date, value, type):
    """
    Functia adauga o noua tranzactie la tranzactiile curente
                                                                :param list: lista de tranzactii curente
                                                                :type list: list
    """
    tran = []
    #try:
    #    t_date = int(input("Introduceti ziua: "))
    #    t_value = float(input("Introduceti suma: "))
    #    t_type = str(input("Tipul de tranzactie (Depozitare/Retragere): "))
    #except:
    #    raise ValueError(colored("Date invalide!", 'red'))
    date = int(date)
    value = float(value)
    try:
        tran = create_transaction(date, value, type)
        validate_transaction(tran)
        add_to_transactions(list, tran)
        print(colored("Tranzactie adaugata cu succes!", 'green'))
    except Exception as ve:
        print(ve)
        raise Exception(ve)


def update_transaction_ui(lista):
    """
    Functia actualizeaza o tranzactie aleasa de utilizator
                                                                :param lista: lista de tranzactii
    """
    tr1 = []
    tr2 = []
    try:
        t_date = int(input("Introduceti ziua: "))
        t_value = float(input("Introduceti suma: "))
        t_type = str(input("Tipul de tranzactie (Depozitare/Retragere): "))
        tr1 = create_transaction(t_date, t_value, t_type)  # tranzactia cautata
        validate_transaction(tr1)
        print("Introduceti noile valori pentru tranzactie: ")
        t_date_new = int(input("Introduceti ziua: "))
        t_value_new = float(input("Introduceti suma: "))
        t_type_new = str(input("Tipul de tranzactie (Depozitare/Retragere): "))
        tr2 = create_transaction(t_date_new, t_value_new, t_type_new)  # tranzactia noua
        validate_transaction(tr2)
    except Exception as ve:
        print(ve)
    if find_transaction(lista, tr1) == True:
        update_transaction(lista, tr1, tr2)
        print(colored("Actualizare reusita.", 'green'))
    else:
        print(colored("Actualizare esuata!", 'red'))


def filter_transaction_ui(lista):
    """
    Filtreaza lista in functie de un tip dat de la tastatura
                                                                    :param lista: lista de tranzactii
                                                                    :type lista: list
    """
    type_t = str(input(("Introduceti tipul(Depozitare/Retragere): ")))
    try:
        validate_type(type_t)
        filtered_list = filter_list(lista, type_t)
        print(colored("Lista filtrata: ", 'yellow'))
        print_current_list(filtered_list)
    except Exception as e:
        print(e)


def delete_transaction_type_ui(lista):
    """
       Functia sterge tranzactiile dintr-o data specificata
                                                                   :param lista: lista de tranzactii
                                                                   :type lista: list
       """
    try:
        tip = str(input("Introduceti tipul tranzactiei: "))
        delete_transaction(lista, tip, -1, get_type)
        print(colored("Stergere efectuata!", 'green'))
    except:
        print(colored("Stergere esuata!", 'red'))


def delete_transaction_day_ui(lista, day):
    """
    Functia sterge tranzactiile dintr-o data specificata
                                                                    :param lista: lista de tranzactii
                                                                    :type lista: list
    """
    day = int(day)
    try:
        delete_transaction(lista, day, -1, get_date)
        print(colored("Stergere efectuata!", 'green'))
    except:
        print(colored("Stergere esuata!", 'red'))


def delete_transaction_period_ui(lista):
    """
    Functia sterge tranzactiile dintr-o perioada data
    :param lista: lista de tranzactii
    """
    try:
        p1 = int(input("Introduceti ziua de inceput: "))
        p2 = int(input("Introduceti ziua de sfarsit: "))
        delete_transaction(lista, p1, p2, get_date)
        print(colored("Stergere efectuata!", 'green'))
    except:
        print(colored("Stergere esuata!", 'red'))


def search_transaction_sum_ui(lista):
    """
    Cauta si afiseaza tranzactiile care au suma mai mare decat suma introdusa
    de utilizator
                                                                    :param lista: lista de tranzactii
                                                                    :type lista: list of lists
    """
    sum = int(input("Introduceti suma: "))
    try:
        print_current_list(search_transaction_sum(lista, sum))
    except:
        print(colored("Nu a fost efectuata cautarea!", 'red'))


def search_transaction_sum_day_ui(lista):
    """
    Tipareste tranzactiile efectualte inainte de o zi si mai mari decat o suma
    :param lista: lista tranzactiilor
    :type lista: list
    """
    ziua = int(input("Introduceti ziua: "))
    sum = int(input("Introduceti suma: "))
    try:
        print_current_list(search_transaction_sum_day(lista, sum, ziua))
    except ValueError:
        print(colored("Nu a fost efectuata cautarea!", 'red'))


def search_transaction_type_ui(lista, type):
    """
    Tipareste tranzactiile de un anumit tip
    :type lista: list
    """
    # tipul = str(input("Introduceti tipul tranzactiei: "))
    try:
        print_current_list(search_transaction_type(lista, type))
    except ValueError:
        print(colored("Nu a fost efectuata cautarea!", 'red'))


def sum_of_transactions_type_ui(lista):
    """
    Suma tuturor tranzactiilor de un anumit tip
    :param lista: lista tranzactiilor
    :type lista: list of lists
    :return: suma tranzactiilor
    :rtype: int
    """
    tipul = str(input("Introduceti tipul: "))
    try:
        n = sum_of_transactions_type(lista, tipul)
        print("Suma tranzactiilor de tipul ", tipul, " este: ", n)
    except:
        print(colored("Nu s-a efectuat suma!", 'red'))


def calculate_balance_ui(lista):
    """
    Calculeaza soldul la o data specificata
    :param lista: lista tranzactiilor
    :type lista: list of lists
    """
    ziua = int(input("Afiseaza soldul la data: "))
    try:
        n = calculate_balance(lista, ziua)
        print("In data de", ziua, "soldul contului era: ", n)
    except:
        print(colored("Nu s-a putut calcula soldul!", 'red'))


def ordered_by_sum_type_ui(lista):
    """
    Afiseaza tranzactiile de un anumit tip ordonate dupa suma
    :param lista: lista tranzactiilor
    :type lista: list of lists
    """
    tipul = str(input("Introduceti tipul: "))
    try:
        print_current_list(ordered_by_sum_type(lista, tipul))
    except:
        print(colored("Nu s-a afisat lista ordonata.", 'red'))


def delete_transaction_sum_type_ui(lista):
    """
    Sterge tranzactiile cu o suma mai mica decat cea specificata de un anumit tip
    :param lista: lista tranzactiilor
    """
    sum = int(input("Suma: "))
    tip = str(input("Tipul tranzactiilor: "))
    try:
        delete_transaction_sum_type(lista, sum, tip)
    except:
        print(colored("Nu s-a efectuat stergerea!", 'red'))


def print_menu():
    print(colored("Adaugare de noi tranzactii", 'blue'))
    print("1. Adaugare tranzactie")
    print("2. Actualizeaza tranzactie (zi, suma, tip)")
    print(colored("Stergere", 'blue'))
    print("3. Sterge cheltuielile pentru o zi specificata (se da ziua)")
    print("4. Sterge cheltuielile pentru o perioada data (se da ziua de inceput si sfarsit)")
    print("5. Sterge tranzactiile de un anumit tip")
    print(colored("Cautari", 'blue'))
    print("6. Tipareste tranzactiile cu sume mai mari decat o suma data")
    print("7. Tipareste tranzactiile efectualte inainte de o zi si mai mari decat o suma (se da suma si ziua)")
    print("8. Tipareste tranzactiile de un anumit tip")
    print(colored("Rapoarte", 'blue'))
    print("9. Suma totala a tranzactiilor de un anumit tip")
    print("10.Soldul contului la o data specificata")
    print("11.Tipareste tranzactiile de un anumit tip ordonate dupa suma")
    print(colored("Filtrare", 'blue'))
    print("12.Elimina toate tranzactiile de un anumit tip")
    print("13.Elimina toate tranzactiile mai mici de o suma data care are tipul specificat")
    print(colored("Undo", 'blue'))
    print("14.Reface ultima operatie")
    print("S. Afiseaza lista tranzactiilor")
    print("E. Inchidere aplicatie")


def print_menu2():
    print("add <day> <sum> <type> - Add new transaction")
    print("delete <day> - Delete transaction from specified day")
    print("filter <type> - Filter specified transaction type")
    print("undo - Undo last operation")
    print("show - Show list of transactions")
    print("exit - Exit application")

def start_2():
    list_of_transactions = []
    current_list = []
    history_list = []
    finished = False
    while not finished:
        current_list = list_of_transactions[:]
        print_menu2()
        command = input("Insert command >>  ")
        option = command.split()
        if option[0] == 'add':
            try:
                add_transaction_ui(list_of_transactions, option[1], option[2], option[3])
            except:
                print(colored("Tranzactia nu s-a realizat!", 'red'))
            else:
                history_list.append(current_list)
        elif option[0] == 'delete':
            try:
                delete_transaction_day_ui(list_of_transactions, option[1])
            except:
                print(colored("Stergere esuata!", 'red'))
            else:
                history_list.append(current_list)
        elif option[0] == 'filter':
            try:
                search_transaction_type_ui(list_of_transactions, option[1])
            except:
                print(colored("Cautare esuata!", 'red'))
        elif option[0] == 'undo':
            try:
                validate_undo(history_list)
                list_of_transactions = undo(list_of_transactions, history_list)
                refresh_history(history_list)
                print(colored("Operatie de undo efectuata!", 'green'))
            except Exception:
                print(colored("Nu s-a efectuat operatia de undo", 'red'))
        elif option[0] == 'Show' or option[0] == 'show':
            print_current_list(list_of_transactions)
        elif option[0] == 'Exit' or option[0] == 'exit':
            finished = True
        else:
            print(colored("Optiune invalida!", 'red'))

def start():
    list_of_transactions = []
    current_list = []
    history_list = []
    finished = False
    while not finished:
        current_list = list_of_transactions[:]
        print_menu()
        option = input("Optiunea este: ")
        if option == '1':
            try:
                add_transaction_ui(list_of_transactions)
            except:
                print(colored("Tranzactia nu s-a realizat!", 'red'))
            else:
                history_list.append(current_list)
        elif option == '2':
            try:
                update_transaction_ui(list_of_transactions)
            except:
                print(colored("Actualizare esuata!", 'red'))
            else:
                history_list.append(current_list)
        elif option == '3':
            try:
                delete_transaction_day_ui(list_of_transactions)
            except:
                print(colored("Stergere esuata!", 'red'))
            else:
                history_list.append(current_list)
        elif option == '4':
            try:
                delete_transaction_period_ui(list_of_transactions)
            except:
                print(colored("Stergere esuata!", 'red'))
            else:
                history_list.append(current_list)
        elif option == '5':
            try:
                delete_transaction_type_ui(list_of_transactions)
            except:
                print(colored("Stergere esuata!", 'red'))
            else:
                history_list.append(current_list)
        elif option == '6':
            try:
                search_transaction_sum_ui(list_of_transactions)
            except:
                print(colored("Cautare esuata!", 'red'))
        elif option == '7':
            try:
                search_transaction_sum_day_ui(list_of_transactions)
            except:
                print(colored("Cautare esuata!", 'red'))
        elif option == '8':
            try:
                search_transaction_type_ui(list_of_transactions)
            except:
                print(colored("Cautare esuata!", 'red'))
        elif option == '9':
            try:
                sum_of_transactions_type_ui(list_of_transactions)
            except:
                print(colored("Nu s-a putut efectua suma!", 'red'))
        elif option == '10':
            try:
                calculate_balance_ui(list_of_transactions)
            except:
                print(colored("A aparut o eroare in calcularea soldului!", 'red'))
        elif option == '11':
            try:
                ordered_by_sum_type_ui(list_of_transactions)
            except:
                print(colored("Nu s-au afisat tranzactiile!", 'red'))
        elif option == '12':
            try:
                filter_transaction_ui(list_of_transactions)
            except:
                print(colored("Filtrare esuata!", 'red'))
        elif option == '13':
            try:
                delete_transaction_sum_type_ui(list_of_transactions)
                print(colored("Tranzactii eliminate!", 'green'))
            except:
                print(colored("Filtrare esuata!", 'red'))
            else:
                history_list.append(current_list)
        elif option == '14':
            try:
                validate_undo(history_list)
                list_of_transactions = undo(list_of_transactions, history_list)
                refresh_history(history_list)
                print(colored("Operatie de undo efectuata!", 'green'))
            except Exception:
                print(colored("Nu s-a efectuat operatia de undo", 'red'))
        elif option == 'S' or option == 's':
            print_current_list(list_of_transactions)
        elif option == 'E' or option == 'e':
            finished = True
        else:
            print(colored("Optiune invalida!", 'red'))
