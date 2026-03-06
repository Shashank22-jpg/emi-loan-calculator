from flask import Flask, render_template, request
import math

app = Flask(__name__)

def calculate_emi(principal, rate, time):
    rate = rate / (12 * 100)
    time = time * 12

    emi = (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
    return round(emi,2)

@app.route('/', methods=['GET','POST'])
def index():

    emi = None
    total_payment = None
    total_interest = None

    if request.method == "POST":

        principal = float(request.form['principal'])
        rate = float(request.form['rate'])
        time = float(request.form['time'])

        emi = calculate_emi(principal, rate, time)

        total_payment = emi * time * 12
        total_interest = total_payment - principal

    return render_template("index.html",
                           emi=emi,
                           total_payment=total_payment,
                           total_interest=total_interest)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)