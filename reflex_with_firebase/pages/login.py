import reflex as rx
from ..firebase import FirebaseState


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
            on_submit=FirebaseState.login,
            reset_on_submit=True,
        ),
        rx.divider(),
        rx.heading("Results"),
        rx.text(LoginState.form_data.to_string()),
    )
