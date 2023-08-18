

<!-- ### Kurulum 
- Install -> Docker Desktop -> https://www.docker.com/products/docker-desktop/
- Register -> Docker Hub -> https://hub.docker.com
- Install -> VSCode Docker Extension -> https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker   
- 
- Docker amaci... tasinabilir sistem altyapisi sunmak.
- toggle
- Docker
- vm 
- 09-09:30 slayt ders anlatimi
- 09:30 kurulum 
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! dockerhub  username:ynsplt   password 782290Yp. #####################
- Docker app kuruldu.
- ikisinde de suan online im.
- Docker app de sol alt taraf yesil olmak zorunda. 
- 09:48 sunumda eksik kalanlari anlatiyor hoca. 
- Data-centerlar da bulunan Dedicated serverlar.(Makinenin tümü) 
- kasanin kendisi Bare Metal
- slot sayisi önemli. kactane disk takabilirim.
- hetzner.com almanyanin en büyük data centerlarindan birisi. 
- VDS (10GbRAM)*5 5 farkli kisiye Toplam dedicated 50GbRAM
- VPS 10 kisiye 4 gb(max) remlik alan verip ortak kullanim aciyor.      Toplam dedicated 16GbRAM 
- 
- 10:35
- her serverin bir IP si vardir.
- bir server icinde cesitli applicationlar var. 
- hep ayni Ip yolluyoruz ama farkli appleri calistirmak icin devreye PORT giriyor. 
- Port 8000 de Django acmak gibi. PORT farkli apllicationlarin addresine ulasmamizi saglar.


#### 80 Port
- default porttur. her adresin sonunda aslinda :80 vardir. 
- 443 SSL icin güvenlik.


#### Terminalde Docker  (hocada docker.md)
- docker --version
- docker version (detayli)
- docker info
- docker --help
- docker help
- docker (command) --help
- docker search (imagename)     docker search python icinde python adi gecen image(resim degil) ara.
- 


- app.py olusturduk.
- in terminal python app.py    _> app.py calistirdik terminalde Hello World! gördük. 
- dockerfile olmak zorunda. uzantiya gerek yok. 
- dockerfile icerisini doldurduk-
- docker.md Image build  kismini yaziyoruz.


#### docker image olusturma
- docker build . --tag my_app
- docker build . -t my_app2 (kisa yol)
- soldaki eklentide görebiliyoruz suan. desktopdaki app de de görebiliyoruz.
- her hangi bi version belirtmessek. latest olarak isaretler. 
- docker olustururken version verme.
- docker build . -t my_app:v2         (ayni isimde farkli versionda olusturdum.)
- Daha önce yapilan islemleri CACH e atti. hafizaya atti. artik yeni comutlar hizli oluyor ve CACH den geliyor. ama ben CACH kullanmadan yapsin istiyorum. asagidaki komut ile. 
- docker build . -t my_app:v4 --no-cache

#### MOLA
- 11:43
- docker image ls  (Tüm imageleri terminalde listeler.) or   docker images
- delete image 
- docker rmi (imagename:version)  -> docker rmi my_app:v2
- with id delete
- docker rmi ab9 (tüm id yazma ilk 3 4 id yeterli. ismi olmadigi icin id ile sildik. idsini docker image ls yaparsak görürüz)
- silinmezse -f (force) kullan
- docker rmi my_app -f
- isim degistirme and copy
- docker tag (oldimagenama) (newimagename) eskisini silmez yenisini olusturur. copy islemide ilur bu yolla. 
- image id leri ayni oluyor bu durumda.
- tüm imageleri tek kalemde silme.
- docker image prune (aktif olmayan tüm imageleri siliyor. yani container acmis olanlari silemez. cach de silinir.)
- docker image prune --help
- docker image prune -a -f yazarsak siler

- container run 
- docker run my_app          docker run my_app:v2
- artik ekrande Hello world gözüküyor CMD python app.py in dockerfile sayesinde. 
- docker run --name (containername) (imagename)

- container listeleme
- docker container ls -a
- docker ps -a

- Container start/stop
- docker start/stop (containername)

- delete container
- docker rm (containername)

- container komple sil
- docker container prune -f (stock konumundaki bütün containerlar silinir..)

- Interactiv mode:
- docker run -it (imagename)
- docker run -it (imagename) sh (shell komutlarini calistiran bir komut.)
- artik dockerin icindeyiz..
- cikmak icin exit -->



















