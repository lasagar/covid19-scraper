from bs4 import BeautifulSoup
import requests

url = 'https://www.ncdhhs.gov/divisions/public-health/covid19/covid-19-nc-case-count'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='block-system-main')

table = soup.find('table')

table_header = table.find_all('th')
table_rows = table.find_all('td')

table_head = [i.text for i in table_header]
table_row = [i.text for i in table_rows]

final_dict = dict(zip(table_head,table_row))

print('COVID-19 North Carolina Dashboard: {}'.format(final_dict))

print('-'*10)

print('NC Cases COVID-19')
print('-'*10)

county_ele = results.find_all('a') # Diff table section

county_elements = [i.text for i in county_ele][1:]
# print(county_elements)

county_section= soup.find_all('section',class_="tab-main no-aside")

val = 0

for i in county_section:
    img_text = i.find_all('img')
    if len(img_text) >= 1:
        print(county_elements[val])
        for j in img_text:
            print(j['src'])
        print("-"*10)
        val += 1
    elif i.find('table'):
        print(county_elements[val])
        table_data = i.find('table')
        columns = table_data.find_all('th')
        cols_list = [z.text for z in columns]
        print(cols_list)
        t_head = table_data.find_all('td')
        t_head_list = [z.text for z in t_head]
        it = iter(t_head_list)
        data_dct = dict(zip(it, it))
        print(data_dct)
        print("*"*50)
        val += 1
    else:
        # print(county_elements[val])
        val += 1
        continue

