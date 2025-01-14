FROM python:3.12-slim

WORKDIR /customer-churn-prediction

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python", "run.py"]
