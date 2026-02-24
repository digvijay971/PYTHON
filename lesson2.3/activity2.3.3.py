num = int(input("give a amstrong number nowwwwwwwwwwww!!!!!!!!!!!!! "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //=10
if num == sum:
    print(num ,"is an amstrong number")
else:
    print(num ,"is not amstrong number")