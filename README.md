# Currency Exchange Web Service
This is a Flask-based web service that provides currency exchange data fetched from an external API and stored in a PostgreSQL database. It offers RESTful APIs to retrieve currency rates by country, currency, as well as other functionalities like fetching the highest and lowest currency of the day and historical data for a particular currency.

Architecture
The project is structured as follows:

```
project/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   ├── routes.py
│   └── tests/
│       └── test_routes.py
│
├── docker/
│   └── Dockerfile
│
├── .env
├── requirements.txt
└── run.py
```

- app/: Contains the main application code.
    - init.py: Initializes the Flask application and database.
    - config.py: Defines configuration variables, including loading from environment variables.
    - models.py: Defines database models using SQLAlchemy.
    - routes.py: Implements API routes for fetching and storing currency exchange data.
    - tests/: Contains test cases for the application routes.
- docker/: Contains the Dockerfile for building a Docker image.
- .env: Stores environment variables.
- requirements.txt: Lists the project dependencies.
- run.py: Entry point for running the Flask application.


## Setup
1. Clone the repository:

> git clone <repository_url>
> cd <repository_directory>

2. Install dependencies:
> pip install -r requirements.txt

3. Create a .env file in the project root and set the following environment variables:
```
SECRET_KEY=<your_secret_key>
DATABASE_URI=<your_database_uri>
API_KEY=<your_api_key>
Replace <your_secret_key>, <your_database_uri>, and <your_api_key> with appropriate values.
```

## Running the Application
To run the application locally, execute:

> python run.py

This will start the Flask server, and the application will be accessible at `http://localhost:5000.`

## Running Tests
To run the tests, execute:

> pytest app/tests/test_routes.py

This will run the test cases defined in test_routes.py and provide the test results.

## Docker

Alternatively, you can build a Docker image and run the application inside a container:

1. Build the Docker image:

> docker build -t currency-exchange .

2. Run the Docker container:
> docker run -p 5000:5000 currency-exchange

This will start the Flask server inside a Docker container, and the application will be accessible at `http://localhost:5000`.

