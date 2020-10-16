# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(petshop):
    return petshop["name"]

def get_total_cash(petshop):
    return petshop["admin"]["total_cash"]

def add_or_remove_cash(petshop, cash):
    petshop["admin"]["total_cash"] += cash

def get_pets_sold(petshop):
    return petshop["admin"]["pets_sold"]
    
def increase_pets_sold(petshop, amount):
    petshop["admin"]["pets_sold"] += amount

def get_stock_count(petshop):
    return len(petshop["pets"])

def get_pets_by_breed(petshop, breed):
    returned_pets = []
    for pet in petshop["pets"]:
        if pet["breed"] == breed:
            returned_pets.append(pet)

    return returned_pets

def find_pet_by_name(petshop, petname):
    returned_pet = None
    for pet in petshop['pets']:
        if pet['name'] == petname:
            returned_pet = pet
    return returned_pet