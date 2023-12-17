-- Sql script that creates a trigger that decreases
CREATE TRIGGER new_order 
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items SET quantity = quantity - NEW.number WHERE name = NEW.item_name;
