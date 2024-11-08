# Smart Streetlight System

This project is a comprehensive solution for managing smart streetlight systems with integrated features such as user management, device control, energy analytics, alert notifications, and monitoring through embedded Power BI dashboards. The application supports database configurations for MySQL, PostgreSQL, and MongoDB, with a flexible API and service-based structure.

## Table of Contents

1. Features
2. Technologies Used
3. Project Structure
4. Installation
5. Configuration
6. Endpoint Usage
7. Testing


------

## Features

- User and Role Management with authentication
- Device Management for smart streetlights
- Real-time Control of streetlights with MQTT integration
- Energy Consumption Analytics
- Alert Notifications and Logging
- Multi-database configuration (MySQL, PostgreSQL, MongoDB)
- Rate Limiting with Redis support
- Embedded Power BI Dashboard for monitoring and reporting

## Technologies Used

- **Flask**: Web framework
- **SQLAlchemy**: ORM for database interactions
- **Flask-RESTful**: RESTful API development
- **Redis**: Session and rate limiting management
- **MQTT (with CloudMQTT)**: Communication protocol for IoT control
- **Power BI Embedded**: Dashboard visualization
- **PostgreSQL, MySQL, MongoDB**: Database options
- **Gunicorn**: Application server
- **pytest, pytest-cov, Faker**: Testing and data generation
- **Docker**: Containerization

## Project Structure

```
/smart-streetlight-system
│
├── app/
│   ├── __init__.py               # Initializes the Flask app
│   ├── config.py                 # Application configuration
│   ├── models/                   # Database models
│   │   ├── user.py               # User model
│   │   ├── role.py               # Role and permission model
│   │   ├── device.py             # Streetlight device model
│   │   ├── alert.py              # Alert model
│   │   ├── energy.py             # Energy analysis data model
│   │   ├── log.py                # Log model
│   ├── api/                      # API modules
│   │   ├── user_api.py           # User management API
│   │   ├── role_api.py           # Role management API
│   │   ├── device_api.py         # Device management API
│   │   ├── alert_api.py          # Alert management API
│   │   ├── energy_api.py         # Energy analysis API
│   │   ├── control_api.py        # Streetlight control API
│   │   ├── map_api.py            # Map monitoring API
│   │   ├── meter_api.py          # Remote meter reading API
│   │   ├── strategy_api.py       # Strategy management API
│   │   ├── db_config_api.py      # Database configuration wizard API
│   ├── services/                 # Service layer
│   ├── utils/                    # Utility functions
│
├── migrations/                   # Database migrations
├── tests/                        # Unit and integration tests
├── dashboard/                    # Power BI Dashboard views
├── requirements.txt              # Project dependencies
├── run.py                        # Application entry point
└── README.md                     # Project documentation
```

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/smart-streetlight-system.git
   cd smart-streetlight-system
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables** (e.g., `DATABASE_URL`, `MQTT_BROKER_URL`).

4. **Run migrations**:

   ```bash
   flask db upgrade
   ```

5. **Start the application**:

   ```bash
   gunicorn -w 4 run:app
   ```

## Configuration

- **Database**: Configure `DATABASE_URL` for PostgreSQL/MySQL and `MONGO_URI` for MongoDB in `config.py`.
- **Redis**: Set `REDIS_URL` for session and rate limit storage.
- **MQTT**: Configure `MQTT_BROKER_URL` and `MQTT_PORT`.
- **Power BI**: Embed settings in `dashboard/templates`.

## Endpoint Usage

### User Management

- **`POST /api/register`** - Register a new user
- **`POST /api/login`** - Login and receive a token
- **`GET /api/users`** - Get all users (admin-only)
- **`GET /api/users/<id>`** - Get specific user details

### Role Management

- **`GET /api/roles`** - Retrieve roles
- **`POST /api/roles`** - Create a new role

### Device Management

- **`GET /api/devices`** - List all devices
- **`POST /api/devices`** - Create a new device
- **`GET /api/devices/<id>`** - Retrieve device details
- **`PUT /api/devices/<id>`** - Update device
- **`DELETE /api/devices/<id>`** - Delete device

### Alert Management

- **`GET /api/alerts`** - Get active alerts
- **`POST /api/alerts`** - Create a new alert
- **`DELETE /api/alerts/<id>`** - Remove an alert

### Energy Analytics

- **`GET /api/energy`** - Retrieve energy usage data
- **`POST /api/energy`** - Upload energy usage data

### Control API (Real-Time Device Control)

- **`POST /api/control/on`** - Turn on streetlight
- **`POST /api/control/off`** - Turn off streetlight

### Map Monitoring

- **`GET /api/map/devices`** - Retrieve location data for all devices

### Meter API (Remote Meter Reading)

- **`GET /api/meter/read`** - Retrieve meter data for devices

### Strategy Management

- **`POST /api/strategy`** - Define new strategy
- **`GET /api/strategy`** - Get current strategies

### Database Configuration Wizard

- **`POST /api/db_config`** - Configure selected database (MySQL, PostgreSQL, or MongoDB)

## Testing

This project includes unit and integration tests for comprehensive validation. Testing utilities include `pytest` with `pytest-cov` for coverage and `Faker` for mock data generation.

1. **Run tests**:

   ```bash
   pytest --cov=app tests/
   ```

2. **Generate test data**:

   - Use `Faker` in `tests/fixtures/fake_data_generator.py` to create mock data for testing scenarios.
