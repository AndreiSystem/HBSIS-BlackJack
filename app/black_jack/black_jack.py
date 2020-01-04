from app.black_jack.cards.cards import A, Q, J, K, Um, Dois, Tres, Quatro, Cinco, Seis, Sete, Oito, Nove, Dez
from app.black_jack.deck.deck import Deck


class BlackJack:
    def __init__(self):
        self._cards = [
            A(),
            Q(),
            J(),
            K(),
            Um(),
            Dois(),
            Tres(),
            Quatro(),
            Cinco(),
            Seis(),
            Sete(),
            Oito(),
            Nove(),
            Dez()
        ]
        self._pt = 0
        self._deck = Deck(self._cards)
        self._saved_cards = []

    def start(self):
        self._deck.shuffle()

        while self.goal_reached():
            input('---Aperte [ENTER] para virar uma carta---')

            tapped_card = self._deck.put_card()
            self._saved_cards.append(tapped_card)

            print(f'carta virada ==> [{tapped_card}]')

            self.calculate()

        self.finish_game()


    def finish_game(self):
        print(f'Pontuação final: {self._pt}')

    def calculate(self):
        self._pt = sum(map(lambda card: card.get_value(), self._saved_cards))

    def goal_reached(self):
        if self._pt >21:
            return False
        return True
