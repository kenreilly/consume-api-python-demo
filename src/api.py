from src.util import Util
from src.config import Config
import json, io, os

# An example API class
class API:

	# Static initialization
	def static_init() -> None:

		return Config.static_init()

	# Get the astronomy image of the day
	def get_image_of_day() -> None:

		# Build URL
		url: str = 'https://api.nasa.gov/planetary/apod'
		url += '?date=' + Util.today_str() + '&hd=false'
		url += '&api_key=' + Config.get_key()
		
		# Get and process data
		data = Util.get_json(url)
		image_url: str = data['url']
		image_filename: str = image_url.split('/')[-1]
		json_filename: str = image_filename + '.json'
		json_data: str = json.JSONEncoder().encode(data)

		# Download the image and write info to disk
		if not os.path.exists('data/'):
			os.makedirs('data/')
		Util.download_file(image_url, 'data/' + image_filename)
		Util.write_json(json_data, 'data/' + json_filename)
