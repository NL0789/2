# Fibo 2584 the game

This game is a variation of the game '<a href="https://en.wikipedia.org/wiki/Threes">threes</a>' or '<a href="https://en.wikipedia.org/wiki/2048_(video_game)">2048</a>', which were created in 2014.

In this variation, you run through 19 (or 17 depending on how you count ones and zeros) numbers in the <a href="https://en.wikipedia.org/wiki/Fibonacci_number">Fibonacci sequence</a> (<a href="https://oeis.org/A000045">OEIS 000045</a>).

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, ...

## Rules

The rules for combining numbers are different, though. You can combine any pair of consequtive Fibonacci numbers to create the next one in the sequence. 

```
1+1 = 2
1+2 = 3
2+3 = 5
3+5 = 8
5+8 = 13
   ...
```

There's one exception. Zero cannot be combined with one to create another one.

The game ends, when you reach 2584 or run out of legal moves. Reaching 2584 results in a 'win' and running out of moves results in a 'game over'.

## Scoring

You receive points for each combined pair of numbers. For example combingin 3 and 5 to 8, gives you 8 points. In addition you reveive 1 point for each tile that is added to the game.

The highscore list is 'two-tiered'. Winning the game is always superior to a game over, independent of the score. Games, that were not 'won' are ranked higher depending on the score. However, the games that are 'won' are ranked higher inversely based on their score. Therefore scoring low while winning the game is the highest ranked result.

```
Rank   Win?   Highest tile   Score  
----   ----   ------------   -----
001    Yes    2584           3789
002    Yes    2584           4569
003    Yes    2584           6653
004    No     1597           6234
005    No     1597           5432
006    No     987            5234
007    No     1597           4954
  ...
```

## Installation

For now, you will need to run the game with a Python interpreter installed. 

* Python ~3.7
* Pygame ~1.9.5

Run with `python fibo_2584.py`.