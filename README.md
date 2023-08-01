# CS361-Communication-Contract
Amusement Park Help
In order to request data from the microservice implemented, the individual project program will send a string to the microservice using socket. 
The python file working as the client (individual project) will send a string to the python file working as the server or host (microservice). The two files
must communicate through the same port. The microservice will also need to be run before the individual project is run in order to connect properly.
The individual project will receive data from the microservice through the same port that data is requested from. After the individual project sends a string
as a request, the microservice will convert the string into a URL for a Wikipedia search. The microservice will send the URL through the port and 
it will be received by the individual project and presented to the user. For example, the microservice will have a host IP address, both programs will 
connect using the same host address and port. The individual project will send "Disneyland" through the port, the microservice will be listening and after
it receives the "Disneyland" request, it will convert it into a URL. The microservice will then send "https://en.wikipedia.org/wiki/Disneyland" through the 
port. The individual project will be listening and receive the proper URL. Then the URL will be given to the user in case they want to further investigate
the amusement park.
Below is a UML of the process:
![Sequence diagram](https://github.com/lkrosenbaum1/CS361-Individual-Milestone/assets/110206998/b1e4c3dc-4a99-4a67-ac35-d60887f86896)
