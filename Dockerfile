FROM python:3.9-slim

# assign working directory 
WORKDIR /channel_processing

# copy all the required files 
COPY requirements.txt .
COPY ./src ./src
COPY ./raw_data ./raw_data
COPY . .

RUN pip install --upgrade pip
# Install dependency inside the container
RUN pip install -r requirements.txt 

# RUN the pytest
RUN pytest  
# RUN the flask server 
CMD [ "python","./src/main.py" ]