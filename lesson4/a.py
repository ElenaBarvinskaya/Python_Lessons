
time = input('Пожалуйста, введите время в формате "часы : минуты": ')
t2 = time.split()
am = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11']
am = {'00':'12',
      '01':'1',
      '02':'2',
      '03':'3',
      '04':'4',
      '05':'5',
      '06':'6',
      '07':'7',
      '08':'8',
      '09':'9',
      '10':'10',
      '11':'11'}
pm = ['12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
pm = {'12':'12',
      '13':'1',
      '14':'2',
      '15':'3',
      '16':'4',
      '17':'5',
      '18':'6',
      '19':'7',
      '20':'8',
      '21':'9',
      '22':'10',
      '23':'11'}
for x in am:
    for y in pm:
        if t2[0] == x:
            t2[0] = am[x]
            t2.append(' am')
        elif t2[0] == y:
            t2[0] = pm[y]
            t2.append(' pm')
time = " ".join(t2)
print(time)