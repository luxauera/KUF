import requests
from bs4 import BeautifulSoup
import pandas as pd


class ParseEarthQuake:
    def __init__(self):
        try:
            self.url = "http://www.koeri.boun.edu.tr/scripts/lst9.asp"
            self.tag = "pre"
            self.soup = BeautifulSoup(
                requests.get(self.url).text, 'html.parser')
            self.pre_tag = self.soup.find(self.tag)
            self.text = self.pre_tag.text[316:]
            self.data_lines = self.text.strip().split('\n')[2:]
            self.df = self.Parse()
            self.mobile_df = self.df[['Tarih', 'Saat', 'ML', 'Yer']].to_html(
                classes="table-container", index=False, border=0, justify="center")
            self.df["Enlem"] = self.df["Enlem"].astype(float)
            self.df["Boylam"] = self.df["Boylam"].astype(float)
            self.df["ML"] = self.df["ML"].astype(float)
            self.df["Derinlik"] = self.df["Derinlik"].astype(float)
        except Exception as e:
            print(f"Error: {e}")
            self.df = pd.DataFrame()
            self.mobile_df = pd.DataFrame()
            self.df['Error'] = ['bouna bağlanılamadı' + str(e)]
            self.mobile_df['Error'] = ['bouna bağlanılamadı' + str(e)]

    def Parse(self):
        records = []
        for i in self.data_lines:
            try:
                filtered = list(filter(lambda x: x != "", i.split(" ")))
                records.append({"Tarih": filtered[0], "Saat": filtered[1], "Enlem": filtered[2],
                               "Boylam": filtered[3], "Derinlik": filtered[4], "ML": filtered[6], "Yer": filtered[8]})
            except:
                records.append({"Tarih": "1900.01.01", "Saat": "00:00:00", "Enlem": 0,
                               "Boylam": 0, "Derinlik": 0, "ML": 0, "Yer": "Nowhere"})
        return pd.DataFrame(records)
