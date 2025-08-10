import numpy as np

# Parameters
COLOR_MATCH_THRESHOLD = 35
MIN_TEAM_DIFF_THRESHOLD = 50

# Team color anchors
team_anchors = {
    'A': None,
    'B': None
}

def color_distance(c1, c2):
    """Euclidean distance between two BGR colors"""
    return np.linalg.norm(np.array(c1) - np.array(c2))

def assign_team(color):
    """
    Assign player to Team A or B based on color proximity.
    color: (B, G, R)
    Returns: 'A' or 'B'
    """
    global team_anchors

    # First color becomes Team A anchor
    if team_anchors['A'] is None:
        team_anchors['A'] = color
        return 'A'

    # Second distinct-enough color becomes Team B anchor
    if team_anchors['B'] is None:
        if color_distance(color, team_anchors['A']) >= MIN_TEAM_DIFF_THRESHOLD:
            team_anchors['B'] = color
            return 'B'
        else:
            return 'A'

    # Compare with both anchors and assign closest
    dist_a = color_distance(color, team_anchors['A'])
    dist_b = color_distance(color, team_anchors['B'])

    return 'A' if dist_a < dist_b else 'B'
