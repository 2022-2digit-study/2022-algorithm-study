def solution(progresses, speeds):
    m_list = []
    for i, j in zip(progresses, speeds):
        val = divmod(100 - i, j)
        if val[1] > 0:
            val = val[0] + 1
            m_list.append(val)
        else:
            m_list.append(val[0])
    answer = []
    cnt = 1
    flag = m_list[0]
    for i in range(1, len(m_list)):
        print(flag, m_list[i])
        if flag >= m_list[i]:
            cnt += 1
        else:
            answer.append(cnt)
            flag = m_list[i]
            cnt = 1
    answer.append(cnt)

    return answer
