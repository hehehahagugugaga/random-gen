from flask import Flask, render_template, request
import random

web = Flask(__name__)

@web.route('/')
def hola():
    return render_template('index.html', result="")

@web.route('/s', methods=['POST'])
def second():
    l = int(request.form.get('ln'))
    u = int(request.form.get('un'))
    n = int(request.form.get('tn'))

    op = []
    while len(op) < n:
        j = random.randint(l, u)
        if j not in op:
            op.append(j)

    return render_template('index.html', result=", ".join(map(str, op)))


if __name__ == '__main__':
    web.run()
