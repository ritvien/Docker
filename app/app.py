from app.api.api import App

def create_app():
    app_instance = App()  
    return app_instance.app

