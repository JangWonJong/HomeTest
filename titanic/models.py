from icecream import ic
from context.domains import Dataset
from context.models import Model

class TitanicModel(object):
    model = Model()
    dataset = Dataset()


    def preprocess(self,train_fname,test_fname):
        this = self.dataset
        that = self.model
        this.train = that.new_dframe(train_fname)
        this.test = that.new_dframe(test_fname)
        # id 추출
        this.id = this.test['PassengerId']
        this.label = this.train['Survived']
        this.train = this.train.drop('Survived', axis=1)
        this = self.drop_feature(this,'Cabin','Ticket','Parch','SibSp')

        '''
        this = self.create_this(self.dataset)
        this = self.name_nominal(this)
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
        for i in feature:
            this.train = this.train.drop(i,axis =1)
            this.test = this.test.drop(i, axis=1)

        '''self.cabin_garbage(df)
        self.ticket_garbage(df)
        self.parch_garbage(df)
        self.sibsp_garbage(df)'''
        return this



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