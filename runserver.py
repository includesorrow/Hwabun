
"""
This script runs the KHUProject_FP application using a development server.
"""

from os import environ
from KHUProject_FP import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '8000'))
    except ValueError:
        PORT = 5555
    # app.run(HOST, PORT)
    app.run(host='0.0.0.0', port=8000) 
