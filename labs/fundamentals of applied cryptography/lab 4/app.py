from flask import (
    Flask, render_template, redirect, request, url_for
    )

from config import Configuration


app = Flask(__name__)
app.config.from_object(Configuration)


@app.route('/')
def index():
    return redirect(url_for('elgamal_page_encrypt'))


@app.route('/encrypt', methods=['POST', 'GET'])
def elgamal_page_encrypt():
    if request.method == 'GET':
        return render_template('elgamal_encrypt.html')
    else:
        result = request.form
        return redirect(url_for('result_page', result=result))


@app.route('/decrypt', methods=['POST', 'GET'])
def elgamal_page_decrypt():
    if request.method == 'GET':
        return render_template('elgamal_decrypt.html')
    else:
        result = request.form
        return redirect(url_for('result_page', result=result))


@app.route('/result')
def result_page(result):
    return render_template('result.html', result=result)


if __name__ == "__main__":
    app.run()
