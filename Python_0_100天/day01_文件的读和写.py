"""
文件读和写详解
"""
# with open('f.txt','r',encoding='utf-8') as f:
#     for line in f:
#         print(line)  # 每读取一行便释放已读1内容，针对文件内容较大的情况

"""
count = 0
with open('f.txt','r',encoding='utf-8') as f:
    for line in f:  # 逐行读取，每读取一行便释放已读1内容，针对文件内容较大的情况
        if count==9:
            print('------我是分隔符-------')
            count +=1
            continue
        print(line)
        count +=1  #打印分隔符
        
# """
# f.tell()  # 返回当前打印的位置，即索引位置
# f.seek(n)  # 回到当前n位置开始向后打印
#
#
# # 二进制写入文件,注意wb ， encode（）
# with open('yesterday','wb') as f:
#     f.write("hello python".encode())
