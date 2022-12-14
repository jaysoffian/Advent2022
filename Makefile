export PIP_DISABLE_PIP_VERSION_CHECK=1

venv/pyvenv.cfg: requirements.txt
	python -m venv venv
	venv/bin/python -m pip install --upgrade pip
	venv/bin/python -m pip install -r requirements.txt
	touch "$@"

venv: venv/pyvenv.cfg
