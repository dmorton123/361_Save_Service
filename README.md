## 361 Save Service
Group 33 David and Lauren

## Communication Contract 
1. We will communicate primarily through Teams. 
2. We will respond to messages within 24 hours, even if it’s just “I see this and have no objectives”. 
3. If a team member has been unresponsive, we will check in over email or on Canvas. 
4. We will be polite and willing to listen to each other, and focus on finding solutions to problems instead of arguing.
5. We will minimize unspoken assumptions about classwork. In particular, we will prioritize communication about our personal intents for completing assignment work and expectations from the other team member. 
6. If a team member is concerned they will not be able to complete their work by the deadline, reach out to team members for help at least 24 hours before the deadline.
   
## Micro-service Description
This service handles saving and loading data so that a session can be ended and picked up later from the same spot it uses Flask and REST API to communicate. It defaults to running on http://localhost:5000. 

pip install -r requirements.txt

It is recommended that you import requests in your main program to help communicate with the service.

communication contract: To save the main program sends a JSON containing data to the save service using a POST request, the save service creates a "saves" folder and puts a file with a name of the users choosing in that folder with the given information. The service also returns a json (which can be converted into a dictionary when received) with the sections "success" which will be either True or False, "message" which contains a short message about the status of the save, and filepath which is the filepath to the new file. To load information the main program requests a JSON using a GET request and a filename, the service sends back a JSON with the sections "success" which will be true or false and "data" which contains the data within the save file.

example save:
```
SAVE_SERVICE_URL = "http://localhost:5000"
SERVICE_TIMEOUT = 5
example_dict = {"health":50, "name": "Joe", "age": 53, location: "Oregon"}
response = requests.post(f"{SAVE_SERVICE_URL}/save", json={"data": example_dict, "filename": "example_name"}, timeout=SERVICE_TIMEOUT)
result = response.json() #turns the json that was returned from the service into a python dict
print(f"Result message: {result.get('message', 'No message in response')}") #this would print the "message" portion of the response
```

this would result in a file called example_name.json being created in a folder called "saves" which will be in the same folder as the microservice is.

example load:
```
response = requests.get(f"{SAVE_SERVICE_URL}/load/{filename}", timeout=SERVICE_TIMEOUT)
result = response.json() #this will convert the recived JSON into a python dictionary given you have imported requests
#from this point you have the data needed to reconstruct the game state from where it was left off
```
UML Diagram:

         Main Program                         Save Microservice
                |                                        |
                |---- POST /save (data, filename) ------>|
                |                                        |
                |<--- JSON {success, message, path} -----|
                |                                        |
                |                                        |
                |---- GET /list-saves ------------------>|
                |                                        |
                |<--- JSON {success, saves[]} -----------|
                |                                        |
                |                                        |
                |---- GET /load/{filename} ------------->|
                |                                        |
                |<--- JSON {success, data} --------------|
                |                                        |

