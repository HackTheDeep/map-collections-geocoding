/*
 *
 * This script creates the top-level organization of our database.
We need to make sure we're connected to the correct database and
that it has spatial capabilities.  We create a staging schema for initial
data imports.
*
*
*/

\c amnh

-- extend our database with PostGIS for spatial functionality
create schema if not exists postgis;
create extension if not exists postgis schema postgis;

create schema if not exists staging;
create schema if not exists amnh;

alter database amnh set search_path=public, postgis, staging, amnh;
