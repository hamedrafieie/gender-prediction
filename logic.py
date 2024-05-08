import pandas as pd
from faker import Faker
from names_dataset import NameDataset, NameWrapper

nd = NameDataset()

def get_gender_and_country(name):
    gender = (NameWrapper(nd.search(name)).gender)
    country = (NameWrapper(nd.search(name)).country)
    return gender,country


# print(f"Predicted gender: {predicted_gender}")
# print(f"Predicted country: {predicted_country}")