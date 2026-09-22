SELECT
    rental_id,
    COUNT(*) AS qtd_pagamentos
FROM payment
GROUP BY rental_id
HAVING COUNT(*) > 1;

SELECT *
FROM payment
WHERE rental_id = 4591;

SELECT *
FROM rental
WHERE rental_id = 4591;