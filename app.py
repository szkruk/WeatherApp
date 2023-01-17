from flask import (
    Flask ,   g,  request, session, url_for
)  
import os
import start

app = Flask(__name__, instance_relative_config=True)
app.secret_key = 'a random string'
app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'database'),
    )

app.register_blueprint(start.bp)  
 
@app.teardown_appcontext
def close_db(error):
    if hasattr(g , 'sqlite_db'):
        g.sqlite3_db.close()


if __name__ =="__main__":
	app.run() 