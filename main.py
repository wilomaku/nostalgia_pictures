from funcs import funcs_text as ft

def main():

    t1 = 'This is a example'
    t2 = 'Hello world'
    t3 = 'This is a world'
    t4 = 'world and example'

    score_sim = ft.match_text_text(t1, t2)
    print(score_sim)
    score_sim = ft.match_text_text(t1, t3)
    print(score_sim)
    score_sim = ft.match_text_text(t2, t3)
    print(score_sim)

    score_sim = ft.match_text_text(t4, t1)
    print(score_sim)
    score_sim = ft.match_text_text(t4, t2)
    print(score_sim)

main()
