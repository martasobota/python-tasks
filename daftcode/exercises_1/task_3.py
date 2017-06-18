# Napisać kod transformujący podany słownik: 
# { 1: 'Poniedziałek', 2: 'Wtorek', 3: 'Środa', 4: 'Czwartek', 5: 'Piątek', 6: 'Sobota', 7: 'Niedziela', } 
# do postaci: 
# { 'Poniedziałek': 1, 'Środa': 3, 'Piątek': 5, 'Niedziela': 7, } Zamiana klucza z wartością i zostawienie tylko dni nieparzystych

week_dict = { 1: 'Poniedziałek', 2: 'Wtorek', 3: 'Środa', 4: 'Czwartek', 5: 'Piątek', 6: 'Sobota', 7: 'Niedziela', } 

new_week_dict = {}

for key, value in week_dict.items():
	if key % 2 != 0:
		new_week_dict[value] = key

print(new_week_dict)
