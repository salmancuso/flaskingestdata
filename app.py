from flask import Flask, render_template, url_for, request

app = Flask(__name__, template_folder='./templates')

@app.route('/')
def index():
  return render_template('pid2process.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   print(request.method)
   if request.method == 'POST':
      result = request.form
      return render_template("results.html",result = result)

if __name__ == "__main__":
    app.run(debug=True, port=1972, host='0.0.0.0')