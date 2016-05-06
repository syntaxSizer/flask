#!flask/bin/python

#imprting app variable from our package and invoke it's run method
#to start the server app holds Flask instance !!!
from app import app
app.run(debug=True)
