Makeeva Angelina 85%
Kareva Alena
Osokina Nastya


import datetime
########

def name_quest ():
  print('Здравствуйте, как вас зовут?')
  name = input()
  print('Очень приятно,', name)

def  money_in_russia_quest():
  print('Вы получаете деньги в России?')
  answer_mirq = input()
  if answer_mirq.lower() == 'нет':
      print('Хорошего дня')
  return answer_mirq


def live_in_russia_quest(answer_mirq):
  cost = 0
  if answer_mirq.lower() == "да":
    print('На данный момент вы живёте в России?')
    ans_1 = input()
    if ans_1.lower() == 'да':
      print('ok')
    elif ans_1.lower() == 'нет':
      current_date = datetime.datetime.now()
      print('В какую дату вы последний раз были в России?')
      day1, month1, year1 = map(int, input().split('.'))
      lastday_date1 = datetime.datetime(year1, month1, day1)
      need_days = datetime.timedelta(days = 183)
      result = current_date - need_days
      day = lastday_date1 - result
      print ((current_date - lastday_date1).days)
      if (current_date - lastday_date1).days > 183:
        print('Вы отсутствовали из-за болезни, обучения, военной службы? ')
        ans_2 = input()
        if ans_2.lower() == 'да':
         print('resident')
        if ans_2.lower() == 'нет':
          print('Вы \n 1)получаете доход по патенту на работу в РФ \n 2)высококвалифицированный специалист \n 3) переселившийся по госпрограмме в РФ \n 4)член экипажей российских судов \n 5)беженец \n 6)гражданин любой из стран ЕАЭС, которые работают по трудовому договру')
          ans_3 = input()
          if ans_3.lower() == 'да':
            print('Сколько вы зарабатываете?')
          zp = input()
          cost += int(zp)
          if ans_3.lower() == 'нет':
            cost = cost + 0
          print('Вы получаете дивиденты?')
          ans_4 = input()
          if ans_4.lower() == 'да':
            cost = cost * 0.15
          if ans_4.lower() == 'нет':
            cost = cost * 0.30
      print('Вы сдаете квартиру?')
      ans_5 = input()
      if ans_5.lower() == 'да':
        print('Сколько стоит?')
        ans_6 = input()
        ans_6 = ans_6 * 0.3
########

name_quest()
answer = money_in_russia_quest()
live_in_russia_quest(answer)