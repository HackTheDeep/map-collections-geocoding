### AMNH Collections PostgreSQL Data Pipeline  

This directory contains a makefile that will import collections data into a PostgreSQL database and output into GeoJSON.

**Usage**  

These require a postgres database (can use localhost) available, and GDAL/OGR2OGR (for the geojson outputs).
1.  Configure environment variables.  These have sensible defaults if you don't set them.  The makefile will create a database called `amnh`.
```shell
$ export PGHOST=[localhost | remote_database]  
$ export PGUSER=[yourusername]
$ export PGPORT=[port]
```  
2.  Run make rules as needed:
```shell
$ make all #runs all the scripts
$ make ornithology # creates pg table
$ make ornithology.geojson # requires ogr2ogr
```  
