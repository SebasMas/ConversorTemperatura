def FtoC(F):
    C = (F - 32)*(5/9)
    return C
def FtoK(F):
    K = (F-32) * (5/9) + 273.15 
    return K
def CtoF(C):
    F = (C)* (9/5) + 32 
    return F
def CtoK(C):
    K = C + 273.15
    return K
def KtoC(K):
    C = K - 273.15
    return C
def KtoF(K):
    F = (K + 273.15) * 9/5 + 32
    return F



condicion = input("Qué temperatura vas a usar?(Ej: K): ")

if condicion == "F":
    F= float(input("Ingrese la temperatura: "))
    print(F," es igual a", FtoC(F),"C")
    print(F," es igual a", FtoK(F),"K")
elif condicion == "K":
    K = float(input("Ingrese la temperatura: "))
    print(K," es igual a", KtoC(K),"C")
    print(K," es igual a", KtoF(K),"F")
elif condicion == "C":
    C = float(input("Ingrese la temperatura: "))
    print(C," es igual a", CtoF(C),"F")
    print(C," es igual a", CtoK(C),"K")
    





