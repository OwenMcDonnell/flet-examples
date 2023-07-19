import os

import flet as ft
from flet.auth.providers.auth0_oauth_provider import Auth0OAuthProvider

AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")
assert AUTH0_DOMAIN, "set AUTH0_DOMAIN environment variable"
AUTH0_CLIENT_ID = os.getenv("AUTH0_CLIENT_ID")
assert AUTH0_CLIENT_ID, "set AUTH0_CLIENT_ID environment variable"
AUTH0_CLIENT_SECRET = os.getenv("AUTH0_CLIENT_SECRET")
assert AUTH0_CLIENT_SECRET, "set AUTH0_CLIENT_SECRET environment variable"


def main(page: ft.Page):

    provider = Auth0OAuthProvider(
        domain=AUTH0_DOMAIN,
        client_id=AUTH0_CLIENT_ID,
        client_secret=AUTH0_CLIENT_SECRET,
        redirect_url="http://localhost:8550/api/oauth/redirect",
    )

    def login_click(e):
        #breakpoint()
        page.login(provider)

    def on_login(e):
        print("Login error:", e.error)
        print("Access token:", page.auth.token.access_token)
        print("User ID:", page.auth.user.id)

    page.on_login = on_login
    page.add(ft.ElevatedButton("Login with Auth0", on_click=login_click))

ft.app(target=main, port=8550, view=ft.WEB_BROWSER)
