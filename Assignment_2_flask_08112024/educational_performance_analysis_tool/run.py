from flask import Flask
from app.config import config
from app.models import db
from app.views.auth import auth_bp
from app.views.dashboard import dashboard_bp
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

# Set up user login management
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(dashboard_bp, url_prefix='/')

if __name__ == '__main__':
    app.run()
