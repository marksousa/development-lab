// economic version 
// require("http").createServer((inRequest, inResponse) => {
//     inResponse.end("Hello from my first Node Web server");
// }).listen(8080);


// didatic version
// http is a imported module
let http = require("http")

// This method creates a web server instance and returns a reference to it.
// You need to complement with the method listen()
http.createServer((request, response) => {
    // #1
    //response.write("Hello? Is there anybody in there?! Just nod if you can hear me.")
    //response.end()
    // or #2 short
    response.end("Hello? Is there anybody in there?! Just nod if you can hear me. Is there anyone at home?")
}).listen(8080); // webserver listen on port 8080 