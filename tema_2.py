# ex.1 radicalul
a = 25
a = 25 ** (1/2)
print(a)

# ex.2 rata lunara
valoare_de_inprumut = int('32000')
numar_de_luni = int('12')
rata_lunara = 32000/12
print(rata_lunara)

# ex.3 media armonica
# formula: 3/[(1/a)+(1/b)+(1/c)]=3abc/(bc+ac+ab)
b = 25
c = 30
d = 35
media_armonica = 3 / ((1 / b) + (1 / c) + (1/d))
print(media_armonica)

media_armonica_1 = (3 * b * c * d) / ((c * d) + (b * d) + (b * c))
print(media_armonica_1)

# ex. 4 media ponderata
# formula: mp = (p1*a1 + p2*a2 + p3 * a3) / (p1 + p2 + p3)
a = 10  # numere
b = 8
c = 5
p = 12  # ponderi
q = 11
r = 6
media_ponderata = ((p * a) + (q * b) + (r * c)) / (p + q + r)
print(media_ponderata)

# ex.5 ecuatia de gradul 1: a * x + b = 0
a = 6
b = 9
solutia = (0 - b) / a
print(solutia)
print(type(solutia))

#  ex. 6 ecuatia de gradul 2: a * x ** 2 + b * x + c = 0.
# formule: delta= b patrat-4ac
#          x1 = (-b + (delta ** (1/2))) / (2 * a)=5178/6=
#          x2 = (-b - (delta ** (1/2))) / (2 * a)
a = 6
b = 12
c = 4
delta = b ** 2 - 4 * a * c
print(delta)

x_1 = (delta ** (1/2) - b) / (2 * a)
print(x_1)
x_2 = (-b - (delta ** (1/2))) / (2 * a)
print(x_2)
# S = { -0.42, -1.57 }


# ex. 7
a = 300
rezultat = ((50/100) * a) * (25 / 100)
print(rezultat)

