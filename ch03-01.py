kakao = []
kakao.append("다현0")
kakao.append("다현1")
kakao.append("다현2")
kakao.append("다현3")
kakao.append("다현4")
print(kakao)
kakao.append(kakao[4])
print(kakao)
kakao[4] = kakao[3]
print(kakao)
kakao[3] = kakao[2]
print(kakao)
kakao[2] = "삽입"
print(kakao)