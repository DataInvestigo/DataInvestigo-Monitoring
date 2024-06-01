# DataInvestigo Monitoring Application

This project is an DataInvestigo Monitoring application using PostgreSQL as the database.

## Prerequisites

- Python 3.x
- PostgreSQL

## Setup Instructions

1. **Clone the repository**
   git clone https://github.com/DataInvestigo/DataInvestigo-Monitoring.git
   cd DataInvestigo-Monitoring

2. **Create a virtual environment and activate it**
   python -m venv venv
   source venv/bin/activate # On Windows, use `venv\Scripts\activate`

3. **Install the required dependencies**
   pip install -r requirements.txt

4. **Set up the environment variables**

   Create a `.env` file in the root of your project and add the following:
   DATABASE_URL=
   DATABASE_NAME=
   DATABASE_USER=
   DATABASE_PASSWORD=
   DATABASE_HOST=
   DATABASE_PORT=
   SECRET_KEY=

5. **Run the application**
   uvicorn app.main:app --reload
