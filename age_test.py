age = input('請輸入您的年齡：')
drink = input('請問你有喝過酒嗎：')
age = int(age)
if drink != '有' and drink != '沒有':
    print('請輸入 有/沒有！')
    raise SystemExit

if drink == '有':
    if age <= 18: 
        print('未成年請勿喝酒！')
    else:
        print('通過測驗')

elif drink == '沒有':
    if age <= 18:
        print('很好！乖小孩！')
    else :
        print('成年人果然還是少喝比較好！')