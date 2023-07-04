# cv2 modulünü import etme
import cv2 
# kamera görüntüsü almak için videocapture kullanma
video=cv2.VideoCapture(0)

while True:
    # alınan görüntünün okunması
    ret,goruntu=video.read()
    
    # Hedef vuruş alanı dikdörtgeninin başlangıç x ve y sinin belirlenmesi 
    x=int(goruntu.shape[1]/2-goruntu.shape[1]/4)
    y=int(goruntu.shape[0]/2-4*goruntu.shape[0]/10)
    
    # Hedef vuruş alanı dikdörtgeninin genişliği uzunluğunun belirlenmesi
    gen=int(int(goruntu.shape[1])/2)
    uz=int(int(goruntu.shape[0])*8/10)
    
    # Dikdörtgenin rectangel komutu ile çıktı alınması
    cv2.rectangle(goruntu,(x,y),( x + gen , y+uz),(204,0,102),4)
    
    # Hedef vuruş alanı yazısı oluşturulması
    cv2.putText(goruntu,"Av: Hedef Vurus Alani",(162,427),1,1,(0,0,0),1)
    
    # Kamera görüş alanı dikdörtgeni oluşturulması
    cv2.rectangle(goruntu,(0,0),(int(goruntu.shape[1]),int(goruntu.shape[0])),(0,153,0),4)

    # Kamera görüş alanı yazısı oluşturulması
    cv2.putText(goruntu,"Ak: Kamera Gorus Alani",(2,475),1,1,(0,0,0),1)
    
    # Oluşturulan görüntünün gösterilmesi
    cv2.imshow("kamera",goruntu)
    
    # while Çıkış fonksiyonun oluşturulması
    if cv2.waitKey(5) & 0xFF ==ord("q"):
        print(f"Çözünürlük: {int(goruntu.shape[1])}x{int(goruntu.shape[0])}")   
        break


goruntu.release()
cv2.destroyAllWindows()
