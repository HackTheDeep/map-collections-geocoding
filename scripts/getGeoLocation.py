import geocoder
import googlemaps

def getLatLon(locationString, geoCodeKey='***REMOVED***', googleKey='***REMOVED***',preferred='geocoder'):
	ret_val = getLocationGeocoder(locationString, geoCodeKey) if preferred=='geocoder' else getLocationGoogle(locationString, googleKey)
	if(ret_val["found"]==False):
		ret_val = getLocationGoogle(locationString, googleKey) if preferred=='geocoder' else getLocationGeocoder(locationString, geoCodeKey)
	return ret_val

def getLocationGeocoder(locationString, a_key):
	g = geocoder.geonames(locationString, key=a_key)
	if(g.lat is None):
		return {"found":False}
	else:
		return {'lat':g.lat,'lng':g.lng,"found":True}

def getLocationGoogle(locationString, a_key):
	gmaps = googlemaps.Client(key=a_key)
	result = gmaps.geocode(locationString)
	if(len(result)>0):
		retVal = result[0]['geometry']['location']
		retVal.update({"found":True})
		return retVal
	else:
		return {"found":False}