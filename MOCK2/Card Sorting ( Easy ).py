import json

class Player:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards
        self.score = 0

    def sort_cards(self):
        suit_order = {'S': 0, 'H': 1, 'D': 2, 'C': 3}
        rank_order = {'K': 0, 'Q': 1, 'J': 2, '10': 3, '9': 4, '8': 5, '7': 6,
                      '6': 7, '5': 8, '4': 9, '3': 10, '2': 11, 'A': 12, '1': 12}

        def compare(card1, card2):
            rank1, suit1 = card1[:-1], card1[-1]
            rank2, suit2 = card2[:-1], card2[-1]

            rank1_order = rank_order.get(rank1, 13)
            rank2_order = rank_order.get(rank2, 13)

            if suit_order[suit1] != suit_order[suit2]:
                return suit_order[suit1] - suit_order[suit2]
            return rank1_order - rank2_order

        n = len(self.cards)
        for i in range(n):
            for j in range(0, n - i - 1):
                if compare(self.cards[j], self.cards[j + 1]) > 0:
                    self.cards[j], self.cards[j + 1] = self.cards[j + 1], self.cards[j]

    def calculate_score(self):
        self.score = 0
        for card in self.cards:
            rank, suit = card[:-1], card[-1]
            if card == "2C" or card == "QS":
                self.score += 50
            elif rank == "A":
                self.score += 15
            elif rank in ["10", "J", "Q", "K"]:
                self.score += 10
            elif rank in ["2", "3", "4", "5", "6", "7", "8", "9", "1"]:
                self.score += 5

    def show_info(self):
        self.sort_cards()
        self.calculate_score()
        print(f"{self.name} -> {self.score} -> {self.cards}")

def sort_players(players):
    n = len(players)
    for i in range(n):
        for j in range(0, n - i - 1):
            if players[j].score < players[j + 1].score:
                players[j], players[j + 1] = players[j + 1], players[j]
    return players

n = int(input())
m = int(input())
players = []

for _ in range(n):
    data = json.loads(input())
    players.append(Player(data[0], data[1]))

for player in players:
    player.calculate_score()

players = sort_players(players)

for player in players:
    player.show_info()