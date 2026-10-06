...
import sys
import json
import requests

url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=43283daa645b0be3112bdc780157faf119ed600398e66a2fe535474a5e47cdc3"

try:

    response = requests.get(url)
    data = response.json()
    #print(data)

except requests.RequestException:
    sys.exit("Error al conectar con la API de CoinCap")



try: 

   
    if len(sys.argv) >= 2:

        valor = sys.argv[1]
        
        
        valorfloat = float(valor)
        
        datas=data.get("data")
        datas=datas.get("priceUsd")


        datas = float(datas)
        amount = valorfloat*datas

        print(f"${amount:,.4f}")

    else: 

        print("Missing command-line argument")

except EOFError:

    print("")
            
except ZeroDivisionError:
        
    print("")
        
except ValueError:
        
    print("Command-line argument is not a number")

except TypeError:

    print("")