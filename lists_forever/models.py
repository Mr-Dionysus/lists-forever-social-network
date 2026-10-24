import sqlalchemy as sa
import sqlalchemy.orm as so

from lists_forever import db


class User(db.Model):
    __tablename__ = "users"

    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(50), unique=True)

    def __repr__(self):
        return f"User(id={self.id}, username={self.username}, email={self.email})"

    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email
