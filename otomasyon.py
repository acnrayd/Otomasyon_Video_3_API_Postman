### Test amacli API otomasyon script'i, Caner Aydin Youtube kanali icin hazirladim.
## Bu script, Sonicwall marka bir firewall'a API uzerinden mudahale eden bir scripttir.

import requests ## HTTP Request'leri yapabilecegimiz modulumuz.
import logging ## Loglama ozelligini kullanacagimiz modulumuz.

url = "https://192.168.2.1/api/sonicos/auth" ## URL degiskenleri HTTP Request'i gonderecegimiz URL'i isaret ediyor.

## logging.info ile isaretli kisimlarin sonucunu denyscriptim.log dosyasi icine yazacak.
logging.basicConfig(filename='denyscriptim.log', level=logging.INFO)

## Logging modulu "append" mantiginda calisiyor, her yeni log geldiginde dosyanin en altina ekler.
## İleride log dosya boyutu sismesin diye onlem almak isteyebilirsiniz. Ben su an almadim.

payload={}

# Header'lar icerisinde auth bilgilerini ve uretici spesifik header'lari ekliyoruz.
# Sonicwall spesifik header'lar asagidaki sekilde - Auth kisminda kullanici adi sifrenizi degistirin tabii.

headers = {
  'Authorization': 'Basic QVBJdGVzdDpUZXN0MTIzISE=', ## ONEMLİ: (Base64 encoded bile olsa) Giris bilgilerinizi benim gibi script icine gommeyin derim.
  'Accept-Encoding': '*/*', ## Gelen cevabin encoding'i ne olursa olsun kabul edecek.
  'Accept': '*/*', ## Gelen cevap ne olursa olsun kabul edecek.
  'Content-Type': "application/json" ## Gonderilen request body'sinin JSON formatinda oldugunu belirtir.
}

response = requests.request("POST", url, headers=headers, data=payload, verify = False)
## verify = False notu ile SSL sertifika dogrulamasini iptal ettik.
## Prod ortaminda verify = False kullanmaniz guvenlik acigi dogurabilir.

print(response.text) ## Gelen response'u ekrana basacak.
logging.info(response.text) ## Gelen response'u log dosyasina yazacak.

## Buradan sonraki kisim ayni script'in farkli amaclar icin modifiye edilmiş halleri.


##### Firewall'da access rule'u update eden script.
url = "https://192.168.2.1/api/sonicos/access-rules/ipv4/uuid/b2c4028a-6982-11a4-0700-18b1690dbe88"

payload2="{\n    \"access_rule\": {\n        \"ipv4\": {\n            \"action\": \"deny\"\n        }\n    }\n}"

response2 = requests.request("PUT", url, headers=headers, data=payload2, verify = False)

print(response2.text)
logging.info(response2.text)

##### Firewall'daki degisiklikleri commit eden script.

url = "https://192.168.2.1/api/sonicos/config/pending"

payload3={}

response3 = requests.request("POST", url, headers=headers, data=payload3, verify = False)

print(response3.text)
logging.info(response3.text)


###### Firewall'dan logout olan script.

url = "https://192.168.2.1/api/sonicos/auth"

payload4={}


response4 = requests.request("DELETE", url, headers=headers, data=payload4, verify = False)

print(response4.text)
logging.info(response4.text)
