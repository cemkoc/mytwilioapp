from flask import Flask, request
from twilio import twiml
from twilio.rest import TwilioRestClient
import os
 
app = Flask(__name__)

callers = {
        "+14152983952": "Jem Koch"
}
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming requests."""
    from_number = request.values.get('From', None)
    body = request.values.get('Body', None)
    resp = twilio.twiml.Response()
    
 	if from_number in callers:
        resp.message("Well hello there " + callers[from_number])
        resp.message("You sent me: " + body)
 	
 	else: 
 		resp.message("Hello, I don't know who you are.")

    return str(resp)
 

if __name__ == "__main__":
    app.run(debug=True)