with open('input.txt') as inp: 
    cards = inp.readlines()

total = 0
for card in cards:
    fst, snd = card.split(' | ')
    winning_nums = [int(x) for x in fst.split(': ')[1].split()]
    my_nums = [int(x) for x in snd.split()]

    my_winners = list(filter(lambda x : x in winning_nums, my_nums))
    if len(my_winners) > 0:
        total += 2**(len(my_winners) - 1)

print(total)