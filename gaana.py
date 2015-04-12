
import urllib2

import simplejson

class gaana:

	def __init__(self):
		self.base_url = "http://api.gaana.com/"

	def getTracks(self,
				  subtype = 'most_popular',
				  token = None,
				  output_format = None,
				  order = None,
				  language = None):

		params = {}

		if subtype in ["most_popular" , "hot_songs" ,"recommendation" ,"song_detail"]:
			params["subtype"] = subtype
		if token:
			params["token"] = token
		if output_format:
			params["format"] = output_format
		if order:
			params["order"] = order
		if language:
			params["language"] = language

		url_specific = self.base_url + "?type=song"
		url = self._buildUrl(url_specific,params)
		print url
		return simplejson.load(urllib2.urlopen(url))

	def _buildUrl(self,url,params):


		for key,value in params.iteritems():
			url += "&%s=%s" % (key,value)
		return url
		


