a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))


dodawanie = a + b
odejmowanie = a - b
mnozenie = a * b

if b != 0:
    dzielenie = a / b
else:
    dzielenie = "Nie można dzielić przez zero."

potegowanie = a ** b


print(f"\nWynik dodawania: {dodawanie}")
print(f"Wynik odejmowania: {odejmowanie}")
print(f"Wynik mnożenia: {mnozenie}")
print(f"Wynik dzielenia: {dzielenie}")
print(f"Wynik potęgowania: {potegowanie}")