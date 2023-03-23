-- find man by id. who fits all the criteria
--there is a suspicious coincidence. since during the check it turned out that 3 teams were almost simultaneously there and worked according to the same scheme.
-- maybe the other 2 teams belayed Bruce
SELECT *
FROM people
WHERE id IN
(select person_id
FROM bank_accounts
WHERE account_number IN
-- find people at the ATM
(SELECT account_number FROM atm_transactions WHERE year = 2021 AND day = 28 AND month = 7 AND transaction_type = 'withdraw' AND atm_location ='Leggett Street'))
AND phone_number IN
-- find people by phone number
(SELECT caller FROM phone_calls WHERE year = 2021 AND day = 28 AND month = 7 AND duration < 60)
AND license_plate IN
-- find people by license plate
(SELECT license_plate FROM bakery_security_logs WHERE year = 2021 AND day =28 AND hour=10 AND minute > 15 AND minute < 30 AND activity='exit')
AND passport_number IN
-- find people by flight id
(SELECT passport_number
FROM passengers
WHERE flight_id IN
(SELECT id FROM flights WHERE origin_airport_id = (SELECT id FROM airports WHERE city = 'Fiftyville') AND year = 2021 AND day = 29 AND month = 7 ORDER BY hour LIMIT 1));



-- find helper by phone number
SELECT name
FROM people
WHERE phone_number IN
(SELECT receiver FROM phone_calls WHERE day = 28 AND month = 7 AND duration < 60 AND caller = '(367) 555-5533');


-- find the city by passport number
SELECT *
FROM airports
WHERE id =
(SELECT destination_airport_id FROM flights WHERE id = (SELECT flight_id FROM passengers WHERE flight_id IN
(SELECT id FROM flights WHERE origin_airport_id = (SELECT id FROM airports WHERE city = 'Fiftyville') AND day = 29 AND month = 7)
AND passport_number= 5773159633));
