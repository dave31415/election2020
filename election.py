from random import Random

prob_trump = {'mi': 0.02,
              'wi': 0.002,
              'az': 0.05,
              'ga': 0.5,
              'nv': 0.05,
              'pa': 0.2}


votes = {'mi': 16,
         'wi': 10,
         'az': 11,
         'ga': 16,
         'nv': 6,
         'pa': 20}

trump_needs = 38


def sim(n=1000000):
    rand = Random()
    rand.seed(27462723)
    wins = 0

    for i in range(n):
        trump_gains = 0
        for k, prob in prob_trump.items():
            vote = votes[k]
            if rand.random() <= prob:
                trump_gains += vote
        if trump_gains >= trump_needs:
            wins += 1

    print('wins: %s out of %s' % (wins, n))
    prob_trump_wins = 100.0*wins/float(n)
    prob_biden_wins = 100.0 - prob_trump_wins
    print('prob_trump_wins: %s percent' % prob_trump_wins)
    print('prob_biden_wins: %s percent' % prob_biden_wins)


if __name__ == "__main__":
    sim()
