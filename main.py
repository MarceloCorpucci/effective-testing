import os

from app import app, db
import admin
import api
import models
import views

from entries.blueprint import entries
app.register_blueprint(entries, url_prefix='/entries')

port = int(os.environ.get("PORT", 5000))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port, threaded=True)
