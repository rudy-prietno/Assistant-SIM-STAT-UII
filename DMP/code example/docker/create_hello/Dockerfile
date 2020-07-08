# argument
ARG TAG=3.6-alpine

# base images
FROM python:${TAG}

# Install gunicorn
RUN pip install gunicorn

# Install falcon
RUN pip install falcon

# add create_api folder from local into folder /create_api in container
ADD ./create_api /create_api

# file permission
RUN chmod +x ./create_api/environment.sh

# expose port
EXPOSE 3000

# set working directory active in container
WORKDIR /create_api

# environment inisiate
ENV env_var_name=${env_var_name} 

# set command for entrypoint in terminal container
CMD ["sh","environment.sh"]