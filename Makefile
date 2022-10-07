SECRET := ./spotify_python/secret.py
VENV := ./spotify_python/senv
AUTH := ./spotify_python/access_token.txt

# Helper commands
auth_file:
	@if [ ! -f ${AUTH} ]; then \
	echo "creating access file.."; \
	touch ${AUTH}; fi \

secret_file:
	@if [ ! -f ${SECRET} ]; then \
	echo "creating secret file.."; \
	echo "user_id = ''\n" >> $(SECRET); \
	echo "client_id = ''\n" >> $(SECRET); \
	echo "client_secret = ''\n" >> $(SECRET); \
	echo "redirect_uri = ''" >> $(SECRET); fi \

virtual_environment:
	@if [ ! -d ${VENV} ]; then \
	echo "creating a virtual environment.."; \
	python3 -m venv $(VENV); fi \


#  Project commands
setup: secret_file auth_file virtual_environment

install:
	@echo "installing dependencies.."
	@pip install -r requirements.txt

