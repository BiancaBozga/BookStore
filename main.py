# This is a sample Python script.
import random
import time
from cmath import sqrt


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class Punct:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def afiseaza_ultim_cuvant(sir):
    if sir=="":
        return ""
    words = sir.split()
    words.sort(reverse=True)
    return words[0]
def distanta_euclidiana(p1,p2):
    a=pow(p2.y-p1.y,2)
    b=pow(p2.x-p1.x,2)
    distanta=sqrt(a+b).real
    return distanta
def produs_scalar_vectori(v1,v2):
    l=len(v1)
    i=0
    s=0
    while(i<l):
        s=s+v1[i]*v2[i]
        i=i+1
    return s
def determina_singura_aparitie(sir):
    words = sir.split()
    rez_inter={}
    rez_final=[]
    for word in words:

        current_count = rez_inter.get(word, 0)
        rez_inter[word] = current_count + 1
    for word, count in rez_inter.items():
        if count == 1:
            rez_final.append(word)
    return rez_final
def cuvinte_unice_Chatgpt(text):
    #CHATGPT
    cuvinte = text.split()
    frecventa_cuvinte = {}

    # Calculează frecvența cuvintelor
    for cuvant in cuvinte:
        cuvant = cuvant.lower()  # Converteste cuvintele la minuscule pentru a evita diferențele de majuscule/minuscule
        frecventa_cuvinte[cuvant] = frecventa_cuvinte.get(cuvant, 0) + 1

    # Selectează cuvintele care apar o singură dată
    cuvinte_unice = [cuvant for cuvant, frecventa in frecventa_cuvinte.items() if frecventa == 1]

    return cuvinte_unice
def val_repeta(sir,n):

    dict = {key: 0 for key in range(1, n)}



    for i in range (0,len(sir)):
        dict[sir[i]]+=1
        if(dict[sir[i]]>1):
            return sir[i]
def elem_majoritar(v):

    frecventa = {}

    for num in v:
        if num in frecventa:
            frecventa[num] += 1
        else:
            frecventa[num] = 1

    for num, aparitii in frecventa.items():
        if aparitii > len(v) // 2:
            return num

    return None
def gaseste_element_majoritar_CHATGPT(nums):
    #CHATGPT
    majoritar = None
    contor = 0

    for num in nums:
        if contor == 0:
            majoritar = num
            contor = 1
        elif num == majoritar:
            contor += 1
        else:
            contor -= 1

    # Verificare dacă elementul găsit este majoritar
    contor = 0
    for num in nums:
        if num == majoritar:
            contor += 1

    if contor > len(nums) // 2:
        return majoritar
    else:
        return None
def al_k_cel_mai_mare(v,k):
    v.sort(reverse=True)

    return v[k-1]
def baza2(n):

    v=[]
    for i in range(1, n + 1):
        str = ""
        temp = i
        # Convert decimal number to binary number
        while temp:
            if temp & 1:
                str = "1" + str
            else:
                str = "0" + str
            temp >>= 1  # Right shift the bits of temp by 1 position
        v.append(str)
    return v
def int_to_binary(num):
    #CHATGPT
    if num == 0:
        return '0'

    binary_representation = ''
    while num > 0:
        remainder = num % 2
        binary_representation = str(remainder) + binary_representation
        num //= 2

    return binary_representation



def baza2_chatgpt(n):
    #CHATGPT
    v=[]
    for i in range(1, n + 1):
        v.append(int_to_binary(i))
    return v
