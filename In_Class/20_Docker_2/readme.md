<!-- Hocanin notlari -->

# Docker

## Yüklemeler:

* Docker Desktop -> https://www.docker.com/products/docker-desktop/
    * Windows ve Macos için setup dosyası mevcut.
    * Linux sistemlere CLI üzerinden kurulum yapılabilir. -> https://docs.docker.com/desktop/install/linux-install/

* Docker Hub -> https://hub.docker.com

* VSCode Docker Extension -> https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker

---

# Server Systems

* Physical Servers (BareMetal Servers):
    * Bilgisayar -> Yüksek donanım, özel işlemciler, özel işletim sistemleri.
    * Kurulum: zor
    * VeriTaşıma: zor
    * Maliyet: yüksek
    * Dedicated Servers

* Virtual Servers (VMs: Virtual Machines):
    * Bir fiziksel makina içinde çok sanal makina.
    * Kurulum: orta (iso image)
    * VeriTaşıma: orta
    * Maliyet: orta
    * Bir makiaden diğer makinaya geçiş zorluğu.
    * Hypervisor yazılımları -> vmware.com
    * VPS (Virtual Private Server), VDS (Virtual Dedicated Server)

* Containers:
    * Bir fiziksel/sanal makina içinde çok konteyner.
    * Kurulum: kolay (docker image)
    * VeriTaşıma: kolay
    * Maliyet: düşük
    * Tüm konteynerları aynı ortamdan yönetebilme.
    * Microservice mimarisi.
    * Container yazılımları -> docker.com

## Temel Bilgiler

* IP ve Port mantığı
* Default portlar 80 443 -> https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers
* http -> 80 * http://clarusway.com == http://clarusway.com:80
* https -> 443 * https://clarusway.com == https://clarusway.com:443 (need SSL)


<!-- benim notlarim
- pull ettigimizde backend ve frontend filelari vardi. 
- dersin amaci frontend ve backend i birlestirmek.
- docker build ./backend -t backend_1
- bash e gectikten sonra not powershell
- docker run --name backend_1 backend_1    first backend_1 container name, other is image name.
- docker run  (kapali kuru icinde calisir)
- docker run -p 8000:8000 --name con_1 backend_1
- docker run -d -p 8000:8000 --name con_2 backend_1      (-d - terminali mesgul etmeden calistirir devam kod yazabilirim)
- docker container ls    (calisan containerlari gösterir)





 -->