# CSV Data Cleanser for AI Training

This Python program, `cleanser.py`, provides a user-friendly command-line interface to clean and preprocess CSV datasets for AI model training. It includes functionalities for:

* **Handling Categorical Data:** One-hot encoding of categorical features.
* **Handling Date Data:** Extracting year, month, day, day of week, and quarter from date features.
* **Outlier Removal:** Removing outliers from numerical columns using the IQR method.
* **Handling Missing Values:** Filling missing values in numerical columns with the average.
* **Data Scaling:** Normalizing or standardizing numerical data.
* **Data Visualization:** Displaying histograms for numerical columns and bar charts for categorical columns.
* **Saving Cleaned Data:** Saving the processed DataFrame to a new CSV file.

## Prerequisites

Before running the program, ensure you have the following Python libraries installed:

```bash
pip install pandas numpy matplotlib
```

**Note:** This script uses `tkinter` for file selection and `matplotlib` with the `TkAgg` backend for displaying plots. While `tkinter` is typically included with Python, the underlying `tk` library might need to be installed separately on some systems.

**Tk Installation (Required for matplotlib's TkAgg backend and tkinter)**

* **Debian/Ubuntu-based systems:**
    ```bash
    sudo apt-get update && sudo apt-get install python3-tk
    ```
* **Fedora:**
    ```bash
    sudo dnf install python3-tkinter
    ```
* **Arch Linux:**
    ```bash
    sudo pacman -S tk
    ```
* **macOS:**
    * Tkinter is usually included with standard Python installations. If you are using a custom python install, ensure that it was installed correctly.
* **Windows:**
    * Tkinter is usually included with standard Python installations. If you have issues, try reinstalling Python from python.org.
* **Anaconda:**
    ```bash
    conda install tk
    ```

## Usage

1.  **Run the script:**
    ```bash
    python cleanser.py
    ```
2.  **Select a CSV file:** A file dialog will appear, allowing you to choose the CSV file you want to process.
3.  **Specify column types:** The program will display the columns in your CSV file and prompt you to specify whether each column is:
    * `y` for categorical
    * `n` for numerical
    * `d` for date
    * `x` to exclude the column from cleaning.
4.  **Choose operations:** A menu will appear with the following options:
    * `auto`: Performs all cleaning operations in a predefined order.
    * `Show`: Displays histograms and bar charts of the data.
    * `Normalise`: Normalizes numerical data.
    * `Standardize`: Standardizes numerical data.
    * `Encode`: Performs one-hot encoding on categorical and date columns.
    * `FillNa`: Fills missing values in numerical columns.
    * `Outlier_Removal`: Removes outliers from numerical columns.
    * `save`: Saves the cleaned data to `cleanedData.csv`.
    * `exit`: Exits the program.
5.  **Follow the prompts:** The program will guide you through each operation.

## Example

```
python cleanser.py
```

The program will open a file dialog. Select your csv. The console will then ask you to define each columns type. Then the menu will appear.

## Output

The cleaned data will be saved to a file named `cleanedData.csv` in the same directory as the script.

## Customization

* You can modify the `OutlierRem` function to use different outlier removal methods.
* You can add more data preprocessing functions to the `cleanser` class.
* You can change the default save path.

## Contributing

Feel free to contribute to this project by submitting pull requests or opening issues.
```
