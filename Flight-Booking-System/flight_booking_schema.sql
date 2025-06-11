
-- Create the main flight booking table
CREATE TABLE IF NOT EXISTS flightbook (
    flightno INT PRIMARY KEY,
    bcity VARCHAR(100),
    dcity VARCHAR(100),
    jtime TIME,
    fare INT,
    airline VARCHAR(100)
);

-- Sample data to populate the flightbook table
INSERT INTO flightbook (flightno, bcity, dcity, jtime, fare, airline) VALUES
(1, 'Raipur', 'Mumbai', '10:00:00', 11000, 'Indigo'),
(2, 'Raipur', 'Delhi', '20:00:00', 14000, 'Vistara'),
(3, 'Mumbai', 'Delhi', '01:00:00', 5000, 'Indigo'),
(4, 'Delhi', 'Kolkata', '21:00:00', 8500, 'SpiceJet'),
(5, 'Delhi', 'Chennai', '23:00:00', 20000, 'AirIndia'),
(6, 'Delhi', 'Paris', '07:00:00', 40000, 'Etihad Airways'),
(7, 'Delhi', 'Dubai', '16:00:00', 30000, 'Emirates'),
(8, 'Delhi', 'NewYork', '19:00:00', 46000, 'Qatar Airways'),
(9, 'Mumbai', 'Tokyo', '00:00:00', 68000, 'Akasa Air'),
(10, 'Mumbai', 'Mauritius', '13:00:00', 35000, 'Emirates');

-- User authentication table
CREATE TABLE IF NOT EXISTS user_detail (
    USERNAME VARCHAR(100),
    EMAIL_ADDRESS VARCHAR(100) PRIMARY KEY,
    PASSWORD VARCHAR(100)
);

-- Passenger booking table (dropped and created dynamically at runtime)
CREATE TABLE IF NOT EXISTS passengers (
    PASSENGERNO INT,
    PASSENGER_NAME VARCHAR(100),
    GENDER VARCHAR(20),
    AGE INT,
    SEAT VARCHAR(10)
);
