import csv, os
from getGeoLocation import getLatLon
from itertools import combinations

# pth = '/Users/katie/map-collections/map-collections-geocoding'
#
# csv_pth = os.path.join(pth, 'csvs')
# fname = 'clean_dataset_iz.csv'

# location_fields_1 = ['Bay / Harbor', 'Continent', 'County', 'Country', 'Department / Province / State', 'Island',
#                     'Island Group', 'Lake / Pond / Reservoir', 'Ocean', 'Specific Locale', 'River/Creek',
#                     'Sea / Gulf / Strait', 'Stream', 'City / Town / Hamlet']

location_fields_1 = ['Island', 'LocIslandName', 'City/Town/Hamlet', 'LocTownship', 'Stream', 'River/Creek',
                     'DraRiverBasin' 'Lake/Pond/Reservoir', 'LocIslandGrouping', 'Island Group', \
                     'Bay/Harbor', 'Loc/Bay/Sound' 'Department / Province / State', 'LocProvinceStateTerritory', \
                     'Country', 'Sea/Gulf/Strait', 'LocSeaGulf', 'LocOcean', 'Ocean']

location_cache = {}

def row_dict_to_query_strings(row_dict):
    return ','.join([row_dict[key] for key in location_fields_1 if len(row_dict[key]) > 1])

def row_dict_to_locations_list(row_dict):
    return [row_dict[key] for key in location_fields_1 if len(row_dict[key]) > 1]

def build_locations_arrays(locations):
    locations_arrays = [locations]
    if len(locations) > 1:
        locations_minus_one = [location_list for location_list in combinations(locations, len(locations) - 1)]
        locations_arrays.extend(locations_minus_one)
    if len(locations) > 2:
        locations_minus_two = [location_list for location_list in combinations(locations, len(locations) - 2)]
        locations_arrays.extend(locations_minus_two)
    return locations_arrays

def query_map_api(row_dict):
    tracking_number = row_dict['Tracking Number']
    found = False
    #locations = [row_dict[key] for key in location_fields_1 if key in row_dict and len(row_dict[key]) > 1]
    locations = []
    print(row_dict)
    for key in location_fields_1:
        if key in row_dict and len(row_dict[key]):
            locations.append(row_dict[key])
    print(locations)
    if ','.join(locations) in location_cache:
        return [tracking_number] + location_cache[','.join(locations)]
    locations_arrays = build_locations_arrays(locations)
    i = 0
    for locations_array in locations_arrays:
        i += 1
        if not found:
            print(','.join(locations_array))
            result = getLatLon(','.join(locations_array))
            lat = result['lat']; lon = result['lng']; found = result['found']
        if found:
            location_cache[','.join(locations)] = [lat, lon]
            return [tracking_number, lat, lon]
        if i > 20:
            return [tracking_number, '', '']

#with open(os.path.join(csv_pth, fname)) as csvfile:
#    reader = csv.DictReader(csvfile)
#    for row in reader:
#        query_map_api(row)













