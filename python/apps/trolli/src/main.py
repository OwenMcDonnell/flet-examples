import os
import flet
from flet.auth.providers.auth0_oauth_provider import Auth0OAuthProvider
from flet.auth.providers.github_oauth_provider import GitHubOAuthProvider
from flet.auth.providers.google_oauth_provider import GoogleOAuthProvider
from app_layout import AppLayout
from board import Board
from data_store import DataStore
from flet import (
    AlertDialog,
    AppBar,
    Column,
    Container,
    ElevatedButton,
    Icon,
    Page,
    PopupMenuButton,
    PopupMenuItem,
    RoundedRectangleBorder,
    Row,
    TemplateRoute,
    Text,
    TextField,
    UserControl,
    View,
    colors,
    icons,
    margin,
    padding,
    theme,
)
from memory_store import InMemoryStore
from user import User

AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")
assert AUTH0_DOMAIN, "set AUTH0_DOMAIN environment variable"
AUTH0_CLIENT_ID = os.getenv("AUTH0_CLIENT_ID")
assert AUTH0_CLIENT_ID, "set AUTH0_CLIENT_ID environment variable"
AUTH0_CLIENT_SECRET = os.getenv("AUTH0_CLIENT_SECRET")
assert AUTH0_CLIENT_SECRET, "set AUTH0_CLIENT_SECRET environment variable"

class TrelloApp(UserControl):
    def __init__(self, page: Page, store: DataStore):
        super().__init__()
        self.page = page
        self.store: DataStore = store
        self.page.on_route_change = self.route_change
        self.boards = self.store.get_boards()
        self.login_profile_button = PopupMenuItem(text="Log in", on_click=self.login)
        self.appbar_items = [
            self.login_profile_button,
            PopupMenuItem(),  # divider
            PopupMenuItem(text="Settings"),
        ]
        self.appbar = AppBar(
            leading=Icon(icons.GRID_GOLDENRATIO_ROUNDED),
            leading_width=100,
            title=Text(f"Trolli", font_family="Pacifico", size=32, text_align="start"),
            center_title=False,
            toolbar_height=75,
            bgcolor=colors.LIGHT_BLUE_ACCENT_700,
            actions=[
                Container(
                    content=PopupMenuButton(items=self.appbar_items),
                    margin=margin.only(left=50, right=25),
                )
            ],
        )
        self.page.appbar = self.appbar
        self.page.update()

    def build(self):
        self.layout = AppLayout(
            self,
            self.page,
            self.store,
            tight=True,
            expand=True,
            vertical_alignment="start",
        )
        return self.layout

    def initialize(self):
        self.page.views.clear()
        self.page.views.append(
            View(
                "/",
                [self.appbar, self.layout],
                padding=padding.all(0),
                bgcolor=colors.BLUE_GREY_200,
            )
        )
        self.page.update()
        # create an initial board for demonstration if no boards
        if len(self.boards) == 0:
            self.create_new_board("My First Board")
        self.page.go("/")

    def login(self, e):
        def close_dlg(e):
            if user_name.value == "" or password.value == "":
                user_name.error_text = "Please provide username"
                password.error_text = "Please provide password"
                self.page.update()
                return
            else:
                user = User(user_name.value, password.value)
                if user not in self.store.get_users():
                    self.store.add_user(user)
                self.user = user_name.value
                self.page.client_storage.set("current_user", user_name.value)

            dialog.open = False
            self.appbar_items[0] = PopupMenuItem(
                text=f"{self.page.client_storage.get('current_user')}'s Profile"
            )
            self.page.update()
        def auth0_login_click(e):
            provider = Auth0OAuthProvider(
                domain=os.getenv("AUTH0_DOMAIN"),
                client_id=os.getenv("AUTH0_CLIENT_ID"),
                client_secret=os.getenv("AUTH0_CLIENT_SECRET")
            )
            self.page.login(provider)
        def github_login_click(e):
            pass
        def google_login_click(e):
            pass    

        auth0_button = ElevatedButton("Login with Auth0", on_click=auth0_login_click)
        github_button = ElevatedButton("Login with Github", on_click=github_login_click, disabled=True)
        google_button = ElevatedButton("Login with Google", on_click=google_login_click, disabled=True)
        dialog = AlertDialog(
            title=Text("Choose an Identity Provider"),
            content=Column(
                [
                    auth0_button,
                    github_button,
                    google_button

                ],
                tight=True,
            ),
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()

    def route_change(self, e):
        troute = TemplateRoute(self.page.route)
        if troute.match("/"):
            self.page.go("/boards")
        elif troute.match("/board/:id"):
            if int(troute.id) > len(self.store.get_boards()):
                self.page.go("/")
                return
            self.layout.set_board_view(int(troute.id))
        elif troute.match("/boards"):
            self.layout.set_all_boards_view()
        elif troute.match("/members"):
            self.layout.set_members_view()
        self.page.update()

    def add_board(self, e):
        def close_dlg(e):
            if (hasattr(e.control, "text") and not e.control.text == "Cancel") or (
                type(e.control) is TextField and e.control.value != ""
            ):
                self.create_new_board(dialog_text.value)
            dialog.open = False
            self.page.update()

        def textfield_change(e):
            if dialog_text.value == "":
                create_button.disabled = True
            else:
                create_button.disabled = False
            self.page.update()

        dialog_text = TextField(
            label="New Board Name", on_submit=close_dlg, on_change=textfield_change
        )
        create_button = ElevatedButton(
            text="Create", bgcolor=colors.BLUE_200, on_click=close_dlg, disabled=True
        )
        dialog = AlertDialog(
            title=Text("Name your new board"),
            content=Column(
                [
                    dialog_text,
                    Row(
                        [
                            ElevatedButton(text="Cancel", on_click=close_dlg),
                            create_button,
                        ],
                        alignment="spaceBetween",
                    ),
                ],
                tight=True,
            ),
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()
        dialog_text.focus()

    def create_new_board(self, board_name):
        new_board = Board(self, self.store, board_name)
        self.store.add_board(new_board)
        self.layout.hydrate_all_boards_view()

    def delete_board(self, e):
        self.store.remove_board(e.control.data)
        self.layout.set_all_boards_view()


def main(page: Page):

    page.title = "Flet Trello clone"
    page.padding = 0
    page.theme = theme.Theme(font_family="Verdana")
    page.theme.page_transitions.windows = "cupertino"
    page.fonts = {"Pacifico": "Pacifico-Regular.ttf"}
    page.bgcolor = colors.BLUE_GREY_200
    app = TrelloApp(page, InMemoryStore())
    page.add(app)
    page.update()
    app.initialize()


flet.app(target=main, assets_dir="../assets")
