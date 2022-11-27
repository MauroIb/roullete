from player import Player
from roulette import Roulette


class Casino:
    """
    Class that models a casino, with a list of player and at least one game
    """
    def __init__(self) -> None:
        """Initiate a casino with a roulette
        """
        self.players = []
        self.game = Roulette()

    def __add_new_player(self,bet_type: str) -> None:
        """Adds new player to the list with a known bet type

        Args:
            bet_type (str): string matching a valid bet type for the player
        """
        self.players.append(Player(bet_type))
    
    def run_casino(self, rounds : int) -> None:
        """Main function to run the casino for n rounds

        Args:
            rounds (int): Rounds being simulated
        """

        # Players join the table with known bet types
        bet_types = self.game.get_valid_bets()
        for bet_type in bet_types:
            self.__add_new_player(bet_type)

        # Casino runs
        for n in range(rounds):

            # Players place a bet
            for n in range(len(self.players)):
                self.players[n].place_bet()
            
            # Game rolls a number
            self.game.roll()

            # Payout
            for n in range(len(self.players)):
                result = self.game.settle_bet(
                        bet_type= self.players[n].bet_type,
                        bet_value= self.players[n].bet_amount)
                self.players[n].recieve_result(result)
        
        # Report results
        for player in self.players:
            print(player)

    