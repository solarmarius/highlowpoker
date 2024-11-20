# High-low poker

Deck is consisting of 48 cards:
- 40 number cards, 4 for each 0-9
- 8 operations cards, 4 for root, 4 for multiplication

Before: every Player has a set consisting of:
- Addition card
- Subtraction card
- Division card

Forced betting: eks (1) chip per game FOR EACH Player

A Game is consistent of:

Round 1:
1. Pass out one number card FOR EACH Player
    - Card is hidden from other players
2. Pass out 2 cards from Deck FOR EACH Player
    - IF Card == root: get one additional Number card
    - IF Card == multi: throw away Addition, Subtraction or Multiplication card
    and receive an Number card

Round 2, first betting:

Action - Description
Pass - ONLY for first player. Do not bet anything
Fold - Throw away card and exit the Game
Raise - Bet more than what is the highest amount on the table
Call - Bet as much as the highest amount on the table

The betting Round lasts until everyone has bet alike Chips
A Player cannot bet more than the lowest amount to a given Player!

At the end of round 2 - every Player receives a Number card

Round 3, create equation:

60 secounds to arrange the Cards to an Equation
which is either close to 1 or 20. 

Each Player selects a 1 / 20 Card

Round 4, second betting:

Alike as round 2, except no giving out Number cards.

Round 5, showoff:

Each player shows their equation and betting 1/20
- IF every Player bets the same 1/20: winner takes all
- IF both 1/20 are in play: split pot in two, give to winner
    - If Pot == not even, throw away 1 Chip
- If 2 or more Players win - divide the Pot equally to the Winners. 

## State representation in High-low Poker

Key - Description - Example Value
deck - 48 cards (40 Number and 8 Operational). - 000011119999RRRRMMMM
hand - The current hand of current player - 184ASDM
chip1 - Chips of player 1 - 14
chip2 - Chips of player 2 - 32
bet - The bet of the current hand - 0 (low) or 1 (high)