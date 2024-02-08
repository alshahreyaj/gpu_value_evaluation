import requests
import re
from bs4 import BeautifulSoup
import json

def extract_table_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the table element you want to extract data from
        table = soup.find('table')
        
        if table:
            rows = table.find_all('tr')
            
            # with open('table_data.txt', 'w') as file:
            json_data = []
            for row in rows:
                columns = row.find_all('td')
                if len(columns) < 3:
                        continue
                arr = []
                for i in range(3):
                    col = columns[i]
                    tmp = col.get_text(strip=True)
                    if i > 0:
                        pattern = r'\((\d+(\.\d+)?)fps\)'
                        match = re.search(pattern, tmp)

                        if match:
                            tmp = match.group(1)
                    arr.append(tmp)

                # row_data = [col.get_text(strip=True) for col in columns[:3]]
                print(arr)
                json_row = {
                    "name": arr[0],
                    "fps1": arr[1],
                    "fps2": arr[2],
                    "price": ""
                }
                json_data.append(json_row)
                # file.write('\t'.join(arr) + '\n')
            with open('table_data.json', 'w') as json_file:
                json.dump(json_data, json_file, indent=4)
            
            print("Table data written to 'table_data.txt'.")
        else:
            print("No table found on the page.")
    else:
        print("Failed to retrieve the webpage.")

if __name__ == "__main__":
    url = "https://www.tomshardware.com/reviews/gpu-hierarchy,4388.html"
    extract_table_data(url)
