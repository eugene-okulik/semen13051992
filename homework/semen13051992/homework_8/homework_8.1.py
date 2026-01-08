from random import randint, choice

'''
def salary_bonus(salary):
    bonus = [True, False]
    choice_bonus = choice(bonus)
    if choice_bonus:
        print(f"{salary}, {choice_bonus} - '${salary + randint(1, 1000)}'")
    else:
        print(f"{salary}, {choice_bonus} - '${salary}'")


salary_bonus(10000)
salary_bonus(20000)
salary_bonus(30000)
'''


def salary_bonus2():
    salary = int(input())
    bonus = [True, False]
    choice_bonus = choice(bonus)
    if choice_bonus:
        print(f"{salary}, {choice_bonus} - '${salary + randint(1, 1000)}'")
    else:
        print(f"{salary}, {choice_bonus} - '${salary}'")


salary_bonus2()
salary_bonus2()
salary_bonus2()
