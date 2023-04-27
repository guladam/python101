import datetime

today = datetime.date.today()
current_year = today.year

birth_year = int(input("ID scanning complete, year of birth: "))

if current_year - birth_year >= 18:
    print("PASS")
else:
    print("FAIL")