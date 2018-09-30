
#题目描述
#有 n 个学生站成一排，每个学生有一个能力值，牛牛想从这 n 个学生中按照顺序选取 k 名学生，要求相邻两个学生的位置编号的差不超过 d，使得这 k 个学生的能力值的乘积最大，你能返回最大的乘积吗？
#输入描述:
#   每个输入包含 1 个测试用例。每个测试数据的第一行包含一个整数 n (1 <= n <= 50)，
#   表示学生的个数，接下来的一行，包含 n 个整数，
#   按顺序表示每个学生的能力值 ai（-50 <= ai <= 50）。
#   接下来的一行包含两个整数，k 和 d (1 <= k <= 10, 1 <= d <= 50)。

 
n=input('n:')
q=input('q:').split() 
kd=input('kd:').split()
      
i=0
a1 = 0
a2 = 0
a3 = 0
b1 = 0
b2 = 0
b3 = 0 

 

while i < int(n)-int(kd[0]):

    while j < int(n)-int(kd[0])+1:
        if j-i >= int(kd[50]):
            break
        while k < int(n)-int(kd[0])+2:
            if kd-j >= int(kd[50]):
                break
            a = (int(q[i]),int(q[j]),int(q[k]))
            b.append(a)
 


