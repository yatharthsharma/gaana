
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
		return simplejson.load(urllib2.urlopen(url))


	def getAlbums(self,
				  subtype = 'most_popular',
				  token = None,
				  output_format = None,
				  order = None,
				  language = None,
				  limit = 40,
				  contentfilter = 1):

		params = {}

		if subtype in ["most_popular" , "new_release" ,"featured_album" ,"similar_album" ,"all_albums", "album" ,"album_detail" ,"album_detail_info"]:
			params["subtype"] = subtype
		if token:
			params["token"] = token
		if output_format:
			params["format"] = output_format
		if order:
			params["order"] = order
		if language:
			params["language"] = language
		if limit:
			params["limit"] = int(limit)
		if contentfilter:
			params["contentfilter"] = int(contentfilter)

		url_specific = self.base_url + "?type=album"
		url = self._buildUrl(url_specific,params)
		return simplejson.load(urllib2.urlopen(url))


	def getArtists(self,
				  subtype = 'most_popular',
				  token = None,
				  output_format = None,
				  order = None,
				  language = None,
				  limit = 40,
				  ):

		params = {}

		if subtype in ["most_popular" , "artist_list" ,"artist_track_listing" ,"artist_album" ,"similar_artist","artist_details" ,"artist_details_info"]:
			params["subtype"] = subtype
		if token:
			params["token"] = token
		if output_format:
			params["format"] = output_format
		if order:
			params["order"] = order
		if language:
			params["language"] = language
		if limit:
			params["limit"] = int(limit)

		url_specific = self.base_url + "?type=artist"
		url = self._buildUrl(url_specific,params)
		return simplejson.load(urllib2.urlopen(url))


	def getGenre(self,
				 subtype = "genre_listing",
				 output_format = None,
				 ):

		params = {}


		if subtype in ["genre_listing" , "genre_details" ,"genre_artist_listing" ,"genre_album_listing" ,"artist_album" ,"artist_track_listing"]:
			params["subtype"] = subtype
		if output_format:
			params["format"] = output_format

		url_specific = self.base_url + "?type=genre"
		url = self._buildUrl(url_specific,params)
		print url
		return simplejson.load(urllib2.urlopen(url))


	def getPlaylist(self,
				   subtype = 'most_popular_playlist',
				   token = None,
				   output_format = None,
				   order = None,
				   language = None,
				   limit = 40,
				  ):

		params = {}

		if subtype in ["most_popular_playlist" , "playlist_home_featured" ,"playlist_detail" ,"user_playlist" ,"topCharts"]:
			params["subtype"] = subtype
		if token:
			params["token"] = token
		if output_format:
			params["format"] = output_format
		if order:
			params["order"] = order
		if language:
			params["language"] = language
		if limit:
			params["limit"] = int(limit)

		url_specific = self.base_url + "?type=playlist"
		url = self._buildUrl(url_specific,params)
		return simplejson.load(urllib2.urlopen(url))


	def search(self,
			   subtype = 'search_Song',
			   token = None,
			   output_format = None,
			   key = None,
			   limit = 40,
				  ):

		params = {}

		if subtype in ["search_song" , "search_artist" ,"search_album" ,"search_playlist" ,"autocomplete","mobileautocomplete"]:
			params["subtype"] = subtype
		if token:
			params["token"] = token
		if output_format:
			params["format"] = output_format
		if key:
			params["key"] = key
		if limit:
			params["limit"] = int(limit)

		url_specific = self.base_url + "?type=search"
		url = self._buildUrl(url_specific,params)
		return simplejson.load(urllib2.urlopen(url))

 	
 	def termsAndConditions(self
			  			 ):

		url = self.base_url + "?type=terms_conditions"
		return urllib2.urlopen(url).read()


	def privacyPolicy(self
			  		 ):

		url = self.base_url + "?type=privacy_policy"
		return urllib2.urlopen(url).read()


	def emailExist(self,
			  	   email = None ):

		params = {}

		if email:
			params["email"] = email


		url_specific = self.base_url + "?type=is_email_exists"
		url = self._buildUrl(url_specific,params)
		return simplejson.load(urllib2.urlopen(url))


	def recentUsers(self,
			  	   limit = 10 ):


		params = {}

		if limit:
			params["limit"] = limit


		url_specific = self.base_url + "?type=people&subtype=recent_user_listing"
		url = self._buildUrl(url_specific,params)
		return simplejson.load(urllib2.urlopen(url))


	def language(self
			  	):

		url = self.base_url + "?type=language"
		return urllib2.urlopen(url).read()




	def _buildUrl(self,url,params):


		for key,value in params.iteritems():
			url += "&%s=%s" % (key,value)
		return url
		


