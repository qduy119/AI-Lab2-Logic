# AI-Lab2-Logic

## Project description
The purpose of this project is to design and implement a logical search agent for a partially observable environment. This will be accomplished by implementing an agent that 
navigates through the Wumpus World.
In summary, the Wumpus World presents key features:
- A network of interconnected 2D caves.
- Rooms that may harbor deadly pits, signaled by a perceivable breeze.
- Presence of a Wumpus in one of the rooms, detectable through a discernible stench.
- We have one arrow that we can shoot in the direction we are facing.
- A quest for a hidden pot of gold.
- Movement options: forward, backward, left, or right by 90 degrees.
The primary objectives encompass locating the gold and potentially eliminating the 
Wumpus to ensure success in this environment
## Setup

### Install  required packages
```shell
 pip install -r requirements.txt
```

### Run game

```
cd source
python main.py 
```