import math

text = "UONCS VAIHG EPAAH IGIRL BIECS TECSW PNITE TIENO IEEFD OWECX TRSRX STTAR TLODY FSOVN EOECO HENIO DAARQ NAELA FSGNO PTE"
input = []
appearance = [0] * 26

# 將文本中的字母提取出來，同時統計每個字母的出現次數
for char in text:
    if char != ' ':
        input.append(char)
        appearance[ord(char) - ord('A')] += 1

length = len(input)
dimension = []
for i in range(2, int(math.sqrt(length)) + 1):
    if length % i == 0:
        dimension.append(i)
        dimension.append(length // i)

vowel = ['A', 'E', 'I', 'O', 'U']
v_percent = [0.0] * len(dimension)
v_count = [[] for _ in range(len(dimension))]

# 計算每個可能維度下的元音分佈情況
for i in range(len(dimension)):
    v_count[i] = [0] * dimension[i]
    for j in range(length):
        for k in range(len(vowel)):
            if input[j] == vowel[k]:
                v_count[i][j % dimension[i]] += 1
                break
    for j in range(len(v_count[i])):
        v_percent[i] += abs(0.4 * length / dimension[i] - v_count[i][j])

# 輸出每個可能維度的結果
for i in range(len(dimension)):
    print(f"{dimension[i]}x{length // dimension[i]} Average diff: {(v_percent[i]/dimension[i]):.2f}")

    rectangle = [['' for _ in range(length // dimension[i])] for _ in range(dimension[i])]
    for j in range(length):
        rectangle[j % dimension[i]][j // dimension[i]] = input[j]
    for j in range(dimension[i]):
        for k in range(length // dimension[i]):
            print(rectangle[j][k], end=' ')
        print(f"\t{v_count[i][j]}\t{abs(0.4 * length / dimension[i] - v_count[i][j]):.1f}")
        
    print()
