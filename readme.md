# Güvenlik Otomasyonu Video Serisi - 3
 ## API, Postman ve Python ile Firewall'a Otomatik Kural Yazıyoruz // API Nedir, Nasıl Kullanılır?
 
Bir çok güvenlik ürünü artık otomasyon için belli API'lar sunmaya başladı. Ancak hepimizin aklında aynı soru var: API nedir, neden ve nasıl kullanılır? Güvenlik otomasyonunda API'ın yeri nedir? Derdimi anlatacak kadar Python biliyorsam, bu API'lar ile otomasyon yazmaya yeter mi?

Bu bölümümüzde, asıl işi programlama olmayan biz güvenlik uzmanları için pratik araçları kullanarak API'lar üzerinden nasıl güvenlik otomasyon akışları yazabileceğimizi konuşacağız. Örnek senaryomuzda, Postman adlı aracı kullanarak API'lar üzerinden Firewall'umuzda kural güncelleyecek bir script oluşturacak, farklı marka olan endpoint security ve firewall ürünlerini ek bir ürüne ihtiyaç duymaksızın birbirine bağlayacağız. 

Örnek Senaryo: Şirket, çalışanlarının üzerinde güvenlik yazılımı olmayan bilgisayarlarını VPN üzerinden şirket ağına bağlamaya izin vermiş. Bağlanan kişisel bilgisayarlardan birinde, LAN'daki diğer bilgisayarlara yayılım yapan bir zararlı yazılım mevcut. Endpoint security'nin zararlı yazılım yayılım tespitinin ardından, otomatik olarak bir script çalıştırılsın ve firewall üzerindeki VPN'den LAN'a olan trafiği kontrol eden Access Rule'u trafiği "deny" edecek şekilde güncellesin istiyoruz.  

Video linki: https://youtu.be/BbR8vMu-sjA

### Videoda kullanılan script'ler:
* otomasyon.py --> Firewall API'ını kullanarak login olan, kural güncelleyen, değişiklikleri commit edip logout olan script.
* denyscriptim.log --> Otomasyon.py dosyasının oluşturduğu olay log'u.

### Videoda kullanılan ilgili adresler:
* Postman: https://www.postman.com
* PYCharm: https://www.jetbrains.com/pycharm/download/
* W3Schools - Python Requests: https://www.w3schools.com/python/module_requests.asp
* W3Schools - HTTP Request Methods: https://www.w3schools.com/tags/ref_httpmethods.asp
* Palo Alto PAN OS için API Reference Guide: https://docs.paloaltonetworks.com/pan-os/9-0/pan-os-panorama-api.html
* Fortinet FortiManager API Reference Guide: https://help.fortinet.com/fweb-mgr/601/api_html/
* Sonicwall API Reference Guide: https://www.sonicwall.com/techdocs/pdf/sonicos-6-5-4-api-reference-guide.pdf
* (Checkpoint için) VPN Compliance Control konfigürasyonu: https://sc1.checkpoint.com/documents/R80.40/WebAdminGuides/EN/CP_R80.40_SecurityManagement_AdminGuide/Content/Topics-SECMG/Compliance-Check.htm
* Logging in Python: https://docs.python.org/3/library/logging.html
* Python PyInstaller: https://pyinstaller.readthedocs.io/en/stable/usage.html
