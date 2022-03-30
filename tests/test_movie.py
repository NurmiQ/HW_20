from unittest.mock import MagicMock
import pytest

from dao.director import DirectorDAO
from setup_db import db


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(db.session)

