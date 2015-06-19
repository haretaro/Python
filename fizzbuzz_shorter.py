for x in range(1,101):print('Fizz'*(x%3==0)+'Buzz'*(x%5==0) or x) # 'hoge' * True = 'hoge', 'hoge' * False = '', '' or 'piyo' = 'piyo', 'hoge' or 'piyo' = 'hoge'
