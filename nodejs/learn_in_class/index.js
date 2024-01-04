const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;

// var url = require('url');

const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    //res.setHeader('content-type','application/json');
    //res.setHeader('content-type','application/pdf');
    //res.setHeader('content-type','text/plain');
    res.write('<h1>Hello programming Technology</h1>');
    // var params = url.parse(req.url, true).query;
    res.end('Hello World\n');
    //stop web
});

server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});