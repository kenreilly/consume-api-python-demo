import urllib.request, urllib.response
import datetime, json

class Util:

	# The current 
	def today_str() -> str:

		return str(datetime.date.today())

	# Call a GET request on the URL and return a string
	def get(url: str) -> bytes:

		with urllib.request.urlopen(url) as response:
   			return response.read()

	# Call a GET request on the URL and return JSON data
	def get_json(url: str) -> dict:

		with urllib.request.urlopen(url) as response:
   			return json.load(response)

	# Download a file and save a local copy
	def download_file(url: str, path: str) -> None:

		return urllib.request.urlretrieve(url, path)

	# Write data to a file on disk
	def write_json(data: dict, path: str) -> None:

		out_file = open(path, 'w')
		out_file.write(data)
		out_file.close()
	