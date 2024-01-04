const express = require('express');
const app = express();
const path = require('path');

let dir = path.join(__dirname, '../../../javascript/button');
let url = path.resolve(__dirname, '../../../javascript/button/button.html');

app.use(express.static(dir));

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Application start and listening on port ${PORT}`);
});

app.get('/main', (req, res) => {
    res.sendFile(url)
});

app.get('/test', (req, res) => {
    res.setHeader('Content-Type', 'text/html')
    res.send('<h1>Hello World</h1>');
});

//404 page

// app.get('*', function (req, res) {
//     //res.status(404).send('Please mercy us, don\'t attack');
//     res.status(404).send('<center><img src="/img/404.jpg" height="100%"></center>');
// });

app.get('*', (req, res) => {
    res.redirect('/main');
});

