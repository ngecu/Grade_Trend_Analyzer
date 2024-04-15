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

    def calculate_distribution_or_histogram(self, data):
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
        mean = format(np.mean(data),".2f")
        std = format(np.std(data),".2f")
        return mean, std

    def calculate_v_value(self, intervals, frequencies):
        total_students = sum(frequencies)
        num_students_above_50 = sum([frequency for interval, frequency in zip(intervals, frequencies) if interval[0] >= 50])
        v_value = num_students_above_50 / total_students
        return format(v_value,".2f")

    def plot_histogram(self, intervals, frequencies, data_2024, mean_2020, std_2020, mean_2024, std_2024, v_value):
        x_ticks_2020 = [f"{interval[0]}-{interval[1]}" for interval in intervals]
        x_ticks_2024 = [f"{grade}-{grade+4}" for grade in range(min(data_2024), max(data_2024)+1, 5)]

        plt.figure(figsize=(12, 8))

        plt.subplot(2, 1, 1)
        plt.bar(x_ticks_2020, frequencies, label='2020 Exam', color='skyblue')
        plt.xlabel('Grade Intervals')
        plt.ylabel('Frequency')
        plt.title('Distribution of 2020 Exam Grades')
        plt.xticks(rotation=45)
        plt.text(0.2, 0.95, f"Mean: {mean_2020}\nStd Dev: {std_2020}\nV Value: {v_value}",
                transform=plt.gca().transAxes, va='top', ha='right')
                
        plt.text(0.95, 0.55, f"My Student ID: 23029665",
                transform=plt.gca().transAxes, va='top', ha='right')
        plt.legend()

        plt.subplot(2, 1, 2)
        plt.hist(data_2024, bins=len(x_ticks_2024), label='2024 Exam', color='orange', edgecolor='black', alpha=0.7)
        plt.xlabel('Grade Intervals')
        plt.ylabel('Frequency')
        plt.title('Distribution of 2024 Exam Grades')
        plt.xticks(rotation=45)
        plt.text(0.2, 0.95, f"Mean: {mean_2024}\nStd Dev: {std_2024}",
                transform=plt.gca().transAxes, va='top', ha='right')

        plt.text(0.95, 0.55, f"My Student ID: 23029665",
                transform=plt.gca().transAxes, va='top', ha='right')

        plt.legend()

        plt.tight_layout()
        plt.subplots_adjust(hspace=0.5)
        plt.show()
        

    def main(self):
        intervals, frequencies = self.read_2020_file('./2020input5.csv')
        data_2024 = self.read_2024_file('./2024input5.csv')
        histogram_2020, bins_2020 = self.calculate_distribution_or_histogram([grade for interval, frequency in zip(intervals, frequencies) for grade in range(interval[0], interval[1]+1) for _ in range(frequency)])
        histogram_2024, bins_2024 = self.calculate_distribution_or_histogram(data_2024)
        
        print("Distribution/Histogram for 2020 Exam:")
        print("intervals :", bins_2020)
        print("Frequencies:", histogram_2020)
        
        print("\nDistribution/Histogram for 2024 Exam:")
        print("intervals :", bins_2024)
        print("Frequencies:", histogram_2024)
        print("\n")

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
