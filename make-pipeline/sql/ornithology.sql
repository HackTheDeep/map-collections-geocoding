begin;

drop table if exists staging.ornithology cascade;

create table staging.ornithology(
  prepirn integer,
  cat_prefix text,
  cat_number text,
  cat_suffix text,
  bio_date_visited_from text,
  bio_date_visited_to text,
  exp_expedition_name text,
  bio_participant text,
  cla_order text,
  cla_family text,
  cla_genus text,
  cla_species text,
  cla_subspecies text,
  loc_continent text,
  loc_country text,
  loc_district_county_shire text,
  loc_island_grouping text,
  loc_island_name text,
  loc_ocean text,
  loc_precise_location text,
  loc_province_state_territory text,
  loc_sea_gulf text,
  loc_township text,
  ter_elevation_from_met text,
  ter_elevation_to_met text,
  ter_verbatim_elevation text,
  lat_preferred_centroid_lat_dec text,
  lat_preferred_centroid_lng_dec text
);

-- imports using psql \copy utility
-- filepaths are relative to where this is called from
-- this assumes you are calling "make" from the project root directory
\copy staging.ornithology FROM './ornithology_aquatic_localities.tsv' with csv header delimiter E'\t' null ''

-- add a primary key to the table
alter table staging.ornithology add column id serial primary key;

drop table if exists amnh.ornithology cascade;
-- create a new table with the cleaned, geographic data
create table amnh.ornithology as (
  select
    id,
    prepirn,
    cat_prefix,
    cat_number,
    cat_suffix,
    bio_date_visited_from, -- ideally cast to date with bio_date_visited_from::date.  Need to clean.
    bio_date_visited_to, -- same as above
    exp_expedition_name,
    bio_participant,
    cla_order,
    cla_family,
    cla_genus,
    cla_species,
    cla_subspecies,
    loc_continent,
    loc_country,
    loc_district_county_shire,
    loc_island_grouping,
    loc_island_name,
    loc_ocean,
    loc_precise_location,
    loc_province_state_territory,
    loc_sea_gulf,
    loc_township,
    ter_elevation_from_met,
    ter_elevation_to_met,
    ter_verbatim_elevation,
    ST_SetSRID(ST_MakePoint(lat_preferred_centroid_lng_dec::numeric, lat_preferred_centroid_lat_dec::numeric), 4326)::geometry(point, 4326)::geometry(point, 4326) as geom
  from staging.ornithology
);


commit;
