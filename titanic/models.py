from icecream import ic
from context.domains import Dataset
from context.models import Model

class TitanicModel(object):
    model = Model()
    dataset = Dataset()


    def preprocess(self,train_fname,test_fname):
        this = self.dataset
        that = self.model
        feature = ['PassengerId','Survived','Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked']
        this.train = that.new_dframe(train_fname)
        this.test = that.new_dframe(test_fname)
        # id 추출
        this.id = this.test[feature[0]]
        this.label = this.train[feature[1]]
        this.train = this.train.drop(feature[1], axis=1)
        this = self.drop_feature(this,feature[11],feature[9],feature[8],feature[7])
        #self.kwargs_sample( name= '이순신, ddd, qqq') kwargs 샘플
        this = self.name_nominal(this)

        '''
        this = self.create_this(self.dataset)
        this = self.embark_nominal(this)
        this = self.pclass_nominal(this)
        this = self.sex_nominal(this)
        this = self.age_ratio(this)
        this = self.fare_ratio(this)
        this = self.create_train(this)'''
        self.print_this(this)
        return this

    @staticmethod
    def print_this(this):
        print('*'*100)
        ic(f'1. Train의 타입 {type(this.train)}\n')
        ic(f'2. Train의 컬럼 {(this.train.columns)}\n')
        ic(f'3. Train의 상위1개 {(this.train.head(1))}\n')
        ic(f'4. Train의 null의 개수 {(this.train.isnull().sum())}\n')
        ic(f'5. Test의  타입 {type(this.test)}\n')
        ic(f'6. Test의  컬럼 {(this.test.columns)}\n')
        ic(f'7. Test의  상위1개 {(this.test.head(1))}\n')
        ic(f'8. Test의  null의 개수{(this.test).isnull().sum()}\n')
        ic(f'9. id의 타입{type(this.id)}\n')
        ic(f'11. id의 상위 10개 {this.id[:10]}\n')
        #ic(f'10. id의 상위 10개 {this.id.head(10)}\n')
        print('*'*100)
        return this

    def create_this(self,dataset)-> object:
        this = dataset
        this.train = self.train
        this.test = self.test
        this.id = self.id
        return this

    @staticmethod
    def drop_feature(this,*feature)->object:#필요없는 feature들을 날림 garbage제거
        '''for i in feature:
            this.train = this.train.drop(i,axis =1)
            this.train.drop(i,axis =1, inplace=True)
            this.test = this.test.drop(i, axis=1)'''

        '''for i in [this.train,this.test]:
            for j in feature:
                i.drop(j, axis=1, inplace=True)'''

        [i.drop(j, axis=1, inplace=True) for j in feature for i in [this.train,this.test]]

        '''self.cabin_garbage(df)
        self.ticket_garbage(df)
        self.parch_garbage(df)
        self.sibsp_garbage(df)'''
        return this

    @staticmethod
    def kwargs_sample( **kwargs)->None:
        print(type(kwargs))
        {print([''.join(f'key:{i},val:{j}') for i,j in kwargs.items()])}


    @staticmethod
    def create_train(this)->object:

        return this

    '''
    Categorical vs Quantitative
    Cate -> nominal(이름) vs ordinal(순서)
    Qaun -> interval(상대) vs ratio(절대)
    '''

    @staticmethod
    def pclass_nominal(this)->object:

        return this

    @staticmethod
    def name_nominal(this) -> object:#name에서 추출할 것이 있음
        combine = [this.train, this.test]#dataset의 train과 test를 편집하기위해 list에 받는다
        for dataset in combine:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.',expand=False)
            ic(dataset['Title'])

        return this

    @staticmethod
    def sex_nominal(this)-> object:

        return this
    @staticmethod
    def age_ratio(this)->object:
        return this

    @staticmethod
    def fare_ratio(this)-> object:

        return this

    @staticmethod
    def cabin_garbage(this)-> object:

        return this

    @staticmethod
    def embark_nominal(this)-> object:

        return this