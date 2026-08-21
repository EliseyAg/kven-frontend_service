from flask import requests
import json


class APIClient:
    def __init__(self, auth_url, user_url, posts_url):
        self.auth_url = auth_url
        self.user_url = user_url
        self.posts_url = posts_url

    def login(self, username, password):
        response = requests.post(
            f"{self.auth_url}/api/auth/login",
            json={
                'username': username,
                'password': password
            },
            timeout=10
        )

        if response.status_code == 200:
            return response.json()
        else:
            return {'error': response.json().get('error', 'Login failed')}

    def register(self, username, password):
        response = requests.post(
            f"{self.auth_url}/api/auth/register",
            json={
                'username': username,
                'password': password
            },
            timeout=10
        )

        if response.status_code == 201:
            return response.json()
        else:
            return {'error': response.json().get('error', 'Registration failed')}
