import geocoder
import googlemaps
from bingmaps.apiservices import LocationByQuery
from keys import googleKey, geoCodeKey, bingKey

def getLocationGeocoder(locationString):
	g = geocoder.geonames(locationString, key=geoCodeKey)
	if(g.lat is None):
		return {"found":False,"lat":"","lng":""}
	else:
		return {'lat':g.lat,'lng':g.lng,"found":True}

def getLocationGoogle(locationString):
	gmaps = googlemaps.Client(key=googleKey)
	result = gmaps.geocode(locationString)
	if(len(result)>0):
		retVal = result[0]['geometry']['location']
		retVal.update({"found":True,"lat":"","lng":""})
		return retVal
	else:
		return {"found":False,"lat":"","lng":""}

def getLocationBing(locationString):
	result = LocationByQuery({'q':locationString,"key":bingKey,"maxResults":"1"})
	coords = result.get_coordinates
	return {"found":False,"lat":"","lng":""} if len(coords)==0 else {'lat':coords[0].latitude,'lng':coords[0].longitude,"found":True}

geoCoders = {'geocoder':getLocationGeocoder,'google':getLocationGoogle,'bing':getLocationBing}

def getLatLon(locationString,order=['geocoder','google','bing']):
	param={"locationString":locationString}
	for function_shorthand in order:
		ret_val=geoCoders[function_shorthand](**param)
		if(ret_val["found"]==True):
			return ret_val
	return {"found":False,"lat":"","lng":""}