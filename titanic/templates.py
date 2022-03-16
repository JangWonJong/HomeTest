from context.domains import Dataset
from context.models import Model
from titanic.models import TitanicModel
from icecream import ic
import matplotlib.pyplot as plt
'''
데이터 시각화
엔티티(개체)를 차트로 표현하는 것

모든 feature를 다 그려야 하지만, 시간 관게상
survived, pclass, sex, embarked의 4개만 그리겠습니다.
템플릿 메소드 패턴으로 구성하시오
'''
class TitanicTemplate(object):
    model = Model()
    dataset = Dataset()

    def __init__(self,fname):
        self.entity = self.model.new_model(fname)
        self.titanic = TitanicModel('train.csv','test.csv')

    def draw_survied_dead(self):
        this = self.entity
        self.survived()
        self.pclass()
        self.sex()
        self.embarked()
        ic(f'트레인의 타입 : {type(this.train)}')
        ic(f'트레인의 컬럼 : {this.train}')
        ic(f'트레인의 상위5행 : {this.train}')
        ic(f'트레인의 하위5행 : {this.train}')
        f, ax = plt.subplots(1,2, figsize=(18, 8))
        this['Survived']
        plt.show()

    @staticmethod
    def survived():
        pass

    @staticmethod
    def pclass():
        pass

    @staticmethod
    def sex():
        pass

    @staticmethod
    def embarked():
        pass