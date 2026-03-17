"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

        # ----- Write your code below this line ----- #

        tags = soup.find('tbody').text
        numbers = tags.split()
        # a = '1,077'  a.replace(',', '')
        # for i in range(len(numbers) % 5):
        #     d.append(numbers[i])
        # print(d)
        male = []
        for i in range(len(numbers)):
            if i % 5 == 2 and ',' in numbers[i]:
                male.append(numbers[i])
        male_total = 0
        for ele in male:
            male_ele = ele.replace(',', '')
            male_total += int(male_ele)
        print('Male Number: ' + str(male_total))
        female = []
        for i in range(len(numbers)):
            if i % 5 == 4 and ',' in numbers[i]:
                female.append(numbers[i])
        female_total = 0
        for ele in female:
            female_ele = ele.replace(',', '')
            female_total += int(female_ele)
        print('Female Number: ' + str(female_total))





        # number = {}
        # for tag in tags:
        #     number = tag.text
        #     print(tag)




if __name__ == '__main__':
    main()
