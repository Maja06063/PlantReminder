USE plantreminderdb;

DELETE FROM specialevent;
DELETE FROM plants;
DELETE FROM species;
DELETE FROM username;

ALTER TABLE species AUTO_INCREMENT = 1;
ALTER TABLE plants AUTO_INCREMENT = 1;
ALTER TABLE specialevent AUTO_INCREMENT = 1;

INSERT INTO username VALUES ('IrenkaSawicka', 123123, 'IrenkaSawicka@jourrapide.com ');
INSERT INTO username VALUES ('KorneliaKornelia',123123, 'KorneliaZajac@rhyta.com');
INSERT INTO username VALUES ('Mariusz23', 123123, 'MariuszSzczepanski@jourrapide.com');
INSERT INTO username VALUES ('Wiesiek78', 123123, 'WieslawWysocki@o2.pl');
INSERT INTO username VALUES ('KubaK', 123123, 'Jakub23@wp.pl');

INSERT INTO species (name,watering_period,fertilization_period,light,species_description) VALUES ('Inny',0,0,0,'Gatunek, którego nie znaleziono na liœcie.');
INSERT INTO species (name,watering_period,fertilization_period,light,species_description) VALUES ('Gerbera',4,21,3,'Dane przedstawione s¹ dla okresu wiosna/lato');
INSERT INTO species (name,watering_period,fertilization_period,light,species_description) VALUES ('Monstera',10,21,2,'Dane przedstawione s¹ dla okresu wiosna/lato');
INSERT INTO species (name,watering_period,fertilization_period,light,species_description) VALUES ('Kaktus',21,28,3,'Dane przedstawione s¹ dla okresu wiosna/lato');
INSERT INTO species (name,watering_period,fertilization_period,light,species_description) VALUES ('Wrzos',2,28,3,'Dane przedstawione s¹ dla okresu wiosna/lato');
INSERT INTO species (name,watering_period,fertilization_period,light,species_description) VALUES ('Fikus',10,21,2,'Dane przedstawione s¹ dla okresu wiosna/lato');
INSERT INTO species (name,watering_period,fertilization_period,light,species_description) VALUES ('Paproc',4,35,2,'Dane przedstawione s¹ dla okresu wiosna/lato');

INSERT INTO plants (login,plant_species,plant_description,watering_period,fertilization_period,light,added_date)
    VALUES ('IrenkaSawicka', 3, 'Ma³a monstera', 8, 20, 3, CAST( NOW() AS Date ));
    
INSERT INTO plants (login,plant_species, plant_description, added_date)
    VALUES ('IrenkaSawicka', 4, 'W kuchi', CAST( NOW() AS Date ));
    
INSERT INTO plants (login, plant_species, added_date) VALUES ('IrenkaSawicka', 5, CAST( NOW() AS Date ));
INSERT INTO plants (login, plant_species, added_date) VALUES ('Mariusz23', 1, CAST( NOW() AS Date ));
INSERT INTO plants (login, plant_species, plant_description, added_date) VALUES ('Mariusz23', 4, 'Ju¿ nie¿ywa', CAST( NOW() AS Date ));
INSERT INTO plants (login, plant_species, added_date) VALUES ('Wiesiek78', 5, CAST( NOW() AS Date ));
INSERT INTO plants (login, plant_species, added_date) VALUES ('Wiesiek78', 2, CAST( NOW() AS Date ));
INSERT INTO plants (login, plant_species, added_date) VALUES ('Wiesiek78', 6, CAST( NOW() AS Date ));
INSERT INTO plants (login, plant_species, fertilization_period, added_date) VALUES ('KubaK', 5, 15, CAST( NOW() AS Date ));

INSERT INTO specialevent (plant_id, event_name, event_description, event_date) VALUES (8, 'Opryskanie roœliny ','Roœlina ma przêdzi¹rki', '2023-09-01');
INSERT INTO specialevent (plant_id, event_name, event_date) VALUES (7, 'Przesadzanie', '2023-09-03');
