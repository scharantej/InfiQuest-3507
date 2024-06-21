### Flask Application Design

#### HTML Files

- `index.html`: The main page of the game. Responsible for displaying the game environment and player actions.
- `level_select.html`: Presents a list of available levels for the player to choose from.
- `game_over.html`: Shown when the player loses the game. Displays the player's score and offers the option to restart.
- `victory.html`: Similar to `game_over.html`, but displayed when the player wins a level.

#### Routes

- `/`: Renders the `index.html` page, starting the game.
- `/level-select`: Renders the `level_select.html` page, allowing the player to select a level.
- `/play`: Handles player moves and updates the game state.
- `/game-over`: Renders the `game_over.html` page, displaying the player's score.
- `/victory`: Renders the `victory.html` page, indicating the level completion.