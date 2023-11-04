USE plantreminderdb;
DROP VIEW EventOfUsers;
DROP VIEW PlantNamesSpecies;

CREATE VIEW EventsOfUsers AS
SELECT SE.special_event_id, SE.event_name, SE.event_description, SE.event_date, P.plant_name, S.name, P.login FROM SpecialEvent SE, Plants P, Species S
WHERE SE.plant_id=P.plant_id AND S.species_id=P.plant_species;

CREATE VIEW PlantNamesSpecies AS
SELECT P.plant_id, P.login, P.plant_name, S.name
FROM Plants P
JOIN Species S ON S.species_id = P.plant_species;
