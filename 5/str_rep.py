def str_rep(num):
  dic={'1':'One','2':'Two', '3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine','0':'Zero'}
  for i in num:
    for j in dic.keys():
      if i==j:
        print(dic[j],"",end="")

num=input("Enter a number:")
str_rep(num)