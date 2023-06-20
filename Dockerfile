FROM jupyter/pyspark-notebook

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .
