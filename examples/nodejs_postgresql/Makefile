include ../commons.mk

.DEFAULT_GOAL := help

## -- Application Developer targets --

.PHONY: set-labels-on-nodejs-app
## Set the binding labels for the NodeJS app
set-labels-on-nodejs-app:
	${Q}oc project service-binding-demo
	${Q}oc patch deployment nodejs-rest-http-crud -p '{"metadata": {"labels": {"connects-to": "postgres", "environment": "demo"}}}'

.PHONY: create-service-binding
## Create the Service Binding
create-service-binding:
	${Q}oc apply -f service-binding.yaml
