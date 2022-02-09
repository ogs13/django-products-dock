###########
# BUILDER #
###########

# pull official base image
FROM python:3.9-slim as builder

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt-get update -qq \
    && apt-get install --no-install-recommends --yes \
        build-essential netcat \
        postgresql-server-dev-all gcc python3-dev \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get autoremove --purge --yes \
        build-essential

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt

#########
# FINAL #
#########

# pull official base image
FROM python:3.9-slim

# create the app user
RUN useradd -ms /bin/bash app && usermod -a -G users app

# create the appropriate directories
ENV HOME=/home/app

#django
ENV APP_HOME=/home/app/core
RUN mkdir $HOME/static_cdn
RUN mkdir $HOME/static_cdn/static

WORKDIR $APP_HOME

# copy entrypoint.prod.sh
COPY entrypoint.sh .
RUN sed -i 's/\r$//g'  $APP_HOME/entrypoint.sh
RUN chmod +x  $APP_HOME/entrypoint.sh

# copy project
COPY . $APP_HOME

# install dependencies
RUN apt-get update -qq \
    && apt-get install --no-install-recommends --yes \
        build-essential netcat \
        postgresql-server-dev-all gcc python3-dev \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get autoremove --purge --yes \
        build-essential

COPY --from=builder /usr/src/app/wheels $HOME/wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache $HOME/wheels/*

# chown all the files to the app user
RUN chown -R app:app $HOME

# change to the app user
USER app

# run entrypoint.prod.sh
ENTRYPOINT ["/home/app/core/entrypoint.sh"]