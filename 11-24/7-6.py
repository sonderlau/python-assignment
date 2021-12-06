import datetime
nums = input()

age =   datetime.datetime.now().year-int(nums[6:10])
sex = "男" if int(nums[16] )% 2 != 0 else "女"

print("你出生于{}年{}月{}日".format(nums[6:10], nums[10:12], nums[12:14]))
print("你今年{}周岁".format(age))
print("你的性别为{}".format(sex))