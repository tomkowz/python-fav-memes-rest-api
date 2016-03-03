import os
from api import app as app_api

port = int(os.environ.get("PORT", 5000))
app_api.run(host='0.0.0.0', port=port)
