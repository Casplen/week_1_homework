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

def remove_pet_by_name(petshop, petname):
    returned_pet = None
    for pet in petshop['pets']:
        if pet['name'] == petname:
            returned_pet = pet
            petshop['pets'].remove(returned_pet)

def add_pet_to_stock(petshop, newpet):
    petshop['pets'].append(newpet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)

def customer_can_afford_pet(customer, pet):
    return customer['cash'] >= pet['price']

def sell_pet_to_customer(petshop, pet, customer):
    if pet == None:
        return None
    elif customer_can_afford_pet(customer, pet) == False:
        return None
    elif customer_can_afford_pet(customer, pet) == True:
        customer['pets'].append(pet)
        remove_pet_by_name(petshop, pet)
        increase_pets_sold(petshop, 1)
        remove_customer_cash(customer, pet['price'])
        add_or_remove_cash(petshop, pet['price'])


