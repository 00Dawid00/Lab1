droga=float(input("Droga pokonana przez samochód (km): "))
spalanie=float(input("Średnie spalanie (l/100km): "))

cena_paliwa = 6.5

zuzycie_paliwa=(droga/100)*spalanie
koszt_podrozy=zuzycie_paliwa*cena_paliwa


print(f"\nPrzewidywane zużycie paliwa: {zuzycie_paliwa:.2f}l")
print(f"Szacowany koszt podróży: {koszt_podrozy:.2f}zł")

