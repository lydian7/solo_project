import pdb
import random

from models.product import Product
from models.manufacturer import Manufacturer
from models.branch import Branch
from models.employee import Employee
from models.sale import Sale
import repositories.product_repository as product_repository
import repositories.manufacturer_repository as manufacturer_repository
import repositories.branch_repository as branch_repository
import repositories.employee_repository as employee_repository
import repositories.sales_repository as sales_repository

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
branch3 = Branch("Tallahassee", "Joanne Brown", 1234)
branch4 = Branch("Akron", "Smith Smitherson", 1234)
branch5 = Branch("Nashua", "Kevin Pearson", 1234)
branch6 = Branch("Rochester", "Mighty Joe", 1234)
branch7 = Branch("Syracuse", "Creed Batton", 1234)
branch8 = Branch("Utica", "Karen Filippelli", 1234)
branch9 = Branch("Pawnee", "Ron Swanson", 1234)
branch10 = Branch("Springfield", "Homer Simpson", 1234)
branch11 = Branch("Fargo", "Lester Nygaard", 1234)
branch12 = Branch("Gilead", "Fred Waterford", 1234)

branches = [branch1, branch2, branch3, branch4, branch5, branch6, branch7, branch8, branch9, branch10, branch11, branch12]

for branch in branches:
    branch_repository.save(branch)

employee1 = Employee("Jim", "Halpert", "Sales Executive", branch1.id)
employee2 = Employee("Andy", "Bernard", "Sales Executive", branch1.id)
employee3 = Employee("Dwight", "Schrute", "Sales Executive", branch1.id)
employee4 = Employee("Michael", "Scott", "Regional Manager", branch1.id)
employee5 = Employee("Pam", "Beesly", "Sales Executive", branch1.id)
employee6 = Employee("Ryan", "Howard", "Temp", branch1.id)
employee7 = Employee("Stanley", "Hudson", "Sales Executive", branch1.id)
employee8 = Employee("Kevin", "Malone", "Sales Executive", branch1.id)
employee9 = Employee("Creed", "Bratton", "Sales Executive", branch1.id)
employee10 = Employee("Toby", "Flenderson", "Sales Executive", branch1.id)


employee11 = Employee("Dandy", "Bernard", "Sales Executive", branch2.id)
employee12 = Employee("Dright", "Schrute", "Sales Executive", branch2.id)
employee13 = Employee("Michel", "Scott", "Regional Manager", branch2.id)
employee14 = Employee("Pamela", "Beesly", "Sales Executive", branch2.id)
employee15 = Employee("Ryanovski", "Howard", "Temp", branch2.id)
employee16 = Employee("Stan", "Hudson", "Sales Executive", branch2.id)
employee17 = Employee("Kev", "Malone", "Sales Executive", branch2.id)
employee18 = Employee("Apollo Creed", "Bratton", "Sales Executive", branch2.id)
employee19 = Employee("Tim", "Halpert", "Sales Executive", branch2.id)
employee20 = Employee("Toby", "Flenderson", "Sales Executive", branch2.id)


employee21 = Employee("Grim", "Halpert", "Sales Executive", branch2.id)
employee22 = Employee("Mandy", "Bernard", "Sales Executive", branch2.id)
employee23 = Employee("Beety", "Schrute", "Sales Executive", branch2.id)
employee24 = Employee("Prison Mike", "Scott", "Regional Manager", branch2.id)
employee25 = Employee("Pamster", "Beesly", "Sales Executive", branch2.id)
employee26 = Employee("Ry", "Howard", "Temp", branch2.id)
employee27 = Employee("Stanislav", "Hudson", "Sales Executive", branch2.id)
employee28 = Employee("Kevanov", "Malone", "Sales Executive", branch2.id)
employee29 = Employee("Creed the band", "Bratton", "Sales Executive", branch2.id)
employee30 = Employee("Toblerone", "Flenderson", "Sales Executive", branch2.id)


employees1 = [employee1, employee2, employee3, employee4, employee5, employee6, employee7, employee8, employee9, employee10]
employees2 = [employee11, employee12, employee13, employee14, employee15, employee16, employee17, employee18, employee19, employee20]
employees3 = [employee21, employee22, employee23, employee24, employee25, employee26, employee27, employee28, employee29, employee30]

all_employees = employees1 + employees2 + employees3

for employee in all_employees:
    employee_repository.save(employee)

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
product14 = Product("Gilette razors 3pack", "Shaving razors", 50, 1.50, 3.99, manufacturer1.id, branch4.id)
product15 = Product("Gilette razors 3pack", "Shaving razors", 35, 1.50, 3.99, manufacturer1.id, branch5.id)
product16 = Product("Gilette razors 3pack", "Shaving razors", 25, 1.50, 3.99, manufacturer1.id, branch6.id)
product17 = Product("Lipton tea bags", "beverages", 50, 1.50, 3.99, manufacturer2.id, branch7.id)
product18 = Product("Lipton tea bags", "beverages", 35, 1.50, 3.99, manufacturer2.id, branch8.id)
product19 = Product("Lipton tea bags", "beverages", 25, 1.50, 3.99, manufacturer2.id, branch9.id)
product20 = Product("Tylenol", "pain killers", 50, 1.50, 3.99, manufacturer3.id, branch4.id)
product21 = Product("Tylenol", "pain killers", 35, 1.50, 3.99, manufacturer3.id, branch5.id)
product22 = Product("Tylenol", "pain killers", 25, 1.50, 3.99, manufacturer3.id, branch6.id)
product23 = Product("Andrex Toilet Paper", "hygiene", 50, 1.50, 3.99, manufacturer4.id, branch7.id)
product24 = Product("Andrex Toilet Paper", "hygiene", 50, 1.50, 3.99, manufacturer4.id, branch8.id)
product25 = Product("Andrex Toilet Paper", "hygiene", 50, 1.50, 3.99, manufacturer4.id, branch9.id)
product26 = Product("Braun Shaver", "hygiene", 50, 49.99, 89.99, manufacturer1.id, branch1.id)

products = [product1, product2, product3, product4, product5, product6, product7, product8, product9, product10, product11, product12, product13,
product14, product15, product16, product17, product18, product19, product20, product21, product22, product23, product24, product25, product26]

for product in products:    
    product_repository.save(product)

sale1 = Sale(10, product1.id, employee1.id)

sales = [sale1]

for sale in sales:
   sales_repository.save(sale)

pdb.set_trace()