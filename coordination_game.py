import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import matrix_power


class RevisionProtocol(object):
    """
    Class which implements the revision protocol.
    """

    def __init__(self, player_id, color, game_length, revision_length, mode='random'):
        """
        Parameters
        ----------
        player_id : int
            player id
        color : string
            Player's color
        game_length : int
            lattice side size
        mode : string
            Specifies how to looking for holes, randomly or nearby.
        """
        # Set internal parameters
        self.player_id = player_id
        self.game_length = game_length
        self.color = color
        self.mode = mode
        self.strategy = np.random.randint(1 + int(self.game_length / 2)) + 1
        self.revision_length = revision_length

    def set_strategy(self):
        strategy = self.strategy
        return strategy


class TransitionMatrix(object):
    """
    Class which implements the transition matrix of the Markov process.
    """

    def __init__(self, number_of_players):
        """
        Parameters
        ----------
        number_of_players : int
            Number of players
        """
        # Set internal parameters
        self.number_of_players = number_of_players

    def q(self, x):
        n = self.number_of_players
        return x * ((1 - x) * n / (n - 1)) ** 3

    def p(self, x):
        n = self.number_of_players
        return (1 - x) * (x * n / (n - 1)) ** 2

    def get_transition_matrix(self):
        n = self.number_of_players
        tm = np.zeros((n + 1, n + 1))
        for i in range(n + 1):
            tm[i, i] = 1 - self.p(i/n) - self.q(i/n)
            if i - 1 >= 0:
                tm[i - 1, i] = self.p((i - 1)/n)
                tm[i, i - 1] = self.q(i/n)
        return tm

    def get_state_tick_k(self, a0, k):
        tm = self.get_transition_matrix()
        p = matrix_power(tm, k)
        ak = a0 @ p
        return ak

    def plot_mean_dynamics(self, a0, t):
        mean_dynamic = []
        for k in range(t):
            ak = self.get_state_tick_k(a0, k)
            expectation = sum(np.linspace(0.0, 1.0, len(ak)) * ak)
            mean_dynamic.append(expectation)
        plt.plot(mean_dynamic)
        plt.show()


def main():
    m = TransitionMatrix(100)
    a0 = np.zeros(m.get_transition_matrix().shape[0])
    a0[int((len(a0)-1) / 2)] = 1
    m.plot_mean_dynamics(a0, 1000)


if __name__ == '__main__':
    main()
