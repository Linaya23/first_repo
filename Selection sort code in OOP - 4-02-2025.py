"""
Input: CSV file consisting unsorted numbers, text
Process: Convert unsorted numbers to unsorted array then sort it using selection sort algorithm and return sorted array, array
Output: Display sorted array in UI, string
"""
import tkinter as tk
from tkinter import messagebox, filedialog
import csv

class selection_sort_app:
    def __init__(self, root):
        self.root = root
        self.root.title("Selection Sort Visualizer")
        
        self.label = tk.Label(root, text="Select a CSV file with numbers:")
        self.label.pack()
        
        self.load_button = tk.Button(root, text="Load CSV", command=self.load_csv)
        self.load_button.pack()
        
        self.sort_button = tk.Button(root, text="Sort", command=self.perform_sort, state=tk.DISABLED)
        self.sort_button.pack()
        
        self.result_label = tk.Label(root, text="Sorted List:")
        self.result_label.pack()
        
        self.numbers = []

    def selection_sort(self, arr):
        n = len(arr)
        for i in range(n-1):
            min_idx = i
            for j in range(i+1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return
        
        try:
            with open(file_path, newline="") as f:
                reader = csv.reader(f)
                self.numbers = [int(num.strip()) for row in reader for num in row]
            self.result_label.config(text=f"Loaded Numbers: {self.numbers}")
            self.sort_button.config(state=tk.NORMAL)
        except Exception as e:
            messagebox.showerror("File Error", f"Error reading file: {e}")

    def perform_sort(self):
        if not self.numbers:
            messagebox.showerror("Error", "No numbers loaded from CSV")
            return

    print("editing 2")
        
        sorted_list = self.selection_sort(self.numbers)
        self.result_label.config(text=f"Sorted List: {sorted_list}")

if __name__ == "__main__":
    root = tk.Tk()
    app = selection_sort_app(root)
    root.mainloop()
