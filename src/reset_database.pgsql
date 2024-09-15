DO $$ 
DECLARE
    r RECORD;
BEGIN
    -- Alle Tabellen im public Schema durchlaufen
    FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = 'public') LOOP
        EXECUTE 'DROP TABLE IF EXISTS ' || quote_ident(r.tablename) || ' CASCADE';
    END LOOP;
END $$;