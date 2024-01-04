# NE PAS TOUCHER
informations = ["lena.fournier@XXXXXXXX.com:fd5a031a8eb1a80132d534d3eddd5134a2ae72bb71bc5b4968f18e1b054f3069","hugo.adam@XXXXXXXX.com:47b99588d6e64d501d368234bb0028682910959b4cfced88824c01b51c105e00","louis.hamon@XXXXXXXX.com:5b7e54eb044b5d501c3f5824d1dc0f7ddce4672ecd2dba1533c1208189103118","sacha.girard@XXXXXXXX.com:a2147bb770a7505fd469ab5b200f8d4b686994a145d8e7e62d0a3620d458977a","christian.chevalier@XXXXXXXX.com:77b408e7d37db8b82c6012eefcfa02a77010632410dc690df657df52587f89c0","aaron.adam@XXXXXXXX.com:9ed84cd62e57033e1315721d05dbdf2447fdecae180fe554a444164a6af602eb","walim.martin@XXXXXXXX.com:37c22e74191344661b59057a381fc7f9a0d060bfc5f7fa90e2f0a253814316a4","nolan.cousin@XXXXXXXX.com:871deb821285ac6127bee23336d91f18669a457043ff02699390a3456ad148ca","alice.gauthier@XXXXXXXX.com:9a871c694e46c70d3b39adf8033f76cc775f4776b32cb12ef659486457b06fb3","kendji.roche@XXXXXXXX.com:c6f1e6ae0f2b907ea6488a2f37b2683dec29a53c2efafd63a8da345e70bd11f9","alix.bernard@XXXXXXXX.com:5952b26791e1070454b45b4c4f6a99467799d55a122479c37a14b4f12ecf18fa","louis.fleury@XXXXXXXX.com:5948ee045b86f7ba41dc5f43a10a16ae94c048c35a91fbbe6878af281b206b23","beatrice.roux@XXXXXXXX.com:646908b2d27ce2a78e60d8f7a9c5a6a85ccc38efbf2f4c6df0ef52dd80fad83a","nolan.silva@XXXXXXXX.com:be8cfd9d3faf8b588bada6f31873e253c9d34b1e46c7e02078fae27d3a818946"]
# NE PAS TOUCHER
import random
import string
import hashlib

alpha=list(string.ascii_uppercase)
for i in informations:
    mdp=""
    firstSplit=i.split(":")
    scdSplit=firstSplit[0].split(".",1)
    prenom=scdSplit[0]
    nom=scdSplit[1].split("@")[0][0:3].upper()
    mdpS=firstSplit[1]
    t=10
    while t>=10 and t<=99:
        for l in  alpha:
            al=str(t)
            maj= l
            mdp=prenom+nom+"@"+al+maj
            sha256_hash = hashlib.new("SHA256")
            sha256_hash.update(mdp.encode())
            mdpH=sha256_hash.hexdigest()
            if mdpH==mdpS:
                print(mdp)
        t+=1
    


