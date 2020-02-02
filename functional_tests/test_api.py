import os
import pytest
import requests


BASE_ADDRESS = os.getenv('WEB_ADDRESS')
ADDRESS = f'http://{BASE_ADDRESS}'


def test_total():
    assert _get_total_ok([1, 2, 3])['total'] == 6


def test_big_value():
    assert _get_total_ok(list(range(10000001)))['total'] == 50000005000000


def test_empty_lists():
    assert _get_total_ok([])['total'] == 0


def test_lists_with_negative_values():
    assert _get_total_ok([-5, -6, 2])['total'] == -9


def test_list_with_string_returns_error():
    assert _get_total({'values': [1, 2, 'three']}).status_code == 400


def test_no_data_returns_error():
    assert _get_total({'values': None}).status_code == 400
    assert _get_total({}).status_code == 400
    assert _get_total(None).status_code == 400


def _get_total(data):
    response = requests.post(
        f'{ADDRESS}/total',
        json=data,
    )
    return response


def _get_total_ok(values=None):
    values = values or []

    response = _get_total({'values': values})
    assert response.status_code == 200
    return response.json()
