# Napisać kod transformujący podany słownik: 
# { 1: 'Poniedziałek', 2: 'Wtorek', 3: 'Środa', 4: 'Czwartek', 5: 'Piątek', 6: 'Sobota', 7: 'Niedziela', } 
# do postaci: 
# { 'Poniedziałek': 1, 'Środa': 3, 'Piątek': 5, 'Niedziela': 7, } Zamiana klucza z wartością i zostawienie tylko dni nieparzystych

dict = { 1: 'Poniedziałek', 2: 'Wtorek', 3: 'Środa', 4: 'Czwartek', 5: 'Piątek', 6: 'Sobota', 7: 'Niedziela', } 

for key in dict:
    print(key)
