from moodul import *
#arithmetic funct kasutamine
print('1 ül')

a = float(input('Sisesta arv 1: '))
b = float(input('Sisesta arv 2: '))
t = input('Tehe: ')
v = arithmetic(a,b,t)
print(v)

print('2 ül')
aasta = int(input('Sisesta aasta:'))
vastus = is_year_leap(aasta)
print(vastus)
if vastus: 
    print(f'{aasta} on liigaasta')
else:
    print(f'{aasta} ei ole liigaasta')

print('3 ül')
S,P,D = float(input('Sisesta ruudu kulg: '))