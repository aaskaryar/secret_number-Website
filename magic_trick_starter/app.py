from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    secret_num = int(request.form['secret_num'])
    orginal_num = secret_num
    # Increase secret_num by 1
    secret_num += 1

    # Next, take the new number and double it
    secret_num *= 2

    # Next, take the new number and add four to it
    secret_num += 4

    # Next, take the new number and divide by two
    secret_num /= 2

    # Next, take the new number and subtract your original secret number from it
    secret_num -= orginal_num

    return render_template('result.html', secret_num=secret_num)

if __name__ == '__main__':
    app.run()
