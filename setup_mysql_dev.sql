-- Prepares a MySQL server for the project.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db . * TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema . * TO 'hbnb_dev'@'localhost';

-- mysql -u hbnb_dev -p
-- hbnb_dev_pwd
-- USE hbnb_dev_db;
-- # 953b9aed-df48-4298-9118-be87ffd598fe STATE
-- # 7ccd2bcb-b447-4b42-b290-678111c80207 CITY 
-- # dbfc557e-0454-4988-b2ff-d117488083f2 CITY
-- # 30c2a559-48fe-4940-a166-026f36713e61 USER
-- #  create Place city_id="7ccd2bcb-b447-4b42-b290-678111c80207" user_id="30c2a559-48fe-4940-a166-026f36713e61" name="Lovely_place" number_rooms=3 number_bathrooms=1 max_guest=6 price_by_night=120 latitude=37.773972 longitude=-122.431297