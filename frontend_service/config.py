import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'frontend-secret-key-change-me')
    DEBUG = os.getenv('FLASK_ENV', 'production') == 'development'

    AUTH_SERVICE_URL = os.getenv('AUTH_SERVICE_URL', 'http://localhost:8001')
    USER_SERVICE_URL = os.getenv('USER_SERVICE_URL', 'http://localhost:8002')
    POSTS_SERVICE_URL = os.getenv('POSTS_SERVICE_URL', 'http://localhost:8003')
