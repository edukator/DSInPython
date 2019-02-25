SUTUN_LIST = list(" ABCDEFGIJKLMNOPQRST")


class SquareBoard:
    def __init__(self,satir_say,sutun_say,yatay_matris=None,dikey_matris=None,kare_kimin=None):
        self.__satir_say = satir_say
        self.__sutun_say = sutun_say

        if yatay_matris == None:
            self.__yatay_kenar_mat = [False] * (self.__satir_say + 1)
            for i in range(satir_say + 1):
                self.__yatay_kenar_mat[i] = [False] * (self.__sutun_say + 1)
                self.__yatay_kenar_mat[i][self.__sutun_say] = True

            for j in range(self.__sutun_say + 1):
                self.__yatay_kenar_mat[0][j] = True
                self.__yatay_kenar_mat[self.__satir_say][j] = True
        else:
            self.__yatay_kenar_mat = list(yatay_matris)
        if dikey_matris == None:

            self.__dikey_kenar_mat = [False] * (self.__satir_say + 1)
            for i in range(self.__satir_say + 1):
                self.__dikey_kenar_mat[i] = [False] * (self.__sutun_say + 1)
                self.__dikey_kenar_mat[i][self.__sutun_say] = True
            for i in range(self.__sutun_say):
                self.__dikey_kenar_mat[0][i] = True

            for j in range(self.__satir_say + 1):
                self.__dikey_kenar_mat[j][0] = True
                self.__dikey_kenar_mat[j][self.__sutun_say] = True
        else:
            self.__dikey_kenar_mat = list(dikey_matris)
        if kare_kimin==None:

            self.__kare_kimin = dict()
            for sat_ind in range(1, self.__satir_say + 1):
                for sut_ind in SUTUN_LIST[1:self.__sutun_say + 1]:
                    self.__kare_kimin[(sat_ind, sut_ind)] = " "

        else:
            self.__kare_kimin=dict(kare_kimin)

    def set_kare_kimin(self,kare,oyuncu):
        self.__kare_kimin[kare] = oyuncu

    def __str__(self):
        rep=""
        for sutun_name in SUTUN_LIST[:self.__sutun_say + 1]:
            rep+=" " + sutun_name + "  "
        rep+="\n"

        for satir in range(2 * self.__satir_say + 1):
            for sutun in range(-1, self.__sutun_say):
                if satir % 2 == 0:  # cift satirlar
                    if sutun == -1:  # ilk girinti
                        rep+="   "
                    else:  # yatay kenarlari ciz veya cizme

                        if self.__yatay_kenar_mat[satir // 2][sutun]:
                            rep+=" ---"  # en basa ve sona true koy.
                        else:
                            rep+="    "
                else:  # tek satirlar
                    if sutun == -1:  # satir no yu yazdir.
                        rep+="  "
                        rep+=str((satir + 1) // 2)
                    else:  # dikey kenari ciz.

                        if self. __dikey_kenar_mat[(satir + 1) // 2][sutun]:
                            my_str = " " +self.__kare_kimin[(satir + 1) // 2, SUTUN_LIST[sutun + 1]] + " "
                            rep+="|" + my_str
                        else:
                            rep+="    "  # secilince ciz
                        if sutun == self.__sutun_say - 1:
                            rep+="|"
            rep+='\n'
        return rep
    def kenar_ciz(self,sat_ind,sut_ind,yon_ind):
        if yon_ind == 'G':
            if self.__yatay_kenar_mat[sat_ind][SUTUN_LIST.index(sut_ind) - 1]:
                return False
            else:
                self.__yatay_kenar_mat[sat_ind][SUTUN_LIST.index(sut_ind) - 1] = True
                return True
        elif yon_ind == 'K':
            if self.__yatay_kenar_mat[sat_ind - 1][SUTUN_LIST.index(sut_ind) - 1]:
                return False
            else:
                self.__yatay_kenar_mat[sat_ind - 1][SUTUN_LIST.index(sut_ind) - 1] = True
                return True
        elif yon_ind == 'B':
            if self.__dikey_kenar_mat[sat_ind][SUTUN_LIST.index(sut_ind) - 1]:
                return False
            else:
                self.__dikey_kenar_mat[sat_ind][SUTUN_LIST.index(sut_ind) - 1] = True
                return True
        elif yon_ind == 'D':
            if self.__dikey_kenar_mat[sat_ind][SUTUN_LIST.index(sut_ind)]:
                return False
            else:
                self.__dikey_kenar_mat[sat_ind][SUTUN_LIST.index(sut_ind)] = True
                return True

    def tamamlanan_kare(self,sat_ind, sut_ind):
        # koordinatlari verilen karenin henüz tamamlanip tamamlanmadiğini boolean olarak döndürür. Bunun için çizilen kenarlari boolen
        # olarak  tutan matrisleri kullanir.
        return self.__yatay_kenar_mat[sat_ind][SUTUN_LIST.index(sut_ind) - 1] and self.__yatay_kenar_mat[sat_ind - 1][
            SUTUN_LIST.index(sut_ind) - 1] and \
               self.__dikey_kenar_mat[sat_ind][SUTUN_LIST.index(sut_ind) - 1] and self.__dikey_kenar_mat[sat_ind][
            SUTUN_LIST.index(sut_ind)]

    def etrafi_tara(self,sat_ind, sut_ind, yon_ind):
        '''
        indisleri  verilen kenarin ait olduğu karelerin listesini döndürür.

        '''
        komsu_kareler = [(sat_ind, sut_ind)]
        if yon_ind == 'D':
            komsu_kareler.append((sat_ind, SUTUN_LIST[SUTUN_LIST.index(sut_ind) + 1]))
        elif yon_ind == 'B':
            komsu_kareler.append((sat_ind, SUTUN_LIST[SUTUN_LIST.index(sut_ind) - 1]))
        elif yon_ind == 'K':
            komsu_kareler.append((sat_ind - 1, sut_ind))
        else:
            komsu_kareler.append((sat_ind + 1, sut_ind))
        return komsu_kareler

    def oyun_bitti_mi(self):
        '''
          oyunun tamamlanıp tamamlanmadığını boolea olarak döndürür.

        '''
        return  " "  in self.__kare_kimin.values()

    def kopyala(self):
        return SquareBoard(self.__satir_say,self.__sutun_say,self.__yatay_kenar_mat,self.__dikey_kenar_mat,self.__kare_kimin)


    def kazanan(self,oyuncu1,oyuncu2):
        '''
        oyun bittiğinde goyunun sonucunu ekrana bastırır.

        '''
        oyuncu1_puan = list(self.__kare_kimin.values()).count(oyuncu1)
        oyuncu2_puan = self.__satir_say * self.__sutun_say - oyuncu1_puan
        print(oyuncu1, " in puanı ", oyuncu1_puan)
        print(oyuncu2, " in puanı ", oyuncu2_puan)
        if oyuncu1_puan == oyuncu2_puan:
            print("Berabere")
        else:
            kazanan=oyuncu1 if oyuncu1>oyuncu2  else oyuncu2
            print("Kazanan", oyuncu)












def oyuncu_degistir(oyuncu,oyuncu1,oyuncu2):
    if oyuncu==oyuncu1:
        return oyuncu2
    else:
        return oyuncu1
def kenar_al():
    sat_ind=int(input("sectigin karenin satiri?"))
    sut_ind=(input(" sectigin karenin sutunu"))
    yon_ind=(input("karenin hangi kenari "))
    return (sat_ind,sut_ind,yon_ind)



oyuncu1 = input(" Birinci oyuncuyu temsil etmek için bir karakter giriniz: ")
oyuncu2 = input(" İkinci oyuncuyu temsil etmek için bir karakter giriniz: ")
satir_say = int(input("oyun alaninin satir sayisini giriniz: [3-7]  "))
sutun_say = int(input("oyun alaninin sütün sayisini giriniz: [3-19]  "))
while not (3<=satir_say<=7 and 3<=sutun_say<=19):
    print(" HATA......istenen aralıkta değerleri giriniz.")
    satir_say = int(input("oyun alaninin satir sayisini giriniz: [3-7]  "))
    sutun_say = int(input("oyun alaninin sütün sayisini giriniz: [3-19]  "))
my_board=SquareBoard(satir_say,sutun_say)
print(my_board)

devam = True
oyuncu = oyuncu1

while (devam):
    print(oyuncu, " oynuyor.")
    (sat_ind, sut_ind, yon_ind) = kenar_al()
    flag = my_board.kenar_ciz(sat_ind, sut_ind, yon_ind)
    while (not flag):
        print("bu kenar zaten işaretli tekrar kenar girisi yapiniz.")
        (sat_ind, sut_ind, yon_ind) = kenar_al()
        flag = my_board.kenar_ciz(sat_ind, sut_ind, yon_ind)

    komsu_kareler = my_board.etrafi_tara(sat_ind, sut_ind, yon_ind)

    dolu_komsu_say = 0
    for komsu in komsu_kareler:

        dolu_mu = my_board.tamamlanan_kare(komsu[0], komsu[1])
        if dolu_mu:
            my_board.set_kare_kimin(komsu,oyuncu)

            dolu_komsu_say += 1
    print(my_board)
    if dolu_komsu_say == 0:
        oyuncu = oyuncu_degistir(oyuncu, oyuncu1, oyuncu2)

    devam=my_board.oyun_bitti_mi()


print("oyun bitti")


print("kopya  olan ")

my_board.kazanan(oyuncu1,oyuncu2)