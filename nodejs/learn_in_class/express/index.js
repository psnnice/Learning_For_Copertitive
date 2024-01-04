const express = require('express');
const app = express();

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Application start and listening on port ${PORT}`);
});

app.get('/', (req, res) => {
    res.setHeader('Content-Type', 'text/html');
    res.send('<h1>Hello World</h1>');
});

