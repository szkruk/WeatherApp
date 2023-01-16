from flask import (
    Flask ,   g,  request, session, url_for
)  
import os
import home

app = Flask(__name__, instance_relative_config=True)

app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'database'),
    )

app.register_blueprint(home.bp)
import os

from flask import Flask

 
@app.teardown_appcontext
def close_db(error):
    if hasattr(g , 'sqlite_db'):
        g.sqlite3_db.close()


if __name__ =="__main__":
	app.run() 