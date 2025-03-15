import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog


class cleanser:
    def __init__(self, control=None, df=None):
        self.control = control
        self.df = df
        self.numerical_columns = [x[0] for x in self.control if x[1] == 'n']
        self.categorical = [x[0] for x in self.control if x[1] == 'y']
        self.dates = [x[0] for x in self.control if x[1] == 'd']
        self.vals = [self.df[x].value_counts() for x in self.categorical]
        self.encoded = True
        for col in self.dates:
            df[col] = pd.to_datetime(df[col])

    def menuLoop(self):
        while(True):
            features = ['auto', 'Show', 'Normalise', 'Standardize', 'Encode', 'FillNa', 'Outlier_Removal', 'save', 'exit']
            [print(i,x, end="\n") for i,x in enumerate(features)]

            match(features[int(input("Enter Operation Choice: "))]):
                case 'save':
                    self.df.to_csv('./cleanedData.csv')
                    return
                case 'auto':
                    self.fillNaEmpty()
                    self.OutlierRem()
                    self.OneHotEnc()
                    self.Normalize() if input('Choose Scaling N/S for Normalization or Standardization\n: ') == 'N' \
                        else self.Standardize()
                    self.show()
                case 'Encode':
                    self.OneHotEnc()
                case 'Outlier_Removal':
                    self.OutlierRem()
                case 'Standardize':
                    self.Standardize()
                case 'Normalise':
                    self.Normalize()
                case 'FillNa':
                    self.fillNaEmpty()
                case 'Show':
                    self.show()
                case 'exit':
                    return

    def OneHotEnc(self):
        for col in self.categorical:
            Ecodf = pd.get_dummies(self.df[col], prefix=col)
            self.df = pd.concat([self.df, Ecodf], axis=1)
            self.df.drop(col, axis=1, inplace=True)
        for col in self.dates:
            Encodf=pd.DataFrame({
            col+'_year': self.df[col].dt.year,
            col+'_month': self.df[col].dt.month,
            col+'_day': self.df[col].dt.day,
            col+'_dayofweek': self.df[col].dt.dayofweek,
            col+'_quarter': self.df[col].dt.quarter
            })
            self.df = pd.concat([self.df, Encodf], axis=1)
            self.df.drop(col, axis=1, inplace=True)

        self.encoded = True
    def OutlierRem(self):
        for col in self.numerical_columns:
            Q1 = self.df[col].quantile(0.25)
            Q3 = self.df[col].quantile(0.75)
            IQR = Q3-Q1
            self.df[col] = self.df[col][(self.df[col] < Q3 + 1.5*IQR) & (self.df[col] > Q1 - 1.5*IQR)]


    def fillNaEmpty(self):
        for col in self.numerical_columns:
            average = np.average(df[col])
            self.df[col].fillna(average)

    def Normalize(self):
        for col in self.numerical_columns:
            maxDat = np.max(df[col])
            minDat = np.min(df[col])
            self.df[col] = (self.df[col]-minDat)/(maxDat-minDat)

    def Standardize(self):
        for col in self.numerical_columns:
            mean = np.mean(df[col])
            devi = np.std(df[col])
            self.df[col] = (self.df[col] - mean)/devi
    def show(self):
        plt.close('all')
        print(self.numerical_columns)
        n_plots = len(self.numerical_columns)
        if self.encoded:
            n_plots += len(self.categorical)
            print(self.categorical)
        n_cols = int(np.floor(np.sqrt(n_plots)))
        n_rows = (n_plots + n_cols - 1) // n_cols

        fig, axes = plt.subplots(n_rows, n_cols, figsize=(12, 10))
        axes = axes.flatten()
        for i, column in enumerate(self.numerical_columns):
            if i < len(axes):
                axes[i].hist(self.df[column], bins='auto', edgecolor='black')
                axes[i].set_title(f'{column} Distribution', fontsize=10)
                axes[i].set_xlabel(column, fontsize=9)
                axes[i].set_ylabel('Frequency', fontsize=9)
                axes[i].tick_params(axis='both', which='major', labelsize=8)
                axes[i].grid(True, linestyle='--', alpha=0.3)

        lasi = len(self.numerical_columns)

        # Then plot categorical columns
        for i, column in enumerate(self.categorical):
            if lasi < len(axes):
                val_counts = self.vals[i]

                axes[lasi].bar(val_counts.index.astype(str), val_counts.values)
                axes[lasi].set_title(f'{column} Distribution', fontsize=10)
                axes[lasi].set_xlabel(column, fontsize=9)
                axes[lasi].set_ylabel('Frequency', fontsize=9)

                # Rotate x-axis labels if there are many categories
                if len(val_counts) > 5:
                    axes[lasi].tick_params(axis='x', rotation=45)

                axes[lasi].grid(True, linestyle='--', alpha=0.3)
                lasi += 1

        # Remove any unused subplots
        for i in range(lasi, len(axes)):
            fig.delaxes(axes[i])

        plt.tight_layout()
        try:
            plt.show()
        except:
            return


def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")], initialdir="*.*")
    return file_path


if __name__ == '__main__':
    selected_file = select_file()
    df = None
    try:
        df = pd.read_csv(selected_file)
    except:
        print("Invalid file, Exiting...")

    print("found columns = " + ' '.join(df.columns))
    #
    print("Enter y or n for if categorical,\nTo not include it in cleaning (i.e. names or ID) enter x\nFor dates type d:")
    data = [input(f"{x} is?(categorical y/n, date d, remove x): ") for x in df.columns]
    control = list(zip(df.columns, data))
    loaded = cleanser(control, df)
    loaded.menuLoop()
