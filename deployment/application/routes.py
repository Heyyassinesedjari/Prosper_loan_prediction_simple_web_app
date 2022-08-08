from application import app
from flask import render_template, url_for, redirect, request
from application.form import StockForm
from application.model import model, scaler

inputs = {}

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home_page():
    return render_template("home.html")

@app.route('/predict', methods=['GET', 'POST'])
def predict_page():
    form=StockForm(company='TWTR')
    if request.method == "POST":
        global inputs
        inputs["LoanCurrentDaysDelinquent"] = form.LoanCurrentDaysDelinquent.data
        inputs["LP_GrossPrincipalLoss"] = form.LP_GrossPrincipalLoss.data
        inputs["LoanFirstDefaultedCycleNumber"] = form.LoanFirstDefaultedCycleNumber.data
        inputs["LoanMonthsSinceOrigination"] =form.LoanMonthsSinceOrigination.data
        inputs["LP_CollectionFees"] = form.LP_CollectionFees.data
        inputs["EstimatedLoss"] = form.EstimatedLoss.data
        inputs["EstimatedReturn"] = form.EstimatedReturn.data
        inputs["LP_CustomerPayments"] = form.LP_CustomerPayments.data
        inputs["EstimatedEffectiveYield"] = form.EstimatedEffectiveYield.data
        inputs["EmploymentStatus"] = form.EmploymentStatus.data
        return redirect(url_for('result_page'))

    return render_template("predict.html", form=form)


@app.route('/result', methods=['GET', 'POST'])
def result_page():
    global inputs
    vector = [[]]
    EmploymentStatus_with_High_percentage_of_successful_borrowers = ['Self-employed', 'Employed', 'Other', 'Part-time']
    for col in inputs.keys():
        if col == "EmploymentStatus":
            if inputs[col] in EmploymentStatus_with_High_percentage_of_successful_borrowers:
                vector[0].append(1)
            else:
                vector[0].append(0)
        else:
            vector[0].append(inputs[col])
    scaled_vector = scaler.transform(vector)
    prediction = model.predict(scaled_vector)
    return render_template("result.html",prediction=prediction[0])