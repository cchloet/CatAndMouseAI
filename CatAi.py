#Christina Torres
import numpy as np

epsilon = 0.2
learning_rate = 0.7
discount = 0.9
class CatAi() :
    def __init__(self, row_size, col_size) :
        self.q_vals = np.zeros((row_size+1, col_size+1, 4))
        self.visited_square = []
        self.actions = []
        self.state = None

    def calculate_qval(self, old_x, old_y, action, reward, new_x, new_y):
        old_q_val = self.q_vals[old_x, old_y, action]
        temp = reward + (discount * np.max(self.q_vals[new_x, new_y])) - old_q_val
        new_q_val = old_q_val + (learning_rate * temp)
        self.q_vals[old_x, old_y, action] = new_q_val
    
    def endGame_q_val(self, final_reward) :
        minus_rate = final_reward/len(self.actions)
        reversed_actions = []
        for i in range(len(self.actions)) :
            index = len(self.actions)
            index = index - (i +1)
            action = self.actions[index]
            reversed_actions.append(action)
        reveresed_visited = []
        for i in range(len(self.visited_square)) :
            index = len(self.visited_square)
            index = index - (i+1)
            square = self.visited_square[index]
            reveresed_visited.append(square)
        
        for i in range(len(reversed_actions)) :
            if (i == (len(reveresed_visited)-1)) :
                break
            future_x, future_y = reveresed_visited[i]
            past_x, past_y = reveresed_visited[i+1]
            self.calculate_qval(past_x, past_y, reversed_actions[i], final_reward, future_x, future_y)
            final_reward -= minus_rate
        #gets reward
    def reward(self, state, min_reward, row_size, col_size):
        runner_xcor, runner_ycor, mode = state
        new_xcor = row_size-1
        new_ycor = col_size-1
        if mode == 'barrier':
            return min_reward -0.50
        if (runner_xcor, runner_ycor) in self.visited_square:
            return -0.20
        if runner_xcor == new_xcor-1 and runner_ycor == new_ycor-1:
            return 10.00
        if mode == 'running':
            return -0.1
        if mode == 'stop':
            return -0.35
        if mode == 'eating':
            return 100.00