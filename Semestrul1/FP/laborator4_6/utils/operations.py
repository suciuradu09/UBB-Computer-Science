def list_copy(lista):
    """
    Face o copie a listei date ca parametru
    :param lista: lista care se copiaza
    :type lista: list of lists
    :return: o copie a listei
    :rtype: list (of lists)
    """
    return lista[:]


def refresh_history(istoric):
    """
    Functia sterge ultima lista din istoric
    :param istoric: lista de istoric
    :type istoric: list of lists
    """
    istoric.pop(-1)

def test_list_copy():
    test_list = [[1, 2, 'Retragere'], [5, 71, 'Depozitare'], [10, 90.92, 'Retragere']]
    assert(test_list == list_copy(test_list))