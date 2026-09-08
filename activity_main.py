
VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

def blackjack_score(hand):
    score = 0
    
    if not isinstance(hand, list) or len(hand) < 2 or len(hand) > 5:
        return "Invalid"
    if any (card not in VALID_CARDS for card in hand):
        return "Invalid"
    for card in hand:
        if card in ['Jack', 'Queen', 'King']:
            score +=  10
        elif card == 'Ace':
            score += 11
        else:
            score += card
    
    while score > 21 and 'Ace' in hand:
        score -= 10
        
    if score > 21:
        return "Bust"
    return score    
        