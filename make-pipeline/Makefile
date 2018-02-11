#	Set database connection variables.  Will read from environment variables if provided.
PGHOST?=localhost
PGUSER?=postgres
PGPORT?=5432
PGDATABASE=amnh

dbconn = "host=$(PGHOST) user=$(PGUSER) port=$(PGPORT) dbname=$(PGDATABASE)"

all: iz_clean ornithology ornithology.geojson

iz_clean: setup-db
	psql $(PGDATABASE) -f ./sql/iz_clean.sql

# requires gdal & ogr2ogr to be installed for this to work
ornithology.geojson: ornithology
	ogr2ogr -f "GeoJSON" ornithology.geojson \
	PG:$(dbconn) \
	-sql "select * from amnh.ornithology where geom is not null"
ornithology: setup-db
	psql $(PGDATABASE) -f ./sql/ornithology.sql

setup-db:
	psql -tc "SELECT 1 FROM pg_database WHERE datname = '$(PGDATABASE)'" | grep -q 1 || psql -c "CREATE DATABASE $(PGDATABASE)"
	psql $(PGDATABASE) -f ./sql/setup.sql
