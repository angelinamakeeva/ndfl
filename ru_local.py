import datetime
cost = 0
print('Здравствуйте, как вас зовут?')
name = input()
print('Очень приятно,', name)
print('Вы получаете деньги в России?')
ans = input()
if ans == 'нет':
    print('Хорошего дня')
if ans == 'да':
    print('На данный момент вы живёте в России?')
    ans_1 = input()
    if ans_1 == 'нет':
      print('Напомните, какое сегодня число?')
      day, month, year = map(int, input().split())
      print('Какого числа вы последний раз были в России?')
      day1, month1, year1 = map(int, input().split())
      current_date = datetime.datetime(year, month, day)
      current_date1 = datetime.datetime(year1, month1, day1)
      need_days = datetime.timedelta(days = 183)
      result = current_date - need_days
      day = current_date1 - result
      if abs(day) > 183:
        print('Вы отсутствовали из-за болезни, обучения, военной службы? ')
        ans_2 = input()
        if ans_2 == 'да':
          ans_10()
        if ans_2 == 'нет':
          print('Вы \n 1)получаете доход по патенту на работу в РФ \n 2)высококвалифицированный специалист \n 3) переселившийся по госпрограмме в РФ \n 4)член экипажей российских судов \n 5)беженец \n 6)гражданин любой из стран ЕАЭС, которые работают по трудовому договру')
          ans_3 = input()
          if ans_3 == 'да':
            print('Сеолько вы зарабатываете?')
            функция def
          if ans_3 == 'нет':
            cost = cost + 0
          print('Вы получаете дивиденты?')
          ans_4 = input()
          if ans_4 == 'да':
            функция def *15
          if ans_4 == 'нет':
            функция def * 30
      print('Вы сдаете квартиру?')
      ans_5 = input()
      if ans_5 == 'да':
        print('Сколько стоит?')
        ans_6 = input()
        ans_6 = ans_6 * 0.3

      else:
        anser_10()

    if ans_1 == 'да':