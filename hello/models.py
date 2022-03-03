import random

def main():
    """업다운
        컴퓨터가 정해주는 1-100까지의 랜덤한 수 한 개를 맞추시오? """

class NumberGolf(object):
    def __init__(self, user):
            self.user = user
            self.computer = random.randint(1, 100)
            a = NumberGolf(input('업다운'))
            print(f'사용자 입력값 : {a.user}  업다운? : {a.updown()}')

    def updown(self):
        u = self.user
        c = self.computer
        while 1:
            if u == c:
                res = f'정답입니다'
            elif u > c:
                res = f'다운'
            elif c < u:
                res = f'업'
            return res





    """q8 = Quiz08Rps(int(input('가위바위보'))) # 가위 1 바위 2 보 3
    print(f'나의 값 : {q8.user} 컴퓨터의 값 : {q8.com} 결과 : {q8.game()}')
    #user가 3일 때  값만 정상으로 나옴
    #ㄴㄴ 정상적으로 나옴
    #입력창(콘솔에 주느값은 String값이 아닌 Int값임 확인하셈
def myRandom(start, end):
    return random.randint(start, end)

class Quiz05Dice(object):
    @staticmethod
    def cast():
        return myRandom(1,6)

class Quiz08Rps(object):
    def __init__(self, user):
        self.user = user
        self.com = myRandom(1,3)

    def game(self):
        c = self.com
        u = self.user
        # 1 가위 2 바위 3 보
        rps = ['가위', '바위', '보']

        if u - c == 0:
               res = f'플레이어 : {rps[u]}, 컴퓨터 : {rps[c]}, 결과 무승부'
        elif u - c == -1 or u - c == 2:
               res = f'플레이어 : {rps[u]}, 컴퓨터 : {rps[c]}, 결과 패배'
        else:
               res = f'플레이어 : {rps[u]}, 컴퓨터 : {rps[c]}, 결과 승리'
        return res








class Quiz09GetPrime(object):
    def __init__(self):
        pass



'''윤년은 4년마다 돌아오는데 100년으로 나누어 떨어지면 평년
     * but 400년으로 나누어 떨어지면 윤년
     * ex) 2020, 2024, 2028 => 윤년
     *     2100, 2200, 2300 => 평년
     *     2000, 2400, 2800 => 윤년
     *     조건이 참일 경우 윤년 아닐 경우 평년'''

class Quiz10LeapYear(object):
    def __init__(self, year):
        self.year = year

    def leapyear(self):
        a = self.year
        if a%4==0 and a%100==0 or a%400==0:
            return '윤년'
        else:
            return '평년'"""







class Quiz12Lotto(object):
    def __init__(self):
        pass

class Quiz13Bank(object): # 이름, 입금, 출금만 구현
    def __init__(self):
        pass

class Quiz14Gugudan(object): # 책받침구구단
    def __init__(self):
        pass

if __name__ == '__main__':
    main()
