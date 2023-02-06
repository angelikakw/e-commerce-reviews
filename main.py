import pandas as pd
from dash_app import show_dashboard


def read_data():
    data = pd.read_csv('Womens Clothing E-Commerce Reviews.csv', index_col=0)
    return data


def main():
    data = read_data()
    show_dashboard(data)


if __name__ == '__main__':
    main()

