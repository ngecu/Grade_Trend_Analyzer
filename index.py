import csv
import numpy as np
import matplotlib.pyplot as plt

class DataScienceAnalyzer:
    def __init__(self):
        self.data_2024 = []

    def read_2020_file(self, filename):
        intervals = []
        frequencies = []
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                values = row[0].split()
                intervals.append((int(values[0]), int(values[1]))) 
                frequencies.append(int(values[2]))
        return intervals, frequencies

    def read_2024_file(self,filename):
        with open(filename, 'r') as file:
              reader = csv.reader(file)
              for row in reader:
                values = row[0].split()
                self.data_2024.append(int(values[0]))
        
        return self.data_2024

    def calculate_histogram(self, data):
        grades  = np.array(data)
        Q1 = np.percentile(grades, 25)
        Q3 = np.percentile(grades, 75)
        IQR = Q3 - Q1
        n = len(grades)
        bin_width = 2 * IQR * n ** (-1/3)
        range_of_data = grades.max() - grades.min()
        num_bins = int(range_of_data / bin_width)
        
        return np.histogram(grades, bins=num_bins, density=False)

    def calculate_mean_and_std(self, data):
        mean = np.mean(data)
        std = np.std(data)
        return mean, std

    def calculate_v_value(self, intervals, frequencies):
        total_students = sum(frequencies)
        num_students_above_50 = sum([frequency for interval, frequency in zip(intervals, frequencies) if interval[0] >= 50])
        v_value = num_students_above_50 / total_students
        return v_value

    def plot_histogram(self, intervals, frequencies, data_2024, mean_2020, std_2020, mean_2024, std_2024, v_value):
        x_ticks = [f"{interval[0]}-{interval[1]}" for interval in intervals]
        plt.bar(x_ticks, frequencies)
        plt.xlabel('Grade Intervals')
        plt.ylabel('Frequency')
        plt.title('Distribution of 2020 Exam Grades')
        plt.xticks(rotation=90)
        plt.text(0.05, 0.95, f"Mean: {mean_2020:.2f}\nStd Dev: {std_2020:.2f}\nV Value: {v_value:.2f}", transform=plt.gca().transAxes, va='top')
        plt.show()

        plt.hist(data_2024, bins=10, color='skyblue', edgecolor='black', alpha=0.7)
        plt.xlabel('Grades')
        plt.ylabel('Frequency')
        plt.title('Distribution of 2024 Exam Grades')
        plt.grid(True)
        plt.text(0.05, 0.95, f"Mean: {mean_2024:.2f}\nStd Dev: {std_2024:.2f}", transform=plt.gca().transAxes, va='top')
        plt.show()

    def main(self):
        intervals, frequencies = self.read_2020_file('./2020input5.csv')
        data_2024 = self.read_2024_file('./2024input5.csv')
        mean_2020, std_2020 = self.calculate_mean_and_std([grade for interval, frequency in zip(intervals, frequencies) for grade in range(interval[0], interval[1]+1) for _ in range(frequency)])
        mean_2024, std_2024 = self.calculate_mean_and_std(data_2024)
        print("2020 Exam Mean:", mean_2020)
        print("2020 Exam Standard Deviation:", std_2020)
        print("2024 Exam Mean:", mean_2024)
        print("2024 Exam Standard Deviation:", std_2024)
        v_value = self.calculate_v_value(intervals, frequencies)
        print("Value V (proportion of students with grade of 50 or higher in 2020 exam):", v_value)
        self.plot_histogram(intervals, frequencies, data_2024, mean_2020, std_2020, mean_2024, std_2024, v_value)


analyzer = DataScienceAnalyzer()
analyzer.main()
