FROM python:3.6
WORKDIR /Project/demo

COPY requirements.txt ./
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN virtualenv flask
RUN flask/bin/pip install flask

COPY . .

# CMD ["gunicorn", "app:app", "-c", "./gunicorn.conf.py"]
CMD ["python" , "app.py" , "--nothreading"]