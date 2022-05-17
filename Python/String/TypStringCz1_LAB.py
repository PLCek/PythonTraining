'''
TypStringCz1_LAB

Typ string cz.1 - LAB

    Utwórz zmienną quote i przypisz jej następującą wartość:   'A good programmer is someone who always looks both ways before crossing a one-way street'

    Wyświetl tekst napisany tylko wielkimi literami

    Wyświetl tekst zapisany tylko małymi literami

    Sprawdź czy tekst kończy się słowem 'street'

    Sprawdź czy tekst jest zapisany wielkimi literami

    Sprawdź, czy tekst skonwertowany do wielkich liter jest zapisany wielkimi literami (Zastosuj złożenie funkcji)

    Poszukaj na której pozycji (licząc od zera) znajduje się w tekście słowo (podnapis)  'one'

    Zamień w tekście słowo (podnapis) 'one' na '1'

    Zamień w tekście słowo (podnapis) 'one' na '1' a słowo 'both' na 2

    Rozdziel napis na mniejsze napisy ze względu na znak rozdzielający jakim jest spacja

    Sprawdź czy napis jest liczbą, liczbą dziesiętną, napisem bez cyfr, napisem z literami i cyframi


W ostatnim zadaniu otrzymujesz 4 wartości false. Zwłaszcza 2 ostatnie wyniki mogą Cię dziwić. Nasz napis zawierał spacje, składał się z
wielu wyrazów i dlatego nie jest alfa-stringiem ani alfanumerykiem

'''

quote = 'A good programmer is someone who always looks both ways before crossing a one-way street'
print(quote.upper())
print()
print(quote.lower())
print()
print(quote.endswith('street'))
print()
print(quote.isupper())
print()
print(quote.upper().isupper())
print()
print(quote.find('one'))
print()
print(quote.replace('one', '1'))
print()
print(quote.replace('one', '1'), quote.replace('both', '2'))
print(quote.split())
print()
print(quote.isdigit())
print()
print(quote.isdecimal())
print()
print(quote.isalpha())
print()
print(quote.isalnum())









