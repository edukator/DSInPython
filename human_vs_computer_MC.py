import random
SUTUN_LIST = list(" ABCDEFGIJKLMNOPQRST")

class SquareBoard:
    def __init__(self,satir_say,sutun_say,yatay_matris=None,dikey_matris=None,kare_kimin=None):
        self.__satir_say=satir_say
        self.__sutun_say=sutun_say

        if yatay_matris==None:
            self.__yatay_kenar_mat = ['EMPTY'] * (self.__satir_say + 1)
            for i in range(satir_say + 1):
                self.__yatay_kenar_mat[i] = ['EMPTY'] * (self.__sutun_say + 1)
                self.__yatay_kenar_mat[i][self.__sutun_say] = 'NOONE'




            for j in range(self.__sutun_say + 1):
                self.__yatay_kenar_mat[0][j] = 'NOONE'
                self.__yatay_kenar_mat[self.__satir_say][j] ='NOONE'
        else:


            self.__yatay_kenar_mat=[[yatay_matris[row][col] for col in range(sutun_say+1)]
             for row in range(satir_say+1)]
        if dikey_matris==None:

            self.__dikey_kenar_mat = ['EMPTY'] * (self.__satir_say + 1)
            for i in range(self.__satir_say + 1):
                self.__dikey_kenar_mat[i] = ['EMPTY'] * (self.__sutun_say + 1)
              #  self.__dikey_kenar_mat[i][self.__sutun_say] = [True,None]
            for  i in range(self.__sutun_say):
                self.__dikey_kenar_mat[0][i] = 'NOONE'

            for j in range(self.__satir_say + 1):
                self.__dikey_kenar_mat[j][0] = 'NOONE'
                self.__dikey_kenar_mat[j][self.__sutun_say] = 'NOONE'
        else:
            self.__dikey_kenar_mat = [[dikey_matris[row][col] for col in range(sutun_say + 1)]
                                      for row in range(satir_say + 1)]
        if kare_kimin==None:

            self.__kare_kimin = dict()
            for sat_ind in range(1, self.__satir_say + 1):
                for sut_ind in SUTUN_LIST[1:self.__sutun_say + 1]:
                    self.__kare_kimin[(sat_ind, sut_ind)] = " "

        else:
            self.__kare_kimin=dict(kare_kimin)

    def set_kare_kimin(self,kare,oyuncu):
        self.__kare_kimin[kare] = oyuncu


    def get_yatay_matris(self):
        return self.__yatay_kenar_mat

    def get_dikey_matris(self):
        return self.__dikey_kenar_mat

    def get_satir_say(self):
        return self.__satir_say

    def get_sutun_say(self):
        return self.__sutun_say

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

                        if self.__yatay_kenar_mat[satir // 2][sutun]!='EMPTY':
                            rep+=" ---"  # en basa ve sona true koy.
                        else:
                            rep+="    "
                else:  # tek satirlar
                    if sutun == -1:  # satir no yu yazdir.
                        rep+="  "
                        rep+=str((satir + 1) // 2)
                    else:  # dikey kenari ciz.

                        if self. __dikey_kenar_mat[(satir + 1) // 2][sutun]!='EMPTY':
                            my_str = " " +self.__kare_kimin[(satir + 1) // 2, SUTUN_LIST[sutun + 1]] + " "
                            rep+="|" + my_str
                        else:
                            rep+="    "  # secilince ciz
                        if sutun == self.__sutun_say - 1:
                            rep+="|"
            rep+='\n'
        return rep
    def kenar_ciz(self,sat_ind,sut_ind,yon_ind,oyuncu):
        if yon_ind == 'G':
            if self.__yatay_kenar_mat[sat_ind][SUTUN_LIST.index(sut_ind) - 1]=='EMPTY':
                self.__yatay_kenar_mat[sat_ind][SUTUN_LIST.index(sut_ind) - 1] = oyuncu
                return True
            else:
                return False

        elif yon_ind == 'K':
            if self.__yatay_kenar_mat[sat_ind - 1][SUTUN_LIST.index(sut_ind) - 1]=='EMPTY':
                self.__yatay_kenar_mat[sat_ind - 1][SUTUN_LIST.index(sut_ind) - 1] = oyuncu
                return True
            else:
                return False


        elif yon_ind == 'B':
            if self.__dikey_kenar_mat[sat_ind][SUTUN_LIST.index(sut_ind) - 1]=='EMPTY':
                self.__dikey_kenar_mat[sat_ind][SUTUN_LIST.index(sut_ind) - 1] = oyuncu
                return True
            else:
                return False


        elif yon_ind == 'D':
            if self.__dikey_kenar_mat[sat_ind][SUTUN_LIST.index(sut_ind)]=='EMPTY':
                self.__dikey_kenar_mat[sat_ind][SUTUN_LIST.index(sut_ind)] = oyuncu

                return True
            else:
                return False


    def tamamlanan_kare(self,sat_ind, sut_ind):
        # koordinatlari verilen karenin henüz tamamlanip tamamlanmadiğini boolean olarak döndürür. Bunun için çizilen kenarlari boolen
        # olarak  tutan matrisleri kullanir.
        return self.__yatay_kenar_mat[sat_ind][SUTUN_LIST.index(sut_ind) - 1]!='EMPTY' and self.__yatay_kenar_mat[sat_ind - 1][
            SUTUN_LIST.index(sut_ind) - 1]!='EMPTY' and \
               self.__dikey_kenar_mat[sat_ind][SUTUN_LIST.index(sut_ind) - 1]!='EMPTY' and self.__dikey_kenar_mat[sat_ind][
            SUTUN_LIST.index(sut_ind)]!='EMPTY'

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

        if oyuncu1_puan == oyuncu2_puan:
            winner="Berabere"
        else:
            winner=oyuncu1 if oyuncu1_puan>oyuncu2_puan  else oyuncu2
        return winner



    def get_bos_kenarlar(self):
        '''
         seçim yapılan kenarlarin listesini triple olarak döndürür.
            (Yatay/Dikey,satir,sutun)
        '''
        bos_kenar=[]

        for satir in range(self.__satir_say+1):
            for sutun in range(self.__sutun_say+1):
                if self.__yatay_kenar_mat[satir][sutun]=='EMPTY':
                    bos_kenar.append(('Yatay',satir,sutun))
                if self.__dikey_kenar_mat[satir][sutun]=='EMPTY':
                    bos_kenar.append(('Dikey',satir,sutun))

        return bos_kenar

    def convert_kenar_koord(self,kenar):

            if kenar[0]=='Yatay':
                yon_ind='G'
                sat_ind=kenar[1]
                sut_ind=str(SUTUN_LIST[kenar[2]+1])
            else:
                yon_ind='D'
                sat_ind=kenar[1]
                sut_ind=str(SUTUN_LIST[kenar[2]])
            return sat_ind,sut_ind,yon_ind

    def rassal_kenar_sec(self):
        bos_kenarlar=self.get_bos_kenarlar()
        kenar=random.choice(bos_kenarlar)
        return self.convert_kenar_koord(kenar)








#HELPER  FUNCTIONS
def oyuncu_degistir(oyuncu,oyuncu1,oyuncu2):
    if oyuncu==oyuncu1:
        return oyuncu2
    else:
        return oyuncu1
def kenar_al():
    sat_ind=int(input("tr: sectigin karenin satiri?  eng:  which  row  do you  choose? "))
    sut_ind=(input("tr: sectigin karenin sutunu? eng: which column do you choose?"))
    yon_ind=(input("tr:karenin hangi kenari ?: eng: which edge  of the square?"))
    return (sat_ind,sut_ind,yon_ind)
def monte_carlo_tek_oyun(board,oyuncu1,oyuncu2):
    devam = True
    oyuncu = oyuncu1
    while (devam):
        #print(oyuncu,"oynuyor")
        (sat_ind, sut_ind, yon_ind) = board.rassal_kenar_sec()
        #print(sat_ind,sut_ind,yon_ind)
        flag=board.kenar_ciz(sat_ind, sut_ind, yon_ind,oyuncu)
        while (not flag):
            print("tr:kenar seçimi sorunlu: eng: warning! the  selection of edge  is  not appropriate.")
            (sat_ind, sut_ind, yon_ind) = board.rassal_kenar_sec()
            flag = board.kenar_ciz(sat_ind, sut_ind, yon_ind,oyuncu)

        komsu_kareler = board.etrafi_tara(sat_ind, sut_ind, yon_ind)
        dolu_komsu_say = 0
        for komsu in komsu_kareler:

            dolu_mu = board.tamamlanan_kare(komsu[0], komsu[1])
            if dolu_mu:
                board.set_kare_kimin(komsu, oyuncu)

                dolu_komsu_say += 1

        if dolu_komsu_say == 0:
            oyuncu = oyuncu_degistir(oyuncu, oyuncu1, oyuncu2)
        #  print(board)
        devam=board.oyun_bitti_mi()

def kenar_puanla(board,player,yatay_skor,dikey_skor,value1,value2):
    #tamamlanmış   bir board un puanlamasını yatay ve dikey skorlara ekle.
    yatay_matris=board.get_yatay_matris()
    dikey_matris=board.get_dikey_matris()
    for row in range(board.get_satir_say()+1):
        for col in range(board.get_sutun_say()+1):
            content_yatay=yatay_matris[row][col]
            content_dikey=dikey_matris[row][col]
            if (content_yatay==player):
                yatay_skor[row][col]+=value1
            elif (content_yatay=='NOONE'):
                pass

            else:
                yatay_skor[row][col]+=value2

            if (content_dikey == player):
                dikey_skor[row][col] += value1
            elif (content_dikey == 'NOONE'):
                pass

            else:
                dikey_skor[row][col] += value2


def skor_guncelle(board,yatay_skor,dikey_skor,oyuncu,oyuncu1,oyuncu2):
    kazanan=board.kazanan(oyuncu1,oyuncu2)
    if kazanan=='Berabere':
        pass
    elif kazanan==oyuncu:
        kenar_puanla(board,oyuncu,yatay_skor,dikey_skor,1,-1)
    else:
        kenar_puanla(board, oyuncu, yatay_skor, dikey_skor, -1, 1)

def  en_iyi_secimi_belirle(board,yatay_skor,dikey_skor):
    """
    oyunda seçilebilir kenarlar içerisinden en yüksek puanlılardan birini rastgele geri döndür.
    :param board:
    :param yatay_skor:
    :param dikey_skor:
    :return:
    """
    boslar=board.get_bos_kenarlar()

    deger_sozlugu = {}
    listem=[]
    for kenar_idx in boslar:
        if kenar_idx[0]=='Yatay':
            deger_sozlugu[kenar_idx]=yatay_skor[kenar_idx[1]][kenar_idx[2]]
        else:
            deger_sozlugu[kenar_idx] = dikey_skor[kenar_idx[1]][kenar_idx[2]]
    maxvalue = max(deger_sozlugu.values())
    for item in deger_sozlugu.keys():
        if deger_sozlugu[item] == maxvalue:
            listem.append(item)

    return board.convert_kenar_koord(random.choice(listem))

def olasiliksal_hamle(board,oyuncu,deney_sayisi,oyuncu1,oyuncu2):
    #  oyuncu olan insan kenar seçimini kenar al fonksiyonu ile yaparken
     # benim ajanım yukarıda yazdığım  yardımcı  fonksiyonlar  yardımı ile
    #  bu  fonksiyon içinde olasılıksal hesaplar yapıp en mantıklı ? kenar seçimini yapıyor.

    yatay_skor = [0] * (board.get_satir_say() + 1)
    for i in range(board.get_satir_say() + 1):
        yatay_skor[i] = [0] * (board.get_sutun_say() + 1)

    dikey_skor = [0] * (board.get_satir_say() + 1)
    for i in range(board.get_satir_say() + 1):
        dikey_skor[i] = [0] * (board.get_sutun_say() + 1)

    for dummy in range(deney_sayisi):
        # kopy_one= SquareBoard(satir_say, sutun_say)
        kopy_one = board.kopyala()
        monte_carlo_tek_oyun(kopy_one, oyuncu1, oyuncu2)
        skor_guncelle(kopy_one, yatay_skor, dikey_skor, oyuncu, oyuncu1, oyuncu2)
    return  en_iyi_secimi_belirle(my_board,yatay_skor,dikey_skor)




#########oyun  burada  başlıyor.###########

oyuncu1 = input(" Sizi  temsil etmesi için  B disinda bir karakter giriniz: \n eng: Enter a character  apart from B  ")
oyuncu2 = 'B'
satir_say = int(input("oyun alaninin satir sayisini giriniz: [3-7] \n  eng:  Enter  number  of rows in game grid:[3-7]   "))
sutun_say = int(input("oyun alaninin sütün sayisini giriniz: [3-19]\n   eng:  Enter  number  of columns in game grid:[3-19]  "))
deney_sayisi=1000 # grid boyutu büyüdükçe bunu arttır.
while not (3<=satir_say<=7 and 3<=sutun_say<=19):
    print(" HATA......istenen aralıkta değerleri giriniz.\n WARNING: Enter  values in desired intervals")
    satir_say = int(input("oyun alaninin satir sayisini giriniz: [3-7] \n  eng:  Enter  number  of rows in game grid:[3-7]   "))
    sutun_say = int(input("oyun alaninin sütün sayisini giriniz: [3-19]\n   eng:  Enter  number  of columns in game grid:[3-19]  "))
cevap=input(" ilk oyuncu olmak istermisiniz? e/h: eng: Would you like to be first  player? y/n")
if (cevap=='e' or cevap=='y'):
    oyuncu=oyuncu1
else:
    oyuncu=oyuncu2
my_board=SquareBoard(satir_say,sutun_say)
print(my_board)
devam=True
while (devam):
    print(oyuncu, " oynuyor. playing")
    if oyuncu=='B':
        (sat_ind, sut_ind, yon_ind) =olasiliksal_hamle(my_board,oyuncu,deney_sayisi,oyuncu1,oyuncu2)
    else:
        (sat_ind, sut_ind, yon_ind) = kenar_al()

    print(sat_ind,sut_ind,yon_ind," seçimini yapti. eng: selection done")
    flag=my_board.kenar_ciz(sat_ind, sut_ind, yon_ind,oyuncu)
    while (not flag):
            print("kenar seçimi sorunlu eng:  selection of the edge is not appropriate")
            if oyuncu == 'B':
                (sat_ind, sut_ind, yon_ind) = olasiliksal_hamle(my_board, oyuncu,deney_sayisi ,oyuncu1, oyuncu2)
            else:
                (sat_ind, sut_ind, yon_ind) = kenar_al()
            flag = my_board.kenar_ciz(sat_ind, sut_ind, yon_ind, oyuncu)

    komsu_kareler =my_board.etrafi_tara(sat_ind, sut_ind, yon_ind)
    dolu_komsu_say = 0
    for komsu in komsu_kareler:

        dolu_mu = my_board.tamamlanan_kare(komsu[0], komsu[1])
        if dolu_mu:
                my_board.set_kare_kimin(komsu, oyuncu)

                dolu_komsu_say += 1
    print(my_board)
    if dolu_komsu_say == 0:
        oyuncu = oyuncu_degistir(oyuncu, oyuncu1, oyuncu2)

    devam=my_board.oyun_bitti_mi()
print("oyun bitti eng: Game  over")
print(my_board)
print ('Kazanan  eng: Winner', my_board.kazanan(oyuncu1, oyuncu2))



