# 🗄️ SQL практика (sql-ex.ru)

В данном файле собраны решения задач с платформы [sql-ex.ru](https://www.sql-ex.ru/).

Каждая задача включает:
- условие задачи
- итоговый запрос

Схемы таблиц с данными доступны по [ссылке](https://www.sql-ex.ru/help/select13.php)

## Задача 1: Найдите номер модели, скорость и размер жесткого диска для всех ПК стоимостью менее 500 дол. 
Вывести: model, speed и hd  
Таблица: Компьютерная фирма

```sql
SELECT model, speed, hd
FROM pc
WHERE price < 500
```

## Задача 2: Найдите производителей принтеров. 
Вывести: maker  
Таблица: Компьютерная фирма

```sql
SELECT DISTINCT maker
FROM Product
WHERE type = 'Printer'
```

## Задача 3: Найдите номер модели, объем памяти и размеры экранов ноутбуков, цена которых превышает 1000 дол.
Таблица: Компьютерная фирма

```sql
SELECT model, ram, screen
FROM Laptop
WHERE price > 1000
```

## Задача 4: Найдите все записи таблицы Printer для цветных принтеров.
Таблица: Компьютерная фирма

```sql
Select *
FROM Printer 
WHERE color = 'y'
```

## Задача 5: Найдите номер модели, скорость и размер жесткого диска ПК, имеющих 12x или 24x CD и цену менее 600 дол.
Таблица: Компьютерная фирма

```sql
SELECT model, speed, hd
FROM PC 
WHERE (cd = '24x' OR cd = '12x') AND price < 600
```

## Задача 6: Для каждого производителя, выпускающего ноутбуки c объёмом жесткого диска не менее 10 Гбайт, найти скорости таких ноутбуков. 
Вывести: производитель, скорость.  
Таблица: Компьютерная фирма

```sql
SELECT DISTINCT maker, speed
FROM Product p
JOIN Laptop l ON p.model = l.model
WHERE l.hd >= 10
```

## Задача 7: Найдите номера моделей и цены всех имеющихся в продаже продуктов (любого типа) производителя B (латинская буква).
Таблица: Компьютерная фирма

```sql
SELECT model, price
FROM (
    SELECT p.model, pc.price
    FROM Product p
    JOIN PC pc ON p.model = pc.model
    WHERE p.maker = 'B'
    
    UNION
    
    SELECT p.model, l.price
    FROM Product p
    JOIN Laptop l ON p.model = l.model
    WHERE p.maker = 'B'
    
    UNION
    
    SELECT p.model, prin.price
    FROM Product p
    JOIN Printer prin ON p.model = prin.model
    WHERE p.maker = 'B'
) AS t
```

## Задача 8: Найдите производителя, выпускающего ПК, но не ноутбуки.
Таблица: Компьютерная фирма

```sql
SELECT maker
FROM Product 
WHERE type = 'PC'

EXCEPT

SELECT maker
FROM Product 
WHERE type = 'Laptop'
```

## Задача 9: Найдите производителей ПК с процессором не менее 450 Мгц. 
Вывести: Maker  
Таблица: Компьютерная фирма

```sql
SELECT DISTINCT maker
FROM Product
JOIN PC ON Product.model = PC.model 
WHERE CAST(REPLACE(PC.speed, 'Мгц', '') AS INT) >= 450
```

## Задача 10: Найдите модели принтеров, имеющих самую высокую цену. 
Вывести: model, price  
Таблица: Компьютерная фирма

```sql
SELECT model, price 
FROM Printer
WHERE price = (SELECT MAX(price) FROM Printer)

```

## Задача 11: Найдите среднюю скорость ПК.
Таблица: Компьютерная фирма

```sql   
SELECT AVG(speed)
FROM PC
```

## Задача 12: Найдите среднюю скорость ноутбуков, цена которых превышает 1000 дол.
Таблица: Компьютерная фирма

```sql   
SELECT AVG(speed)
FROM Laptop
WHERE price > 1000
```

## Задача 13: Найдите среднюю скорость ПК, выпущенных производителем A.
Таблица: Компьютерная фирма

```sql   
SELECT AVG(PC.speed)
FROM PC
JOIN Product p ON p.model = PC.model
WHERE p.maker = 'A'
```

## Задача 14: Найдите класс, имя и страну для кораблей из таблицы Ships, имеющих не менее 10 орудий.
Таблица: Корабли

```sql
SELECT s.class, s.name, c.country
FROM Classes c
JOIN Ships s ON s.class = c.class
WHERE numGuns >= 10
```

## Задача 15: Найдите размеры жестких дисков, совпадающих у двух и более PC. 
Вывести: HD  
Таблица: Компьютерная фирма

```sql   
SELECT hd
FROM PC
GROUP BY hd
HAVING COUNT(code) >= 2
```

## Задача 16: Найдите пары моделей PC, имеющих одинаковые скорость и RAM. В результате каждая пара указывается только один раз, т.е. (i,j), но не (j,i) 
Вывести: модель с большим номером, модель с меньшим номером, скорость и RAM.  
Таблица: Компьютерная фирма

```sql
SELECT DISTINCT(p1.model), p2.model, p1.speed, p1.ram
FROM PC p1
JOIN PC p2 ON p1.speed= p2.speed AND p1.ram = p2.ram
WHERE p1.model > p2.model
```

## Задача 17: Найдите модели ноутбуков, скорость которых меньше скорости каждого из ПК.
Вывести: type, model, speed  
Таблица: Компьютерная фирма

```sql
SELECT DISTINCT p.type, l.model, l.speed
FROM Laptop l
JOIN Product p ON p.model = l.model
WHERE l.speed < (SELECT MIN(speed) FROM PC)
```

## Задача 18: Найдите производителей самых дешевых цветных принтеров. 
Вывести: maker, price  
Таблица: Компьютерная фирма

```sql
SELECT DISTINCT maker, price
FROM Product
JOIN Printer ON Product.model = Printer.model
WHERE color = 'y'
  AND price = (SELECT MIN(price) FROM Printer WHERE color = 'y')
```

## Задача 19: Для каждого производителя, имеющего модели в таблице Laptop, найдите средний размер экрана выпускаемых им ноутбуков.
Вывести: maker, средний размер экрана.  
Таблица: Компьютерная фирма

```sql
SELECT p.maker, AVG(l.screen) AS avg_screen_size
FROM Laptop l 
LEFT JOIN Product p ON p.model = l.model 
GROUP BY p.maker
```

## Задача 20: Найдите производителей, выпускающих по меньшей мере три различных модели ПК. 
Вывести: Maker, число моделей ПК.  
Таблица: Компьютерная фирма

```sql
SELECT maker, COUNT(model) AS count_model
FROM Product p
WHERE type = 'PC'
GROUP BY maker 
HAVING COUNT(maker) >= 3
```

## Задача 21: Найдите максимальную цену ПК, выпускаемых каждым производителем, у которого есть модели в таблице PC.
Вывести: maker, максимальная цена.  
Таблица: Компьютерная фирма

```sql
SELECT p.maker, MAX(pc.price) AS max_price
FROM Product p
JOIN PC pc ON pc.model = p.model
GROUP BY p.maker
```

## Задача 22: Для каждого значения скорости ПК, превышающего 600 МГц, определите среднюю цену ПК с такой же скоростью. 
Вывести: speed, средняя цена.  
Таблица: Компьютерная фирма

```sql
SELECT DISTINCT speed, AVG(price) AS avg_price
FROM PC pc
WHERE speed > 600
GROUP BY speed
```

## Задача 23: Найдите производителей, которые производили бы как ПК со скоростью не менее 750 МГц, так и ноутбуки со скоростью не менее 750 МГц.
Вывести: Maker  
Таблица: Компьютерная фирма

```sql
SELECT p.maker 
FROM Product p
LEFT JOIN PC pc ON pc.model = p.model
WHERE pc.speed >= 750 

INTERSECT

SELECT p.maker 
FROM Product p
LEFT JOIN Laptop l ON l.model = p.model
WHERE l.speed >= 750
```

## Задача 24: Перечислите номера моделей любых типов, имеющих самую высокую цену по всей имеющейся в базе данных продукции.
Таблица: Компьютерная фирма

```sql
SELECT model 
FROM PC
WHERE price = (SELECT max(price) FROM (SELECT price FROM PC UNION ALL SELECT price FROM Laptop UNION ALL SELECT price FROM Printer) AS t)

UNION 

SELECT model 
FROM Laptop
WHERE price = (SELECT max(price) FROM (SELECT price FROM PC UNION ALL SELECT price FROM Laptop UNION ALL SELECT price FROM Printer) AS t)

UNION 

SELECT model 
FROM Printer
WHERE price = (SELECT max(price) FROM (SELECT price FROM PC UNION ALL SELECT price FROM Laptop UNION ALL SELECT price FROM Printer) AS t)
```

## Задача 25: Найдите производителей принтеров, которые производят ПК с наименьшим объемом RAM и с самым быстрым процессором среди всех ПК, имеющих наименьший объем RAM. 
Вывести: Maker  
Таблица: Компьютерная фирма

```sql
SELECT  DISTINCT p.maker 
FROM Product p
WHERE model IN (
SELECT model 
FROM PC 
WHERE ram = (SELECT MIN(ram) FROM PC)
and speed = (SELECT MAX(speed) FROM PC WHERE ram = (SELECT MIN(ram) FROM PC))
)
and p.maker IN (
SELECT maker
FROM Product 
WHERE type = 'Printer'
)
```

## Задача 26: Найдите среднюю цену ПК и ноутбуков, выпущенных производителем A (латинская буква). 
Вывести: одна общая средняя цена.  
Таблица: Компьютерная фирма

```sql
SELECT AVG(price)
FROM (
    SELECT price
    FROM PC pc
    JOIN Product p ON p.model = pc.model
    WHERE p.maker = 'A'

    UNION ALL

    SELECT price
    FROM Laptop l
    JOIN Product p ON p.model = l.model
    WHERE p.maker = 'A'
) AS t;
```

## Задача 27: Найдите средний размер диска ПК каждого из тех производителей, которые выпускают и принтеры. 
Вывести: maker, средний размер HD.   
Таблица: Компьютерная фирма

```sql
SELECT p.maker, AVG(pc.hd)
FROM PC pc
JOIN Product p ON p.model = pc.model
WHERE p.maker IN (SELECT maker FROM Product WHERE type = 'Printer')
GROUP BY p.maker
```

## Задача 28: Используя таблицу Product, определить количество производителей, выпускающих по одной модели.
Таблица: Компьютерная фирма

```sql
SELECT COUNT(*)
FROM (
    SELECT maker
    FROM Product
    GROUP BY maker
    HAVING COUNT(*) = 1
) t
```

## Задача 29: В предположении, что приход и расход денег на каждом пункте приема фиксируется не чаще одного раза в день [т.е. первичный ключ (пункт, дата)], написать запрос с выходными данными (пункт, дата, приход, расход). Использовать таблицы Income_o и Outcome_o.
Таблица: Фирма вторсырья

```sql
SELECT
    COALESCE(i.point, o.point) AS point,
    COALESCE(i.date, o.date) AS date,
    i.inc,
    o.out
FROM Income_o i
FULL JOIN Outcome_o o
    ON i.point = o.point
   AND i.date = o.date
```

## Задача 30: В предположении, что приход и расход денег на каждом пункте приема фиксируется произвольное число раз (первичным ключом в таблицах является столбец code), требуется получить таблицу, в которой каждому пункту за каждую дату выполнения операций будет соответствовать одна строка.
Вывод: point, date, суммарный расход пункта за день (out), суммарный приход пункта за день (inc). Отсутствующие значения считать неопределенными (NULL).  
Таблица: Фирма вторсырья

```sql
SELECT 
    COALESCE(i.point, o.point) AS point,
    COALESCE(i.date, o.date) AS date,
    o.out AS outcome,
    i.inc AS income
FROM
(
    SELECT point, date, SUM(inc) AS inc
    FROM Income
    GROUP BY point, date
) i
FULL JOIN
(
    SELECT point, date, SUM(out) AS out
    FROM Outcome
    GROUP BY point, date
) o
ON i.point = o.point 
AND i.date = o.date;
```

## Задача 31: Для классов кораблей, калибр орудий которых не менее 16 дюймов, укажите класс и страну.
Таблица: Корабли

```sql
SELECT class, country 
FROM Classes
WHERE bore >= 16
```

## Задача 32: Одной из характеристик корабля является половина куба калибра его главных орудий (mw). С точностью до 2 десятичных знаков определите среднее значение mw для кораблей каждой страны, у которой есть корабли в базе данных.
Таблица: Корабли

```sql
SELECT country,
       CAST(AVG(POWER(bore, 3) / 2) AS NUMERIC(10, 2))
FROM (
    SELECT country, bore, name
    FROM Classes c
    INNER JOIN Ships s ON s.class = c.class

    UNION

    SELECT country, bore, class
    FROM Classes c
    INNER JOIN Outcomes o 
        ON o.ship = c.class
       AND o.ship NOT IN (SELECT DISTINCT name FROM Ships)
) AS n
GROUP BY country;
```

## Задача 33: Укажите корабли, потопленные в сражениях в Северной Атлантике (North Atlantic). 
Вывод: ship  
Таблица: Корабли

```sql
SELECT ship
FROM Outcomes
WHERE battle = 'North Atlantic' AND result = 'sunk'
```