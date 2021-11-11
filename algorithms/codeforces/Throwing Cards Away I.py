while True:
    n = int(input())
    if n == 0:
        break

    discarded_cards = []
    remaining_card = [i for i in range(1, n + 1)]

    while len(remaining_card) != 1:
        discarded_cards.append(remaining_card[0])
        remaining_card = remaining_card[1:]
        remaining_card.append(remaining_card[0])
        remaining_card = remaining_card[1:]

    if discarded_cards:
        print("Discarded cards:", ', '.join(map(str, discarded_cards)))
    else:
        print("Discarded cards:")
    print("Remaining card:", remaining_card[0])