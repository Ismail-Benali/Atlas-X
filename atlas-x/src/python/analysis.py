def analyze_data(data):
    """
    Analyzes the given data and returns the results.
    
    Parameters:
    data (list): A list of numerical values to analyze.

    Returns:
    dict: A dictionary containing the mean, median, and standard deviation of the data.
    """
    import numpy as np

    mean = np.mean(data)
    median = np.median(data)
    std_dev = np.std(data)

    return {
        'mean': mean,
        'median': median,
        'std_dev': std_dev
    }

def load_data(file_path):
    """
    Loads data from a specified file.

    Parameters:
    file_path (str): The path to the data file.

    Returns:
    list: A list of data points loaded from the file.
    """
    import pandas as pd

    data = pd.read_csv(file_path)
    return data.values.tolist()

def main():
    """
    Main function to execute the data analysis.
    """
    data = load_data('data.csv')  # Example file path
    results = analyze_data(data)
    print(results)

if __name__ == "__main__":
    main()