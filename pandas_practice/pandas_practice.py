import pandas as pd
import requests
import glob

csv_files = glob.glob("./data_t/*.csv")
txt_files = glob.glob("./data_t/*.txt")
excel_files = glob.glob("./data_t/*.xlsx")

salary = pd.DataFrame()

for cf in csv_files:
    csv = pd.read_csv(cf)
    salary = salary.append(csv)

for tf in txt_files:
    txt = pd.read_csv(tf, sep="\t")
    salary = salary.append(txt)

for ef in excel_files:
    exc = pd.read_excel(ef)
    salary = salary.append(exc)

"""
def currency_exchange(from_cur,to_cur='AUD'):
    response = requests.get("https://free.currconv.com/api/v7/convert?q="+ from_cur + "_" + to_cur + "&compact=ultra&apiKey=96b96bece5a5280ed8df")
    return list(response.json().values())[0]
"""
cur_to_AUD_dict = {
    "EUR": 1.5711111,
    "USD": 1.3611111,
    "GBP": 1.8411111,
    "AUD": 1
}


def currency_exchange(from_cur):
    return cur_to_AUD_dict[from_cur]


salary['salary_AUD'] = round(
    salary['salary'] * salary['currency_code'].apply(currency_exchange), 2)

print(salary)

for bn in salary['bank_name'].unique():
    salary[salary['bank_name'] == bn].to_csv(
        './data_t/exported/salary_%s.csv' % (bn))

bk_names = salary['bank_name'].unique()
print(bk_names)

for bn in bk_names:
    salary_nab = salary[salary['bank_name'] == bn]
    salary[salary['bank_name'] == bn].to_csv("./data_t/exported/salary_%s.csv" % (bn))
