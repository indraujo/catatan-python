## Tipe Data dan Variable
## Tipe Data
'''
None 
    - NoneType
Numeric
    - int
    - float
Boolean
    - bool
Sequence
    - str
    - list
    - tuple
Set
    - set
Map
    - dict
'''
# None or NULL
print(type(None))

# Integer
print(type(1))

# String
print(type("1"))

# Boolean
print(type(True))

# Float
print(type(3.14))

# Complex
print(type(9j))

# List
print(type([1,2,3,4,5]))

# Tuple
print(type((1,2,3,4,5)))

# Dictionary
print(type({"a":1,"b":2,"c":3}))

## variable tidak boleh dimulai dengan angka
'''
Nama dari sebuah variabel harus dimulai dengan huruf (a-z, A-Z)
atau karakter garis bawah underscore (_) dan tidak dapat dimulai dengan angka (0-9).
Variabel hanya boleh mengandung karakter alfabet dan bilangan dan underscore
(a-z, A-Z, 0-9, _)
Variabel bersifat case-sensitive yang mengartikan bahwa
variabel TINGGI, tinggi, dan Tinggi merujuk pada tiga variabel berbeda.
'''

nama = 3
print(nama)