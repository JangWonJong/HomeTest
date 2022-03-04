from domains import Member
from domains import my100, myRandom, myMember

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
        members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                        "권혜민", "서성민", "조현국", "김한슬", "김진영",
                        '심민혜', '권솔이', '김지혜', '하진희', '최은아',
                        '최민서', '한성수', '김윤섭', '김승현',
                        "강 민", "최건일", "유재혁", "김아름", "장원종"]
        m = members[myMember(0,23)]
        w = this.weight[myRandom(40,100)]
        h = this.height[myRandom(140,200)]
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

