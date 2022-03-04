<h1>OTHELLO</h1>

### Table of Contents
- [Game Rules and Instructions](#game-rules-and-Instructions)
- [Project Descicption](#project-description)
- [How to Run](#how-to-run)
- [heuristics](#heuristic)
- [Genetic Algorithm](#Genetic-Algorithm)
### Game rules and Instructions
<a href="https://www.mastersofgames.com/rules/reversi-othello-rules.htm#:~:text=Each%20piece%20played%20must%20be,to%20match%20the%20player's%20colour.">Rules</a>
### Project Description
This program is an implementation of OTHELLO game with python (Pygame) . </br>
It can be played in Both single-player and Multiplayer mode.
</br>
The heart of the AI is an alpha-beta algorithm. you can change Depth in the main function. </br>Additionally, the Min-Max algorithm is implemented and can be used instead of alpha-beta.
### How to Run
At first, it's needed to install pygame library and MachineGunk-nyqg.ttf font as prerequisites. Then, run main.py and enjoy the game.

### Heuristics
The value of a node was approximated by our linear value function based
on board features:
1. Corner Disks: number of pieces Which have corner point.
2. Mobility: number of available moves.
3. Piece Difference: proportion of the pieces on the board that are yours.
4. Value Matrix: score based on relative value of positions taken.
### Project Link
- [reversi](https://github.com/smrh1379/reversi)
