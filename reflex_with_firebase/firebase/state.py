import reflex as rx
from reflex_with_firebase.firebase.config import auth, firestore_db


class FirebaseState(rx.State):
    exception_message: str = ""

    @rx.event(background=True)
    async def register(self, form_data):
        async with self:
            try:
                auth.create_user_with_email_and_password(form_data["email"], form_data["password"])
            except Exception as exc:
                self.exception_message = exc

    @rx.event(background=True)
    async def login(self, form_data):
        async with self:
            try:
                user = auth.sign_in_with_email_and_password(form_data["email"], form_data["password"])
            except Exception as exc:
                self.exception_message = exc
