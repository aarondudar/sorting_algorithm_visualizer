import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

# Sorting Algorithms with comparison counters

def bubble_sort(arr):
    """Bubble Sort with step-by-step visualization"""
    arr = arr.copy()
    n = len(arr)
    comparisons = 0
    steps = [arr.copy()]
    
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                steps.append(arr.copy())
    
    return arr, comparisons, steps


def merge_sort(arr):
    """Merge Sort with step-by-step visualization"""
    comparisons = [0]  # Use list to make it mutable in nested functions
    steps = []
    
    def merge(arr, left, mid, right):
        left_arr = arr[left:mid + 1]
        right_arr = arr[mid + 1:right + 1]
        
        i = j = 0
        k = left
        
        while i < len(left_arr) and j < len(right_arr):
            comparisons[0] += 1
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
            steps.append(arr.copy())
        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
            steps.append(arr.copy())
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
            steps.append(arr.copy())
    
    def merge_sort_recursive(arr, left, right):
        if left < right:
            mid = (left + right) // 2
            merge_sort_recursive(arr, left, mid)
            merge_sort_recursive(arr, mid + 1, right)
            merge(arr, left, mid, right)
    
    arr = arr.copy()
    steps.append(arr.copy())
    merge_sort_recursive(arr, 0, len(arr) - 1)
    
    return arr, comparisons[0], steps


def insertion_sort(arr):
    """Insertion Sort with step-by-step visualization"""
    arr = arr.copy()
    n = len(arr)
    comparisons = 0
    steps = [arr.copy()]
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
                steps.append(arr.copy())
            else:
                break
        
        arr[j + 1] = key
        steps.append(arr.copy())
    
    return arr, comparisons, steps


# Streamlit App
def main():
    st.set_page_config(page_title="Sorting Algorithm Visualizer", layout="wide")
    
    st.title("🔢 Sorting Algorithm Visualizer")
    st.markdown("Visualize how different sorting algorithms work with comparison counters")
    
    # Sidebar for inputs
    st.sidebar.header("Configuration")
    
    # Array size input
    array_size = st.sidebar.slider(
        "Array Size",
        min_value=5,
        max_value=50,
        value=20,
        step=1,
        help="Select the size of the array to sort"
    )
    
    # Algorithm selection
    algorithm = st.sidebar.selectbox(
        "Choose Sorting Algorithm",
        ["Bubble Sort", "Merge Sort", "Insertion Sort"],
        help="Select the sorting algorithm to visualize"
    )
    
    # Generate random array button
    if st.sidebar.button("Generate New Array"):
        st.session_state.array = np.random.randint(1, 100, size=array_size)
    
    # Initialize array if not exists
    if 'array' not in st.session_state:
        st.session_state.array = np.random.randint(1, 100, size=array_size)
    
    # Adjust array size if changed
    if len(st.session_state.array) != array_size:
        st.session_state.array = np.random.randint(1, 100, size=array_size)
    
    # Display original array
    st.subheader("Original Array")
    col1, col2 = st.columns([3, 1])
    
    with col1:
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.bar(range(len(st.session_state.array)), st.session_state.array, color='steelblue')
        ax.set_xlabel("Index")
        ax.set_ylabel("Value")
        ax.set_title("Unsorted Array")
        st.pyplot(fig)
        plt.close()
    
    with col2:
        st.write("Array values:")
        st.write(st.session_state.array)
    
    # Sort button
    if st.button("🚀 Start Sorting", type="primary"):
        st.subheader(f"Sorting with {algorithm}")
        
        # Sort based on selected algorithm
        if algorithm == "Bubble Sort":
            sorted_arr, comparisons, steps = bubble_sort(st.session_state.array)
        elif algorithm == "Merge Sort":
            sorted_arr, comparisons, steps = merge_sort(st.session_state.array)
        else:  # Insertion Sort
            sorted_arr, comparisons, steps = insertion_sort(st.session_state.array)
        
        # Display metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Comparisons", comparisons)
        with col2:
            st.metric("Array Size", array_size)
        with col3:
            st.metric("Total Steps", len(steps))
        
        # Visualization
        st.subheader("Sorting Visualization")
        
        # Create placeholder for animation
        chart_placeholder = st.empty()
        
        # Animate sorting steps
        step_speed = st.sidebar.slider(
            "Animation Speed (steps/sec)",
            min_value=1,
            max_value=20,
            value=5,
            help="Control the speed of the visualization"
        )
        
        progress_bar = st.progress(0)
        
        for idx, step in enumerate(steps):
            fig, ax = plt.subplots(figsize=(10, 4))
            ax.bar(range(len(step)), step, color='coral')
            ax.set_xlabel("Index")
            ax.set_ylabel("Value")
            ax.set_title(f"{algorithm} - Step {idx + 1}/{len(steps)}")
            ax.set_ylim([0, max(st.session_state.array) + 10])
            
            chart_placeholder.pyplot(fig)
            plt.close()
            
            progress_bar.progress((idx + 1) / len(steps))
            time.sleep(1 / step_speed)
        
        # Final sorted array
        st.success("✅ Sorting Complete!")
        st.subheader("Sorted Array")
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            fig, ax = plt.subplots(figsize=(10, 4))
            ax.bar(range(len(sorted_arr)), sorted_arr, color='lightgreen')
            ax.set_xlabel("Index")
            ax.set_ylabel("Value")
            ax.set_title("Sorted Array")
            st.pyplot(fig)
            plt.close()
        
        with col2:
            st.write("Sorted values:")
            st.write(sorted_arr)
    
    # Information section
    st.sidebar.markdown("---")
    st.sidebar.subheader("About")
    st.sidebar.info(
        """
        **Sorting Algorithms:**
        
        - **Bubble Sort**: O(n²) - Simple comparison-based algorithm
        - **Merge Sort**: O(n log n) - Divide and conquer algorithm
        - **Insertion Sort**: O(n²) - Builds sorted array one item at a time
        
        The comparison counter shows how many comparisons each algorithm makes.
        """
    )


if __name__ == "__main__":
    main()
