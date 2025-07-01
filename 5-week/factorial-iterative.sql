create or replace function 
  ifac(n integer) returns integer
as $$
declare
  i integer;
  result integer := 1;
  x record;
begin
  for i in 1..n loop
    result := result * i;
  end loop;
  return result;
end;
$$ language plpgsql;
