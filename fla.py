# from flask import Flask     
# app = Flask(__name__) 
  
# @app.route('/')       
# def hello(): 
#     return 'HELLO'
  
# if __name__=='__main__': 
#    app.run(debug=True)


# from flask import Flask 
# app = Flask(__name__) 

# @app.route('/hello/<name>') 
# def hello_name(name): 
#     return 'Hello  GeeksforGeeks%s!' % name 

# if __name__ == '__main__': 
#     app.run(debug = True)

# from flask import Flask 

# app = Flask(__name__) 

# @app.route('/blog/<int:postID>')
# def show_blog(postID): 
#     return 'Blog Number %d' % postID  

# @app.route('/rev/<float:revNo>')
# def revision(revNo): 
#     return 'Revision Number %f' % revNo  

# if __name__ == '__main__': 
#     app.run(debug=True)

# from flask import Flask, redirect, url_for
# app = Flask(__name__)


# @app.route('/admin') 
# def hello_admin(): 
#     return 'Hello Admin'


# @app.route('/guest/<guest>')
# def hello_guest(guest):  
#     return 'Hello %s as Guest' % guest


# @app.route('/user/<name>')
# def hello_user(name):
#     if name == 'admin':  
#         return redirect(url_for('hello_admin'))
#     else:
#         return redirect(url_for('hello_guest', guest=name))


# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask,render_template
an=Flask(__name__)
@an.route('/')


def home():
    return render_template('abc.html')

if __name__=="__main__":
    an.run(debug=True)
