import os
import environ

env = environ.Env()

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ENV_FILE = os.path.join(BASE_DIR, '.env')

environ.Env.read_env(ENV_FILE)

DATABASE = {
	"default": {
        "url": env.str('MONGO_URL', default='mongodb://localhost:27017')
    }
}
