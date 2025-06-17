https://cgi.cse.unsw.edu.au/~cs3311/25T2/pracs/01/index.php

### Initial setup

1. `ssh vxdb02`
2. `3311 pginit`
3. `source /localstorage/${YOUR_ZID_HERE}/env` 
4. `p1`: start server
5. `p0`: stop server

### Trying it out

```sql
CREATE TABLE people (
    givenName   text,
    familyName  text,
    age         integer check (age > 0 and age < 150),
    balance     numeric(10,2),
    id          serial,
    PRIMARY KEY (givenName, familyName)
);

-- Insert data into the people table
INSERT INTO people (givenName, familyName, age, balance) VALUES
('John', 'Doe', 30, 1000.50),
('Jane', 'Smith', 25, 1500.75),
('Alice', 'Johnson', 40, 2000.00),
('Bob', 'Brown', 35, 1200.25),
('Charlie', 'Davis', 28, 1800.90);
```

1. Save this file as `test1.sql` 
2. Create a new database called `test1`
    - `createdb test1`
3. Dump the above file into our new database
    - `psql test1 -f test1.sql`
4. Open our newly created database
    - `psql test1`
5. Perform a simple query;
    - `select * from people;`
6. Exit
    - `\q` or `exit`