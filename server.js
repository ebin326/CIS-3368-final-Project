const express = require('express'); // Serves our pages to a specified port
const app = express();
const cors = require('cors');
const axios = require('axios').create({baseURL: "http://127.0.0.1:5000"}); // Makes external API calls into our frontend server
const bodyParser  = require('body-parser');
const path = require('path');

app.use(bodyParser.urlencoded());
app.use(express.static('Frontend'));
app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(cors());

// Set the view engine to ejs & defines views directory
app.set('views', path.join(__dirname, 'views/'));
app.set('view engine', 'ejs');

const headers = {
    'content-type': 'application/json'
}

// Dashboard
app.get('/', function(req, res) {
    res.render('login.ejs', {
    });
});

// Dashboard
app.get('/dashboard', function(req, res) {
    res.render('dashboard.ejs', {
    });
});

app.listen(8000);
console.log('Front-End server running on port 8000!');