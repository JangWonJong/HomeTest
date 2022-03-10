import random
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

class Quiz20:

    def quiz20list(self) -> str:
        list1 = [1, 2, 3, 4]
        # print(list1,type(list1))
        list2 = ['math', 'english']
        print('리스트1: ', list1[0], list1[-1], list1[-2])
        print('리스트1에서 1번째,2번째 성분출력: ', list1[1:3])
        print('리스트2에서 math출력:', list2[0])
        print('리스트2에서 a출력: ', list2[0][1])
        print('리스트2에서 math english 출력 :', list2[0], list2[1])
        list3 = [1, '2', [1, 2, 3]]
        list4 = [1, 2, 3]
        list5 = [4, 5]
        list4[-2:] = []
        print('리스트4 두배 출력: ', 2 * list4)
        print('리스트4와 리스트5 합치기:', list4 + list5)
        print('리스트4에 리스트5 성분합치기:', list4.append(list5))
        print('리스트4,5에서 [1,2] 출력해보기', list4)
        list6 = [[1, 2], [0, 5]]
        # 2를 출력해보시오
        a = [1, 2]
        b = [0, 5]
        c = [a, b]
        c[0][1] = 10
        print(list6[0][1])
        print(c)

        return None

    def quiz21tuple(self) -> str:
        tuple1 = (1, 2)
        tuple2 = (0, (1, 4))
        print(tuple1 + tuple2)

        return None

    def quiz22dict(self) -> str: return None

    def quiz23listcom(self) -> str:
        print('--------------legacy---------------')
        a = []
        for i in range(5):
            a.append(i)
        print(a)
        print('--------------comprehension---------------')
        a2 = [i for i in range(5)]
        print(a2)
        return None


    def quiz24zip(self)->{}:
        url = 'https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc, 'lxml') # html.parser vs lxml
        ls1 = self.find_music(soup, 'title')
        ls2 = self.find_music(soup, 'artist')
        dict ={}
        #self.dict1(ls1,ls2)
        #self.dict2(ls1,ls2)
        for i,j in zip(ls1,ls2):
            dict[i] = j
        print(dict)
        return dict



    @staticmethod
    def dict1(ls1,ls2) -> None:
        dict = {}
        for i in range(0, len(ls1)):
            dict [ls1[i]] = ls2[i]
        print(dict)

    @staticmethod
    def dict2(ls1, ls2):
        dict = {}
        for i, j in enumerate(ls1):
            dict[j] = ls2[i]
        print(dict)

    def print_music_list(self, soup)->None:
        artists = soup.find_all('p', {'class': 'artist'})
        artists = [i.get_text() for i in artists]
        # print(''.join(i for i in artists))
        titles = soup.find_all('p', {'class': {'titles'}})
        titles = [i.get_text() for i in titles]
        # print(''.join(i for i in titles))

    def find_rank(self,soup):
        for i,j in enumerate(['artist','title']):
            for i,j in enumerate(self.find_music(soup,j)):
                print(f'{i}위 : {j}')
            print('*'*100)

            ''' self.bugs(soup,'artist')
             self.bugs(soup,'title')'''

    @staticmethod
    def find_music(soup,class_nm)->[]:
        ls = soup.find_all('p', {'class': class_nm})
        return [i.get_text() for i in ls]


    def quiz25dictcom(self) -> str:
        return None


    def quiz26map(self) -> str: return None

    def quiz27melon(self) -> str:
        headers = {'User-Agent':'Mozilla/5.0' }
        url = 'https://www.melon.com/chart/index.htm?dayTime=2022030816'
        req = urllib.request.Request(url, headers=headers)
        soup = BeautifulSoup(urlopen(req).read(), 'lxml')#실시간차트 제목 출력하기
        #print(''.join([i.get_text() for i in soup.find_all('div',{'class':'ellipsis rank01'})[0:3]]))#세로출력
        print([i.get_text().strip() for i in soup.find_all('div', {'class': 'ellipsis rank01'})[0:3]])#가로출력(공백은 있음)

        '''a = soup.find_all('div',{'class':'ellipsis rank02'})
        a = [i.get_text() for i in a]
        print(''.join(i for i in a))'''

        '''a = soup.find_all('div',class_='ellipsis rank02')
        for i in a :
            print(i.get_text())'''


    def quiz28dataframe(self) -> None:
        dict = self.quiz24zip()
        df = pd.DataFrame.from_dict(dict, orient='index')
        print(df)
        df.to_csv('./save/bugs.csv', sep=',', na_rep='NaN')



    def quiz29(self) -> str: return None


