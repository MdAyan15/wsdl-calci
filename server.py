from spyne import Application, rpc, ServiceBase, Integer, Float
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from flask import Flask, send_from_directory, request, Response
from flask_cors import CORS
import os

# Calculator SOAP Service
class CalculatorService(ServiceBase):
    @rpc(Integer, Integer, _returns=Integer)
    def add(self, a, b):
        return a + b

    @rpc(Integer, Integer, _returns=Integer)
    def subtract(self, a, b):
        return a - b

    @rpc(Integer, Integer, _returns=Integer)
    def multiply(self, a, b):
        return a * b

    @rpc(Integer, Integer, _returns=Float)
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return float(a) / float(b)

# Flask app
app = Flask(__name__)
CORS(app)

# SOAP app
soap_app = Application(
    [CalculatorService],
    tns='calculator',
    name='CalculatorService',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

soap_wsgi_app = WsgiApplication(soap_app)

# Routes
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/soap/calculator', methods=['GET', 'POST', 'OPTIONS'])
def soap_service():
    status_headers = {}

    def start_response(status, headers, exc_info=None):
        status_headers['status'] = status
        status_headers['headers'] = headers

    result = b"".join(soap_wsgi_app(request.environ, start_response))

    status_code = int(status_headers['status'].split()[0])
    response = Response(result, status=status_code)

    for header_name, header_value in status_headers['headers']:
        response.headers[header_name] = header_value

    return response

# Run server
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))  # Render uses PORT env variable
    print(f"Calculator Web Service running on http://localhost:{port}")
    print(f"WSDL available at: http://localhost:{port}/soap/calculator?wsdl")
    app.run(host='0.0.0.0', port=port)
