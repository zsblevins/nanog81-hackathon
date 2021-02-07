"""Application API."""

from flask import Blueprint
from flask_restx import Api  # type: ignore

from .device import api as ns_device


blueprint = Blueprint("api", __name__)

api = Api(blueprint)

api.add_namespace(ns_device)

