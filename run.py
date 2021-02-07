"""Run application."""
import os
from hackathon.api.app import app
from hackathon.models import engine, Base
from sqlalchemy_utils import database_exists, create_database
import logging

logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":

    os.remove('/tmp/hackathon.db')
    create_database(engine.url)
    from hackathon.models.device import DeviceModel, ConfigModel  # noqa
    Base.metadata.create_all(bind=engine)

    # Create our 3 initial devices
    DeviceModel.create('core-rtr1', '192.168.123.2', 'core')
    DeviceModel.create('core-rtr2', '192.168.123.3', 'core')
    DeviceModel.create('tor1', '192.168.123.4', 'tor')

    app.run(debug=True, port=8000)
