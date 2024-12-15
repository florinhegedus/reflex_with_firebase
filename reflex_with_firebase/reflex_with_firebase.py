"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from .navigation import routes
from .pages import login_form, register_form


app = rx.App()
app.add_page(
    login_form,
    route=routes.LOGIN_ROUTE
)
app.add_page(
    register_form,
    route=routes.REGISTER_ROUTE
)
