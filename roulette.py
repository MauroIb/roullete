import random
from typing import Callable

BLACK = [2, 4, 6,8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
RED = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

class Roulette():

    def __init__(self) -> None:
        """Initiate a roulette object with default values"""
        self.rolled_number = None
        pass
    
    def roll(self) -> None:
        """Roll a new number
        """
        self.rolled_number  = random.randint(0, 36)
        print(f'{self.rolled_number=}')

    def bet_even(rolled_number) -> bool:
        return rolled_number % 2

    def bet_uneven(rolled_number) -> bool:
        return not (rolled_number % 2)

    def bet_black(rolled_number) -> bool:
        return rolled_number in BLACK
        
    def bet_red(rolled_number) -> bool:
        return rolled_number in RED
    
    def bet_high(rolled_number) -> bool:
        return rolled_number > 18
    
    def bet_low(rolled_number) -> bool:
        return (rolled_number > 18) and not 0

    # Dictionary of methods for each bet type. 
    bets = {
            'even' : bet_even,
            'uneven' : bet_uneven,
            'black' : bet_black,
            'red' : bet_red,
            'low' : bet_low,
            'red' : bet_high
            }
    
    def get_valid_bets(self) -> list : 
        """Returns a list of valid bet types

        Returns:
            list: list of strings
        """
        return self.bets.keys()

    def settle_bet(self, bet_type: str, bet_value : int) -> int:
        """Settle a bet for a player. Returns how much the player has won

        Args:
            bet_type (str): type of bet, matching a bets dictionary key
            bet_value (int): how much the player has bet

        Returns:
            int: amount the player has earned
        """
        bet = self.bets[bet_type]
        if bet(self.rolled_number):
            return bet_value * 2
        return 0
    
