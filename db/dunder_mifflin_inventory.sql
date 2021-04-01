DROP TABLE branches;
DROP TABLE products;
DROP TABLE manufacturers;

CREATE TABLE manufacturers (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    type VARCHAR,
    active BOOLEAN
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    description VARCHAR,
    quantity INT,
    purchase_price FLOAT,
    selling_price FLOAT
);

CREATE TABLE branches (
    id SERIAL PRIMARY KEY,
    location VARCHAR,
    manager VARCHAR,
    manufacturer_id INT REFERENCES manufacturers(id),
    product_id INT REFERENCES products(id)
);

-- INSERT INTO manufacturers (name, type, active) VALUES ('Procter & Gamble', 'FMCG', True);
-- INSERT INTO manufacturers (name, type, active) VALUES ('UNILEVER', 'FMCG', True);
-- INSERT INTO manufacturers (name, type, active) VALUES ('Johnson & Johnson', 'FMCG', True);

-- INSERT INTO products (name, description, quantity, purchase_price, selling_price) VALUES ('Gilette', '3pack blade', 50, 0.99, 2.99);
-- INSERT INTO products (name, description, quantity, purchase_price, selling_price) VALUES ('Gilette', '6pack blade', 50, 1.50, 3.99);
-- INSERT INTO products (name, description, quantity, purchase_price, selling_price) VALUES ('Gilette', '10pack blade', 50, 3.50, 6.99);
-- INSERT INTO products (name, description, quantity, purchase_price, selling_price) VALUES ('Axe Body Spray', 'Africa deodorant', 50, 1.29, 3.99);
-- INSERT INTO products (name, description, quantity, purchase_price, selling_price) VALUES ('Axe Body Spray', 'Dry White deodorant', 50, 1.29, 3.99);
-- INSERT INTO products (name, description, quantity, purchase_price, selling_price) VALUES ('Axe Body Spray', 'Sports Extra deodorant', 50, 1.29, 3.99);
-- INSERT INTO products (name, description, quantity, purchase_price, selling_price) VALUES ('J&J Baby Shampoo', 'Baby shampoo', 50, 1.50, 4.99);
-- INSERT INTO products (name, description, quantity, purchase_price, selling_price) VALUES ('Baby powder', 'talk powder for babies', 50, 1.29, 3.99);
-- INSERT INTO products (name, description, quantity, purchase_price, selling_price) VALUES ('Wet wipes', 'wet wipes for babies', 50, 1.29, 3.99);

-- INSERT INTO branches (location, manager, manufacturer_id, product_id) VALUES ('Scranton', 'Michael Scott', 1, 1);
-- INSERT INTO branches (location, manager, manufacturer_id, product_id) VALUES ('Scranton', 'Michael Scott', 1, 2);
-- INSERT INTO branches (location, manager, manufacturer_id, product_id) VALUES ('Scranton', 'Michael Scott', 1, 3);
-- INSERT INTO branches (location, manager, manufacturer_id, product_id) VALUES ('Scranton', 'Michael Scott', 2, 4);
-- INSERT INTO branches (location, manager, manufacturer_id, product_id) VALUES ('Scranton', 'Michael Scott', 2, 5);
-- INSERT INTO branches (location, manager, manufacturer_id, product_id) VALUES ('Scranton', 'Michael Scott', 2, 6);
-- INSERT INTO branches (location, manager, manufacturer_id, product_id) VALUES ('Scranton', 'Michael Scott', 3, 7);
-- INSERT INTO branches (location, manager, manufacturer_id, product_id) VALUES ('Scranton', 'Michael Scott', 3, 8);
-- INSERT INTO branches (location, manager, manufacturer_id, product_id) VALUES ('Scranton', 'Michael Scott', 3, 9);

-- INSERT INTO branches (location, manager, manufacturer_id, product_id) VALUES ('Talahasse', 'Julia Smith', 1, 1);
-- INSERT INTO branches (location, manager, manufacturer_id, product_id) VALUES ('Talahasse', 'Julia Smith', 1, 2);
-- INSERT INTO branches (location, manager, manufacturer_id, product_id) VALUES ('Talahasse', 'Julia Smith', 1, 3);
-- INSERT INTO branches (location, manager, manufacturer_id, product_id) VALUES ('Talahasse', 'Julia Smith', 2, 4);
-- INSERT INTO branches (location, manager, manufacturer_id, product_id) VALUES ('Talahasse', 'Julia Smith', 2, 5);
-- INSERT INTO branches (location, manager, manufacturer_id, product_id) VALUES ('Talahasse', 'Julia Smith', 2, 6);
-- INSERT INTO branches (location, manager, manufacturer_id, product_id) VALUES ('Talahasse', 'Julia Smith', 3, 7);
-- INSERT INTO branches (location, manager, manufacturer_id, product_id) VALUES ('Talahasse', 'Julia Smith', 3, 8);
-- INSERT INTO branches (location, manager, manufacturer_id, product_id) VALUES ('Talahasse', 'Julia Smith', 3, 9);


-- INSERT INTO branches (location, manager, manufacturer_id, product_id) VALUES ('Philly', 'Frank Sinatra', 1, 1);
-- INSERT INTO branches (location, manager, manufacturer_id, product_id) VALUES ('Philly', 'Frank Sinatra', 1, 2);
-- INSERT INTO branches (location, manager, manufacturer_id, product_id) VALUES ('Philly', 'Frank Sinatra', 1, 3);
-- INSERT INTO branches (location, manager, manufacturer_id, product_id) VALUES ('Philly', 'Frank Sinatra', 2, 4);
-- INSERT INTO branches (location, manager, manufacturer_id, product_id) VALUES ('Philly', 'Frank Sinatra', 2, 5);
-- INSERT INTO branches (location, manager, manufacturer_id, product_id) VALUES ('Philly', 'Frank Sinatra', 2, 6);
-- INSERT INTO branches (location, manager, manufacturer_id, product_id) VALUES ('Philly', 'Frank Sinatra', 3, 7);
-- INSERT INTO branches (location, manager, manufacturer_id, product_id) VALUES ('Philly', 'Frank Sinatra', 3, 8);
-- INSERT INTO branches (location, manager, manufacturer_id, product_id) VALUES ('Philly', 'Frank Sinatra', 3, 9);


