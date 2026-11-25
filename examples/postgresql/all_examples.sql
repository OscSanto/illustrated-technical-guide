-- Execute selectively: includes EXPLAIN, schema reset, and a transaction rollback.

CREATE ROLE analyst LOGIN PASSWORD 'replace-with-a-strong-password';
CREATE DATABASE shoplab OWNER analyst;

DROP TABLE IF EXISTS order_items, orders, products, customers CASCADE;
CREATE TABLE customers (
  customer_id integer PRIMARY KEY,
  name text NOT NULL,
  region text NOT NULL,
  joined_on date NOT NULL
);
CREATE TABLE products (
  product_id integer PRIMARY KEY,
  name text NOT NULL,
  category text NOT NULL,
  price numeric(10,2) NOT NULL CHECK (price >= 0)
);
CREATE TABLE orders (
  order_id integer PRIMARY KEY,
  customer_id integer NOT NULL REFERENCES customers(customer_id),
  ordered_on date NOT NULL,
  status text NOT NULL CHECK (status IN ('paid','pending','cancelled'))
);
CREATE TABLE order_items (
  order_id integer NOT NULL REFERENCES orders(order_id),
  product_id integer NOT NULL REFERENCES products(product_id),
  quantity integer NOT NULL CHECK (quantity > 0),
  unit_price numeric(10,2) NOT NULL CHECK (unit_price >= 0),
  PRIMARY KEY (order_id, product_id)
);

INSERT INTO customers VALUES
 (1,'Ada','South','2026-01-03'),(2,'Ben','North','2026-01-07'),
 (3,'Cleo','South','2026-02-01'),(4,'Dee','West','2026-02-12');
INSERT INTO products VALUES
 (10,'Notebook','Stationery',8.00),(11,'Pen Set','Stationery',5.00),
 (12,'Mouse','Electronics',25.00);
INSERT INTO orders VALUES
 (100,1,'2026-03-01','paid'),(101,1,'2026-03-08','paid'),
 (102,2,'2026-03-10','paid'),(103,3,'2026-03-11','pending'),
 (104,2,'2026-03-12','cancelled');
INSERT INTO order_items VALUES
 (100,10,2,8.00),(100,11,1,5.00),
 (101,12,1,25.00),(102,10,1,8.00),
 (103,12,2,25.00),(104,11,3,5.00);
SELECT * FROM customers ORDER BY customer_id;
SELECT COUNT(*) AS orders, COUNT(DISTINCT customer_id) AS buyers FROM orders;

SELECT order_id, ordered_on, status
FROM orders
WHERE ordered_on >= DATE '2026-03-08'
  AND status = 'paid'
ORDER BY ordered_on DESC
LIMIT 10;

SELECT c.region,
       COUNT(DISTINCT o.order_id) AS paid_orders,
       COALESCE(SUM(oi.quantity * oi.unit_price),0) AS revenue
FROM customers c
JOIN orders o ON o.customer_id = c.customer_id
JOIN order_items oi ON oi.order_id = o.order_id
WHERE o.status = 'paid'
GROUP BY c.region
HAVING SUM(oi.quantity * oi.unit_price) >= 10
ORDER BY revenue DESC;

-- Every customer, including Dee with no orders:
SELECT c.name, COUNT(o.order_id) AS order_count
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.name
ORDER BY c.customer_id;
-- Expected: Ada 2, Ben 2, Cleo 1, Dee 0.

-- Count paid orders without accidentally dropping zero-order customers:
SELECT c.name,
       COUNT(o.order_id) FILTER (WHERE o.status = 'paid') AS paid_orders
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.name
ORDER BY c.customer_id;

WITH customer_revenue AS (
 SELECT c.customer_id, c.name,
        COALESCE(SUM(oi.quantity * oi.unit_price)
          FILTER (WHERE o.status = 'paid'),0) AS paid_revenue
 FROM customers c
 LEFT JOIN orders o ON o.customer_id = c.customer_id
 LEFT JOIN order_items oi ON oi.order_id = o.order_id
 GROUP BY c.customer_id, c.name
)
SELECT name, paid_revenue,
       DENSE_RANK() OVER (ORDER BY paid_revenue DESC) AS revenue_rank
FROM customer_revenue
ORDER BY paid_revenue DESC, name;

SELECT p.category,
       SUM(oi.quantity) AS units_sold,
       SUM(oi.quantity * oi.unit_price) AS revenue
FROM products p
JOIN order_items oi ON oi.product_id = p.product_id
JOIN orders o ON o.order_id = oi.order_id AND o.status = 'paid'
GROUP BY p.category
ORDER BY revenue DESC;

EXPLAIN (ANALYZE, BUFFERS, VERBOSE)
SELECT * FROM orders
WHERE customer_id = 1
ORDER BY ordered_on DESC;

CREATE INDEX idx_orders_customer_date
ON orders (customer_id, ordered_on DESC);
ANALYZE orders;

EXPLAIN (ANALYZE, BUFFERS)
SELECT * FROM orders
WHERE customer_id = 1
ORDER BY ordered_on DESC;

-- Run before and after each change; save both plans.
EXPLAIN (ANALYZE, BUFFERS)
SELECT o.customer_id, COUNT(*)
FROM orders o
WHERE o.status = 'paid'
  AND o.ordered_on >= DATE '2026-03-01'
GROUP BY o.customer_id;

CREATE INDEX idx_orders_paid_date_customer
ON orders (ordered_on, customer_id)
WHERE status = 'paid';
ANALYZE orders;

BEGIN;
UPDATE products SET price = price + 1 WHERE product_id = 10;
SELECT product_id, price FROM products WHERE product_id = 10;
ROLLBACK; -- Safe experiment: no permanent change

-- Example backup from your shell:
-- pg_dump -h localhost -U analyst -d shoplab -Fc -f shoplab.dump