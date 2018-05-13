from flask import Flask, render_template, request
import generateChart

app=Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        try:
            return render_template("input.html")
        except Exception as e:
            return '''<h1>ERROR </h1>
                        
                        <p>%s</p>'''.format(e)
        
@app.route('/plot', methods=['GET', 'POST'])
def plot():
    if request.method == 'POST':
        try:
            plot(
            EqTicker=request.form['ticker'],
            start=request.form['startDate'],
            end=request.form['endDate'],
            request.form['quandlKey'])
        except Exception as e:
            return '''<h1>ERROR </h1>
                        
                        <p>%s</p>'''.format(e)

    return render_template("plot.html")
                           #,
                           #script1=script1,
                           #div1=div1,
                           #cdn_css=cdn_css,
                           #cdn_js=cdn_js,
                           #error=error)
    if request.method == 'GET':
        return render_template("input.html")

if __name__ == '__main__':
    app.run()