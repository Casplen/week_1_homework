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


