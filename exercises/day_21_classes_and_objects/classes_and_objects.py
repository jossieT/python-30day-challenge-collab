from collections import Counter
import math

class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        total = 0
        for i in self.data:
            total += i
        return total

    def min(self):
        minimum = self.data[0]
        for i in range(len(self.data)):
            if self.data[i] < minimum:
                minimum = self.data[i]
        return minimum

    def max(self):
        maximum = self.data[0]
        for i in range(len(self.data)):
            if self.data[i] > maximum:
                maximum = self.data[i]
        return maximum

    def range(self):
        diff = self.max() - self.min()
        return diff

    def mean(self):
        average = self.sum() / self.count()
        return average

    def median(self):
        new_data = sorted(self.data)
        med = new_data[len(new_data) // 2]
        return med

    def mode(self):
        age_counts = Counter(self.data)
        max_count = max(age_counts.values())
        modes = [age for age, count in age_counts.items() if count == max_count]

        if len(modes) == len(self.data):
            return {'mode': None, 'count': 0}  # No mode case
        else:
            # Return the first mode if multiple exist (or single mode)
            return {'mode': modes[0], 'count': max_count}

    def std(self):
        n = len(self.data)
        if n < 2:
            return 0.0
        mean = self.mean()
        squared_diffs = [(x - mean) ** 2 for x in self.data]
        variance = sum(squared_diffs) / n
        return math.sqrt(variance)

    def variance(self):
        n = len(self.data)
        mean = self.mean()
        squared_diffs = [(x - mean) ** 2 for x in self.data]
        variance = sum(squared_diffs) / n
        return variance

    def freq_dist(self):
        count = len(self.data)
        if count == 0:
            return []

        freq = Counter(self.data)
        # Calculate percentages and create tuples (percentage, value)
        distribution = [(round((v / count) * 100, 1), k) for k, v in freq.items()]
        # Sort by percentage descending, then by value ascending
        distribution.sort(key=lambda x: (-x[0], x[1]))
        return distribution


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)

print('Count:', data.count())
print('Sum: ', data.sum())
print('Min: ', data.min())
print('Max: ', data.max())
print('Range: ', data.range())
print('Mean: ', data.mean())
print('Median: ', data.median())
print('Mode: ', data.mode())
print('Standard Deviation: ', data.std())
print('Variance: ', data.variance())
print('Frequency Distribution: ', data.freq_dist())

