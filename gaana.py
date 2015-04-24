import urllib2
import simplejson

class gaana:

	def __init__(self):
		self.base_url = "http://api.gaana.com/"
		self.base_user_url = "http://api.gaana.com/user.php?"

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
		return simplejson.load(urllib2.urlopen(url))

	def getUserToken(self
					):
		url = self.base_user_url + "type=registrationtoken"
		return simplejson.load(urllib2.urlopen(url))

	def registerUser(self,
				   	key = None,
				    regtoken = None,
				    fullname = None,
				    nickname = None,
				    email = None,
				    password = None,
				    dob = None,
				    gender = None
					 ):

		params = {}

		if key:
			params["key"] = key
		if regtoken:
			params["regtoken"] = regtoken
		if fullname:
			params["fullname"] = fullname
		if nickname:
			params["nickname"] = nickname
		if email:
			params["email"] = email
		if password:
			params["password"] = password
		if dob:
			params["dob"] = dob
		if gender in ["male" , "female"]:
			params["gender"] = gender

		url_specific = self.base_user_url + "type=registration"
		url = self._buildUrl(url_specific,params)
		print url
		return simplejson.load(urllib2.urlopen(url


	def fbLogin(	self,
				   	fbtoken = None,
				    fbid = None,
				    fullname = None,
				    fbrealtoken = None,
				    email = None,
				    dob = None,
				    gender = None
					 ):

		params = {}

		if fbtoken:
			params["fbtoken"] = fbtoken
		if fbid:
			params["fbid"] = fbid
		if fullname:
			params["fullname"] = fullname
		if fbrealtoken:
			params["fbrealtoken"] = fbrealtoken
		if email:
			params["email"] = email
		if dob:
			params["dob"] = dob
		if gender in ["male" , "female"]:
			params["gender"] = gender

		url_specific = self.base_user_url + "type=authenticate&subtype=fb"
		url = self._buildUrl(url_specific,params)
		print url
		return simplejson.load(urllib2.urlopen(url))

	def fbConnect(	self,
				   	fbtoken = None,
				    fbid = None,
				    fullname = None,
				    token = None,
				    switchsocialasset = None,
					 ):

		params = {}

		if fbtoken:
			params["fbtoken"] = fbtoken
		if fbid:
			params["fbid"] = fbid
		if fullname:
			params["fullname"] = fullname
		if token:
			params["token"] = token
		if switchsocialasset:
			params["switchsocialasset"] = switchsocialasset

		url_specific = self.base_user_url + "type=authenticate&subtype=fb_connect"
		url = self._buildUrl(url_specific,params)
		print url
		return simplejson.load(urllib2.urlopen(url))


	def userLogin(self,
				    username = None,
				    password = None,
					 ):

		params = {}

		if username:
			params["username"] = username
		if password:
			params["password"] = password


		url_specific = self.base_user_url + "type=authenticate"
		url = self._buildUrl(url_specific,params)
		print url
		return simplejson.load(urllib2.urlopen(url))


	def forgotPassword(self,
				   	  email = None,
					 ):

		params = {}

		if email:
			params["email"] = email



		url_specific = self.base_user_url + "type=forgotpassword"
		url = self._buildUrl(url_specific,params)
		print url
		return simplejson.load(urllib2.urlopen(url))

	def getUserProfile(self,
				    token = None,
				    friend_id = None,
				    is_friend_info = None
					 ):

		params = {}

		if token:
			params["token"] = token
		if friend_id:
			params["friend_id"] = friend_id
		if is_friend_info:
			params["is_friend_info"] = is_friend_info


		url_specific = self.base_user_url + "type=profile"
		url = self._buildUrl(url_specific,params)
		print url
		return simplejson.load(urllib2.urlopen(url))

	def getProfileImage(self,
				    	token = None,
					 ):

		params = {}

		if token:
			params["token"] = token

		url_specific = self.base_user_url + "type=profile_image"
		url = self._buildUrl(url_specific,params)
		print url
		return simplejson.load(urllib2.urlopen(url))


	def mySongs(self,
			   token = None,
			   output_format = None,
			   friend_id = None,
			   is_friend_info = None,
			   limit = 40,
			   contentfilter = None
			  ):

		params = {}

		if token:
			params["token"] = token
		if output_format:
			params["format"] = output_format
		if friend_id:
			params["friend_id"] = friend_id
		if is_friend_info:
			params["is_friend_info"] = is_friend_info
		if limit:
			params["limit"] = int(limit)
		if contentfilter:
			params["contentfilter"] = contentfilter


		url_specific = self.base_user_url+ "type=mysongs&subtype=favorites"
		url = self._buildUrl(url_specific,params)
		print url
		return urllib2.urlopen(url).read()

	def myAlbums(self,
			   token = None,
			   output_format = None,
			   friend_id = None,
			   is_friend_info = None,
			   limit = 40,
			   contentfilter = None
			  ):

		params = {}

		if token:
			params["token"] = token
		if output_format:
			params["format"] = output_format
		if friend_id:
			params["friend_id"] = friend_id
		if is_friend_info:
			params["is_friend_info"] = is_friend_info
		if limit:
			params["limit"] = int(limit)
		if contentfilter:
			params["contentfilter"] = contentfilter


		url_specific = self.base_user_url+ "type=myalbums&subtype=favorites"
		url = self._buildUrl(url_specific,params)
		print url
		return urllib2.urlopen(url).read()

	def myArtists(self,
				   token = None,
				   output_format = None,
				   friend_id = None,
				   is_friend_info = None,
				   limit = 40,
				   contentfilter = None
			  ):

		params = {}

		if token:
			params["token"] = token
		if output_format:
			params["format"] = output_format
		if friend_id:
			params["friend_id"] = friend_id
		if is_friend_info:
			params["is_friend_info"] = is_friend_info
		if limit:
			params["limit"] = int(limit)
		if contentfilter:
			params["contentfilter"] = contentfilter


		url_specific = self.base_user_url+ "type=myartists&subtype=favorites"
		url = self._buildUrl(url_specific,params)
		print url
		return urllib2.urlopen(url).read()


	def myPlaylists(self,
				   token = None,
				   output_format = None,
				   friend_id = None,
				   is_friend_info = None,
				   limit = 40,
				   contentfilter = None
			  ):

		params = {}

		if token:
			params["token"] = token
		if output_format:
			params["format"] = output_format
		if friend_id:
			params["friend_id"] = friend_id
		if is_friend_info:
			params["is_friend_info"] = is_friend_info
		if limit:
			params["limit"] = int(limit)
		if contentfilter:
			params["contentfilter"] = contentfilter


		url_specific = self.base_user_url+ "type=myplaylists&subtype=favorites"
		url = self._buildUrl(url_specific,params)
		print url
		return urllib2.urlopen(url).read()



	def addToFavorites(self,
					   token = None,
					   subtype = None,
					   id = None,
					   title = None,

			  ):

		params = {}



		if subtype in ["song" ,"album" , "playlist","artist"]:
			params["subtype"] = subtype
		if token:
			params["token"] = token
		if id:
			params["id"] = id
		if title:
			params["title"] = title


		url_specific = self.base_user_url+ "type=favorite&actionstatus=1"
		url = self._buildUrl(url_specific,params)
		print url
		return urllib2.urlopen(url).read()

	def removeFromFavorites(self,
					   token = None,
					   subtype = None,
					   id = None,
					   title = None,

			  ):

		params = {}



		if subtype in ["song" ,"album" , "playlist","artist"]:
			params["subtype"] = subtype
		if token:
			params["token"] = token
		if id:
			params["id"] = id
		if title:
			params["title"] = title


		url_specific = self.base_user_url+ "type=favorite&actionstatus=0"
		url = self._buildUrl(url_specific,params)
		print url
		return urllib2.urlopen(url).read()

	def recentUserTracks(self,
				      token = None,
				      friend_id = None,
				      is_friend_info = None
					 ):

		params = {}

		if token:
			params["token"] = token
		if friend_id:
			params["friend_id"] = friend_id
		if is_friend_info:
			params["is_friend_info"] = is_friend_info


		url_specific = self.base_user_url + "type=recent_heard"
		url = self._buildUrl(url_specific,params)
		print url
		return simplejson.load(urllib2.urlopen(url))


	def recentUserActivity( self,
				      		token = None,
				     	    friend_id = None,
				      		is_friend_info = None
					 ):

		params = {}

		if token:
			params["token"] = token
		if friend_id:
			params["friend_id"] = friend_id
		if is_friend_info:
			params["is_friend_info"] = is_friend_info


		url_specific = self.base_user_url + "type=recent_activity"
		url = self._buildUrl(url_specific,params)
		print url
		return simplejson.load(urllib2.urlopen(url))


	def getGaanaFriends( self,
				      		token = None,
				     	    output_format = None,
					 ):

		params = {}

		if token:
			params["token"] = token
		if output_format:
			params["format"] = output_format

		url_specific = self.base_user_url + "type=gaana_friends"
		url = self._buildUrl(url_specific,params)
		print url
		return simplejson.load(urllib2.urlopen(url))

	def getFbFriends( self,
		      		  token = None,
		     	      output_format = None,
					 ):

		params = {}

		if token:
			params["token"] = token
		if output_format:
			params["format"] = output_format

		url_specific = self.base_user_url + "type=fb_friends"
		url = self._buildUrl(url_specific,params)
		print url
		return simplejson.load(urllib2.urlopen(url))

	def inviteFriends( self,
		      		  token = None,
		     	      output_format = None,
					 ):

		params = {}

		if token:
			params["token"] = token
		if output_format:
			params["format"] = output_format

		url_specific = self.base_user_url + "type=invited_friends"
		url = self._buildUrl(url_specific,params)
		print url
		return simplejson.load(urllib2.urlopen(url))


	def referFriends( self,
				     token = None,
				     referredIdentities = None,
				     referenceMedia =None
					 ):

		params = {}

		if token:
			params["token"] = token
		if referredIdentities:
			params["referredIdentities"] = referredIdentities
		if referenceMedia:
			params["referenceMedia"] = referenceMedia

		url_specific = self.base_user_url + "type=password_change"
		url = self._buildUrl(url_specific,params)
		print url
		return simplejson.load(urllib2.urlopen(url))


	def createPlaylist( self,
		      		  token = None,
		      		  title=None,
		     	      output_format = None,
					 ):

		params = {}

		if token:
			params["token"] = token
		if title:
			params["title"] = title
		if output_format:
			params["format"] = output_format

		url_specific = self.base_user_url + "type=createplaylist"
		url = self._buildUrl(url_specific,params)
		print url
		return simplejson.load(urllib2.urlopen(url))

	def addToPlaylist( self,
		      		  token = None,
		      		  id=None,
		     	      trackids = None,
					 ):

		params = {}

		if token:
			params["token"] = token
		if id:
			params["id"] = id
		if trackids:
			params["trackids"] = trackids

		url_specific = self.base_user_url + "type=addtoplaylist"
		url = self._buildUrl(url_specific,params)
		print url
		return simplejson.load(urllib2.urlopen(url))

	def deleteFromPlaylist( self,
		      		  token = None,
		      		  id=None,
		     	      trackids = None,
					 ):

		params = {}

		if token:
			params["token"] = token
		if id:
			params["id"] = id
		if trackids:
			params["trackids"] = trackids

		url_specific = self.base_user_url + "type=myplaylists&subtype=delete_tracks"
		url = self._buildUrl(url_specific,params)
		print url
		return simplejson.load(urllib2.urlopen(url))

	def updatePlaylist( self,
		      		  token = None,
		      		  id=None,
		     	      trackids = None,
					 ):

		params = {}

		if token:
			params["token"] = token
		if id:
			params["id"] = id
		if trackids:
			params["trackids"] = trackids

		url_specific = self.base_user_url + "type=myplaylists&subtype=edit_playlist"
		url = self._buildUrl(url_specific,params)
		print url
		return simplejson.load(urllib2.urlopen(url))

	def deletePlaylist( self,
		      		  token = None,
		      		  id=None,
		     	      trackids = None,
					 ):

		params = {}

		if token:
			params["token"] = token
		if id:
			params["id"] = id
		if trackids:
			params["trackids"] = trackids

		url_specific = self.base_user_url + "type=myplaylists&subtype=delete_playlist"
		url = self._buildUrl(url_specific,params)
		print url
		return simplejson.load(urllib2.urlopen(url))






	def _buildUrl(self,url,params):


		for key,value in params.iteritems():
			url += "&%s=%s" % (key,value)
		return url



