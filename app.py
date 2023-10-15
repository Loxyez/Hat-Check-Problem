from flask import Flask, render_template, request

app = Flask(__name__)

# variable that must be natural number
def derangements(n: int, memo={0:1, 1: 0, 2: 1}):

    # Incase of n = 1 or n = 2 it just an n - 1
    if n in memo:
        return memo[n]
    
    # recursive the recurrence relation
    # return the result of !(n-1) * d(n - 1) + d(n - 2)
    return (n - 1) * (derangements(n - 1) + derangements(n - 2))

MAX_LIMIT = 30

@app.route('/', methods=['GET', 'POST'])

def index():
    result = None
    if request.method == 'POST':
        try:

            n = int(request.form.get('n'))

            if n > MAX_LIMIT:
                result = "infinity"
            elif n < 0:
                result = "Number must be > 0"
            else:
                result = derangements(n)
        except ValueError:
            result = "Invalid input. Please enter a positive integer."

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)