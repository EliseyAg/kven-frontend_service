from flask import requests
import json


class APIClient:
    def __init__(self, auth_url, user_url, posts_url):
        self.auth_url = auth_url
        self.user_url = user_url
        self.posts_url = posts_url
