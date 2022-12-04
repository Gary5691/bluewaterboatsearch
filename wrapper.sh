#!/bin/bash

#start the scraper
#python3 scrape.py &

#start the searcher
python3 search.py &

#start the gunicorn and point it at the webapp
gunicorn -w 4 -b 0.0.0.0:8000 webapp:app &

wait -n 
