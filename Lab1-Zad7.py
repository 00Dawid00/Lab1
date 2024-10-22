print("równanie liniowe ax+b=0")

def solve_linear_equation(a, b):
    if a==0:
        if b==0:
            return "Równanie posiada nieskończenie wiele rozwiązań."
        else:
            return "Równanie nie posiada rozwiązań."
    else:
        x = -b/a
        return f"x = {x}"

a_in = float(input("Podaj a: "))
b_in = float(input("Podaj b: "))

result = solve_linear_equation(a_in, b_in)
print(result)