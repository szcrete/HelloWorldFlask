from flask import Flask
app = Flask(__name__)


urls = (
    '/users', 'list_users',
    '/users/(.*)', 'get_user'
)



app = web.application(urls, globals())

class list_users:        
    def GET(self):
      output = 'users:[child]';
      return output

if __name__ == "__main__":
    app.run()




#@app.route('/')
#def hello_world():
#  return 'Hey its Python Flask application! Bonjour Justin!'

#if __name__ == '__main__':
#  app.run()
