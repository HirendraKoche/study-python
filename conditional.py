# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years

def get_age():
    v_age_in = int(input("Enter your age: "))
    print ("You are old enough to drive") if v_age_in >= 18 else print(f"Wait for {18 - v_age_in} Years.")

# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.

def get_age_2():
    v_myage_int = 32
    v_age_int = int(input("Enter your age: "))
    if v_age_int > v_myage_int:
        if v_age_int - v_myage_int == 1:
            print("Your are older than me by an year.")
        else:
            print(f"Your are older than me by {v_age_int - v_myage_int} years")
    elif v_age_int == v_age_int:
        print("We are of same age.")
    else:
        if v_myage_int - v_age_int == 1:
            print("I am older than you by an year.")
        else:
            print(f"I am older than you by {v_myage_int - v_age_int} years")

# Write a code which gives grade to students according to theirs scores
def get_grade(marks: float) -> str:
    if marks in range(80, 101):
        return 'A'
    elif marks in range(70, 80):
        return 'B'
    elif marks in range(60, 70):
        return 'C'
    elif marks in range(50, 60):
        return 'D'
    else:
        return 'F'

# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

def get_session(month: str) -> str:
    autumn_tp = ('September', 'October', 'November')
    winter_tp = ('December', 'January', 'February')
    spring_tp = ('March', 'April', 'May')
    summer_tp = ('June', 'July', 'August')

    if month in autumn_tp:
        return 'Autumn'
    elif month in winter_tp:
        return 'Winter'
    elif month in spring_tp:
        return 'Spring'
    elif month in summer_tp:
        return 'Summer'
    else:
        return None

# if __name__ == '__main__':
#     data = input("Enter month: ")   
#     result = get_session(data)
#     if data == '':
#         print(f"Month can not be empty.")
#     elif result is not None:
#         print(f"Session is {result}")
#     else:
#         print(f"{data} not a month.")


# Exersize 3
person={'first_name': 'Asabeneh',
        'last_name': 'Yetayeh',
        'age': 250,
        'country': 'Finland',
        'is_marred': True,
        'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
        'address': {
            'street': 'Space street',
            'zipcode': '02210'
            }
        }

if 'skills' not in person.keys():
    print("Disc dose not have skills key.")
else:
    skill_len = len(person['skills'])
    skill_set = set(person['skills'])
    if skill_len == 2 and {'React', 'JavaScript'}.issubset(skill_set):
        print('He is a front end developer')
    elif skill_len == 3 and {'Node', 'Python', 'MongoDB'}.issubset(skill_set):
        print('He is a backend developer')
    elif {'React', 'Node', 'MongoDB'}.issubset(skill_set):
        print('He is a fullstack developer')
    else:
        print('unknown title')
