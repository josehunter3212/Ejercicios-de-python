''''
Determinar si un year es bisiesto
'''


year = int(input("Ingrse el year que desea verificar"))
if year % 4 == 0 and(year % 100 !=0 or year  % 400 == 0 or year % 100 == 0):
    print('El year',year,'es un year bisicesto')
else:
    print('El year ',year,'no es un year bisicesto')
