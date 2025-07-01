create or replace function 
  rfac(n integer) returns integer
as $$
begin
  if n < 0 then
    raise exception 'Negative input not allowed';
  elsif n = 0 then
    return 1;
  else
    return n * rfac(n - 1);
  end if;
end;
$$ language plpgsql;
