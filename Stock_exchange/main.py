import stock_parser as stp


if __name__ == '__main__':
    downloader = stp.StockDataDownloader('KO', '2022-03-01', '2023-03-01')
    downloader.download_and_save_csv('KO.csv')
    # downloader.download_and_save_json('KO.json')

