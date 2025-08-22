# Airline Market RPK Analyzer

This web application provides a visual analysis of Revenue Passenger Kilometers (RPK) for various airline markets. Users can select a market, specify a date range, and view the corresponding RPK data on a scatter plot. This tool is designed to help users understand airline performance and trends over time.

## Features

-   **User Authentication:** Secure login and registration system.
-   **Market Selection:** Choose from a list of available airline markets.
-   **Date Filtering:** Filter RPK data by a specific start and end date.
-   **Interactive Charting:** View RPK data on a scatter plot powered by Plotly.js.
-   **Data Visualization:** Clear and intuitive visualization of RPK trends.
-   **Include Null Data:** Option to include or exclude null data points from the chart.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

-   [Docker](https://www.docker.com/get-started)
-   [Docker Compose](https://docs.docker.com/compose/install/)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2.  **Build and run the Docker containers:**

    ```bash
    docker-compose up --build
    ```

    This command will build the Docker image for the Flask application and start the `web` and `db` services. The application will be available at `http://localhost:5000`.

3.  **Create the database tables:**

    The application is configured to create the necessary database tables on startup.

## Usage

1.  **Register a new account:** Navigate to `http://localhost:5000/register` to create a new user account.
2.  **Log in:** After registering, log in with your credentials at `http://localhost:5000/login`.
3.  **Access the dashboard:** Once logged in, you will be redirected to the dashboard at `http://localhost:5000/`.
4.  **Analyze RPK data:**
    -   Select a market from the dropdown menu.
    -   (Optional) Specify a start and end date for the data you want to analyze.
    -   (Optional) Check the "Include Null Data" box to include data points with null RPK values.
    -   Click the "Submit" button to generate the chart.

## Technology Stack

-   **Backend:**
    -   [Flask](https://flask.palletsprojects.com/): A lightweight WSGI web application framework in Python.
    -   [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/): A Flask extension that adds support for SQLAlchemy.
    -   [Flask-Login](https://flask-login.readthedocs.io/): A Flask extension that provides user session management.
    -   [Psycopg2](https://www.psycopg.org/): A PostgreSQL adapter for Python.

-   **Frontend:**
    -   [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript): The programming language for the web.
    -   [Plotly.js](https://plotly.com/javascript/): A high-level, declarative charting library.
    -   [Choices.js](https://github.com/jshjohnson/Choices): A lightweight, configurable select box/text input plugin.
    -   [Tailwind CSS](https://tailwindcss.com/): A utility-first CSS framework.

-   **Database:**
    -   [PostgreSQL](https://www.postgresql.org/): A powerful, open-source object-relational database system.

-   **DevOps:**
    -   [Docker](https://www.docker.com/): A platform for developing, shipping, and running applications in containers.
    -   [Docker Compose](https://docs.docker.com/compose/): A tool for defining and running multi-container Docker applications.
