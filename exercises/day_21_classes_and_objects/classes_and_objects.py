from collections import Counter


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




