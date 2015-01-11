var express = require('express');
var router = express.Router();

/* GET images home listing page. */
router.get('/images', function(req, res) {
  res.send('respond with a resource');
  //res.render('index', { title: 'Images' });
});



module.exports = router;
