FROM ubuntu:18.04


# Set working directory
WORKDIR /app


RUN apt-get update &&\
    apt-get install python3.7 -y &&\
    apt-get install python3-pip -y &&\
    apt-get install graphviz -y

RUN git clone https://github.com/ansahaRH/streamlit_app_test.git .

#Copy the requirements file into a container
COPY requirements.txt .

#Install the dependencies mentioned in a requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

#Copy the rest of the application code 
COPY . . 

#Expose the port
EXPOSE 8501

#Command to run streamlit apps
CMD ["streamlit", "run", "menu_demo.py", "--server.port=8501", "--server.address=0.0.0.0"]

