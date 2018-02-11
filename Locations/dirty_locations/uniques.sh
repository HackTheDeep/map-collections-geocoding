cat oceans.csv | sort -u > oceans_unique.csv
cat countries.csv | sort -u > countries_unique.csv
cat continents.csv | sort -u > continents_unique.csv
cat states.csv | sort -u > states_unique.csv
cat counties.csv | sort -u > counties_unique.csv
cat cities.csv | sort -u > cities_unique.csv
cat locales.csv | sort -u > locales_unique.csv
find . -name "*.csv" | xargs wc -l > wordcounts.txt
