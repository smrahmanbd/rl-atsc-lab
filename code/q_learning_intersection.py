"""Q-learning for one small intersection, in plain Python (no extra packages).

This is the same toy world as the Foundation animation on the course website:

* Two one-way roads cross: the North road and the West road.
* Every second the agent picks one of two actions:
      0 = keep the current green      1 = switch (costs one second of yellow)
* Reward: minus one point for every car still waiting, every second.
* State: (cars waiting on North, cars waiting on West, which road has green).
  Queue lengths are grouped into 0, 1-2, 3-5 and 6+ so the Q-table has
  4 x 4 x 2 = 32 boxes, with two scores (keep, switch) in each box.

Run it:
    python q_learning_intersection.py            # train, print the learning curve and the table
    python q_learning_intersection.py --moves 20000 --seed 3
"""
import argparse
import random

CAP = 10               # most cars a road can hold in its queue
RATE = (0.32, 0.16)    # chance a new car arrives each second: (North, West)
GAMMA = 0.9            # discount: how much the future counts
ALPHA = 0.2            # learning rate: how far a score moves toward the better guess
LABELS = ("0", "1-2", "3-5", "6+")


class Intersection:
    def __init__(self, rng):
        self.rng = rng
        self.queue = [3, 2]   # cars waiting: [North, West]
        self.green = 0        # 0 = North has green, 1 = West has green

    def state(self):
        return (self.queue[0], self.queue[1], self.green)

    def step(self, action):
        """Advance one second. Returns the reward (a negative number)."""
        if action == 1:                       # switch: one second of yellow, nobody moves
            self.green = 1 - self.green
        elif self.queue[self.green] > 0:      # keep: one car leaves from the green road
            self.queue[self.green] -= 1
        for road in (0, 1):                   # new cars arrive at random
            if self.rng.random() < RATE[road] and self.queue[road] < CAP:
                self.queue[road] += 1
        return -(self.queue[0] + self.queue[1])


def bucket(n):
    return 0 if n == 0 else 1 if n <= 2 else 2 if n <= 5 else 3


def box(state):
    north, west, green = state
    return green * 16 + bucket(north) * 4 + bucket(west)


def epsilon(move):
    """Share of random moves: starts at 100 % and falls to 5 % over 2,500 moves."""
    return max(0.05, 1 - move / 2500)


def fixed_timer(moves, rng):
    """Baseline: a plain timer that switches every 5 seconds."""
    env, waiting = Intersection(rng), 0
    for t in range(moves):
        waiting -= env.step(1 if t % 5 == 4 else 0)
    return waiting / moves


def train(moves, rng, report_every=500):
    q = [[0.0, 0.0] for _ in range(32)]       # the Q-table: 32 boxes x 2 actions
    env, curve, waiting = Intersection(rng), [], 0
    s = env.state()
    for move in range(moves):
        if rng.random() < epsilon(move):      # random move (explore)
            a = rng.randrange(2)
        else:                                 # table move (exploit)
            a = 1 if q[box(s)][1] > q[box(s)][0] else 0
        r = env.step(a)
        s2 = env.state()
        better_guess = r + GAMMA * max(q[box(s2)])
        q[box(s)][a] += ALPHA * (better_guess - q[box(s)][a])
        s = s2
        waiting -= r
        if (move + 1) % report_every == 0:
            curve.append((move + 1, waiting / report_every))
            waiting = 0
    return q, curve


def print_table(q):
    for green, name in ((0, "North"), (1, "West")):
        print(f"\nWhile the {name} road has green (K = keep, S = switch)")
        print("North queue \\ West queue " + "".join(f"{l:>6}" for l in LABELS))
        for n in range(4):
            row = "".join(f"{'K' if q[green * 16 + n * 4 + w][0] >= q[green * 16 + n * 4 + w][1] else 'S':>6}" for w in range(4))
            print(f"{LABELS[n]:>25}{row}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--moves", type=int, default=10000)
    ap.add_argument("--seed", type=int, default=1)
    args = ap.parse_args()
    rng = random.Random(args.seed)
    print(f"Fixed 5-second timer: {fixed_timer(40000, random.Random(args.seed)):.2f} cars waiting on average")
    table, curve = train(args.moves, rng)
    print("\nMoves made   Average cars waiting   Random moves")
    for move, avg in curve:
        print(f"{move:>10}   {avg:>20.2f}   {epsilon(move):>11.0%}")
    print_table(table)
