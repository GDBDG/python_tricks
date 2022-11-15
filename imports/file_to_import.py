"""
Constantes à importer dans le main, pour étudier leur comportement dans les imports
"""

INT_CONST = 1
# Les 256 entiers ne sont pas gérés pareil en mémoire
INT_CONST_2 = 300
INT_CONST_3 = 3
INT_CONST_4 = 400
TAB_CONST_1 = [3]
TAB_CONST_2 = ["toto"]

print("Value initiale")
print(f"Value INT_CONST : {INT_CONST}, ID INT_CONST : {id(INT_CONST)}")
print(f"Value INT_CONST2 : {INT_CONST_2}, ID INT_CONST2 : {id(INT_CONST_2)}")
print(f"Value INT_CONST : {INT_CONST_3}, ID INT_CONST : {id(INT_CONST_3)}")
print(f"Value INT_CONST2 : {INT_CONST_4}, ID INT_CONST2 : {id(INT_CONST_4)}")
print(f"Value TAB_CONST : {TAB_CONST_1},  ID TAB_CONST : {id(TAB_CONST_1)}")
print(f"Value TAB_CONST : {TAB_CONST_2},  ID TAB_CONST : {id(TAB_CONST_2)}\n")


def print_state():
    print(f"Value INT_CONST : {INT_CONST}, ID INT_CONST : {id(INT_CONST)}")
    print(f"Value INT_CONST2 : {INT_CONST_2}, ID INT_CONST2 : {id(INT_CONST_2)}")
    print(f"Value INT_CONST : {INT_CONST_3}, ID INT_CONST : {id(INT_CONST_3)}")
    print(f"Value INT_CONST2 : {INT_CONST_4}, ID INT_CONST2 : {id(INT_CONST_4)}")
    print(f"Value TAB_CONST : {TAB_CONST_1},  ID TAB_CONST : {id(TAB_CONST_1)}")
    print(f"Value TAB_CONST : {TAB_CONST_2},  ID TAB_CONST : {id(TAB_CONST_2)}\n")


def change_state():
    global INT_CONST, INT_CONST_2, INT_CONST_3, INT_CONST_4, TAB_CONST_1, TAB_CONST_2
    INT_CONST = 2
    INT_CONST_2 = 301
    INT_CONST_3 += 1
    INT_CONST_4 += 1
    TAB_CONST_1.append(5)
    TAB_CONST_2 = ["tititi"]
    print("Value après modif")
    print_state()
