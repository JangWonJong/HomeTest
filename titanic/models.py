from icecream import ic
from context.domains import Dataset
from context.models import Model

class TitanicModel(object):
    model = Model()
    dataset = Dataset()

    def __init__(self, train_fname, test_fname):
        self.train = self.model.new_model(train_fname)
        self.test = self.model.new_model(test_fname)
        # id 추출
        ic(f'트레인 컬럼 {self.train.columns}')
        ic(f'트레인 헤드 {self.train.head()}')
        ic(self.train)

    def preprocess(self):
        df = self.train
        df = self.drop_feature(df)
        df = self.name_nominal(df)
        df = self.embark_nominal(df)
        df = self.pclass_nominal(df)
        df = self.sex_nominal(df)
        df = self.age_ratio(df)
        df = self.fare_ratio(df)
        df = self.create_train(df)
        df = self.create_label(df)
        return df

    def drop_feature(self,df)->object:#필요없는 feature들을 날림 garbage제거

        '''self.cabin_garbage(df)
        self.ticket_garbage(df)
        self.parch_garbage(df)
        self.sibsp_garbage(df)'''
        return df

    @staticmethod
    def create_label(df)->object:

        return df

    @staticmethod
    def create_train(df)->object:

        return df

    '''
    Categorical vs Quantitative
    Cate -> nominal(이름) vs ordinal(순서)
    Qaun -> interval(상대) vs ratio(절대)
    '''

    @staticmethod
    def pclass_nominal(df)->object:

        return df

    @staticmethod
    def name_nominal(df) -> object:#name에서 추출할 것이 있음

        return df

    @staticmethod
    def sex_nominal(df)-> object:

        return df
    @staticmethod
    def age_ratio(df)->object:
        return df

    @staticmethod
    def fare_ratio(df)-> object:

        return df

    @staticmethod
    def cabin_garbage(df)-> object:

        return df

    @staticmethod
    def embark_nominal(df)-> object:

        return df