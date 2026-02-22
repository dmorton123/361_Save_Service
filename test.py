import requests
SAVE_SERVICE_URL = "http://localhost:5000"
SERVICE_TIMEOUT = 5


def save(dict, filename = "example_name"):
    
    
    response = requests.post(f"{SAVE_SERVICE_URL}/save", json={"data": dict, "filename": filename}, timeout=SERVICE_TIMEOUT)
    result = response.json() #turns the json that was returned from the service into a python dict
    print(f"Result message: {result.get('message', 'No message in response')}") #this would print the "message" portion of the response


def load(filename):
    response = requests.get(f"{SAVE_SERVICE_URL}/load/{filename}", timeout=SERVICE_TIMEOUT)
    result = response.json() #this will convert the recived JSON into a python dictionary given you have imported requests
    print(result)



def main(): 
    choice = 0
    
    while int(choice) != 3: 
        choice = input("Press 1 to save. \nPress 2 to load. \nPress 3 to exit.\n")
    
        if int(choice) == 1: 

            example_dict = {"health":50, "name": "Joe", "age": 53, "location": "Oregon"}
            filename = input("Save as: ")

            save(example_dict, filename)
            choice = 0
        
        if int(choice) == 2:

            filename = input("Which file would you like to load?\n")
            load(filename)


    
if __name__ == "__main__":
    main()