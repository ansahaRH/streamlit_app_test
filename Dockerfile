FROM registry.redhat.io/ubi8/python-39:latest

COPY . .

EXPOSE 8080

RUN echo "Installing softwares and packages" && \     
    pip3 install -r requirements.txt

# CMD ["streamlit","run","menu_demo.py"]

CMD ["streamlit", "run", "--server.port=8080", "menu_demo.py"]