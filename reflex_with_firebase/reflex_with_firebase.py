"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from dotenv import load_dotenv

load_dotenv()

from .navigation import routes
from .firebase import signup_form, login_form, AuthState


def signup() -> rx.Component:
    return rx.center(
        signup_form(login_path="/", error_message="Please provide a valid username and password.", email_validation=True),
        height="100vh",
    )


def user_info() -> rx.Component:
    return rx.vstack(
        rx.heading("User info"),
        rx.text(AuthState.email)
    )


def index() -> rx.Component:
    return rx.center(
        rx.cond(
            AuthState.is_logged_in,
            rx.vstack(
                rx.heading("You are logged in", size="1"),
                user_info(),
                rx.cond(
                    AuthState.is_email_verified,
                    rx.text("Your email is verified."),
                    rx.text("Please verify your email."),
                ),
                rx.button("Logout", on_click=AuthState.logout),
            ),
            login_form(error_message="Credentials are not valid."),
        ),
        height="100vh",
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.add_page(signup)
