#Makeeva Angelina 85%
#Kareva Alena 70%
#Osokina Nastya 90%


import datetime
import ru_local as ru
########

cost = 0

def name_quest ():
  print(ru.HELLO)
  name = input()
  print(ru.NICE, name)

def  money_in_russia_quest():
  print(ru.MINR)
  answer_mirq = input()
  if answer_mirq.lower() == ru.NO:
      print(ru.GOODDAY)
  return answer_mirq

def res():
  cost = 0
  print(ru.SELF)
  ans_7 = input()
  if ans_7.lower == ru.YES:
    print(ru.GOODDAY)
  if ans_7.lower() == ru.NO:

    print(ru.GIFTAD)
    ans_8 = input()
    if ans_8.lower() == ru.YES:
      print(ru.SUM4)
      ans_9 = input()
      if ans_9.lower() == ru.YES:
        print(ru.WRITESUM)
        vg = input()
        cost += (int(vg) - 4000) * 0.35
      elif ans_9.lower() == ru.NO:
        print(ru.NINAD)
    if ans_8.lower() == ru.NO:
      print(ru.SECOND)

    print(ru.REALTY)
    ans_10 = input()
    if ans_10.lower() == ru.YES:
      print(ru.NREALTY)
      ans_11 = input()
      if ans_11.lower() == ru.LIV:
        print(ru.CTREALTY)
        ct = input()
        cost += (int(ct)-1000000) * 0.13
      if ans_11.lower() == ru.UNLIV:
        print(ru.REALTYYEAR)
        ans_12 = input()
        if ans_12.lower() == ru.YES:
          print(ru.NCTREALTY)
          ctn = input()
          cost += (int(ct)-250000) * 0.13
        if ans_12.lower() == ru.NO:
          print(ru.SECOND)
    if ans_10.lower == ru.NO:
      print(ru.SECOND)

    print(ru.ZB)
    ans_13 = input()
    if ans_13.lower() == ru.YES:
      print(ru.SUMZB)
      zb = int(input())
      if zb >= 5000000:
        cost += zb * 0.15
      elif zb < 5000000:
        cost += zb * 0.13
    if ans_13.lower() == ru.NO:
      print(ru.SECOND)

    print(ru.RENT)
    ans_14 = input()
    if ans_14.lower() == ru.YES:
      print(ru.CTRENT)
      ans_15 = int(input())
      cost += ans_15 * 0.13
    print(ru.ZP)
    zp = int(input())
    if zp * 12 >= 5000000:
      cost += (zp * 12) * 0.15
    elif zp * 12 < 5000000:
      cost += (zp * 12) * 0.13
  print(ru.NDFL, cost)

def live_in_russia_quest(answer_mirq):
  cost = 0
  if answer_mirq.lower() == ru.YES:
    print(ru.LIVEINR)
    ans_1 = input()
    if ans_1.lower() == ru.YES:
      res()

    elif ans_1.lower() == ru.NO:
      current_date = datetime.datetime.now()
      print(ru.DATEINR)
      day1, month1, year1 = map(int, input().split('.'))
      lastday_date1 = datetime.datetime(year1, month1, day1)
      need_days = datetime.timedelta(days = 183)
      result = current_date - need_days
      day = lastday_date1 - result
      print ((current_date - lastday_date1).days)
      if (current_date - lastday_date1).days > 183:
        print(ru.WHYABS)
        ans_2 = input()
        if ans_2.lower() == ru.YES:
         res()
        if ans_2.lower() == ru.NO:
          print(ru.REASONS)
          ans_3 = input()
          if ans_3.lower() == ru.YES:
            print(ru.ZP)
          zp = int(input())
          cost += zp * 12
          if ans_3.lower() == ru.NO:
            cost = cost + 0
          print(ru.DIVIDEND)
          ans_4 = input()
          if ans_4.lower() == ru.YES:
            cost += cost * 0.15
          if ans_4.lower() == ru.NO:
            cost += cost * 0.30
          print(ru.RENT)
          ans_5 = input()
          if ans_5.lower() == ru.YES:
            print(ru.CTRENT)
            ans_6 = input()
            cost += ans_6 * 0.3
          print(ru.NDFL, cost)
########

name_quest()
answer = money_in_russia_quest()
live_in_russia_quest(answer)
