import pytest
import requests
from unittest.mock import MagicMock, call

from main import app


@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            pass
        yield client


def test_ep_hello(client, monkeypatch):
    """Testing ensure ep_hello is operating correctly

    :return:
    """

    # execute
    actual = client.get('/api/v1/hello/', follow_redirects=True, content_type='application/json')

    # expect
    print(actual.json)
    assert actual.json == {'hello': 'world'}
    # assert False


def test_get_mock(client, monkeypatch):
    """Testing ensure ep_hello is operating correctly

    :return:
    """
    # init

    request_mock = MagicMock()
    monkeypatch.setattr('requests.post', request_mock)
    request_mock.return_value.status_code = 200
    request_mock.return_value.content = 'this is lame'

    # execute
    actual = requests.post('https://www.google.com')

    # expect
    assert actual.status_code == 200
    assert call('https://www.google.com') in request_mock.mock_calls
    print(actual.content)

    print(request_mock.mock_calls)
    # assert False


def test_generic():
    """


    :return:
    """
    # init

    # execute function

    # expect a result.
