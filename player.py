from collections import deque

class Player():

    def __init__(self, bet_type : str) -> None:
        """Initiates player obj with a set bet type

        Args:
            bet_type (str): _description_
        """
        self.__reset_bet_list()
        self.bet_type = bet_type
        self.bet_amount = 0
        self.balance = 0

    def __repr__(self) -> str:
        return f'{self.bet_type= }\t{self.balance= }\t{self.bet_amount= }\t {self.bet_list= }\t'
    
    def __calculate_bet_amount_logic(self) -> None:
        """Logic for calculating how much the player will bet next round
        """
        self.bet_amount = self.bet_list[0] + self.bet_list[-1]

    def __reset_bet_list(self) -> None:
        """Resets the bet list to it's defualt parameters
        """
        self.bet_list = deque([1,2,3,4])
    
    def place_bet(self) -> None:
        """Main function for placing a bet. 
        It relies on a list of past bets and has a threshhold before reseting it. 
        """
        THRESHHOLD = 4000
        self.__calculate_bet_amount_logic()
        if self.bet_amount > THRESHHOLD:
            # If betting too much, reset list
            self.__reset_bet_list()
            self.__calculate_bet_amount_logic()
        self.balance -= self.bet_amount
    
    def recieve_result(self, result : int) -> None:
        """
        The player learns if they won or not.
        Changes balance and bet_list accordingly.
        
        Args:
            result (bool): Value describing a win
        """
        if result:
            # Append last bet to list, add earnings to balance
            self.bet_list.append(self.bet_amount)
            self.balance += result
        else:
            # Remove first and last elements if possible
            if len(self.bet_list) < 3:
                self.__reset_bet_list()
            else:
                self.bet_list.pop()
                self.bet_list.popleft()