import pdb
import random

from models.product import Product
from models.manufacturer import Manufacturer
from models.branch import Branch
import repositories.product_repository as product_repository
import repositories.manufacturer_repository as manufacturer_repository
import repositories.branch_repository as branch_repository

product_repository.delete_all()
manufacturer_repository.delete_all()
branch_repository.delete_all()

manufacturer1 = Manufacturer("Procter & Gamble", "Cosmetics")
manufacturer2 = Manufacturer("Unilever", "Cosmetics")
manufacturer3 = Manufacturer("Johnson & Johnson", "Cosmetics")
manufacturer4 = Manufacturer("Kimberly Clark", "Cosmetics")
manufacturer5 = Manufacturer("U-To", "Cosmetics")
manufacturer6 = Manufacturer("Needful Things", "Cosmetics")
manufacturer7 = Manufacturer("Lil' Bits", "Cosmetics")
manufacturer8 = Manufacturer("Immortality Field Resort", "Cosmetics")
manufacturer9 = Manufacturer("Weyland Corpo", "Cosmetics")
manufacturer10 = Manufacturer("Stark Industries", "Cosmetics")
manufacturer11 = Manufacturer("Duff Beer", "Cosmetics")
manufacturer12 = Manufacturer("Sterling Cooper", "Cosmetics")

manufacturers = [manufacturer1, manufacturer2, manufacturer3, manufacturer4, manufacturer5, manufacturer6, manufacturer7, manufacturer8, manufacturer9, manufacturer10, manufacturer11, manufacturer12]

for manufacturer in manufacturers:
    manufacturer_repository.save(manufacturer)

branch1 = Branch("Scranton", "Michael Scott", 1234)
branch2 = Branch("Long Island", "Dwight Schrute", 1234)
branch3 = Branch("Talahasse", "Joanne Brown", 1234)

branches = [branch1, branch2, branch3]

for branch in branches:
    branch_repository.save(branch)

product1 = Product("Gilette razors 3pack", "Shaving razors", 50, 1.50, 3.99, manufacturer1.id, branch1.id)
product2 = Product("Gilette razors 3pack", "Shaving razors", 35, 1.50, 3.99, manufacturer1.id, branch2.id)
product3 = Product("Gilette razors 3pack", "Shaving razors", 25, 1.50, 3.99, manufacturer1.id, branch3.id)
product4 = Product("Lipton tea bags", "beverages", 50, 1.50, 3.99, manufacturer2.id, branch1.id)
product5 = Product("Lipton tea bags", "beverages", 35, 1.50, 3.99, manufacturer2.id, branch2.id)
product6 = Product("Lipton tea bags", "beverages", 25, 1.50, 3.99, manufacturer2.id, branch3.id)
product7 = Product("Tylenol", "pain killers", 50, 1.50, 3.99, manufacturer3.id, branch1.id)
product8 = Product("Tylenol", "pain killers", 35, 1.50, 3.99, manufacturer3.id, branch2.id)
product9 = Product("Tylenol", "pain killers", 25, 1.50, 3.99, manufacturer3.id, branch3.id)
product10 = Product("Andrex Toilet Paper", "hygiene", 50, 1.50, 3.99, manufacturer4.id, branch1.id)
product11 = Product("Andrex Toilet Paper", "hygiene", 50, 1.50, 3.99, manufacturer4.id, branch2.id)
product12 = Product("Andrex Toilet Paper", "hygiene", 50, 1.50, 3.99, manufacturer4.id, branch3.id)
product13 = Product("Braun Shaver", "hygiene", 50, 49.99, 89.99, manufacturer1.id, branch1.id)

products = [product1, product2, product3, product4, product5, product6, product7, product8, product9, product10, product11, product12, product13]

for product in products:    
    product_repository.save(product)


# for product in product_repository.select_all():
#     print (product.__dict__)

# for branch in branch_repository.select_all():
#     print(branch.__dict__)

pdb.set_trace()