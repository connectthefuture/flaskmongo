var express = require('express');
var router = express.Router();

var mongoose = require('mongoose');
mongoose.connect('mongodb://127.0.0.1:27017/gridfs_file7', function(err) {
    if(err) {
        console.log('connection error', err);
    } else {
        console.log('connection successful');
    }
});

/* GET home page. */
router.get('/', function(req, res) {
  var results = db.gridfs_file7.fs.files.find().skip(0).limit(6)
  res.render('index', { title: 'Mongo Node' });
});

module.exports = router;
