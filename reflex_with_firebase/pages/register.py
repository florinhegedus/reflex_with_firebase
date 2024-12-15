import reflex as rx
from ..firebase import FirebaseState
import json


class RegisterState(rx.State):
    form_data: dict = {}
    message: str = "NOT SET"

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        FirebaseState.register(self.form_data)


def register_form():
    return rx.vstack(
        rx.heading("Register"),
        rx.form(
            rx.vstack(
                rx.text("Email"),
                rx.input(
                    placeholder="user@reflex.dev",
                    name="email",
                ),
                rx.text("Password"),
                rx.input(
                    placeholder="password",
                    name="password",
                    type="password",
                ),
                rx.button("Register", type="submit"),
            ),
            on_submit=FirebaseState.register,
            reset_on_submit=True,
        ),
        rx.divider(),
        rx.heading("Results"),
        rx.text(RegisterState.form_data.to_string()),
    )