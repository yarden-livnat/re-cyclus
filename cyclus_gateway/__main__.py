import os
from cyclus_gateway import create_app

app = create_app(os.getenv('FLASK_ENV') or 'development')
# app = create_app()
app.run(host='0.0.0.0', port=5000, debug=True)
