create or replace function
  sqr(n integer) returns integer
as $$
begin
  return n * n;
end;
$$ language plpgsql;