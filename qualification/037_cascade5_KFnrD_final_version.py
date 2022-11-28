# Witold Formański
# zadanie 2.

# Wysyłam kolejne rozwiązanie, ponieważ wpadłem na pomysł, jak wykorzystać system dwójkowy do uproszczenia działań.
# Program napisałem w Pythonie, więc proszę o przeklejenie poniższego kodu do odpowiedniego komplitora.

# moje podejście oparte jest o spostrzeżenie, że gdyby ponumerować odcinki od 0 do 2^k-1 i zapisać ich numery w systemie binarnym, 
# to liczba zer (również na początku) w zapisie odpowiada liczbie pomnożeń razy m0, które należy wykonać i odpowiednio tyle, 
# ile razy w zapisie występuje cyfra 1, tyle razy należy pomnożyć razy m1, aby w wyniku otrzymać miarę odcinka

# korzystam z bilblioteki Matplotlib:

import matplotlib
import matplotlib.pyplot as plt

# zadawane parametry:

k = 12
m1 = 0.7

# warunek m0 + m1 = 1:

m0 = 1 - m1

# tworzę listę, na której przechowywane są (jako stringi) liczby od 0 do 2^k-1 w systemie binarnym

y_bin = []

for i in range(0,2**k):
	y_bin.append(bin(i)[2:])

# przeprowadzam iterację, w której sumuję liczbę jedynek występujących w binarnym zapisie; 
# dla każdego elementu listy y_bin tworzę odpowiadający mu element na liście y_ones:

y_ones = []

for i in range(0,2**k):
	ones = 0
	for digit_str in y_bin[i]:
		digit_int = int(digit_str)
		ones += digit_int
	y_ones.append(ones)

# korzystając z listy y_ones mnożę parametry m0 i m1 w odpowiednich potęgach:

y_final = []
y = 0

for i in range(0,2**k):
	y = (m1**y_ones[i]) * (m0**(k-y_ones[i]))
	y_final.append(y)

# tworzę 2^k-elementowy zbiór argumentów rozmieszczonych na odcinku [0;1]:

x= []

for i in range(1,2**k+1):
	x.append(i/2**k - 1/2**(k+1))

# rysuję wykres słupkowy:

fig, ax = plt.subplots()
ax.bar(x,y_final, 1/2**k, edgecolor = 'darkgreen', color = 'green')
ax.set(title = 'Kaskada multiplikatywna - podejście binarne')
plt.show()