# Brutally stolen and corrected from
# https://towardsdatascience.com/hands-on-introduction-to-reinforcement-learning-in-python-da07f7aaca88

# ... and a little bit modified

# Same goes for Maze and RLAgent, obviously

from Maze import Maze
from RLAgent import Agent
import matplotlib.pyplot as plt

if __name__ == '__main__':
    maze = Maze()
    robot = Agent(maze.maze, alpha=0.1, random_factor=0.4)
    moveHistory = []
    indices = []

    maze.print_maze()

    for i in range(5000):

        while not maze.is_game_over():
            state, _ = maze.get_state_and_reward()  # get the current state
            # choose an action (explore or exploit)
            action = robot.choose_action(state, maze.allowed_states[state])
            maze.update_maze(action)  # update the maze according to the action
            state, reward = maze.get_state_and_reward()  # get the new state and reward
            # update the robot memory with state and reward
            robot.update_state_history(state, reward)
            if maze.steps > 1000:
                # end the robot if it takes too long to find the goal
                maze.robot_position = (5, 5)
        robot.learn()  # robot should learn after every episode
        # get a history of number of steps taken to plot later
        if i % 50 == 0:
            print(f"{i}: {maze.steps}")
            moveHistory.append(maze.steps)
            indices.append(i)
        maze = Maze()  # reinitialize the maze

plt.semilogy(indices, moveHistory, "b")
plt.show()
