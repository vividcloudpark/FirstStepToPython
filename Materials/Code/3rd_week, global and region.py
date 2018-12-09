def test_a():
    try:
        print(tutor)
    except:
        print("no tutor!")
        pass
    return

def test_b(tutor):
    try:
        print(tutor)
    except:
        print("no tutor!")
        pass
    return



if __name__ == "__main__":
    tutor = 'cloud'
    professor = '조성준교수님'
    test_a()
    test_b(tutor)
    print("1번째 test_b 완료")
    test_b(professor)
    print("2번째 test_b 완료")

