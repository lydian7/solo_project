import pdb

from models.product import Product
from models.manufacturer import Manufacturer
from models.branch import Branch
import repositories.product_repository as product_repository

product1 = Product("Gilette razors 3pack", "Shaving razors", 50, 1.50, 3.99)

product_repository.save(product1)


pdb.set_trace()