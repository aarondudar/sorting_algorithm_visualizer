# Sorting Algorithm Visualizer

An interactive sorting algorithm visualizer built with Python and Streamlit.

## Features

- **Multiple Sorting Algorithms**: Bubble Sort, Merge Sort, and Insertion Sort
- **Comparison Counter**: Track the number of comparisons made by each algorithm
- **Interactive Controls**:
  - Adjustable array size (5-50 elements)
  - Algorithm selection
  - Animation speed control
  - Generate new random arrays
- **Visual Animation**: Watch the sorting process step-by-step with bar charts
- **Real-time Metrics**: Display total comparisons, array size, and steps taken

## Installation

1. Clone or download this repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

The app will open in your default web browser.

## How to Use

1. **Configure Settings** (Left Sidebar):

   - Use the slider to select array size (5-50)
   - Choose a sorting algorithm from the dropdown
   - Click "Generate New Array" to create a new random array

2. **Start Sorting**:

   - Click the "🚀 Start Sorting" button
   - Adjust animation speed if desired
   - Watch the visualization and metrics

3. **View Results**:
   - See the total number of comparisons made
   - View the sorted array
   - Compare different algorithms on the same data

## Algorithms Included

- **Bubble Sort**: O(n²) time complexity - Simple comparison-based algorithm
- **Merge Sort**: O(n log n) time complexity - Efficient divide and conquer algorithm
- **Insertion Sort**: O(n²) time complexity - Builds sorted array incrementally

## Requirements

- Python 3.7+
- Streamlit
- NumPy
- Matplotlib
