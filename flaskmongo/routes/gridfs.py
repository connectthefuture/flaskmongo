var express = require('express');
var router = express.Router();

var mongoose = require('mongoose');
var gridfs_file7 = require('../models/gridfs_file7.js');

/* GET /gridfs_file7 listing. */
router.get('/gridfs/', function(req, res, next) {
  gridfs_file7.find(function (err, gridfs_file7) {
    if (err) return next(err);
    res.json(gridfs_file7);
  });
});

//module.exports = router;


// /* GET images home listing page. */
// router.get('/images', function(req, res) {
//   res.send('respond with a resource');
//   //res.render('index', { title: 'Images' });
// });

// /* GET images from /gridfs/:id by id. */
router.get('/gridfs/:id', function (req, res, next) {
  gridfs_file7.findById(req.params.id, function(err, filename){
    if(err) res.send(err);
    res.json(filename);
  });
});

/* POST /gridfs */
router.post('/gridfs/', function(req, res, next) {
  gridfs_file7.create(req.body, function (err, post) {
    if (err) return next(err);
    res.json(post);
  });
});

/* PUT /gridfs/:id */
router.put('/gridfs/:id', function(req, res, next) {
  gridfs_file7.findByIdAndUpdate(req.params.id, req.body, function (err, post) {
    if (err) return next(err);
    res.json(post);
  });
});

/* DELETE /todos/:id */
router.delete('/gridfs/:id', function(req, res, next) {
  gridfs_file7.findByIdAndRemove(req.params.id, req.body, function (err, post) {
    if (err) return next(err);
    res.json(post);
  });
});


module.exports = router;
