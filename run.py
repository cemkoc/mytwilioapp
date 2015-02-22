from flask import Flask, request, redirect
import twilio.twiml
import os

app = Flask(__name__)

# callers = {
#         "+14152983952": "Jem Koch"
# }
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming requests."""
    from_number = request.values.get('From', None)
    body = request.values.get('Body', None)
    resp = twilio.twiml.Response()
    
    if body:	
    	resp.message("You sent me: " + body)
    else:
    	resp.message("You sent nothing.")

    return str(resp)
 

if __name__ == "__main__":
    app.run(debug=True)