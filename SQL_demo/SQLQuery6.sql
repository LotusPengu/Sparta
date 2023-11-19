ALTER TABLE films
	ADD budget DECIMAL (10,0), synopsis VARCHAR (200);

ALTER TABle films
	ALTER COLUMN runtime_mins DECIMAL (5,2);

ALTER TABLE films
	DROP COLUMN box_office_usd;
