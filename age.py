drive = input('你有沒有開過車？：')
if drive != '有' and drive != '沒有' :
    print('只能輸入有或是沒有')
    raise SystemExit

age = input('請問您的年齡為？：')
age = float(age)

if drive == '有' :
    if age >= 18 :
        print('很好！你有考駕照且沒有違法')
    else :
        print('奇怪你怎麼有開過車')

if drive == '沒有' :
    if age >= 18 :
        print('那你可以趕快去考個駕照了！')
    else :
        print('再等幾年就可以考駕照了！')
