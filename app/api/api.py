from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from app.api.html_response import get_html
from app.api.predict import predict_gender_from_image

class App:
    def __init__(self):
        self.app = FastAPI()
        self._register_routers()
    def _register_routers(self):
        self.app.get("/", response_class=HTMLResponse)(get_html)
        self.app.post("/predict-gender/")(predict_gender_from_image)
