current_year = 2026

def get_info():
    name = input('your name:')
    age = input('age:')
    birth_year =0
    try:
        birth_year = current_year - int(age)
    except:
        print('enter valid age')
    print_info(year= birth_year, name=name)

def print_info(name, year):
    print("Hi {} your birth year is {}".format(name, year))

get_info()