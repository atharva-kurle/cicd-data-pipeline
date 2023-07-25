FROM python

WORKDIR /app

COPY . .

RUN pip install pandas

CMD ["python3","pipeline.py"]

COPY /app .
