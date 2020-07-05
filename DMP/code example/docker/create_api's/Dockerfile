# try python:3.6-alpine and pypy:3.6

FROM python:3.6-alpine
# FROM pypy:3.6

# expose port in containers
EXPOSE 5000

# Install gunicorn
RUN pip install gunicorn

# Install falcon
RUN pip install falcon

# copy create_api folder from local into folder /create in container
COPY ./create_api /create_api

# set working directory active in container
WORKDIR /create_api

# set command for entrypoint in terminal container
CMD ["gunicorn", "-b", "0.0.0.0:5000", "main:app"]