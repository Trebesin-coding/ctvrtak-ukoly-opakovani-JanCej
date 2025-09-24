import random
import json


seznam_studentu = {
    "Pepa": {"znamka": None},
    "Honza": {"znamka": None},
    "Franta": {"znamka": None},
    "Dan": {"znamka": None}
}


zadane_jmeno = input("Zadej jméno studenta: ")


if zadane_jmeno in seznam_studentu:
    nahodna_znamka = random.randint(1, 5)
    seznam_studentu[zadane_jmeno]["znamka"] = nahodna_znamka
    print(f"{zadane_jmeno} dostal známku {nahodna_znamka}")
else:
    odpoved = input(f"{zadane_jmeno} není v seznamu. Přidat ho? (ano/ne): ")
    
    if odpoved == "ano":
        nova_znamka = random.randint(1, 5)
        seznam_studentu[zadane_jmeno] = {"znamka": nova_znamka}
        print(f"{zadane_jmeno} byl přidán se známkou {nova_znamka}")
    else:
        print("Student nebude přidán.")


with open("znamky.json", "w", encoding="utf-8") as soubor:
    json.dump(seznam_studentu, soubor, ensure_ascii=False, indent=4)

print("Aktuální seznam studentů:")
print(seznam_studentu)


