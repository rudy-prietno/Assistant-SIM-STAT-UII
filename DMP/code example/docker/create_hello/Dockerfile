# argument
ARG TAG=3.6-alpine

# base images
FROM python:${TAG}

# Install gunicorn
RUN pip install gunicorn

# Install falcon
RUN pip install falcon

# add create_hello folder from local into folder /create_hello in container
ADD ./create_hello /create_hello

# file permission
RUN chmod +x ./create_hello/environment.sh

# expose port
EXPOSE 3000

# set working directory active in container
WORKDIR /create_hello

# environment inisiate
ENV env_var_name=${env_var_name} 

# set command for entrypoint in terminal container
CMD ["sh","environment.sh"]