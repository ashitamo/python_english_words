import re

# with open('去空行.txt','r',encoding='utf8') as rq:
#     lines=rq.readlines()
# with open('w.txt','w',encoding='utf8') as rw:
#     for i in lines:
#         if len(i)<=1:
#             pass
#         else:
#             rw.write(i)

# msg="bank (2)n./v.堤；堆積"
# #a=re.search(r"(.*?) (.*?[.])(.*)",msg)
# a=re.search(r"(.*?) (.*[.])(.*)",msg)
# #[0-9]+|[o]|[r][e]+
# print(a.group(1))
# b=re.sub(r'[(].*[)]','',a.group(2))
# print(b)
# print(a.group(3))
# print(a.group(1)+" "+b+" "+a.group(3))

# with open('去空行.txt','r',encoding='utf8') as rq:
#     lines=rq.readlines()
# with open('w.txt','w',encoding='utf8') as rw:
#     for i in lines:
#         a=re.search(r"(.*?) (.*[.])(.*)",i)
#         if a:
#             s1=a.group(1)
#             s2=re.sub(r'[(].*[)]+|[/]','',a.group(2))
#             s3=a.group(3)
#             rw.write(f"{s1} {s2} {s3}\n")

# with open('規格化.txt','r',encoding='utf8') as rq:
#     lines=rq.readlines()
# with open('w.txt','w',encoding='utf8') as rw:
#     for i in lines:
#         a=re.search('(.*?) (.*?) (.*)',i)
#         s1=re.sub('[/]',";",a.group(1))
#         s2=a.group(2)
#         s3=re.sub('[/]',";",a.group(3))
#         rw.write(f"{s1} {s2} {s3}\n")


# a=
# b=
# c=
# d=
# e=
# f=
# g=
# h=
# i=
# j=
# k=
# l=
# m=
# n=
# o=
# p=
# q=
# r=
# s=
# t=
# u=
# v=
# w=
# x=
# y=
# z=

# lis=['a*'][]
# n=0
# with open('原檔.txt','r',encoding='utf8') as rq:
#     line1=rq.readlines()
# with open('w.txt','r',encoding='utf8') as rq: 
#     line2=rq.readlines()
# for i in range(0,len(line1),1):
#     if line1[i] != line2[i+n]:
#         n
#         print(f'{line1[i]}  {line2[i]} {i}')
#         #break
        
# # 
#     for i in sorted(lines):
#         rw.writelines(i)
#         # for 
        # if i[0][1]=='*a' or i[0]=='a' or i[0][1]=='*A' or i[0]=='A':
# with open('./words/1.txt','r',encoding='utf8') as rq:
#     lines=rq.readlines()
# print(lines[0].count(' '))
# s="xdwwdwdwdwdwd"
# print(s[1:])
with open('./words/1.txt','r',encoding='utf8') as rq:
            lines=rq.readlines()
for i in range(0,len(lines),1):
        #a=re.search('(.*)#(.*?)',lines[i])
        wordlist=lines[i].split('#')
        print(wordlist)

# with open('w.txt','w',encoding='utf8') as rw:
#     for w in range(97, 123):
#         for i in lines:
#             x=re.match(r'[*]'+chr(w-32),i)
#             y=re.match(chr(w-32),i)
#             z=re.match(r'[*]'+chr(w),i)
#             n=re.match(chr(w),i)
#             if x or y or z or n:
#                 rw.write(i)
            # if i[0]+i[1]=='*'+chr(w-32) or i[0]==chr(w-32) or i[0]==chr(w) or i[0]+i[1]=='*'+chr(w):
            #     rw.write(i)
            #     print(chr(w-32))
            #     print(chr(w))
            