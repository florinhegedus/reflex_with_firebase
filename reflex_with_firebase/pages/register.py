import reflex as rx
from ..firebase import FirebaseState


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