'''heuristics_option2
This file augments Wicked_Problem.py with heuristic information,
so that it can be used by an A* implementation.

The particular heuristic incorporates all the factors of a given state. 
The heuristic value returned is the number of regions that have no reached their
goal stats. This ensures admissability because the number of actions performed 
for all regions to reach a goal state is always higher than the number of regions.

'''

from Wicked_Problem import *

def h(s):
  ''' returns the number of regions that have not reached their goal states '''
  goal_state_sf = [0.0204, 0.03035, 0.0269, 0.0159, 0.0278, 0.04645, 0.0242, 0.0409]
  goal_state_treatment = 0.9

  rc = s.rc_complete
  rs = 12 - s.research_start
  sum = 0.0
  for i in range(8):
    time = s.quarter + 4 * s.year
    if(s.d[i]['sf'] > goal_state_sf[i]):
        sum += (s.d[i]['sf'] - goal_state_sf[i])
    if(s.d[i]['treatment'] < goal_state_treatment):
        sum += goal_state_treatment - s.d[i]['treatment']
  if sum != 0:
    sum = sum * 100 + rs
    sum = sum / (rc * 5 + 1)
  return sum