def teste():
    #teste prima cerinta
    assert (afiseaza_ultim_cuvant("Ana are mere") == "mere")
    assert(afiseaza_ultim_cuvant("ultima zi")=="zi")
    assert(afiseaza_ultim_cuvant("")=="")
    #test a doua cerinta
    punct1 = Punct(1, 5)
    punct2 = Punct(4, 1)
    assert (distanta_euclidiana(punct1, punct2) == 5.0)
    punct1 = Punct(1, 1)
    punct2 = Punct(2, 2)
    assert (distanta_euclidiana(punct1, punct2) == sqrt(2).real)
    punct1 = Punct(5, 7)
    punct2 = Punct(4, 4)
    assert (distanta_euclidiana(punct1, punct2) == sqrt(10).real)
    #teste cerinta 3
    v1 = [1, 0, 2, 0, 3]
    v2 = [1, 2, 0, 3, 1]
    assert (produs_scalar_vectori(v1, v2) == 4)
    v1 = [1, 0, 3,0]
    v2 = [4, 5, 6,7]
    assert (produs_scalar_vectori(v1, v2) == 22)
    v3 = [-1, 0, 1]
    v4 = [2, -2, 1]
    assert (produs_scalar_vectori(v3, v4) == -1)
    #teste cerinta 4
    assert (determina_singura_aparitie("ana are ana mere") == ['are', 'mere'])
    assert (determina_singura_aparitie("ana are  mere") == ['ana','are', 'mere'])
    assert (determina_singura_aparitie("ana are ana mere mere are ") == [])
    #teste cerinta 5
    assert (val_repeta([1, 2, 3, 4, 2], 5) == 2)
    assert (val_repeta([1, 2, 3, 4,7,7], 8) == 7)
    assert (val_repeta([1, 2, 3, 4, 5,5], 6) == 5)
    #teste cerinta 6

    assert(elem_majoritar([2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2])==2)
    assert(elem_majoritar([2, 3,4,5])==None)
    assert(elem_majoritar([2,2,3,3])==None)
    assert(elem_majoritar([2, 2,3])==2)
    #teste cerinta 7
    assert(al_k_cel_mai_mare([1,2,4,5],2)==4)
    assert (al_k_cel_mai_mare([1, 2, 4, 5], 1) == 5)
    assert (al_k_cel_mai_mare([1, 2, 4, 5], 3) == 2)
    assert (al_k_cel_mai_mare([1, 2, 4, 5], 4) == 1)
    #teste cerinta 8
    assert (baza2(4) == ['1', '10', '11', '100'])
    assert (baza2(5) == ['1', '10', '11', '100', '101'])
    assert (baza2(15) == ['1', '10', '11', '100', '101', '110', '111', '1000', '1001', '1010', '1011', '1100', '1101',
                          '1110', '1111'])


if __name__ == '__main__':
    teste()
    #problema 8 eficienta
    start_time = time.time_ns()
    baza2(2000)
    baza2(1000)
    baza2(15)

    end_time = time.time_ns()


    elapsed_time = end_time - start_time

    elapsed_time_ms1 = (end_time - start_time)

    print(f"Timpul total scurs: {elapsed_time_ms1} nanosecunde")
    start_time = time.time_ns()
    baza2_chatgpt(2000)
    baza2_chatgpt(1000)
    baza2_chatgpt(15)

    end_time = time.time_ns()


    elapsed_time = end_time - start_time

    elapsed_time_ms2 = (end_time - start_time)

    print(f"Timpul total scurs: {elapsed_time_ms2} nanosecunde")

    #problema 4 eficienta

    cuvinte_disponibile = ["ana", "are", "mere", "rosii", "si", "mere", "verzi", "ana", "are", "pere"]


    text_generat = " ".join(random.choice(cuvinte_disponibile) for _ in range(2000))

    start_time = time.time_ns()
    determina_singura_aparitie(text_generat)

    end_time = time.time_ns()


    elapsed_time = end_time - start_time

    elapsed_time_ms1 = (end_time - start_time)

    print(f"Timpul total scurs: {elapsed_time_ms1} nanosecunde")

    start_time = time.time()
    cuvinte_unice_Chatgpt(text_generat)
    end_time = time.time()


    elapsed_time = end_time - start_time

    elapsed_time_ms2 = (end_time - start_time) * 1000

    print(f"Timpul total scurs: {elapsed_time_ms2} nanosecunde")



    #cerinta 6

    random_values = [random.randint(1, 10) for _ in range(20000 - 1)]


    random_values.extend([5] * (20000 // 2 + 1))

    # Amestecă lista pentru a face ordinea aleatoare
    random.shuffle(random_values)



    start_time = time.time_ns()
    elem_majoritar(random_values)

    end_time = time.time_ns()

    elapsed_time = end_time - start_time

    elapsed_time_ms1 = (end_time - start_time)

    print(f"Timpul toal scurs: {elapsed_time_ms1} nanosecunde")

    start_time = time.time_ns()
    gaseste_element_majoritar_CHATGPT(random_values)
    end_time = time.time_ns()

    elapsed_time = end_time - start_time

    elapsed_time_ms2 = (end_time - start_time)

    print(f"Timpul totall scurs: {elapsed_time_ms2} nanosecunde")
    #e mai eficienta a mea ;)









