import sys

if len(sys.argv) != 3:
	print(f"Usage: {sys.argv[0]} OI_NUMER OI_ETAP")
	exit(0)

import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import csv
import re

OI_NUMER = sys.argv[1]
OI_ETAP = sys.argv[2]

URL = f'https://www.oi.edu.pl/l/{OI_NUMER}oi_{OI_ETAP}etap_wyniki/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

header = []

for element in soup.find_all("tr"):
	for column in element.find_all("th"):
		label = column.text.replace('\n', '').replace('\r', '').lstrip().rstrip()
		header.append(label)

	if len(header) > 0:
		break;

with open(f'data/oi{OI_NUMER}_etap{OI_ETAP}.csv', 'w', encoding='UTF-8') as f:

	writer = csv.writer(f);
	writer.writerow(header)

	for element in soup.find_all("tr"):
		row = []
		for column in element.find_all("td"):
			data = column.text.replace('\n', '').replace('\r', '')
			if data == "":
				data = "0"
			
			if re.match(r"[-+]?\d+(\.0*)?$", data.replace(' ', '')) is not None:
				data = int(data)

			row.append(data)

		if row == []:
			continue

		writer.writerow(row)

