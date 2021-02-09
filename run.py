"""Run application."""
import os
from hackathon.api.app import app
from hackathon.models import engine, Base
from hackathon.tasks import initialize_lab
from sqlalchemy_utils import database_exists, create_database
import logging

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    if os.path.exists('/tmp/hackathon.db'):
        os.remove('/tmp/hackathon.db')
    create_database(engine.url)
    from hackathon.models.device import DeviceModel, ConfigModel  # noqa

    Base.metadata.create_all(bind=engine)

    # Initialize lab
    initialize_lab()
    app.run(debug=True, port=8000)
