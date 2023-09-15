How to use my crud API

Creating New user with POST request is done by sending a POST request

POST request to 'https://hngx-omarko-1.onrender.com/api/' with the username passed in the body as json {"name": "mark"} 
  => returns {"name": "mark", "userid": "20e3aa9d1c284de1bc9a8bed23b45b6f"}


RETRIEVING ALL users is done by sending a GET request:

GET request to 'https://hngx-omarko-1.onrender.com/api/' 
  => returns [{"name": "mark", "userid": "20e3aa9d1c284de1bc9a8bed23b45b6f"}]
    a list of all users



Retrieving a particular user based on userid is done by sending a GET request:

GET request to 'https://hngx-omarko-1.onrender.com/api/20e3aa9d1c284de1bc9a8bed23b45b6f 
  => return {"name": "mark", "userid": "20e3aa9d1c284de1bc9a8bed23b45b6f"}



Updating a user based on the userid is done by sending a PUT request

PUT request to 'https://hngx-omarko-1.onrender.com/api/20e3aa9d1c284de1bc9a8bed23b45b6f' with data passed in body as json {"name": sam"} 
  => return {"name": "sam", "userid": "20e3aa9d1c284de1bc9a8bed23b45b6f"}



Deleting a user based on the userid is done by sending a DELETE request:

DELETE request to 'https://hngx-omarko-1.onrender.com/api/20e3aa9d1c284de1bc9a8bed23b45b6f' 
  => return {"message": "User deleted successfully"}


GET request to 'https://hngx-omarko-1.onrender.com/api/20e3aa9d1c284de1bc9a8bed23b45b6f' 
  => return {"error": "data not found"}


GET request to 'https://hngx-omarko-1.onrender.com/api/' 
  => return []



NOTE: The userid used here is a sample of the userid generated when a new user is created
