from app import create_app 
from api.api_routes import api_bp

if __name__ == "__main__":
    app, db, socketio = create_app()
    app.register_blueprint(api_bp, url_prefix='/api')
    socketio.run(app, host="0.0.0.0")


