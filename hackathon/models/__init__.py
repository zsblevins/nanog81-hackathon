"""Database models."""

from sqlalchemy import create_engine  # type: ignore
from sqlalchemy.ext.declarative import declarative_base  # type: ignore
from sqlalchemy.orm import scoped_session, sessionmaker  # type: ignore

sqlite_file = '/tmp/hackathon.db'
engine = create_engine("sqlite:///{}".format(sqlite_file), echo=False)
Base = declarative_base()


def get_session():
    """Return a SQLAlchemy session."""
    return scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
