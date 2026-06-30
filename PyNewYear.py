"""
Nickolay Dezhko желает вам Счастливого Нового года и веселого Рождества ;3

***
Веточка в иголочках,
Шарик золотой.
Сверкает наша ёлочка
Серебряной звездой.

Орехи, бусы , бантики
На веточках висят.
Конфеты в ярких фантиках
Для взрослых и ребят.

Под елкою снегурочка,
С ней рядом Дед Мороз.
Он деточкам в кошёлочке
Подарочки привёз.

Минутки, будто всадники,
Торопят стрелок ход.
Всё готово к празднику.
Скоро Новый Год.
(Фаина Фанни )
"""
import time
import datetime
import random
elka = random.randint(1, 3)
if elka == 1:
     print(r"""
     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
     ^^^^^^^^^^^^^^^^^^#^^^^^^^^^^^^^^^^^^
     ^^^^^^^^^^^^^^^^^###^^^^^^^^^^^^^^^^^
     ^^^^^^^^^^^^^^^#######^^^^^^^^^^^^^^^
     ^^^^^^^^^^^^^#O#########^^^^^^^^^^^^^
     ^^^^^^^^^^#####O########O##^^^^^^^^^^
     ^^^^^^^^^^^#######O###O###^^^^^^^^^^^
     ^^^^^^^^^^^^^###########^^^^^^^^^^^^^
     ^^^^^^^^^^^#O#############^^^^^^^^^^^
     ^^^^^^^^^#####O#############^^^^^^^^^
     ^^^^^###########O###########O###^^^^^
     ^^^^^^^#############O###O#####^^^^^^^
     ^^^^^^^^^^^^#############^^^^^^^^^^^^
     ^^^^^^^^^^#################^^^^^^^^^^
     ^^^^^^^^##O##################^^^^^^^^
     ^^^^^######O####################^^^^^
     ^############O##################O###^
     ^^^^############O############O###^^^^
     ^^^^^^^^^###########O####O##^^^^^^^^^
     ^^^^^^^^^^^^^^^^^^##^^^^^^^^^^^^^^^^^
     """)
elif elka == 2:
    print(r"""
     .       *
                              |         *
                   .    *         .            *
                                          /
                *      .       ,    *          .    *
                               `;.
                      *   -      ;:,   -    *     -   .
              .  -               ,:;:,
                     .          ,:;%;;:,           *
                          /    ::;%#%;::   *    .
                   *           ::;%#%;:'
                                `:%#%'  .   .,,.
                         *    .    #     .,sSSSSs
                                   #  .,sSSSSSSSS
                                .,sSSSSSSSSSSSS'
                           .,sSSSSSSSSSSSSSSSSSs,
                       .sSSSSSSSSSSSSSSSSSSSSSSSS
                       sSSSSSSSSSSSSSSSSSSSSSSSS'
                       `SSSSSSSSSSSSSSSSSSSSSSS'
                       sSSSS;nww;SSS;mwwwn;SSSSs
                       `SSS;nnw;sSSSs;wwwnnn;SSSs
                      .sSS;nnnw;SSSSS;wwwnnn%;SSS
                     .SSSS;nnnww;SSS;mwwwnnn%;SS'
                     SSSSS;nnnwwwmmmmmwwwnnn%%;
                     `SSS'%nnnwwwmmmmmwwwnnn%%;
                        ;%%nnnwwwmmmmmwwwnnn%%;
                        ;%%nnnwwwmmmmmwwwnnn%%;
                        ;%%nnnwwwmmmmmwwwnnn%%;
                        ;%%nnnwwwmmmmmwwwnnn%%;
                        ;%%nnnwwwmmmmmwwwnnn%%;
                        ;%%nnnwwwmmmmmwwwnnn%%;
                        ;%%nnnwwwmmmmmwwwnnn%%;
                        ;%%nnnwwwmmmmmwwwnnn%%;
                        ;%%nnnwwwmmmmmwwwnnn%%;
      ,                 ;%%nnnwwwmmmmmwwwnnn%%;
   .,;;;,.,;            ;%%nnnwwwmmmmmwwwnnn%%;        ;     ;
     `;;;;,;;;,.,;      ;%%nnnwwwmmmmmnnnnnn%%;  ,    .;;,.,;;;.
      ;;;;;;;;,;;;;;,., ;%%nnnnnnnnn;,ooo,;n%%;   ;;;;;,;;,;;,;;;,.
      ;'   `;;;;;;,;;;;.;%%nnn;,ooo,;OOOOO;n%%;  .;;,;;;;;;;;;;,;;'',
            ;'  ';;;;,;;,...   OOOOO;`OOO'..,,;,;;,;;;''';;;''';;'
                  ';;'    '''''`OOO'OOooo' ''' ;'   '     '     '
                   '         ;,.,;, `OOO'
                         ;,.;;';;;';,;.
                     ;,.;;';;;;;;;;;;;'
                   .,;;;;;;;;;;;;;;;'
                     ';'  ';'   ';;
   """)
elif elka == 3:
    print(r"""
    ad888888b,    ,a8888a,     ad888888b,  8888888888
   d8"     "88  ,8P"'  `"Y8,  d8"     "88  '''''''d8'
           a8P ,8P        Y8,         a8P        a8P'
        ,d8P"  88          88      ,d8P"        a8P'
      a8P"     88          88    a8P"          a8P'
    a8P'       `8b        d8'  a8P'           a8P'
   d8"          `8ba,  ,ad8'  d8"            a8P'
   88888888888    "Y8888P"    88888888888   a8P'
   
   happy new year my friends :3
""")
print("fork by tret_game")
countdown = lambda : datetime.datetime(2027,1,1,0,0) - datetime.datetime.now()
while True:
    print ('\r',countdown(), '              ',end="")
    time.sleep(0.5)