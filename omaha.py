from itertools import product


class Card:
    def __init__(self, value, color):
        # values:
        # 2-2
        # 3-3
        # 4-4
        # 5-5
        # 6-6
        # 7-7
        # 8-8
        # 9-9
        # T-10
        # J-11
        # Q-12
        # K-13
        # A-14

        # colors:
        # spade
        # club
        # diamond
        # heart 
        if value in range(2,15):
            
            if color in ["spade","club","diamond","heart"]:
                self.value = value
                self.color = color
            else:
                raise ValueError("Enter valid card color (spade / club / diamond / heart)")
        else:
            raise ValueError("Enter valid card value")
    
    def __str__(self):
        return str(self.value) + self.color

class Hand:
    def __init__(self, card1, card2, card3, card4):
        self.cards = [card1, card2, card3, card4]
    
    def __str__(self):
        cardString =""
        for card in self.cards:
            cardString.join(str(card))
        print(cardString)

c1 = Card(4,"spade")
c2 = Card(5,"spade")
c3 = Card(6,"spade")
c4 = Card(4,"club")
cards =[c1, c2, c3, c4]
cardString =""
for card in cards:
    cardString = cardString.join(str(card))
    print(cardString)
print(cardString)


