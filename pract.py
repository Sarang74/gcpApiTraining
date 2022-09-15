from flask import Flask
app = Flask(__name__)
@app.route('/') 

def sara():
    name = 'My name is Sarang'
    return name

if __name__ == "__main__":
    app.run(debug =True)
