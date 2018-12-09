def namechecker(name):
    if "성준" in name:
        print("혹시 조교수님?")
    elif "글경" in name:
        print("글경관계자세요?")
    elif "cloud" in name:
        print("운한이니?")
    elif ("가천" in name) or ("교수" in name):
        print("아이쿠야!")
    else:
        print("누구...?")

namechecker((input("이름을 밝히시오    ")))