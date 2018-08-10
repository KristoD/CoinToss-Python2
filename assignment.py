import random

def coin_toss():
    head_count = 0
    tails_count = 0
    for i in range(1,5001):
        num = random.random()
        num_rounded = round(num)
        if num_rounded == 0:
            head_count += 1
        else:
            tails_count += 1
        print "Attempt #" + str(i) + ": Throwing a coin... It's head!... Got " + str(head_count) + " head(s) so far and " + str(tails_count) + " tails(s) so far"
coin_toss()