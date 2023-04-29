import requests
import re

if __name__ == '__main__':
    r = requests.get('https://www.set.or.th/th/market/get-quote/warrants/')
    warrants = re.findall('\\b[A-Z]+-W\\d', r.text)
    fr = open("warrants.txt", "r")
    old_list = fr.read().split(',')
    fr.close()
    new_list = ['SET:'+x.replace('-', '.') for x in warrants]
    if len(old_list) == len(new_list):
        if len(set(old_list) & set(new_list)) == len(old_list):
            print('No change...')
    else:
        fw = open("warrants.txt", "w")
        fw.write(','.join(new_list))
        fw.close()
        print(f'Updated... for now we have {len(new_list)} warrants.')

