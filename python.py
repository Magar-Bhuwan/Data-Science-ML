def blackjack_hand_greater_than(hand_1, hand_2):
    def hand_value(hand):
        value = 0
        aces = 0
        
        for card in hand:
            if card in ['J', 'Q', 'K']:
                value += 10
            elif card == 'A':
                aces += 1
            else:
                value += int(card)
        
        # Add aces as 11 where possible, otherwise 1
        for _ in range(aces):
            if value + 11 <= 21:
                value += 11
            else:
                value += 1
        
        return value

    h1 = hand_value(hand_1)
    h2 = hand_value(hand_2)

    return h1 <= 21 and (h1 > h2 or h2 > 21)

help(range)