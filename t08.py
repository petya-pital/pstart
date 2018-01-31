# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 15:29:44 2018

@author: Петя
"""

cl = ["Red","Green","White" ,"Black"]
print( "%s %s"%(cl[0],cl[-1]))
print( "%s %s"%(cl[0],cl[-2]))# процентик знак форматирования строки бывает
# %s - строка %f - вещественный %d - целый and escho do hera 
#see f/e list of agrements https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting
#[-1] = последнийб [-2] = предпоследний
#принцип написания тут хотя мб он многолик первые процентики говорят нам что мы будем форматмировать(типизировать строку)
#хреньб а потом сразу дожна идти под знаком вопроса  коллекция в ширнармассле строк в нужно количестве
print('%d'%(8.777)) #-- целая часть\
print('%.2f'%(8.999))#  fuck intpart
print('%.2f'%(8.9))# fuck intpart