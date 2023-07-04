# cv2 modulünü import etme.
import cv2 

# Video görüntüsü almak için videocapture kullanma.
video=cv2.VideoCapture(0)

# Aktif video çözünürlüğünün bulunması ve yazdırılması.
a=int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
b=int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f"Çözünürlük: {a}x{b}")

# Hedef vuruş alanı dikdörtgeninin başlangıç x ve y sinin belirlenmesi.
x=int(a/2-a/4)
y=int(b/2-4*b/10)

# Hedef vuruş alanı dikdörtgeninin genişliği uzunluğunun belirlenmesi.
gen=int(a/2)
uz=int(b*8/10)

while True:
    # Alınan görüntünün okunması.
    ret,goruntu=video.read()
    
    # Hedef vuruş alanı dikdörtgeninin rectangel komutu ile çıktı alınması.
    cv2.rectangle(goruntu,(x,y),( x + gen , y+uz),(204,0,102),4)
    
    # Hedef vuruş alanı yazısı oluşturulması.
    cv2.putText(goruntu,"Av: Hedef Vurus Alani",(int(a/4),int(b*9/10)-2),1,1,(0,0,0),1)
    
    # Kamera görüş alanı dikdörtgeni oluşturulması.
    cv2.rectangle(goruntu,(0,0),(a,b),(0,153,0),4)

    # Kamera görüş alanı yazısı oluşturulması.
    cv2.putText(goruntu,"Ak: Kamera Gorus Alani",(0,b-2),1,1,(0,0,0),1)

    # Oluşturulan görüntünün gösterilmesi.
    cv2.imshow("kamera",goruntu)
    
    # while Çıkış fonksiyonun oluşturulması.
    if cv2.waitKey(5) & 0xFF ==ord("q"):
        break

goruntu.release()
cv2.destroyAllWindows()
