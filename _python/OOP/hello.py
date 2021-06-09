from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'
# import statements, maybe some other routes
    
@app.route('/dojo')
def dojo():
  return "dojo"
      
@app.route('/say/<name>')
def say(name):
  return "Hi " + name

@app.route('/repeat/<int:num>/<word>')
def repeat(num , word):
    str = ""
    for i in range (int(num)):
        str = str + word
    return(str)



# app.run(debug=True) should be the very last statement! 
  # Return the string 'Hello World!' as a response
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.