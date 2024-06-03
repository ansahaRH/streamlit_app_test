#Python Image
FROM python3:9-slim

# Set working directory
WORKDIR /app


RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/streamlit/streamlit-example.git .

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

