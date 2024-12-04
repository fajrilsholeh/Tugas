# operasi aritmatika 

a = 10
b = 3

# oprasi tambah +
hasil = a + b 
print(a,"+" , b, "=" , hasil)

# operasi kurang -
hasil = a - b
print(a,"-" , b, "=" , hasil)

# operasi perkalian *
hasil = a * b 
print(a,"*" , b, "=" , hasil)

# operasi pembagian /
hasil = a / b 
rint(a,"/" , b, "=" , hasil)

# operasi modulasi %
hasil = a % b 
print(a,"%" , b, "=" , hasil)

# operasi floor division 
hasil = a // b 
rint(a,"//" , b, "=" , hasil)

# operasi expone 
hasil = a ** b 
rint(a,"**" , b, "=" , hasil)

# prioritas operasi armatika

"""
    1, ()
    2, *, **, / %, //
    3, =, -
"""

x = 3
y = 2
z = 4

hasil = x**y * (z + x ) / y - y % z // x
print(hasil)