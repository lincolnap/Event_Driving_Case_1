# Data Enginner Proyects
> Este repo es para trabajar con proyectos de data engineer adicionas de su ruta adicional agregado los casos de uso mas comunes en esta area

## Prerequisitos
> Para efectuar los siguientes codigos se necesita lo siguientes items: 
* Docker
* Visual Code o ide de su preferencia
* python

## Servicios Utilizados
 * [Kafka](./kafka/)
 * [Postgres](./PG/)
 * [Files](./src/)

## Arquitectura Utilizada
![Arquitetura](./src/Arquitera_kafka.svg)

### Instalador de componentes
Se encuenta un archivo makefile para simplicar la vida a la hora de levantar la infraestrutura

1. Levantar el servicio de kafka con el siguiente comando 
``` bash
make kaf_up
```
2. Levantar la Base de Datos

``` bash
make pg_go
```





