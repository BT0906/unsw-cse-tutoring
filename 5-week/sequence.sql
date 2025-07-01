create or replace function
  seq(start integer, stop integer) returns setof integer
as $$
begin
  for i in start..stop loop
    return next i;
  end loop;
  return;
end;
$$ language plpgsql;