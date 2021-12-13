from flask import Flask, render_template, request, json
from game_of_life import GameOfLife

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        width = request.form.get('width')
        height = request.form.get('height')
        GameOfLife(int(width), int(height))
    return render_template('index.html')


@app.route("/live")
def live():
    game = GameOfLife()
    if game.counter > 0:
        game.form_new_generation()
    game.counter += 1
    return render_template('live.html', game=game)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
