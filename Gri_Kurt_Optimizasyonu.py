#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 02:22:18 2022

@author: barisbalci
"""

import math
from random import random
import numpy as np

for t in range(0,durma_kriteri):
    
#başlangıç çözüm matrisinde amaç foksiyonun minimum yapan (en iyi)3 çözüm (alfa, beta ve delta kurtlarının) belirtilmesi
#Amaç: Tüm aday çözümlerine ait amaç foksiyonu değerlerinin depolandığı vektör

Amac = OPT[AF][:]

#Amaç fonksiyonu değerlerinin problemin yapısı doğrultusunda sıralanması:
#Buradan örnek olarak minimizasyon olduğu durumda küçükten büyüğe doğru sıralama yapılmoş olup sütün değerlerinin sıralanması nedeniyle parametre değeri olarak 2 kullanılmıştır.

    obj_deger=sorted(Amac)
    obj_sıra=np.argsort(Amac)

#sırasıyla ilk üç kurdun(amaç foksiyonu açısından en iyi 3 değeri sağlayan) belirlenmesi

    alfa_r = obj_sira[0]
    beta_r = obj_sira[1]
    delta_r = obj_sira[2]
    
#kurt_av arası uzaklığı etkileyen vektör(a) değerlerinin iterasyon adımları boyunca güncellenmesi
    a[0][t] = 2-2*(t/durma_kriteri)
    
#en iyi 3 kurda ait konnumların belirlenmesi
#alfa kurduna ait konum
    bir_X1 = OPT[0][alfa_r]
    bir_X2 = OPT[1][alfa_r]
    
    ......
    
#Beta kurduna ait konum
    bir_X1 = OPT[0][beta_r]
    bir_X2 = OPT[1][beta_r]
    .......
    
#Delta kurduna ait konum
    iki_X1 = OPT[0][delta_r]
    iki_X2 = OPT[0][delta_r]
    .......

#YENİ ÇÖZÜM MATRİSİNİN GWD ALGORİTMASI KURALLARINA GÖRE OLUŞTURULMASI

    for i in random(0,wn):
        
#Kurdun ava saldırı durumunu etkileyen vektör(A) değerlerinin her bir kurda yönelik olarak yeniden hesaplanması
    
    A[0][i]=2*random()*a[0][t]-a[0][t]
    
    A1=2*a[0][t]*random()-a[0][t]
    C1=2*random()
    
#alfa kurdu ile herhangi bir omega gri kurdu arasındaki uzaklığın belirlenmesi
    
    D_alfa[0][i]=abs(C1*bir_X1-OPT[0][i])
    D_alfa[1][i]=abs(C1*bir_X2-OPT[1][i])
    
#alfa kurdu için yeni konum vektörlerinin belirlenmesi

    X1_ay=bir_X1-A1*D_alfa[0][i]
    X2_ay=bir_X2-A1*D_alfa[0][i]
    ......
    
    A2=2*a[0][t]*random()-a[0][t]
    C2=2*random()
    
#Beta kurdu ile herhangi bir omega gri kurdu arasındaki uzaklığın belirlenmesi
    D_beta[0][i]=abs(c2*iki_X1-OPT[0][i])
    D_beta[1][i]=abs(C2*iki_X2-OPT[1][i])
    .....

#Beta kurdu için yeni konnum vektörlerinin belirlenmesi
    X1_by=iki_X1-A2*D_beta[0][i]
    X2_by=iki_X2-A2*D_beta[1][i]

    A3=2*a[0][t]*random()-a[0][t]    
    C3=2*random()
    
#Delta kurdu ile herhangi bir omega gri kurdu arasındaki uzaklığın belirlenmesi

    D_delta[0][i]=abs(C3*uc_X1-OPT[0][i])
    D_delta[1][i]=abas(C3*uc_X2-OPT[1][i])
    
#Delta kurdu için yeni kkonum vektörlerinin belirlenmesi

    X1_dy=uc_X1-A3*D_delta[0][i]
    X2_dy=uc_X2-A3*D_delta[1][i]
    
#tasarım değişkenlerine ait yeni değerilerin (omega gri kurdunun ava göre) belirlenmesi
    
    if abs(A[0][i])<1:
        X1new = (X1_ay+X1_by+X1_dy)/3
        X2new = (X2_ay+X1_by+X1_dy)/3
        ....
    else:
        X1new = X1min+(X1maks-X1min)*random()
        X2new = X2min+(X2maks-X2min)*random()
        
        
deger = min(OPT[AF][:])
sira = np.argmin(OPT[AF])

    






 
