import io, os

class Config:
	
	# Variables loaded from .env
	env: dict = {
		'NASA_API_KEY': ''
	}

	# Load environment variables from .env
	def load_env(path: str) -> bool:

		try:
			with io.open(path) as stream:
				for line in stream:
					parts = line.split('=')
					Config.env[parts[0]] = parts[1].strip()
			return True
		except:
			return False


	def get_key() -> str:
		return Config.env['NASA_API_KEY']

	# Initialize this class
	def static_init() -> bool:

		if os.path.isfile('.env'):
			return Config.load_env('.env')
		else:
			return Config.load_env('.env.default')
			