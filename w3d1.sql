-- ES.1
SELECT Citta FROM AEROPORTO WHERE NumPiste IS NULL; 

-- ES.2
SELECT TipoAereo FROM VOLO WHERE CittaPart = 'TORINO';

-- ES.3
SELECT CittaPart FROM VOLO WHERE CittaArr = 'BOLOGNA'; 

-- ES4
SELECT CittaPart, CittaArr FROM VOLO WHERE IdVolo = 'AZ274';

-- ES.5
SELECT TipoAereo, GiornoSett, OraPart FROM VOLO WHERE CittaPart LIKE 'B%O%' AND CittaArr LIKE'%E%A';