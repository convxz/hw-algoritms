def naive_search_substr(s1: str, s2: str) -> bool:
    """
    возвращает True, если строка s1 содержит в себе строку s2, иначе False
    s1: str - строка в которой происхолит поиск s2
    s2: str - строка, которую ищем в s1
    return: bool - True, если строка s1 содержит в себе строку s2, иначе False
    """
    len_s1 = len(s1)
    len_s2 = len(s2)
    min_len = min(len_s1, len_s2)
    for i in range(min_len):
        if s1[i:min_len-1] == s2:
            return True
    return False


if __name__ == "__main__":
    print(naive_search_substr("домашнее по алгоритмам", "домашнее"))
