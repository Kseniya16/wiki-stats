#!/usr/bin/python3

import os
import sys
import math

import array

import statistics

from matplotlib import rc
rc('font', family='Droid Sans', weight='normal', size=14)

import matplotlib.pyplot as plt


class WikiGraph:

    def load_from_file(self, filename):
        print('Загружаю граф из файла: ' + filename)

        with open(filename) as f:
            (n, _nlinks) = map(int, f.readline().split())

            self._titles = []
            self._sizes = array.array('L', [0]*n)
            self._links = array.array('L', [0]*_nlinks)
            self._redirect = array.array('B', [0]*n)
            self._offset = array.array('L', [0]*(n+1))

            for i in range(n):
                self._titles.append(f.readline().rstrip())
                a,b,c = map(int,f.readline().split())
                self._sizes[i] = a
                self._redirect[i] = b

                for j in range(c):
                    self._links[self._offset[i]+j] = int(f.readline())

                self._offset[i+1] = self._offset[i] + c


            # TODO: прочитать граф из файла

        print('Граф загружен')

    def get_number_of_links_from(self, _id):
        return (self._offset[_id+1]-self._offset[_id])

    def get_links_from(self, _id):
        return self._links[self._offset[_id]:self._offset[_id+1]]

    def get_id(self, title):
        return self._titles.index[title]

    def get_number_of_pages(self):
        return len(self._titles)

    def is_redirect(self, _id):
        return self._redirect[_id]

    def get_title(self, _id):
        return self._titles[_id]

    def get_page_size(self, _id):
        return self._sizes[_id]


graph=WikiGraph()
graph.load_from_file('wiki_small.txt')
n=graph.get_number_of_pages()
s=0
Q=[]
C=[]
for i in range(n):
    if graph.is_redirect(i)!=0:
        s=s+1
        C.append(graph.get_links_from(i))
    else:

    Q.append(graph.get_number_of_links_from(i))
q1=min(Q)
q2=Q.count(q1)
q3=max(Q)
q4=Q.count(Q)
q5=graph.get_title(Q.index(q3))
sr=statistics.mean(Q)
otk=statistics.stdev(Q)
for i in C:

print('количество статей с перенаправлением',s,"\n",
      'минимальное количество ссылок из статьи', q1, "\n",
      'количество статей с минимальным количеством ссылок',q2,"\n",
      'максимальное количество ссылок из статьи', q3,"\n",
      'количество статей с максимальным количеством ссылок',q4, "\n",
      'статья с наибольшим количеством ссылок', q5, "\n",
      'среднее количество ссылок в статье', sr, '(',otk,')',"\n",
      )








def hist(fname, data, bins, xlabel, ylabel, title, facecolor='green', alpha=0.5, transparent=True, **kwargs):
    plt.clf()
    # TODO: нарисовать гистограмму и сохранить в файл


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Использование: wiki_stats.py <файл с графом статей>')
        sys.exit(-1)

    if os.path.isfile(sys.argv[1]):
        wg = WikiGraph()
        wg.load_from_file(sys.argv[1])
    else:
        print('Файл с графом не найден')
        sys.exit(-1)

    # TODO: статистика и гистограммы