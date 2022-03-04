<h1>OTHELLO</h1>

### Table of Contents
- [Game Rules and Instructions](#game-rules-and-Instructions)
- [Project Descicption](#project-description)
- [How to Run](#how-to-run)
- [heuristics](#heuristic)
- [Genetic Algorithm](#Genetic-Algorithm)
### Game rules and Instructions <a href="https://www.ultraboardgames.com/othello/game-rules.php">Rules</a>
![image](https://user-images.githubusercontent.com/75033638/156724182-bf117e3a-e422-4795-99ba-fa5c6fa7336c.png)</br>
The board will start with 2 black discs and 2 white discs at the centre of the board.</br>
They are arranged with black forming a North-East to South-West direction.</br>
White is forming a North-West to South-East direction.</br>
Each player gets 32 discs and black always starts the game.</br>
Then the game alternates between white and black until:</br>

one player can not make a valid move to outflank the opponent.</br>
both players have no valid moves.
When a player has no valid moves, he pass his turn and the opponent continues.</br>

A player can not voluntarily forfeit his turn.</br>

When both players can not make a valid move the gane ends.
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
### Genetic Algorithm
Genetic Algorithm and machine learning was used to make Heuristic parameters better.
In the begining
### Project Link
- [reversi](https://github.com/smrh1379/reversi)

