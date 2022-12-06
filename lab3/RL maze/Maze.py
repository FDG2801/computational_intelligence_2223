import numpy as np

#actions that can be performed (up, down, left, right)
ACTIONS = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

class Maze(object):
    #maze construction parameters 
    def __init__(self):
        self.end = (5, 5)
        self.maze = np.zeros((6, 6))
        #costruzione labirinto
        self.maze[0, 0] = 2
        self.maze[5, :5] = 1
        self.maze[:4, 5] = 1
        self.maze[2, 2:] = 1
        self.maze[3, 2] = 1
        self.maze[self.end] = -1
        self.robot_position = (0, 0)
        self.steps = 0
        self.construct_allowed_states()

    def print_maze(self):
        print('---------------------------------')
        for row in self.maze:
            for col in row:
                if col == 0:
                    print(' 0 ', end="") # empty space
                elif col == 1:
                    print(' X ', end="") # walls
                elif col == 2:
                    print(' R ', end="") # robot position
                elif col == -1:
                    print(' E ', end="")
            print("\n")
        print('---------------------------------')

    def is_allowed_move(self, state, action):
        # check allowed move from a given state
        y, x = state
        y += ACTIONS[action][0]
        x += ACTIONS[action][1]
        if y < 0 or x < 0 or y > 5 or x > 5:
            # if robot will move off the board
            return False
        # if robot moves into empty space or its original start position
        return self.maze[y, x] <= 0 or self.maze[y, x] == 2

    def construct_allowed_states(self):
        # create a dictionary of allowed states from any position
        # using the isAllowedMove() function
        # this is so that you don't have to call the function every time
        allowed_states = {}
        for y, row in enumerate(self.maze):
            for x, col in enumerate(row):
                # iterate through all spaces
                if self.maze[(y,x)] != 1:
                    # if the space is not a wall, add it to the allowed states dictionary
                    allowed_states[(y,x)] = []
                    for action in ACTIONS:
                        if self.is_allowed_move((y,x), action) & (action != 0):
                            allowed_states[(y,x)].append(action)
        self.allowed_states = allowed_states

    def update_maze(self, action):
        y, x = self.robot_position # get current position
        self.maze[y, x] = 0 # set the current position to 0
        y += ACTIONS[action][0] # get new position
        x += ACTIONS[action][1] # get new position
        #si muove in due assi quindi 
        self.robot_position = (y, x) # set new position
        self.maze[y, x] = 2 # set new position
        self.steps += 1 # add steps

    def is_game_over(self):
        # check if robot in the final position
        return self.robot_position == self.end

    def get_state_and_reward(self):
        return self.robot_position, self.give_reward()

    def give_reward(self):
        # if at end give 0 reward
        # if not at end give -1 reward
        return -1 * int(not self.robot_position == self.end)