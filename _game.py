import os
import sys
import random
import operator
import collections

class Skill:
    _id = None
    _skill = None
    _skill_name = ['일반 스킬', '강화 스킬', '지속 스킬', '방어 스킬']
    _skill_prop = []
    _skill_stats = [95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105]

    def __init__(self, id, _property_, _property):
        self._id = id
        default = _property_
        count = 0
        for i in _property:
            if int(i) != 0:
                for j in range(1, i+1):
                    self._skill_prop.append(default[count])
            count += 1
     
        _skill = collections.namedtuple('Skill', 'name property stats')
        self._skill = _skill(name=(random.sample(self._skill_name, 1)[0]), property=(random.sample(self._skill_prop, 1)[0]), stats=(random.sample(self._skill_stats, 1)[0]))

    def view_skill_detail(self):
        print('스킬명: ', self._skill.name)
        print('스킬 속성: ', self._skill.property)
        print("스킬 데미지: %s" % (str(self._skill.stats) + '%'))

class Card:
    _id = None
    _level = 0
    _name = "이름"
    _property_ = ['불', '물', '대지', '바람', '전기']
    _property = [0, 0, 0, 0, 0] # 불, 물, 대지, 바람, 전기
    _skill = [None, None, None, None]
    _skill_point = 0
    _depende_property = 0

    def __init__(self):
        while True:
            total = 10
            for i in range(0, 5):
                if total != 0:
                    up = random.randint(0, 6)
                    if up <= total:
                        total -= up
                        self._property[i] = up
                    else:
                        break
                else:
                    break
            total = 0
            for i in range(0, 5):
                total += self._property[i]
            if total != 10:
                continue
            else:
                break
        index, value = max(enumerate(self._property), key=operator.itemgetter(1))
        self._depende_property = self._property_[index]
        self._skill[0] = Skill(0, self._property_, self._property)

    def view_card_detail(self, id):
        self._skill[id].view_skill_detail()

    def add_skill(self):
        if self._skill_point > 2:
            print("더 이상 스킬을 추가 할 수 없습니다.")
        else:
            self._skill_point += 1
            self._skill[self._skill_point] = Skill(self._skill_point, self._property_, self._property)

if __name__ == "__main__":
    c = Card()
    clear = lambda: os.system('cls')
    while True:
        print("게임 셋팅")
        print("1. 카드 상세 확인")
        print("2. 스킬 상세 확인")
        print("3. 스킬 추가 확인")
        print("4. 종료")
        try:
            num = int(input("입력: "))
        except:
            clear()
            continue

        if num == 1:
            count = 0
            print("레벨:",c._level)
            print("카드 이름:",c._name)
            print("***카드 능력치***")
            for i in c._property:
                if count == 0:
                    print("불 속성:",i)
                    count+=1
                elif count == 1:
                    print("물 속성:",i)
                    count+=1
                elif count == 2:
                    print("대지 속성:",i)
                    count+=1
                elif count == 3:
                    print("바람 속성:",i)
                    count+=1
                elif count == 4:
                    print("전기 속성:",i)
                    count+=1
            count = 0
            print("카드 방어 능력:",c._depende_property)
            print("******스킬******")
            for i in c._skill:
                if i != None:
                    print("ID:", count+1)
                    c.view_card_detail(count)
                    count+=1
            tmp = input("아무 값을 입력하면 원래 화면으로 넘어갑니다.")
            clear()
        elif num == 2:
            try:
                tmp = int(input("몇번 스킬을 확인하겠습니까?"))
                c.view_card_detail(tmp-1)
            except AttributeError:
                print("존재하지 않는 번호입니다.")
            tmp2 = input("아무 값을 입력하면 원래 화면으로 넘어갑니다.")
            clear()
            continue
        elif num == 3:
            c.add_skill()
            tmp = input("아무 값을 입력하면 원래 화면으로 넘어갑니다.")
            clear()
        elif num == 4:
            sys.exit(1)
        
            