from python:3.12
RUN apt update -y && apt install awscli -y
workdir /app
copy . /app
RUN pip install -r requirements.txt
RUN pip install --upgrade accelerate
RUN pip uninstall transformers
RUN pip install transformers

CMD ["python3","app.py"]