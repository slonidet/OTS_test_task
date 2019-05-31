import os

import pandas as pd
from flask import Flask, request, redirect, flash, render_template
from sklearn.linear_model import LinearRegression


app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')
train_file_path = os.environ.get('TRAIN_FILE')


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # check if submitted file is csv
        if len(file.filename.rsplit('.', 1)) <= 1:
            flash('Please upload .csv file')
            return redirect(request.url)
        elif file.filename.rsplit('.', 1)[1].lower() != 'csv':
            flash('Please upload .csv file')
            return redirect(request.url)
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            test_df = pd.read_csv(file.stream)
            prediction = model.predict(test_df[['x0', 'x3', 'x4', 'x5', 'x7']])
            test_df['y'] = prediction
            return render_template(
                'result.html',
                tables=[test_df.to_html(classes='data')],
                titles=test_df.columns.values
            )
    return render_template('index.html')


if __name__ == '__main__':
    df = pd.read_csv(train_file_path)
    X = df[['x0', 'x3', 'x4', 'x5', 'x7']]
    Y = df['y']
    model = LinearRegression().fit(X, Y)
    app.run()
