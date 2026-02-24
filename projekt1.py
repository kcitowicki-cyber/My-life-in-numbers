print("KALKULATOR ŻYCIA")
      
name = input("Podaj swoje imię: ")
age = int(input("Podaj swój wkek: "))
months = age * 12
days = age * 365
hours = days * 24

print("Cześć " + name + " !")
print("Żyjesz około " + str(months) +
     " miesięcy.")
print("Co daje około " + str(days) + " dni")
print("Co przekłada się na około " + str(hours) + " życia.")
