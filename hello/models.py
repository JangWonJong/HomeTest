import random
def main():
    q8 = Quiz08Rps(int(input('가위바위보'))) # 가위 1 바위 2 보 3
    print(f'나의 값 : {q8.user} 컴퓨터의 값 : {q8.com} 결과 : {q8.game()}')


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
        if u == 1:
            if c == 1:
                res = f'플레이어 : {rps[0]}, 컴퓨터 : {rps[0]}, 결과 패배'
            elif c == 2:
                res = f'플레이어 : {rps[0]}, 컴퓨터 : {rps[1]}, 결과 승리'
            elif c == 3:
                res = f'플레이어 : {rps[0]}, 컴퓨터 : {rps[2]}, 결과 무승부'
        if u == 2:
            if c == 1:
                res = f'플레이어 : {rps[1]}, 컴퓨터 : {rps[0]}, 결과 패배'
            elif c == 2:
                res = f'플레이어 : {rps[1]}, 컴퓨터 : {rps[1]}, 결과 승리'
            elif c == 3:
                res = f'플레이어 : {rps[1]}, 컴퓨터 : {rps[2]}, 결과 무승부'
        if u == 3:
            if c == 1:
                res = f'플레이어 : {rps[2]}, 컴퓨터 : {rps[0]}, 결과 패배'
            elif c == 2:
                res = f'플레이어 : {rps[2]}, 컴퓨터 : {rps[1]}, 결과 승리'
            elif c == 3:
                res = f'플레이어 : {rps[2]}, 컴퓨터 : {rps[2]}, 결과 무승부'

            return res




class Quiz09GetPrime(object):
    def __init__(self):
        pass

class Quiz10LeapYear(object):
    def __init__(self):
        pass

class Quiz11NumberGolf(object):
    def __init__(self):
        pass

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
