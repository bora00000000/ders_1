sozcukler = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL": " bir şakaya karşılık cevap",
            "SHEESH": "onaylanmamak",
            "CREEPY": "KORKUNÇ",
            "AGGRO": "agresifleşmek" ,
            }
            
sozcuk = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")


if sozcuk in sozcukler.keys():
    print(sozcukler[sozcuk])
else:
    print("aradğınız kelime mevcut değil")
    
