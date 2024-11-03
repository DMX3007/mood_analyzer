# to Start
	docker-compose up -d

# test positive request
	curl -X POST http://localhost:5000/analyze -H "Content-Type: application/json" -d '{"emailText": "Здравствуйте мой любимый клиент мы звоним вам чтобы сообщить вам отличную новость"}'

# test aggressive request 
	curl -X POST http://localhost:5000/analyze -H "Content-Type: application/json" -d '{"emailText": "Идиот"}'

