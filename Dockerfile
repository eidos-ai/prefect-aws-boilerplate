FROM prefecthq/prefect:latest-python3.9
RUN /usr/local/bin/python -m pip install --upgrade pip
COPY . /opt/repository/
COPY src /opt/repository/src/
COPY flows /opt/repository/flows/
WORKDIR /opt/repository
ENV PYTHONPATH "${PYTHONPATH}:/opt/repository/"
RUN pip install -r requirements.txt