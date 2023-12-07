with open('input.txt') as inp: 
    cards = inp.readlines()
    for i, card in enumerate(cards):
        fst, snd = card.split(' | ')
        winning_nums = [int(x) for x in fst.split(': ')[1].split()]
        my_nums = [int(x) for x in snd.split()]

        cards[i] = {'card_num':i+1, 'winning_nums':winning_nums, 'my_nums':my_nums}

card_wins = {}

total = 0
for i, card in enumerate(cards):
    winning_nums = card['winning_nums']
    my_nums = card['my_nums']
    my_winners = list(filter(lambda x : x in winning_nums, my_nums))

    card_wins[i+1] = []
    for j in range(len(my_winners)):
        card_wins[i+1].append(card['card_num']+j+1)


total = {card_num:1 for card_num in card_wins}
for card_num in card_wins:
    for new_card in card_wins[card_num]:
        total[new_card] += total[card_num]
    
print(sum(total.values()))