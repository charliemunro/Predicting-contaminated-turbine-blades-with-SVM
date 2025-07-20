# Average Relative Abundance Analysis

This repository contains tools to compute and visualize the average relative abundance of samples based on microbial/taxa data in CSV format.

## Files

- **analysis.py**  
  - Loads a CSV file (`input_csv`) with the first column as sample identifiers and remaining columns as taxa abundances.
  - Computes the mean abundance across taxa for each sample.
  - Prints the average abundances to the console.
  - Generates and saves a bar plot of the results (default: `average_abundance.png`).

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/abundance-analysis.git
   cd abundance-analysis
   ```

2. (Recommended) Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install pandas matplotlib
   ```

## Usage

```bash
python analysis.py path/to/data.csv --output-plot myplot.png
```

- `path/to/data.csv` should be a CSV where:
  - Column 1: Sample names/IDs
  - Columns 2..N: Numeric abundances for each taxon
- `--output-plot` (optional): Filename to save the bar plot (default: `average_abundance.png`).

## Example

```bash
python analysis.py data/samples.csv -o results/avg_abundance.png
```

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
