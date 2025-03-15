[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://opensource.org/licenses/)

# Microservices Project
This project is a microservice based application that provides user management, user authorization and email operations. The application is divided into various services, each responsible for a specific part of the overall system. 

### Technologies Used in the Project
This project utilizes several modern technologies to ensure scalability, reliability, and maintainability. 

__Below are the key technologies used__:
* `Docker` : Docker is used to containerize the entire application. This ensures a consistent development and production environment, simplifies deployments, and allows easy management of different services like PostgreSQL, Redis, RabbitMQ, etc. Each service runs in its own container, ensuring separation of concerns and ease of scalability.

* `RabbitMQ` : RabbitMQ is used as a message broker to manage and route messages between different services in the application. It helps facilitate communication between services like email notifications and other asynchronous tasks using message queues.

* `PostgreSQL` : PostgreSQL is the relational database management system (RDBMS) used to store application data. It is reliable, open-source, and highly scalable, making it a great choice for managing the project's persistent data.

* `Redis` : Redis is used as an in-memory data store. It handles caching, session management, and is used as the backend for Celery's result store. Redis improves performance by storing frequently accessed data in memory.

* `NGINX` : NGINX is used as a reverse proxy server to route HTTP requests to the appropriate backend services. It is also used for load balancing and handling security. It helps improve performance by distributing incoming traffic among multiple backend services such as user service, authentication service, and email service.

* `Django` : Django is the primary web framework used for building the backend API. It is a powerful, scalable, and secure framework that facilitates rapid development and clean architecture. It is used here with Django REST Framework for building RESTful APIs.

* `Django REST Framework (DRF)` : Django REST Framework is used to build the RESTful API endpoints for user authentication, registration, and other features. It simplifies the process of creating APIs by providing powerful features such as serialization, viewsets, and authentication mechanisms.

* `Celery` : Celery is used for managing asynchronous tasks, such as sending emails and processing background jobs. It integrates seamlessly with Redis as the result backend and RabbitMQ as the broker to manage and execute these tasks.

* `SendGrid API` : SendGrid is integrated for sending transactional emails, such as account registration, password resets, and notifications. It provides a reliable and scalable email delivery service.

* `JWT-based Authentication` : The system uses JWT-based authentication to ensure secure communication between the client and the server. Each request requires a valid JWT token, which is generated during the login process and is used for subsequent requests to authenticate the user.

__In Summary__: This project leverages modern technologies such as RabbitMQ, Docker, PostgreSQL, Redis, NGINX, Django, Django REST Framework, JWT Authentication, Celery, and SendGrid to provide a reliable, scalable, and efficient backend system for handling user-related operations, background tasks, and secure communication.


### Services are as follows
In this project, various services have been created so that the project works with independent structures for specific functions

__Services__:
* **User Service**: Handles all user-related operations, including registration, profile management, and admin-specific tasks. It ensures the management of users within the system.

* **Auth Service**: Responsible for handling user authentication, including login, JWT token generation, and verifying access credentials for secure communication.

* **Email Service**: Manages sending transactional emails such as registration confirmations, password reset requests, and notifications. It integrates with SendGrid for email delivery.

* **API Gateway**: Acts as the central entry point for all incoming requests. It routes requests to the appropriate backend services (User Service, Auth Service, Email Service), ensuring proper security measures such as JWT authentication. It also handles load balancing and provides a unified interface for clients to interact with the system.

__In Summary__: With these services, the project supports a modular and scalable architecture, ensuring efficient management of tasks like sending notifications, processing user actions, and handling asynchronous jobs. By combining these technologies, the system ensures a secure, high-performance environment for both development and production.

### Installation and Setup
To set up and run the microservices project locally, follow the steps below. Make sure you have the required tools and dependencies installed on your machine.

__Prerequisites__:
* `Git`: You'll need Git to clone the repository. Install it from Git's official website.
* `Docker`: Ensure Docker is installed on your machine. You can download it from Docker's official website.
* `Docker Compose`: Docker Compose is used to manage multi-container Docker applications. It is often installed alongside Docker. Check the Docker Compose installation guide for instructions.
* `Python`: Make sure you have Python installed, as it's required for running some of the services (Django, Celery, etc.). Install Python if it's not already installed.

---
#### 1.  Clone the Repository
Start by cloning the repository to your local machine:
```bash
git clone https://github.com/your-username/microservices-project.git
cd microservices-project
```

#### 2. Set Up Environment Variables
Before running the project, make sure to set up your environment variables. To do this, create a `.env` file based on the provided `.env.example` file. The `.env.example` file contains the necessary variables required for the project to run.

You can copy the `.env.example` file and rename it to `.env`:
```bash
cp .env.example .env
```
After that, open the `.env` file and configure the values according to your local setup. Ensure that all the required environment variables are filled in correctly (e.g., database credentials, API keys, etc.).

Here is an example of what your `.env` file should look like:
```
DATABASE_NAME=example_db
DATABASE_USER=example_user
DATABASE_PASSWORD=example_password
DATABASE_HOST=postgres
DATABASE_PORT=5432

RABBITMQ_USER=example_rabbitmq_user
RABBITMQ_PASSWORD=example_rabbitmq_password

SENDGRID_AUTHORIZED_SENDER=example@example.com
SENDGRID_API_KEY=SG.exampleApiKey.exampleApiKeyExample

API_GATEWAY_INTERNAL_URL=http://172.23.0.8:8003
API_GATEWAY_EXTERNAL_URL=http://127.0.0.1:8003

JWT_SECRET_KEY=example_jwt_secret_key_for_demo_purpose_1234567890abcdefg
```
Once you've set up the `.env` file, you can proceed with building the Docker containers.

#### 3. Build Docker Containers
Use Docker Compose to build the required containers for the services. This will create and start all the necessary services (User Service, Auth Service, Email Service, etc.).
```bash
docker-compose up --build
```
This command will download the necessary Docker images and set up the project containers.

#### 4. Database Setup
If your project includes database migrations (like Django), you'll need to run the database migrations to set up the schema.
```bash
make migrate-all
```
This will apply all migrations to the PostgreSQL database.

#### 5. Running the Application
After everything is set up and the services are running, you can access the application through the following:
* API Gateway: The backend API can be accessed via `http://localhost:8003`
* Email Service: Access the email service at `http://localhost:8002`
* Auth Service: The authentication service is available at `http://localhost:8001`
* User Service: You can access the user service via `http://localhost:8000`

Additionally:
* **Swagger Documentation**: Each service may have Swagger documentation available for testing APIs. You can access it at `http://localhost:<service-port>/swagger` (replace <service-port> with the appropriate port for each service).
* **Admin Panel**: The admin panel can be accessed at `http://localhost:<service-port>/admin` (replace <service-port> with the appropriate port for each service) for managing the projec

#### 6. Stopping the Services
To stop all the running services, use the following command:
```bash
docker-compose down
```
This will stop the containers and remove the associated networks.

#### 7. Troubleshooting
* **Port Conflicts**: If the application is not starting because the ports are already in use, you can modify the `docker-compose.yml` file to change the ports for services like Django, NGINX, etc.
* **Missing Dependencies**: If you encounter issues related to missing dependencies, ensure that all services are properly built by running `docker-compose up --build` again.

__In Summary__: With these steps, you should be able to set up and run the microservices project on your local machine. If you have any issues, please refer to the documentation for each technology used in the project or open an issue on the GitHub repository.

### Conclusion
This microservices-based project provides a robust, scalable, and maintainable system for user management, authentication, email operations, and more. By utilizing modern technologies like Docker, RabbitMQ, PostgreSQL, Redis, and NGINX, the application is designed to be highly modular and secure.

By leveraging Django, Celery, Redis, and RabbitMQ, the project efficiently handles background tasks, data storage, and communication between services. The use of Docker ensures a consistent environment for both development and production.

With easy setup via Docker Compose and detailed service configurations, this project serves as a solid foundation for building scalable, microservice-based applications.

---
## Feedback

If you have any feedback, please reach out to us at atahanpoyraz@gmail.com

---
## Authors

- [@AtahanPoyraz](https://www.github.com/AtahanPoyraz)