const express = require('express');
const mysql = require('mysql2');

const app = express();
const port = 3000;

// Create a MySQL connection pool
const pool = mysql.createPool({
    host: 'localhost',
    user: 'root',
    password: '',                 
    database: 'iot',  
    waitForConnections: true,
    connectionLimit: 10,
    queueLimit: 0
});

// Simple select query
app.get('/location', (req, res) => {
    pool.query('SELECT * FROM location', (error, results, fields) => {
        if (error) {
            console.error(error);
            res.status(500).send('Error retrieving data from the database');
        } else {
            res.json(results);
        }
        
    });
});

app.get('/location/json/:id', (req, res) => {
    var sql = 'SELECT * FROM location WHERE location_id = ' +req.params['id']
    pool.query(sql, (error, results, fields) => {
        if (error) {
            console.error(error);
            res.status(500).send('Error retrieving data from the database\n'+sql);
        } else {
            res.json(results);
            res.end();
        }
    });
});

const bodyParser = require('body-parser');
const path = require('path');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
// Simple select query


app.use(express.static(path.join(__dirname, 'public')));
app.get('/insert.html', (req, res) => {
    res.sendFile(__dirname + '/insert.html');
});


app.post('/locations', (req, res) => {
    console.log("asdasd")
    const { location_name } = req.body;
    
    // SQL Query to insert data into the location table
    const sql = `INSERT INTO location (location_name) VALUES (?)`;

    // Execute the query with the provided data
    pool.query(sql, [location_name], (err, result) => {
        if (err) {
            return res.status(500).json({ error: err.message });
        }
        //Return the ID of the inserted row
        res.json({ id: result.insertId });
    });
});


//Start the Express server
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});


// MySQL select table

