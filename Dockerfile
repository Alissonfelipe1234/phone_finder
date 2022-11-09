FROM python:3.11-alpine3.15
	
WORKDIR /application
	
RUN pip install --upgrade pip
	
COPY requirements.txt .
	
RUN pip install -r requirements.txt
	
COPY app.py .
COPY orchestration.py orchestration.py
	
ENTRYPOINT ["python","./app.py"]