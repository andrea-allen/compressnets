import numpy as np


class TemporalNetwork:
    """
    Stores consecutive Snapshot() objects representing static
    adjacency matrices for each snapshot for consecutive time windows.
    """

    def __init__(self, snapshots):
        """
        Create a TemporalNetwork instance from a list of Snapshot objects.

        :param snapshots: list of Snapshot objects
        """
        self.snapshots = snapshots
        self.length = len(snapshots)

    def get_ordered_pairs(self):
        pairs = list([(self.snapshots[i], self.snapshots[i + 1]) for i in range(0, len(self.snapshots) - 1)])
        return pairs

    def get_time_network_map(self):
        return {snapshot.end_time: snapshot.A for snapshot in self.snapshots}

    def equals(self, another_net):
        if self.length != another_net.length:
            return False
        else:
            for i in range(self.length):
                if not self.snapshots[i].equals(another_net.snapshots[i]):
                    return False
        return True

    def set_all_betas(self, new_beta):
        for snapshot in self.snapshots:
            snapshot.set_new_beta(new_beta)


class Snapshot:
    """
    One static network for a single time window of a temporal network.
    Provide instance with start time, end time, adjacency matrix A as a numpy array, and infection rate beta.
    """

    def __init__(self, start_time, end_time, beta, A):
        """

        :param start_time: float or int
        :param end_time: float or int
        :param beta: float between (0,1), infection rate for snapshot
        :param A: numpy array, representing the adjacency matrix
        """
        self.start_time = start_time
        self.end_time = end_time
        self.A = A
        self.N = len(self.A)
        self.beta = beta
        self.duration = self.end_time - self.start_time
        self.dd_normalized = self.set_dd_dist()

    def scaled_matrix(self):
        return self.beta * (self.end_time - self.start_time) * self.A

    def equals(self, another_snapshot):
        return self.start_time == another_snapshot.start_time and self.end_time == another_snapshot.end_time \
               and self.beta == another_snapshot.beta and self.duration == another_snapshot.duration \
               and np.array_equal(self.A, another_snapshot.A)

    def set_dd_dist(self):
        dd = np.array([np.sum(self.A[i]) / self.N for i in range(self.N)])
        if np.sum(dd) == 0:
            return dd
        dd = dd / np.sum(dd)
        return dd

    def set_new_beta(self, new_beta):
        self.beta = new_beta
