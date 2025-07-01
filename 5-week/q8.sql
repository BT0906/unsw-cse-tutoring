create or replace function 
  hotelsIn(_addr text) returns text
as $$
declare
  howmany integer;
  result text;
  p record;
begin
  select count(*) into howmany from Bars where addr = _addr;

  if (howmany = 0) then
    return 'There are no hotels in ' || _addr;
  end if;

  result := 'Hotels in ' || _addr || ':';

  for p in select * from Bars where addr = _addr
  loop
    result := result || ' ' || p.name;
  end loop;
  return result;
end;
$$ language plpgsql;