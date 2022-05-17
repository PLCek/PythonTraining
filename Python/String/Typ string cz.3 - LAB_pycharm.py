#Typ string cz.3 - LAB

'''

Czy wiesz, że twórca języka Python - Guido Van Rossum - był fanem latającego cyrku Monty Pythona? Tak. To od tego wzięła się nazwa języka!

1. Wejdź na stronę Wikipedii poświęconej Monty Pytonowi

https://en.wikipedia.org/wiki/Monty_Python

Skopiuj fragment z paragrafu zatytuowanego "Monty Python".

2. W skrypcie utwórz zmienną article i przypisz jej wartość skopiowanego tesktu.

Uwaga! Skopiowany tekst jest długi i zawiera znaki ENTER. Jeśli chcesz przypisać do zmiennej taki tekst możesz użyć konstrukcji z trzema apostrofami o tak:

zmienna = '''
#dłuuugi tekst i jeszcze
#dłuższy tekst i....
'''

3. Skonwertuj tekst do dużych liter i wyświetl go. Zrób to w jednej instrukcji.

4. Wyświetl tekst zamieniając 'monty' na 'flying'. Ponieważ python rozpoznaje małe i duże litery przed zamianą skonwertuj go na małe litery.
Ponownie postaraj się to zrobić w jednym poleceniu.

5. Rozbij tekst na słowa ze względu na spacje i wyświetl tą listę.

6. Wyświetl tekst w postaci:
        word python appears 3 times
oczywiście liczba (tutaj 3) powinna być wyliczona, jako ilość wystąpień tekstu python w zmiennej article

7. Poleceniem print wyświetl tekst:
to print the \ you need to put \ twice in your text like this: \\

8. Poleceniem print wyświetl tekst

The best hits of '80s!!!

Zrób to na 2 sposoby:
-raz tekst powinien być zamknięty w pojedynczym apostrofie '
-a drugi raz tekst powinien być zamknięty w cudzysłowiu "

9. Teraz zrobisz "mini kalkulator" do kantoru wymiany walut. Chcemy wyświetlić tabelkę w postaci:

cur   exchange amount
USD   3.65     64.10958904109589
EUR   4.23     55.31914893617021
w tym celu:

-najpierw zadeklaruj zmienną amountPLN i wpisz do niej wartość 234

-następnie wyświetl teksty rozdzielając wartości tabulatorem, tak aby to co zostanie wypisane na ekranie
przypominało tabelkę (skorzystaj do tego z kilku poleceń print, jednolinijkowy print byłby zbyt trudny do zrozumienia)

-wartości w kolumnie amount wylicz dzieląc amountPLN przez aktualny kurs USD i EUR (w tym przykładzie są to 3.65 i 4.23)

10. Zadeklaruj zmienną ValueAsText i wpisz do niej wartość '123.45'

11. Zadeklaruj zmienną factor o wartości 1.23

12. Wyświetl tekst:

value is  123.45 factor is 1.23 value*factor= 151.8435

podczas obliczania value * factor skonwertuj zmienną ValueAsText na typ float

'''


article = '''Monty Python (also collectively known as the Pythons)[2][3] were a British surreal comedy troupewho
created the sketch comedy television show Monty Python's Flying Circus, which first aired on the BBC in 1969. Forty-five
episodes were made over four series. The Python phenomenon developed from the television series into something larger in
scope and influence, including touring stage shows, films, albums, books and musicals. The Pythons' influence on comedy
has been compared to the Beatles' influence on music.[4][5][6] Regarded as an enduring icon of 1970s pop culture,
their sketch show has been referred to as being \"an important moment in the evolution of television comedy\".[7]" '''

print(article.upper())

print()

print(article.lower().replace('monty', 'flying'))

print()

print(article)
