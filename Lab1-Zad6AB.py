import random

droga=random.randint(0,1000)
print(f"Losowo wygenerowana droga pokonana przez samochód: {droga}km")

spalanie=float(input("Średnie spalanie (l/100km)"))
cena_paliwa=float(input("Podaj cenę paliwa (zł/l)"))

zuzycie_paliwa=(droga/100)*spalanie
koszt_podrozy=zuzycie_paliwa*cena_paliwa


print(f"\nPrzewidywane zużycie paliwa: {zuzycie_paliwa:.2f}l")
print(f"Szacowany koszt podróży: {koszt_podrozy:.2f}zł")
