from icecream import ic
from context.domains import Dataset
from context.models import Model

class TitanicModel(object):
    def __init__(self, train_fname, test_fname):
        self.model = Model()
        self.dataset = Dataset()
        self.train = self.model.new_model(train_fname)
        self.test = self.model.new_model(test_fname)
        # id 추출
        ic(f'트레인 컬럼 {self.train.columns}')
        ic(f'트레인 헤드 {self.train.head()}')
        ic(self.train)

    def preprocess(self):
        self.sibsp_garbage()
        self.parch_garbage()
        self.ticket_garbage()
        self.cabin_garbage()
        self.name_nominal()
        self.embark_nominal()
        self.pclass_nominal()
        self.sex_nominal()
        self.age_ratio()
        self.fare_ratio()
        self.create_train()
        self.create_label()


    def create_label(self)->object:
        pass

    def create_train(self)->object:
        pass
    def drop_feature(self)->object:#필요없는 feature들을 날림 garbage제거ㅏ
        pass
    '''
    Categorical vs Quantitative
    Cate -> nominal(이름) vs ordinal(순서)
    Qaun -> interval(상대) vs ratio(절대)
    '''
    def pclass_nominal(self)->object:
        pass
    def name_nominal(self) -> object:#name에서 추출할 것이 있음
        pass
    def sex_nominal(self)-> object:
        pass
    def age_ratio(self)-> object:
        pass
    def sibsp_garbage(self)-> object:
        pass
    def parch_garbage(self)-> object:
        pass
    def ticket_garbage(self)-> object:
        pass
    def fare_ratio(self)-> object:
        pass
    def cabin_garbage(self)-> object:
        pass
    def embark_nominal(self)-> object:
        pass