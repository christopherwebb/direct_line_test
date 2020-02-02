# Direct Line Python Code Challenge

A microservice to return the sum of a list of ints

### Assumptions

* Used Flask, as it's fairly light weight (in comparison to Django) and well known
* The API endpoint, while not having any side effects, was added as a `POST` request, in
  order to deal with requests involving large numbers of integers to add.

## Getting up and running locally

To get started, first run

```
make init
```

Then run
```
make run
```

## Running tests

To run the tests, run

```
make tests
```

## Making requests

Examples:
```
~|⇒ docker-compose up -d
~|⇒ python3

import requests

numbers_to_add = [1, 2, 3]
response = requests.get('http://localhost:8000/total', data={'values': numbers_to_add})
assert response.json()['total'] == 6

numbers_to_add = list(range(10000001))
response = requests.get('http://localhost:8000/total', data={'values': numbers_to_add})
assert response.json()['total'] == 50000005000000

Python 3.5.1 (default, Feb 27 2016, 14:48:44)
>>> import requests

>>> numbers_to_add = [1, 2, 3]

>>> total_url = 'http://localhost:5000/total'

>>> response = requests.post(total_url, json={'values': numbers_to_add})
>>> assert response.json()['total'] == 6

>>> numbers_to_add = list(range(10000001))
>>> response = requests.post(total_url, json={'values': numbers_to_add})
>>> assert response.json()['total'] == 50000005000000
```
