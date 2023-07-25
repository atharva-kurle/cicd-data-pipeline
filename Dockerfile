FROM python

RUN pip install pandas

EXPOSE 8000

CMD ["python3","pipeline.py"]
