#https://github.com/datasciencedojo/datasets/blob/master/titanic.csv
from titanic.models import TitanicModel
from titanic.templates import TitanicTemplate
from titanic.views import TitanicView
if __name__ == '__main__':
    view = TitanicView()

    while 1:
        menu = input('1.전처리 2.템플릿')
        if menu == '1':
            print(' #### 1. 전처리 #### ')
            model = TitanicModel('train.csv','test.csv')
            # view.preprocess('train.csv','test.csv')

        elif menu == '2':
            print('#### 2. 템플릿 ####')
            template = TitanicTemplate()
            break