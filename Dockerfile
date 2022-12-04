FROM ubuntu:focal
WORKDIR /usr/src/app
RUN DEBIAN_FRONTEND=noninteractive \
apt update && \
apt install -yq --no-install-recommends python3 python3-pip
RUN python3 -m pip install requests bs4 gunicorn flask
RUN mkdir templates
COPY templates/index.html templates/index.html
COPY webapp.py .
COPY got_boats.json .
COPY scrape.py .
COPY search.py .
COPY wrapper.sh .
EXPOSE 8000
ENTRYPOINT ["./wrapper.sh"]