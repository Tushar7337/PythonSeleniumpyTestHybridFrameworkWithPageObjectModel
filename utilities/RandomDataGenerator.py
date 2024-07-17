import random
from datetime import datetime

from faker import Faker

fake = Faker()

def random_first_name():
    first_name = fake.first_name()
    return first_name

def random_last_name():
    last_name = fake.last_name()
    return last_name

def random_phone_number():
    phone_number = random.randint(1111111111,9999999999)
    return phone_number

def generate_random_email_with_timestamp():
    current_time = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    return current_time