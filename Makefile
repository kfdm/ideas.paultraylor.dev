VENV_DIR := .venv
PYTHON_BIN := $(VENV_DIR)/bin/python
SYSTEM_PYTHON ?= python3.10


$(VENV_DIR):
	$(SYSTEM_PYTHON) -m venv $(VENV_DIR)
	$(PYTHON_BIN) -m pip install -r scripts/requirements.txt

$(PYTHON_BIN): $(VENV_DIR)


server: static/css/syntax.css
	hugo server --buildDrafts --buildFuture --port 1515

# https://xyproto.github.io/splash/docs/all.html
static/css/syntax.css:
	hugo gen chromastyles --style=friendly > static/css/syntax.css


.PHONY: clean
clean:
	rm static/css/syntax.css
	rm -rf public

.PHONY: sort
sort: $(PYTHON_BIN)
	$(PYTHON_BIN) scripts/sort.py
