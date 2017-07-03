# Napisać kod transformujący podany słownik: 
# { 1: 'Poniedziałek', 2: 'Wtorek', 3: 'Środa', 4: 'Czwartek', 5: 'Piątek', 6: 'Sobota', 7: 'Niedziela', } 
# do postaci: 
# { 'Poniedziałek': 1, 'Środa': 3, 'Piątek': 5, 'Niedziela': 7, } Zamiana klucza z wartością i zostawienie tylko dni nieparzystych

week_dict = { 1: 'Poniedziałek', 2: 'Wtorek', 3: 'Środa', 4: 'Czwartek', 5: 'Piątek', 6: 'Sobota', 7: 'Niedziela', }

for key, value in week_dict.copy().items():
    if key % 2 != 0:
        week_dict[value] = key
    del week_dict[key]

print(week_dict)