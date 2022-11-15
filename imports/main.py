"""
Tests des comportements d'imports
"""


def imports_from():
    print("Test en imports from")
    from imports.file_to_import import change_state
    from imports.file_to_import import INT_CONST, INT_CONST_2, TAB_CONST_1, TAB_CONST_2, INT_CONST_3,INT_CONST_4
    change_state()
    print("Etat des valeur importées après modif")
    print(f"Value INT_CONST : {INT_CONST}, ID INT_CONST : {id(INT_CONST)}")
    print(f"Value INT_CONST2 : {INT_CONST_2}, ID INT_CONST2 : {id(INT_CONST_2)}")
    print(f"Value INT_CONST : {INT_CONST_3}, ID INT_CONST : {id(INT_CONST_3)}")
    print(f"Value INT_CONST2 : {INT_CONST_4}, ID INT_CONST2 : {id(INT_CONST_4)}")
    print(f"Value TAB_CONST : {TAB_CONST_1},  ID TAB_CONST : {id(TAB_CONST_1)}")
    print(f"Value TAB_CONST : {TAB_CONST_2},  ID TAB_CONST : {id(TAB_CONST_2)}\n")
    """
    Conclusion : via un import en from, çà copie l'adress mémoire.
    En cas de réaffectation de variable, la variable dans le fichier initial change d'adress,
    Mais dans le fichier qui importe, il reste sur la première adresse.
    Dans le cas d'un append, comme l'adresse ne change pas, çà prend bien en compte les modifs.
    """


def imports_simple():
    print("Tests en imports simples")
    import file_to_import as fi
    fi.change_state()
    print("Etat des valeur importées après modif")
    print(f"Value INT_CONST : {fi.INT_CONST}, ID INT_CONST : {id(fi.INT_CONST)}")
    print(f"Value INT_CONST2 : {fi.INT_CONST_2}, ID INT_CONST2 : {id(fi.INT_CONST_2)}")
    print(f"Value INT_CONST : {fi.INT_CONST_3}, ID INT_CONST : {id(fi.INT_CONST_3)}")
    print(f"Value INT_CONST2 : {fi.INT_CONST_4}, ID INT_CONST2 : {id(fi.INT_CONST_4)}")
    print(f"Value TAB_CONST : {fi.TAB_CONST_1},  ID TAB_CONST : {id(fi.TAB_CONST_1)}")
    print(f"Value TAB_CONST : {fi.TAB_CONST_2},  ID TAB_CONST : {id(fi.TAB_CONST_2)}\n")
    """
    Comportement différent, en cas de modif dans le fichier original, la modif est prise en compte dans 
    le fichier qui importe
    """

def imports_mixes1():
    print("Tests en imports mixes1")
    import file_to_import as fi
    from imports.file_to_import import change_state
    change_state()
    print("Etat des valeur importées après modif")
    print(f"Value INT_CONST : {fi.INT_CONST}, ID INT_CONST : {id(fi.INT_CONST)}")
    print(f"Value INT_CONST2 : {fi.INT_CONST_2}, ID INT_CONST2 : {id(fi.INT_CONST_2)}")
    print(f"Value INT_CONST : {fi.INT_CONST_3}, ID INT_CONST : {id(fi.INT_CONST_3)}")
    print(f"Value INT_CONST2 : {fi.INT_CONST_4}, ID INT_CONST2 : {id(fi.INT_CONST_4)}")
    print(f"Value TAB_CONST : {fi.TAB_CONST_1},  ID TAB_CONST : {id(fi.TAB_CONST_1)}")
    print(f"Value TAB_CONST : {fi.TAB_CONST_2},  ID TAB_CONST : {id(fi.TAB_CONST_2)}\n")

def imports_partout():
    print("imports dans tous les sens")
    import file_to_import as fi
    print("premier import")
    print(f"Value INT_CONST : {fi.INT_CONST}, ID INT_CONST : {id(fi.INT_CONST)}")
    print(f"Value INT_CONST2 : {fi.INT_CONST_2}, ID INT_CONST2 : {id(fi.INT_CONST_2)}\n")
    from imports.file_to_import import change_state, print_state
    print("deuxieme import")
    print(f"Value INT_CONST : {fi.INT_CONST}, ID INT_CONST : {id(fi.INT_CONST)}")
    print(f"Value INT_CONST2 : {fi.INT_CONST_2}, ID INT_CONST2 : {id(fi.INT_CONST_2)}\n")
    import file_to_import as fi
    # Cet import ne change rien, çà vaut la même chose qu'au premier, mais pas ce qui est dans le fichier
    # a cet instant
    print("troisième import")
    print(f"Value INT_CONST : {fi.INT_CONST}, ID INT_CONST : {id(fi.INT_CONST)}")
    print(f"Value INT_CONST2 : {fi.INT_CONST_2}, ID INT_CONST2 : {id(fi.INT_CONST_2)}\n")
    print_state()
    change_state()
    print("Etat des valeur importées après modif")
    print(f"Value INT_CONST : {fi.INT_CONST}, ID INT_CONST : {id(fi.INT_CONST)}")
    print(f"Value INT_CONST2 : {fi.INT_CONST_2}, ID INT_CONST2 : {id(fi.INT_CONST_2)}\n")


if __name__ == '__main__':
    # imports_from()
    # imports_simple()
    # imports_mixes1()
    imports_partout()