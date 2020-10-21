#Pure Functions (Fungsi Murni) #mengalikan angka dengan 2
def multiply_2_pure(angka):
    nomer_baru = []
    for n in angka:
        nomer_baru.append(n * 2)
    return nomer_baru

nomer_asli = [1, 3, 5, 10]
ganti_nomer = multiply_2_pure(nomer_asli)
print(nomer_asli) # outputnya [1, 3, 5, 10]
print(ganti_nomer)  # outputnya [2, 6, 10, 20]

#contoh lamda
a = lambda x: x**5
print(a(5)) #outputnya 3.125

# contoh First-Class Functions
def b(c):
    return c**3
print(b(3))
print(f'Tipe fungsi b: {type(b)}') #outputnya 27 

# contoh Higher-Order Functions

#map
merek = ['acer', 'asus', 'apple', 'hp', 'lg']
contoh_map = map(lambda x: f'aku pake laptop merek {x}', merek)
print(contoh_map)
for name in contoh_map:
    print(name)

#filter 
# Without using lambdas
def starts_with_B(s):
    return s[0] == "B"  #diganti disini
fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
filter_object = filter(starts_with_B, fruit)
print(list(filter_object)) #outputnya banana

#contoh filter menggunakan lamda
fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
filter_object = filter(lambda s: s[0] == "A", fruit)
print(list(filter_object)) # outputnya Apple, Apricot

#reduce Function
from functools import reduce

def add(x, y):
    return x + y
list = [2, 4, 7, 3]
print(reduce(add, list))

#conoth reduce mneggunakan lamda
from functools import reduce

list = [2, 4, 7, 3]
print(reduce(lambda x, y: x + y, list))
print("nilai awal: " + str(reduce(lambda x, y: x + y, list, 10)))