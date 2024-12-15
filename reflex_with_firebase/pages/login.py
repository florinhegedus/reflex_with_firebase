import reflex as rx
from ..firebase import FirebaseState


class LoginState(rx.State):
    form_data: dict = {}

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data
        FirebaseState.login(self.form_data)


def login_form() -> rx.Component:
    return rx.vstack(
        rx.heading("Login"),
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
                rx.button("Login", type="submit"),
            ),
            on_submit=LoginState.handle_submit,
            reset_on_submit=True,
        ),
        rx.divider(),
        rx.heading("Results"),
        rx.text(LoginState.form_data.to_string()),
    )
