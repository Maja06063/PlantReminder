USE plantreminderdb;

DELETE FROM SpecialEvent;
DELETE FROM Plants;
DELETE FROM Species;
DELETE FROM UserName;

ALTER TABLE Species AUTO_INCREMENT = 1;
ALTER TABLE Plants AUTO_INCREMENT = 1;
ALTER TABLE SpecialEvent AUTO_INCREMENT = 1;

INSERT INTO UserName VALUES ('IrenkaSawicka', 123123, 'IrenkaSawicka@jourrapide.com ');
INSERT INTO UserName VALUES ('KorneliaKornelia',123123, 'KorneliaZajac@rhyta.com');
INSERT INTO UserName VALUES ('Mariusz23', 123123, 'MariuszSzczepanski@jourrapide.com');
INSERT INTO UserName VALUES ('Wiesiek78', 123123, 'WieslawWysocki@o2.pl');
INSERT INTO UserName VALUES ('KubaK', 123123, 'Jakub23@wp.pl');

INSERT INTO Species (name,watering_period,fertilization_period,light) VALUES ('Inny',0,0,0);
INSERT INTO Species (name,watering_period,fertilization_period,light) VALUES ('Gerbera',4,21,3);
INSERT INTO Species (name,watering_period,fertilization_period,light) VALUES ('Monstera',10,21,2);
INSERT INTO Species (name,watering_period,fertilization_period,light) VALUES ('Kaktus',21,28,3);
INSERT INTO Species (name,watering_period,fertilization_period,light) VALUES ('Wrzos',2,28,3);
INSERT INTO Species (name,watering_period,fertilization_period,light) VALUES ('Fikus',10,21,2);
INSERT INTO Species (name,watering_period,fertilization_period,light) VALUES ('Paproc',4,35,2);

INSERT INTO Plants (login,plant_species, plant_name,watering_period,fertilization_period,light,last_watering_date, last_fertilization_date, plant_description)
    VALUES ('IrenkaSawicka', 3, 'Ma�a monstera', 8, 20, 3, CAST( NOW() AS Date ), CAST( NOW() AS Date ), 'Ro�lina posiada prz�dziorki');

INSERT INTO Plants (login,plant_species,  plant_name, last_watering_date, last_fertilization_date, plant_description)
    VALUES ('IrenkaSawicka', 4, 'W kuchi', CAST( NOW() AS Date ), CAST( NOW() AS Date ), 'Nie przelewa�, lubi du�o s�o�ca');

INSERT INTO Plants (login, plant_species, last_watering_date, last_fertilization_date) VALUES ('IrenkaSawicka', 5, CAST( NOW() AS Date ), CAST( NOW() AS Date ));
INSERT INTO Plants (login, plant_species, last_watering_date, last_fertilization_date) VALUES ('Mariusz23', 1, CAST( NOW() AS Date ), CAST( NOW() AS Date ));
INSERT INTO Plants (login, plant_species,  plant_name, last_watering_date, last_fertilization_date) VALUES ('Mariusz23', 4, 'Ju� nie�ywa', CAST( NOW() AS Date ), CAST( NOW() AS Date ));
INSERT INTO Plants (login, plant_species, last_watering_date, last_fertilization_date) VALUES ('Wiesiek78', 5, CAST( NOW() AS Date ), CAST( NOW() AS Date ));
INSERT INTO Plants (login, plant_species, last_watering_date, last_fertilization_date) VALUES ('Wiesiek78', 2, CAST( NOW() AS Date ), CAST( NOW() AS Date ));
INSERT INTO Plants (login, plant_species, last_watering_date, last_fertilization_date) VALUES ('Wiesiek78', 6, CAST( NOW() AS Date ), CAST( NOW() AS Date ));
INSERT INTO Plants (login, plant_species, fertilization_period, last_watering_date, last_fertilization_date) VALUES ('KubaK', 5, 15, CAST( NOW() AS Date ), CAST( NOW() AS Date ));

INSERT INTO SpecialEvent (plant_id, event_name, event_description, event_date) VALUES (8, 'Opryskanie ro�liny ','Ro�lina ma prz�dzi�rki', '2023-09-01');
INSERT INTO SpecialEvent (plant_id, event_name, event_date) VALUES (7, 'Przesadzanie', '2023-09-03');
