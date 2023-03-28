# Home Assignment

This is a simple web application that allows users to purchase random items and view their purchase history.

### Technologies Used

- Python FastApi for the API
- MongoDB for the database
- Kafka for pub/sub messaging
- React for the front-end

### Requirements

- Docker and Docker Compose

### Getting Started

1. Clone the repository: `git clone https://github.com/liorcic/home_assignment_is.git`
2. Navigate to the project directory: `cd home_assignment_is`
3. Create environmment variables: `export MONGO_USER=root MONGO_PASSWORD=password`
4. Create a directory for persistent data called db_data: `mkdir db_data`
5. Build and start the containers: `docker-compose up -d`

### Usage

Currently, the front end is not supported. However you can use the swagger documentation of the customer web server in order to interact with the different components.

1. Open a web browser and go to `http://localhost:6200/docs`
2. Click on the different tabs and try them out.

The user web service is using another api responsible of the crud opertions on mongodb.

You can access the server api at the url `http://localhost:6201/docs`

### API Endpoints

- `POST /buy`: Trigger's a random buy request
- `GET /buyList`: Get all purchases
- `GET /buyList/{user_id}`: Get all purchases of a specific user

**POST /buy**

No body required since it will generate a random purchase.

Response body:
```json
{
  "username": "string",
  "user_id": 0,
  "price": 0,
  "product": "string",
  "timestamp": "2023-01-01T00:00:00.000000"
}
```

**GET /buyList**

Response body:

```json
[
  {
    "_id": "string",
    "username": "string",
    "user_id": 0,
    "price": 0,
    "product": "string",
    "timestamp": "2023-01-01T00:00:00.000000"
  }
]
```
