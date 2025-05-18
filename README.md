# Calculator Web Service and Client

This project consists of two parts:
1. A SOAP web service that provides calculator operations
2. A modern web interface to interact with the calculator service

## Prerequisites
- Python 3.x
- Required Python packages:
  - spyne (for SOAP web service)
  - flask (for web server)
  - flask-cors (for CORS support)

## Installation

1. Install the required packages:
```bash
pip install spyne flask flask-cors
```

## Running the Application

1. Start the server:
```bash
python server.py
```

2. Open your web browser and navigate to:
```
http://localhost:8000
```

The web interface will be displayed, allowing you to:
- Enter two numbers
- Choose an operation (addition, subtraction, multiplication, division)
- See the result instantly

## Features
- Modern, responsive web interface
- Real-time calculations
- Error handling
- Mobile-friendly design

## Available Operations
- Addition
- Subtraction
- Multiplication
- Division

## Note
The application is now ready for hosting as it:
- Uses a production-ready Flask server
- Implements CORS for cross-origin requests
- Has a responsive, mobile-friendly interface
- Includes proper error handling 