import random
availiable_numbers = [x for x in range(10)] # list(range(10))
size = 26

def generate_account_number():
    new_number_list = [str(random.choice(availiable_numbers)) for _ in availiable_numbers]
    new_number_str = ''.join(new_number_list)

    return new_number_str