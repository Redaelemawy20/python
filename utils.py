from datetime import datetime

def get_info():
    name = input('your name: ')
    age = input('age: ')
    
    try:
        current_year = datetime.now().year
        birth_year = current_year - int(age)
        return name, birth_year
    except:
        print('enter valid age')
        return None, None


def print_info(name, year):
    print("Hi {} your birth year is {}".format(name, year))





print(sum([1, 20, 393, 33]))

li = [{'age': 33}, {'age': 23}, {'age': 53}]
print(sum(x['age'] for x in li))