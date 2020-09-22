import sqlite3
import pandas as pd
import string


def stocks(year):
    year_query = f"""SELECT price.id, price.open, price.close, date.date, company.name, company.id as 'company_id'
                FROM price 
                JOIN date 
                ON date.id = price.id
                JOIN company
                ON company.id = price.company_id
                WHERE date.date LIKE '{year}%';"""
    df = pd.DataFrame(c.execute(year_query))
    df.dropna()
    df. columns = [col[0] for col in c.description]
    return df


def begins_with_count(letter,df):
    first_letters = df['name'].apply(lambda x: x[0])
    return first_letters.count(letter)


def pop_freq_dict(df):
    freq_dict = {}
    for char in string.ascii_uppercase:
        try:
            freq_dict.update({char: begins_with_counts(char, df)})
        except:
            continue    
    return freq_dict


plt.hist(pop_freq_dict(stocks(2017)).values())
plt.title('Letter Histogram')
fig = plt.figure(figsize = (10,10))
ax = fig.add_subplot(111)