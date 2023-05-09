.ONESHELL:
SHELL = /bin/bash

.PHONY: env
env :
	source /srv/conda/etc/profile.d/conda.sh
	conda env create -f environment.yml 
	conda activate Opioid
	conda install ipykernel
	python -m ipykernel install --user --name Opioid --display-name "IPython - Opioid"
	
	
.PHONy: all
all:
	jupyter execute main.ipynb
	jupyter execute preprocessing.ipynb



	
.PHONY: html
html:
	jupyter-book build .


.PHONY: html-hub
html-hub: conf.py
	sphinx-build  . _build/html -D html_baseurl=${JUPYTERHUB_SERVICE_PREFIX}proxy/absolute/8000
	@echo
	@echo "To start the Python http server, use:"
	@echo "python -m http.server --directory ${PWD}/_build/html"
	@echo "and visit this link with your browser:"
	@echo "https://stat159.datahub.berkeley.edu/user-redirect/proxy/8000/index.html"


conf.py: _config.yml _toc.yml
	jupyter-book config sphinx .


.PHONY : clean
clean:
	rm -rf figures/*
	rm -rf _build/html/
	rm -rf _build/*

.PHONY : help
help : Makefile
	@sed -n 's/^##//p' $<