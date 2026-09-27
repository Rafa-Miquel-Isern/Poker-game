# Poker game

# Mini Poker – Python Card Game

A text-based card game in Python where you play against the computer, built for
CSCE 160 (Intro to Programming). It mixes poker-style hand scoring with a
blackjack-style bust limit.

## How it works
- Place a bet from your $100 wallet, then you and the PC are each dealt two cards
- Draw extra cards (up to 5), but a dice roll sets a random point limit each round (21–24). Go over it and you bust
- Hands are scored by their highest card, with bonuses for holding an Ace or a flush (all cards of one suit)
- Suits break ties (♠ > ♥ > ♦ > ♣). Win the round and you double your bet
- The game ends when your wallet reaches $0

## Concepts
Python · OOP (Card, Deck, Player, Dice classes) · operator overloading (`__gt__`) · input validation · randomness
