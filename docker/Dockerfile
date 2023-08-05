FROM python:3.9 AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
COPY . .

RUN apt-get update && apt-get install -y libnss3-dev libgtk-3.0 libgbm-dev libnss3 libatk-bridge2.0-0 libasound2
RUN apt-get clean

RUN wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/115.0.5790.170/linux64/chrome-linux64.zip
RUN unzip chrome-linux64.zip
RUN rm -rf chrome-linux64.zip
RUN wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/115.0.5790.170/linux64/chromedriver-linux64.zip
RUN unzip chromedriver-linux64.zip
RUN rm -rf chromedriver-linux64.zip

CMD ["bash"]
