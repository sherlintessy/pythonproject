"""Routes for the course resource.
"""

"""
-------------------------------------------------------------------------
Challenge general notes:
-------------------------------------------------------------------------

1. Bonus points for returning sensible HTTP codes from the API routes
2. Bonus points for efficient code (e.g. title search)
"""

from flask import render_template
import connexion
import data
app = connexion.App(__name__, specification_dir='./')
#app.add_api('swagger.yml')
# Import the API routes
from routes.course import *
def home():
    return render_template('home.html')
# Required because app is imported in other modules
if __name__== '__main__':
    print("Loading data", end=" ")
    data.load_data()
    print("... done")
    app.run(debug=False)
