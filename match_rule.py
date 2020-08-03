import csv
import os
import re

keyword_file = 'keyword.csv'

def keywordReader(keyword_file):
    with open(keyword_file, 'r') as fp:
        reader = csv.reader(fp)
        data = []
        for row in reader:
            data.append(row)
        return data

def splitText(file_name):
    with open(file_name, 'r', encoding='utf-8') as fp:
        try:
            txt = fp.read()
            if txt is '':
                # print(file_name + ' is none')
                return False
            txt = txt.replace('\n', '')
            txt = txt.split('。')
            return txt
        except:
            print("read file met error")
            return False

def matchRule(data, title, keyword):
    row = len(keyword)
    col = len(keyword[0])
    res_plause = []
    res_behav = []
    res_title = []
    for i in range(row - 1):
        for j in range(col):
            if keyword[i+1][j] is '':
                continue
            for k in range(len(data)):
                for t in range(len(data[k])):
                    plause = data[k][t]
                    if keyword[i+1][j] in plause:
                        res_behav.append(j)
                        res_plause.append(plause)
                        res_title.append(title[k])
    return res_plause, res_behav, res_title

def saveCsv(res_plause, res_behav, res_title, header, file_name):
    with open(file_name, 'w', encoding='utf-8-sig', newline='') as fp:
        writer = csv.writer(fp)
        for i in range(len(res_plause)):
            writer.writerow([res_plause[i], header[res_behav[i]], res_title[i]])
    print("ok")

if __name__ == '__main__':
    keyword = keywordReader(keyword_file)
    current_dir = './sichuanTxt'
    title = []
    data = []
    for root, dir, files in os.walk(current_dir):
        i = 0
        for txt_file_name in files:
            i += 1
            file_name = current_dir + '/' +txt_file_name
            txt = splitText(file_name)
            if txt is not False and len(txt) is not 1:
                title.append(txt_file_name)
                data.append(txt)
        print(i)

    res_plause, res_behav,res_title = matchRule(data, title, keyword)
    print(res_title)
    saveCsv(res_plause, res_behav, res_title, keyword[0], 'res.csv')

