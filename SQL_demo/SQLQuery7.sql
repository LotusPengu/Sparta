CREATE TABLE ice_cream (
	id INT,
	flavour VARCHAR (20),
	price DECIMAL (4,2)
);

INSERT INTO ice_cream
	(id, flavour, price)
VALUES
	(1, 'Vanilla', 3.99),
	(2, 'Chocolate Chip', 3.99),
	(3, 'Raspberry Ripple', 3.99);

SELECT * FROM ice_cream

UPDATE ice_cream
	SET flavour = 'Mint Chocolate Chip'
	WHERE id = 2;

UPDATE ice_cream
	SET price = 4.99
	WHERE price = 3.99;

DELETE FROM ice_cream
	WHERE flavour = 'Raspberry Ripple'
	-- may also use id = 3