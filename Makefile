build:
	docker build -t adder_service:latest .

run:
	docker-compose up

test:
	docker-compose up -d
	docker-compose run -e WEB_ADDRESS='web:5000' web pytest /code/functional_tests
