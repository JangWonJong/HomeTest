from domains import Member
from domains import my100, myRandom, members

class Quiz00:
    def quiz00calculator(self)-> float:
        a = my100()
        b = my100()
        opcode = ['+','-','*','/']
        ran = opcode[myRandom(0,3)]
        if ran=='+': res = a + b
        elif ran=='-': res = a - b
        elif ran=='*': res = a * b
        elif ran=='/' : res = a / b
        print(f' 출력값: {a} {ran} {b} = {res}')

        return None

    def quiz01bmi(self)-> float :
        this = Member()
        m = members[myRandom(0,23)]
        w = myRandom(40,100)
        h = myRandom(140,200)
        bmi = w / (h * h) * 10000

        if bmi >= 35:
            res = f'고도비만'
        elif bmi >= 29.9:
            res = f'중도 비만 (2단계 비만)'
        elif bmi >= 24.9:
            res = f'경도 비만 (1단계 비만)'
        elif bmi >= 22.9:
            res = f'과체중'
        elif bmi >= 22.9:
            res = f'정상'
        else:
            res = f'저체중'

        print(f'이름 : {m}, 키 : {h}, 몸무게 : {w}, BMI 상태 : {res}')
        return None

    def quiz02dice(self)->int:
        res = myRandom(1,6)
        print(f'주사위 결과는 {res}입니다')

    def quiz03rps(self)->int:
        c = myRandom(0,2)
        u = myRandom(0,2)
        r = u - c
        # 1 가위 2 바위 3 보
        rps = ['가위', '바위', '보']
        if r == 0:
            res = f'플레이어: {rps[u]} ㅣ 컴퓨터: {rps[c]} ☞ 무승부'
        elif r == -1 or r == 2:
            res = f'플레이어: {rps[u]} ㅣ 컴퓨터: {rps[c]} ☞ 패배'
        elif r == 1 or r == -2:
            res = f'플레이어: {rps[u]} ㅣ 컴퓨터: {rps[c]} ☞ 승리'

        print(f'{res}')
        return None

    def quiz04leap(self)->int:
        year = myRandom(0,3000)
        if year % 4 == 0 and year % 100 == 0 or year % 400 == 0:
            res = '윤년'
        else:
            res = '평년'

        print(f'{year}년은 {res}입니다')

    def quiz05grade(self)->float:
        m = members[myRandom(0,23)]
        kor = myRandom(0,100)
        eng = myRandom(0,100)
        math = myRandom(0,100)
        total = kor+eng+math
        avg = total/3
        #grade = ['A','B','C','D','E','F']
        if avg >= 60 :
            res = '합격'
        else:
            res = '불합격'

        print(f'{m}의 언어점수 : {kor} 영어점수 : {eng} 수학점수 : {math}\n'
              f'총점 : {total}\n평균 : {avg}\n합격여부 : {res}')

    def quiz06memberChoice(self)->float:
        res = members[myRandom(0,23)]
        print(f'당첨된 학생은 {res}입니다')