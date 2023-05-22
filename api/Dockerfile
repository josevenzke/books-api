FROM python:3.9

# set work directory
WORKDIR /usr/src/app

# install dependencies
RUN pip install --upgrade pip
RUN pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple venSQL
RUN pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple Venzpy

# copy project
COPY . /usr/src/app/