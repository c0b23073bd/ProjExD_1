import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2= pg.transform.flip(bg_img, True, False)##7
    kk_img = pg.image.load("fig/3.png")##2
    kk_img = pg.transform.flip(kk_img, True, False)##2
    kk_rct = kk_img.get_rect()######8-1
    kk_rct.center = 300, 200 #####8-2
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()####8-3
        if key_lst[pg.K_UP]:  # 上矢印キーがTrueなら
            kk_rct.move_ip((0, -1))  # こうかとんの縦座標を-1する
        if key_lst[pg.K_DOWN]:  # 下矢印キーがTrueなら
            kk_rct.move_ip((0, +1))  # こうかとんの縦座標を+1する
        if key_lst[pg.K_LEFT]:  # 下矢印キーがTrueなら
            kk_rct.move_ip((-1, 0))  # こうかとんの横座標を-1する
        if key_lst[pg.K_RIGHT]:  # 下矢印キーがTrueなら
            kk_rct.move_ip((+1, 0))  # こうかとんの横座標を+1する

        #x = -(tmr%800)###6
        x = -(tmr%3200)####7
        screen.blit(bg_img, [x, 0])###6
        screen.blit(bg_img, [x+1600, 0])####7
        screen.blit(bg_img, [x+3200, 0])#####7
        screen.blit(bg_img, [x+4800, 0])######7
        #screen.blit(kk_img, [300, 200])##4
        screen.blit(kk_img, kk_rct)  # 練習４ -> 練習8-5
        pg.display.update()
        tmr += 1        
        #clock.tick(200)##5
        clock.tick(400)######7


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()