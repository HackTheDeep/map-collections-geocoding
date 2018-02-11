import pip

try:
	import geocoder
except ImportError:
	pip.main(['install','geocoder'])
	import geocoder
	
try:
	import googlemaps
except ImportError:
	pip.main(['install','googlemaps'])
	import googlemaps

def getLatLon(locationString, geoCodeKey='oceanocoders', googleKey='AIzaSyA3k5SpAOOdB0Bw92ZYcHDb6GTzxlJvMBg'):
	g = geocoder.geonames(locationString, key=geoCodeKey)
	if(g.lat is None):
		gmaps = googlemaps.Client(key=googleKey)
		result = gmaps.geocode(locationString)
		return result[0]['geometry']['location']
	else:
		return {'lat':g.lat,'lng':g.lng}