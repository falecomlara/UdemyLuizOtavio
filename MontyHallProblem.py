"""author: `Bernardo Costa <bernardoantunescosta at gmail.com>`"""
# https://medium.com/@bernardo.costa/o-modo-pythonic-de-ver-o-problema-de-monty-hall-60d50f120732

import random


class MontyHall:
    """Monty Hall Simulator Class."""

    def __init__(self):
        self.doors = list('123')
        self.reward_door = None
        self.guess = None
        self.goat_door = None
        self.load_reward()

    def load_reward(self):
        self.reward_door = self._random_choice(self.doors)

    def set_random_guess(self, guess=1):
        self.guess = self._random_choice(self.doors)

    def set_guess(self):
        self.guess = guess

    def open_goat_door(self):
        self.goat_door = self._random_choice([x for x in self.doors if x != self.guess and x != self.reward_door])

    def switch_door(self):
        self.guess = [x for x in self.doors if x != self.guess and x != self.goat_door][0]

    def validade_guess_door(self):
        return self.guess == self.reward_door

    @staticmethod
    def _random_choice(seq):
        return random.choice(seq)

acumulator = [0, 0]

for _ in range(10**6):
  mh = MontyHall()
  mh.set_random_guess()
  mh.open_goat_door()
  mh.switch_door()  # comment to don't swich
  result = mh.validade_guess_door()
  if result: acumulator[0] += 1
  acumulator[1] += 1
  if acumulator[1] % 10000 == 0:
    print(acumulator[1])

print(f'{acumulator} Win probability: {(acumulator[0]/acumulator[1])*100}%')