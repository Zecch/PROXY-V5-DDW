import requests
import time
from colorama import init, Fore, Back, Style


init()


print(Fore.GREEN + "WELCOME TO")

time.sleep(4)


print(Back.BLACK + "DDW V5 PROXY")

time.sleep(5)



print(Back.BLACK + "Tiktok: swipeddw")

time.sleep(4)


print("[+] Iniciando Proceso")

time.sleep(9.5)

print("[+] Correcto ")

print("[+] Buscando Proxys en la base de datos")

time.sleep(10.5)

print("[+] Proxys Encontradas")

time.sleep(5.9)

print("[+] Iniciando Transferencia")


time.sleep(5.9)

def download_proxies(url, output_file):
    try:
        # Make a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Extract the file name from the URL
            file_name = url.split("/")[-1].split(".")[0]

            # Open the file in write mode and write the proxies
            with open(f"{output_file}_{file_name}.txt", 'w') as file:
                file.write(response.text)
            print(f"[+] Se instalaron las proxys correctamente se guardaron en  {output_file}_{file_name}.txt")
            
            time.sleep(5.9)
         
        else:
            print(f"[+] No se pudo descargar las proxys por un error en{url}. Status code: {response.status_code}")

    except Exception as e:
        print(f"[-] Ocurrio un error: {str(e)}")

if __name__ == "__main__":
    # List of proxy URLs and their corresponding output file names
    proxy_urls = [
        ("https://proxyspace.pro/https.txt", "https"),
        ("https://proxyspace.pro/socks4.txt", "socks4"),
        ("https://proxyspace.pro/socks5.txt", "socks5"),
        ("https://proxyspace.pro/http.txt", "http"),
    ]

    for url, name in proxy_urls:
        # Call the function to download and save proxies
        download_proxies(url, name)

