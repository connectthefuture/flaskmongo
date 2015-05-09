//

db.inventory.aggregate(
   [
      {
         "$project":
           {
             "item": 1,
             "discount":
               {
                 "$cond": { "if": { "$gte": [ "$qty", 250 ] }, "then": 30, "else": 20 }
               }
           }
      }
   ]
);



db.inventory.aggregate(
   [
     {
       "$project":
          {
            "item": 1,
            "yearSubstring": { "$substr": [ "$quarter", 0, 2 ] },
            "quarterSubtring": { "$substr": [ "$quarter", 2, -1 ] }
          }
      }
   ]
);


db.inventory.aggregate(
          [
            { "$project": 
                { "itemDescription": 
                    { "$concat": [ "$item", " - ", "$description" ] } 
                }     
            }
          ]
);


db.survey.find(
        { "results": { 
            "$elemMatch": { 
                "product": "xyz", 
                "score": { "$gte": 8 } 
                } 
            } 
        }
);



db.survey.find(
            { "results": { 
                "$elemMatch": { 
                    "product": "xyz", 
                    "score": { "$gte": 8 } 
                    } 
                } 
            }
);



db.books.aggregate( 
                    [
                      { "$group": { 
                          "_id" : "$author", 
                          "books": {"$push": "$title" } 
                          } 
                      },
                      { "$out": "authors" }
                    ]
                );
               
               
db.products.find( { "sku":  { "$regex": /^ABC/i } });
              
              
              
//
//
//'''
//So what does this mean to you? Basically you can completely ignore that this is the case unless you are doing something like unit testing. You will notice that code which depends on a request object will suddenly break because there is no request object. The solution is creating a request object yourself and binding it to the context. The easiest solution for unit testing is to use the test_request_context() context manager. In combination with the with statement it will bind a test request so that you can interact with it. Here is an example:
//'''
//from flask import request
//
//with app.test_request_context('/hello', method='POST'):
//    # now you can do something with the request until the
//    # end of the with block, such as basic assertions:
//    assert request.path == '/hello'
//    assert request.method == 'POST'
//    # The other possibility is passing a whole WSGI environment to the request_context() method:
//
//from flask import request
//
//with app.request_context(environ):
//    assert request.method == 'POST'
//'''
//The Request Object
//The request object is documented in the API section and we will not cover it here in detail (see request). Here is a broad overview of some of the most common operations. First of all you have to import it from the flask module:
//'''
//from flask import request
//'''The current request method is available by using the method attribute. To access form data (data transmitted in a POST or PUT request) you can use the form attribute. Here is a full example of the two attributes mentioned above:
//'''
//@app.route('/login', methods=['POST', 'GET'])
//def login():
//    error = None
//    if request.method == 'POST':
//        if valid_login(request.form['username'],
//                       request.form['password']):
//            return log_the_user_in(request.form['username'])
//        else:
//            error = 'Invalid username/password'
//    # the code below is executed if the request method
//    # was GET or the credentials were invalid
//    return render_template('login.html', error=error)
//'''
//What happens if the key does not exist in the form attribute? In that case a special KeyError is raised. You can catch it like a standard KeyError but if you don’t do that, a HTTP 400 Bad Request error page is shown instead. So for many situations you don’t have to deal with that problem.
//
//To access parameters submitted in the URL (?key=value) you can use the args attribute:
//'''
//searchword = request.args.get('key', '')
//
//'''
//We recommend accessing URL parameters with get or by catching the KeyError because users might change the URL and presenting them a 400 bad request page in that case is not user friendly.
//
//For a full list of methods and attributes of the request object, head over to the request documentation.
//
//File Uploads
//You can handle uploaded files with Flask easily. Just make sure not to forget to set the enctype="multipart/form-data" attribute on your HTML form, otherwise the browser will not transmit your files at all.
//
//Uploaded files are stored in memory or at a temporary location on the filesystem. You can access those files by looking at the files attribute on the request object. Each uploaded file is stored in that dictionary. It behaves just like a standard Python file object, but it also has a save() method that allows you to store that file on the filesystem of the server. Here is a simple example showing how that works:
//'''
//from flask import request
//
//@app.route('/upload', methods=['GET', 'POST'])
//def upload_file():
//    if request.method == 'POST':
//        f = request.files['the_file']
//        f.save('/var/www/uploads/uploaded_file.txt')
//'''  ...
//If you want to know how the file was named on the client before it was uploaded to your application, you can access the filename attribute. However please keep in mind that this value can be forged so never ever trust that value. If you want to use the filename of the client to store the file on the server, pass it through the secure_filename() function that Werkzeug provides for you:
//'''
//from flask import request
//from werkzeug import secure_filename
//
//@app.route('/upload', methods=['GET', 'POST'])
//def upload_file():
//    if request.method == 'POST':
//        f = request.files['the_file']
//        f.save('/var/www/uploads/' + secure_filename(f.filename))
