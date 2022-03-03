<h1>Reversi</h1>

### Table of Contents
- [Project Descicption](#project-description)
- [How to Run](#how-to-run)
- [heuristics](#heuristic)
- [Genetic Algorithm](#Genetic-Algorithm)

### Project Descicption
This program is an implementation of Reversi (OTHELLO) game with python.
</br>
The heart of the AI is an alpha-beta algorithm. you can change Depth in the main function. </br>Additionally, the Min-Max algorithm is implemented and can be used instead of alpha-beta.
### How to Run
At first, it's needed to install pygame library and MachineGunk-nyqg.ttf font as prerequisites. Then, run the main.py code and enjoy the game.

### Heuristics
The value of a node was approximated by our linear value function based
on board features:
1. Corner Disks: number of pieces Which have corner point.
2. Mobility: number of available moves.
3. Piece Difference: proportion of the pieces on the board that are yours.
4. Value Matrix: score based on relative value of positions taken.
### Project Link
- [reversi](https://github.com/smrh1379/reversi)
