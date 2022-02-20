// npm install request --save // require("request")

let http = require("http")

http.createServer((request, response) => {
    const requestModule = require("request")
    requestModule(
        "http://worldtimeapi.org/api/timezone/America/Sao_Paulo",
        function (inErr, inResp, inBody){
            // response.end(
            //     `Hello, from my first Node Web Server: ${inBody} - ${inErr} - ${inResp}`
            // )
            response.end(inBody) // prettify on browser  
        }
    );
}).listen(8080);