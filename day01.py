li = [1,3,4,6,8,9,2,5]
li2 = li.sort()

n = int(input('숫자 입력 : '))

s_index=0
e_index=len(li)-1

while s_index<e_index:
    m_index=(s_index+e_index)//2
    if n < li[m_index]:
        e_index=m_index
    elif n > li[m_index]:
        s_index=m_index
    else:
        print(m_index)
        break

