from moodul import *
#arithmetic funct kasutamine
print('1 ül')

# a = float(input('Sisesta arv 1: '))
# b = float(input('Sisesta arv 2: '))
# t = input('Tehe: ')
# v = arithmetic(a,b,t)
# print(v)

# print('2 ül')
# aasta = int(input('Sisesta aasta:'))
# vastus = is_year_leap(aasta)
# print(vastus)
# if vastus: 
#     print(f'{aasta} on liigaasta')
# else:
#     print(f'{aasta} ei ole liigaasta')

# print('3 ül')
# S,P,D = float(input('Sisesta ruudu kulg: '))

# print('4 ül')
# k=int(input("sisesta kuu number: "))
# v= season(k)
# print(v)

# print('5 ül')
# years =  int(input('sisesta years'))
# a = int(input('sisesta raha'))
# while True: 
#     if years < 0 or a < 0:
#         print('sisesta normalsed')
#     else:
#         vastus1 = bank(a, years)
#         break

print('ül 6')
arv1 = float(input('sisesta num'))
vastus2 = is_prime(arv1)
print(vastus2)


print('7 ül')
kuu=int(input("sisesta kuu number: "))
paev=int(input("sisesta paev: "))
v=date(kuu, paev)
print(v)

print('8 ül')