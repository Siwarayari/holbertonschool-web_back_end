-- SQL script that lists all bands with
SELECT `band_name` , IFNULL(split, YEAR(CURDATE())) - formed as lifespan
FROM metal_bands Where `style` Like '%Glam Rock%';
