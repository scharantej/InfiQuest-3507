
# main.py
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'secretkey'

levels = [
  {
    'id': 1,
    'name': 'Level 1',
    'description': 'This is the first level of the game.',
    'map': [
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
    ],
    'player_position': (0, 0),
    'goal_position': (4, 4),
  },
  {
    'id': 2,
    'name': 'Level 2',
    'description': 'This is the second level of the game.',
    'map': [
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0],
    ],
    'player_position': (0, 0),
    'goal_position': (4, 4),
  },
]

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/level-select')
def level_select():
  return render_template('level_select.html', levels=levels)

@app.route('/play', methods=['POST'])
def play():
  level_id = request.form['level_id']
  level = [level for level in levels if level['id'] == int(level_id)][0]
  session['level'] = level
  return redirect(url_for('play_level', level_id=level_id))

@app.route('/play-level/<level_id>')
def play_level(level_id):
  level = [level for level in levels if level['id'] == int(level_id)][0]
  return render_template('play_level.html', level=level)

@app.route('/game-over')
def game_over():
  return render_template('game_over.html')

@app.route('/victory')
def victory():
  return render_template('victory.html')

if __name__ == '__main__':
  app.run(debug=True)
