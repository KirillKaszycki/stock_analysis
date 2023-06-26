import yfinance as yf
import pandas as pd


class StockDataDownloader:
    def __init__(self, ticker, start_date, end_date):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date

    def download_data(self):
        data = yf.download(self.ticker, self.start_date, self.end_date)
        return data

    def process_data(self, data):
        file = pd.DataFrame(data)
        file.reset_index(inplace=True)
        file['Ticker'] = self.ticker
        cols = file.columns.tolist()
        cols.insert(1, cols.pop(cols.index('Ticker')))
        file = file.reindex(columns=cols)
        return file

    def save_to_csv(self, file, filename):
        file.to_csv(filename, index=False, header=True)

    def save_to_json(self, file, filename):
        file.to_json(filename)

    def download_and_save_csv(self, filename):
        data = self.download_data()
        processed_data = self.process_data(data)
        self.save_to_csv(processed_data, filename)
        print(processed_data)

    def download_and_save_json(self, filename):
        data = self.download_data()
        processed_data = self.process_data(data)
        self.save_to_json(processed_data, filename)
        print(processed_data)


