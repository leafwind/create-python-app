# this is our first build stage, it will not persist in the final image
FROM python:3.7.7 as intermediate
LABEL maintainer="leafwind.cs@gmail.com"

# Install OS dependencies

# for PyHive
RUN apt-get update && apt-get install -y --no-install-recommends libsasl2-modules libsasl2-dev python3-pip

# Install Python dependencies

# add credentials on build
ARG SSH_PRIVATE_KEY
RUN mkdir /root/.ssh/ && echo "${SSH_PRIVATE_KEY}" > /root/.ssh/id_rsa && chmod 600 /root/.ssh/id_rsa
# make sure your domain is accepted
RUN touch /root/.ssh/known_hosts && ssh-keyscan github.com >> /root/.ssh/known_hosts
# install requirements (both Git and PyPI)

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# 2nd stage, this is MUST to prevent from leaking private key
# ref: https://vsupalov.com/build-docker-image-clone-private-repo-ssh-key/

FROM python:3.7.7
LABEL maintainer="leafwind.cs@gmail.com"

# copy the repository from the previous image

# for libsasl2
COPY --from=intermediate /usr/lib/x86_64-linux-gnu/sasl2 /usr/lib/x86_64-linux-gnu/sasl2
# for site-packages like PyYaml
COPY --from=intermediate /usr/local/lib/python3.7/site-packages /usr/local/lib/python3.7/site-packages

COPY . /opt/my_python_app
WORKDIR /opt/my_python_app

CMD ./run.sh