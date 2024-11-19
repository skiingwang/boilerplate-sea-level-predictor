import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig = plt.figure(figsize=(10, 7))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope, intercept, a, b, c = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = np.array([2010, 2020, 2030, 2040, 2050, 2060])

    # Create second line of best fit
    y = slope * x + intercept
    level = pd.DataFrame({'Year': x, 'CSIRO Adjusted Sea Level': y})
    plt.scatter(level['Year'], level['CSIRO Adjusted Sea Level'])

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()