FROM python:3.12.5-alpine

# Create a directory for the application
RUN mkdir /DjangoHelloWorld
WORKDIR /DjangoHelloWorld

# Copy the application code and the .pg_service.conf file
COPY . .
COPY .pg_service.conf /root/.pg_service.conf
COPY .my_pgpass /root/.my_pgpass

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port
EXPOSE 8000

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]