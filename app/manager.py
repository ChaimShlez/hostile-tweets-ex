import pandas as pd
from app.fetcher import Fetcher

class Manager:
    def __init__(self):
        pass

    def run(self):
        fetcher=Fetcher()
        data=fetcher.get_data()
        data.pd
