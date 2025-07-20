import pandas as pd
import matplotlib.pyplot as plt
import argparse

def load_data(path):
    """
    Load the CSV data into a pandas DataFrame.
    Assumes first column is sample name and remaining columns are taxa.
    """
    df = pd.read_csv(path, index_col=0)
    return df


def compute_average_abundance(df):
    """
    Compute average relative abundance of each sample across taxa.
    Returns a Series indexed by sample.
    """
    return df.mean(axis=1)


def plot_abundance(avg_abundance, output):
    """
    Generate and save a bar plot of average relative abundance.
    """
    plt.figure(figsize=(10, 6))
    avg_abundance.sort_values(ascending=False).plot(kind='bar')
    plt.ylabel('Average Relative Abundance')
    plt.xlabel('Sample')
    plt.title('Average Relative Abundance per Sample')
    plt.tight_layout()
    plt.savefig(output)
    print(f"Plot saved to {output}")


def main():
    parser = argparse.ArgumentParser(
        description='Compute and plot average relative abundance from CSV.'
    )
    parser.add_argument(
        'input_csv',
        help='Path to the input CSV file with sample data'
    )
    parser.add_argument(
        '--output-plot', '-o',
        default='average_abundance.png',
        help='Filename for the output plot'
    )
    args = parser.parse_args()

    # Load and process
    df = load_data(args.input_csv)
    avg = compute_average_abundance(df)

    # Display summary
    print("Average relative abundance per sample:")
    print(avg)

    # Plot
    plot_abundance(avg, args.output_plot)

if __name__ == '__main__':
    main()
