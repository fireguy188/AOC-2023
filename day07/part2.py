hands = {}
with open('input.txt') as inp: 
    for line in inp:
        hand, bid = line.split()
        hands[hand] = int(bid)

def greater_than(hand1, hand2):
    cards = 'J23456789TQKA'
    for c in range(5):
        if cards.index(hand1[c]) > cards.index(hand2[c]):
            return True
        if cards.index(hand1[c]) < cards.index(hand2[c]):
            return False

def sort_hands(hands):
    # minsort
    sorted_hands = []
    while hands:
        smallest = 0
        for h in range(len(hands)):
            if greater_than(hands[smallest], hands[h]):
                smallest = h
        sorted_hands.append(hands[smallest])
        del hands[smallest]
    
    return sorted_hands

primary_ranks = {x:[] for x in range(1, 8)}
for hand in hands:
    # go through every possible card for J
    best_rank = 0
    for new_card in '23456789TQKA':
        new_hand = hand.replace('J', new_card)

        count = {}
        for card in new_hand:
            if not card in count:
                count[card] = 0
            count[card] += 1
            
        if max(count.values()) == 5:
            # 5 of a kind
            best_rank = max(7, best_rank)
            continue

        if max(count.values()) == 4:
            # 4 of a kind
            best_rank = max(6, best_rank)
            continue

        if 2 in count.values() and 3 in count.values():
            # full house
            best_rank = max(5, best_rank)
            continue

        if max(count.values()) == 3:
            # 3 of a kind
            best_rank = max(4, best_rank)
            continue

        if list(count.values()).count(2) == 2:
            # 2 pair
            best_rank = max(3, best_rank)
            continue

        if 2 in count.values():
            # 1 pair
            best_rank = max(2, best_rank)
            continue

        # high card
        best_rank = max(1, best_rank)
    
    primary_ranks[best_rank].append(hand)

primary_ranks = {rank:sort_hands(primary_ranks[rank]) for rank in primary_ranks}
ultimate_ranking = []
for rank in primary_ranks:
    for hand in primary_ranks[rank]:
        ultimate_ranking.append(hand)

total = 0
for rank in range(len(ultimate_ranking)):
    total += (rank+1)*hands[ultimate_ranking[rank]]
print(total)