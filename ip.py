import requests

def get_ip_address(url):
  """
  Bir web sitesinin IP adresini alır.

  Parametreler:
    url: IP adresi alınacak web sitesinin URL'si.

  Dönüş Değeri:
    Web sitesinin IP adresi.
  """

  try:
    response = requests.get(f"https://check-host.net/ip/{url}")
    return response.text
  except:
    return None

# Kullanıcıdan URL girmesini iste
url = input("IP adresini bulmak istediğiniz web sitesinin URL'sini girin: ")

# IP adresini al
ip_address = get_ip_address(url)

# IP adresini yazdır
if ip_address:
  print(f"Web sitesinin IP adresi: {ip_address}")
else:
  print(f"IP adresi alınamadı.")
