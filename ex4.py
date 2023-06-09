elev1 = []
elev2 = []
nume_elev1 = input("Introduceți numele elevului 1: ")
prenume_elev1 = input("Introduceți prenumele elevului 1: ")
nota_elev1 = float(input("Introduceți nota elevului 1: "))
elev1.append(nume_elev1.upper())
elev1.append(prenume_elev1.upper()[0]+prenume_elev1[1::])
elev1.append(nota_elev1)
nume_elev2 = input("Introduceți numele elevului 2: ")
prenume_elev2 = input("Introduceți prenumele elevului 2: ")
nota_elev2 = float(input("Introduceți nota elevului 2: "))
elev2.append(nume_elev2.upper())
elev2.append(prenume_elev2.upper()[0]+prenume_elev2[1::])
elev2.append(nota_elev2)
if nota_elev1 > nota_elev2:
    print("Elevul cu nota mai mare este:", prenume_elev1, nume_elev1)
elif nota_elev1 < nota_elev2:
    print("Elevul cu nota mai mare este:", prenume_elev2, nume_elev2)
else:
    print("Amândoi elevii au obținut aceeași notă.")
if nota_elev1 < nota_elev2:
    print("Elevul cu nota mai mică este:", prenume_elev1, nume_elev1)
elif nota_elev1 > nota_elev2:
    print("Elevul cu nota mai mică este:", prenume_elev2, nume_elev2)
else:
    print("Amândoi elevii au obținut aceeași notă.")
print("|", elev1[0], "|", elev1[1], "|", elev1[2], "|")
print("|", elev2[0], "|", elev2[1], "|", elev2[2], "|")