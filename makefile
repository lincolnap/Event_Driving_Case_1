kaf_up:
	docker-compose -f kafka/kafka-tools.yml up -d

kaf_down:
	docker-compose -f PG/pg.yml down

kaf_down_all:  
	docker-compose down -f kafka/kafka-tools.yml --rmi all

pg_go:
	docker-compose -f PG/pg.yml up -d

pg_down:
	docker-compose -f PG/pg.yml down

pg_down_all:
	docker-compose -f PG/pg.yml down --rmi all