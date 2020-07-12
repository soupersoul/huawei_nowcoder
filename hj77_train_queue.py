all_trains = ['1','2','3']

re = []
def do_stack(all_trains, insite, outsite):
    if not all_trains and not insite:
        re.append(' '.join(outsite))
    else:
        if insite:
            outsite.append(insite.pop())
            do_stack(all_trains, insite, outsite)
            insite.append(outsite.pop())
        if all_trains:
            insite.append(all_trains.pop(0))
            do_stack(all_trains, insite, outsite)
            all_trains.insert(0, insite.pop())
do_stack(all_trains, [], [])
print(re)