# NE PAS TOUCHER
code = "7912072481150294082409449910713578666450253"
echantillons = ["5553657995917996:phhhi", "444841597818610281013:rhqx", "5541536725892565:vqxit", "4780204865254909031208374:watk", "44362252420088611:ucgf","44743652944904811:ldsb","76901535222394498713990891655:lwdappr","8356218178448272126858200180603967075829608203935:skkshfar","768285422591857946866510173799947329:jjpofnj","4882679262332999981668104:fsvi"]
import string
decode=""
lgr=int((len(code)-1))
alpha=list(string.ascii_lowercase)
diviseur=int(code[0])
digit=int(lgr/diviseur)
for i in range(1,len(code)-1,digit):
    value=int(code[i:i+digit])%26
    decode=decode+alpha[value]
print(decode)

    
