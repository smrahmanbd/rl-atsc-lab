# Reinforcement Learning for Adaptive Traffic Signal Control

A two-level module, with an interactive website, on how a traffic signal controller can **learn** good timing from trial, error and reward. Part of [CE677 Traffic Control and Operation](https://github.com/smrahmanbd/ce677-traffic-control-and-operation).

**Website:** https://smrahmanbd.github.io/rl-atsc-lab/

| Level | What you learn | Online | Study guide | Slides |
|---|---|---|---|---|
| **Foundation** (beginner) | Agent, state, action, reward; return and discount; the Q-table and its update rule; random moves and table moves (epsilon-greedy); reading a trained table; from table to neural network (DQN); designing a signal agent | [Interactive lesson](https://smrahmanbd.github.io/rl-atsc-lab/foundation.html): six steps and one extra, with a live junction, a Q-table and a small neural network | [PDF](docs/materials/RL_Foundation_Study_Guide.pdf) | [PPTX](docs/materials/RL_Foundation_Presentation.pptx) · [PDF](docs/materials/RL_Foundation_Presentation.pdf) |
| **Research** | Where RL sits among fixed-time, actuated, adaptive and max-pressure control; pressure; landmark methods from IntelliLight to language-model hybrids; multi-agent control; fair testing; seven gaps; eight research ideas | [Research page](https://smrahmanbd.github.io/rl-atsc-lab/research.html) with a pressure calculator, timeline, gap explorer and idea cards | [PDF](docs/materials/RL_Research_Study_Guide.pdf) | [PPTX](docs/materials/RL_Research_Presentation.pptx) · [PDF](docs/materials/RL_Research_Presentation.pdf) |

## What is in the repository

```
docs/                 the website (GitHub Pages serves this folder)
  index.html          home
  foundation.html     the interactive lesson (self-contained, no build step)
  research.html       the research page
  materials/          study guides (PDF) and slide decks (PPTX and PDF)
code/
  q_learning_intersection.py   the lesson's Q-learning agent in plain Python
research/
  literature.md       reference list, gap table and research ideas
  references.json     the same references as data
```

## Run the code

```bash
python code/q_learning_intersection.py              # trains for 10,000 moves, prints the learning curve and the table
python code/q_learning_intersection.py --moves 20000 --seed 3
```

No packages are needed beyond Python 3. The script uses the same toy junction as the lesson: two one-way roads, random arrivals, two actions (keep or switch) and a reward of minus one point per waiting car each second. With seed 1 a fixed 5-second timer leaves 2.43 cars waiting on average, and the trained table settles near 1.2.

## Website locally

```bash
cd docs && python -m http.server 8000      # http://localhost:8000
```

## Honesty note

The Foundation numbers come from a small simulated junction with no pedestrians, turning movements or minimum green times. They are illustrative and are not field results. The 5-second timer used as a baseline is not tuned. In the Research level, results quoted from papers are the authors' reported figures, mostly from simulation; each reference was checked against its source page (see `research/literature.md`).

MIT licensed.
