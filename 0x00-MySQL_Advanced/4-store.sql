-- script that creates a trigger that decreases the quantity of an item after adding a new order.
DELIMITER $$
CREATE TRIGGER new_item_ordered
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
        SET items.quantity = items.quantity - NEW.number
        WHERE items.name = NEW.item_name;
END $$
DELIMITER ;
