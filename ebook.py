from app import create_app, db
import os
from flask_migrate import Migrate

config_name = os.getenv('FLASK_CONFIG') or 'default'
# print('config_name', config_name)

app = create_app(config_name)
# app.config.from_object(config[config_name])
# bootstrap = Bootstrap(app)
from app.models import Book, db


SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_content():
    return dict(db=db, Book=Book)

if __name__ == '__main__':
    app.run(debug=True)
