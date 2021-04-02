import pdb

from models.product import Product
from models.manufacturer import Manufacturer
from models.branch import Branch
import repositories.product_repository as product_repository
import repositories.manufacturer_repository as manufacturer_repository

manufacturer_repository.delete_all()
product_repository.delete_all()

manufacturer1 = Manufacturer("Procter & Gamble", "Cosmetics", True)

manufacturer_repository.save(manufacturer1)

product1 = Product("Gilette razors 3pack", "Shaving razors", 50, 1.50, 3.99, manufacturer1)

product_repository.save(product1)


pdb.set_trace()