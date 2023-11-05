USE plantreminderdb;

DELETE FROM SpecialEvent;
DELETE FROM Plants;
DELETE FROM Species;
DELETE FROM UserName;

ALTER TABLE Species AUTO_INCREMENT = 1;
ALTER TABLE Plants AUTO_INCREMENT = 1;
ALTER TABLE SpecialEvent AUTO_INCREMENT = 1;

INSERT INTO UserName VALUES ('IrenkaSawicka', "4297f44b13955235245b2497399d7a93", 'IrenkaSawicka@jourrapide.com ');
INSERT INTO UserName VALUES ('KorneliaKornelia',"4297f44b13955235245b2497399d7a93", 'KorneliaZajac@rhyta.com');
INSERT INTO UserName VALUES ('Mariusz23', "4297f44b13955235245b2497399d7a93", 'MariuszSzczepanski@jourrapide.com');
INSERT INTO UserName VALUES ('Wiesiek78', "4297f44b13955235245b2497399d7a93", 'WieslawWysocki@o2.pl');
INSERT INTO UserName VALUES ('KubaK', "4297f44b13955235245b2497399d7a93", 'Jakub23@wp.pl');

INSERT INTO Species (name,watering_period,fertilization_period) VALUES ('Inny',0,0);
INSERT INTO Species (name,watering_period,fertilization_period) VALUES ('Gerbera',4,21);
INSERT INTO Species (name,watering_period,fertilization_period) VALUES ('Monstera',10,21);
INSERT INTO Species (name,watering_period,fertilization_period) VALUES ('Kaktus',21,28);
INSERT INTO Species (name,watering_period,fertilization_period) VALUES ('Wrzos',2,28);
INSERT INTO Species (name,watering_period,fertilization_period) VALUES ('Fikus',10,21);
INSERT INTO Species (name,watering_period,fertilization_period) VALUES ('Paproæ',4,35);

INSERT INTO Plants (login,plant_species, plant_name,watering_period,fertilization_period,last_watering_date, last_fertilization_date, plant_description)
    VALUES ('IrenkaSawicka', 3, 'Ma³a monstera', 8, 20, CAST( NOW() AS Date ), CAST( NOW() AS Date ), 'Roœlina posiada przêdziorki');

INSERT INTO Plants (login,plant_species,  plant_name, last_watering_date, last_fertilization_date, plant_description)
    VALUES ('IrenkaSawicka', 4, 'W kuchi', CAST( NOW() AS Date ), CAST( NOW() AS Date ), 'Nie przelewaæ, lubi du¿o s³oñca');

INSERT INTO Plants (login, plant_species, last_watering_date, last_fertilization_date) VALUES ('IrenkaSawicka', 5, CAST( NOW() AS Date ), CAST( NOW() AS Date ));
INSERT INTO Plants (login, plant_species, last_watering_date, last_fertilization_date) VALUES ('Mariusz23', 1, CAST( NOW() AS Date ), CAST( NOW() AS Date ));
INSERT INTO Plants (login, plant_species,  plant_name, last_watering_date, last_fertilization_date) VALUES ('Mariusz23', 4, 'Ju¿ nie¿ywa', CAST( NOW() AS Date ), CAST( NOW() AS Date ));
INSERT INTO Plants (login, plant_species, last_watering_date, last_fertilization_date) VALUES ('Wiesiek78', 5, CAST( NOW() AS Date ), CAST( NOW() AS Date ));
INSERT INTO Plants (login, plant_species, last_watering_date, last_fertilization_date) VALUES ('Wiesiek78', 2, CAST( NOW() AS Date ), CAST( NOW() AS Date ));
INSERT INTO Plants (login, plant_species, last_watering_date, last_fertilization_date) VALUES ('Wiesiek78', 6, CAST( NOW() AS Date ), CAST( NOW() AS Date ));
INSERT INTO Plants (login, plant_species, fertilization_period, last_watering_date, last_fertilization_date) VALUES ('KubaK', 5, 15, CAST( NOW() AS Date ), CAST( NOW() AS Date ));

INSERT INTO SpecialEvent (plant_id, event_name, event_description, event_date) VALUES (8, 'Opryskanie roœliny ','Roœlina ma przêdziorki', '2023-09-01');
INSERT INTO SpecialEvent (plant_id, event_name, event_date) VALUES (7, 'Przesadzanie', '2023-09-03');
INSERT INTO SpecialEvent (plant_id, event_name, event_date) VALUES (8, 'Kupno nowej doniczki', '2023-09-03');
INSERT INTO SpecialEvent (plant_id, event_name, event_date) VALUES (8, 'Opryskanie roœliny',  CAST( NOW() AS Date ));