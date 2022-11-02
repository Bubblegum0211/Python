#8-8
def make_album():
    active = True
    while active:
        test = {}
        geshou=input("歌手")
        zhuanji=input('专辑')
        geqvshu=input('歌曲数目')
        test['歌手'] = geshou
        test['专辑'] = zhuanji
        test['歌曲数'] = geqvshu
        print(test)
        tuichu=input("是否离开？（yes/no）")
        if tuichu == 'yes':
            active = False
make_album()