create or replace function spread(str text) returns text
as $$
declare
  result text := '';
  i integer;
begin
  for i in 1 .. length(str) loop
    -- we add the space before the next character which prevents trailing spaces
    if i > 1 then
      result := result || ' ';
    end if;
    result := result || substr(str, i, 1);
  end loop;
  return result;
end;
$$ language plpgsql;