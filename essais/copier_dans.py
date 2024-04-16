
import pyperclip
from time import sleep

from_clipboard  = """x_Génital, Urétral
x_LBA, Pulmonaire, Nasal
x_LCR, Biopsie, Urines
x_LBA, Pulm, LCR, Biopsie ... Cong
x_Aspiration naso-pharyngée
x_LBA, Pulmonaire, Pleural T°amb
x_LCR 500 µl minimum
x_Urines 24 h - Echantillon
x_Sang Total EDTA 2 tubes T°amb
x_Sang Total tube STREK T° amb
x_Urines 24 h acid. - Echantillon
x_Selles Echantillon
x_LCR, Sérum Cong
x_Air  expiré
x_Plasma EDTA 3 Aliq. Cong < 6h
x_Sang Total EDTA.
x_Sérum GEL à décanter (pas pneum)
x_Plasma EDTA 
x_Sang Total EDTA sur Buvard
x_LCR, Pulm, Urines, biopsies
x_Plasma EDTA 2 tubes Cong < 2h
x_Sérum GEL Cong < 2h (pas pneum)
x_Sérum GEL 2 tubes Cong
x_Urines 24 h acid.50 ml
x_Sérum GEL à décanter
x_Sang Total Hép. SS Cong
x_Sérum GEL + Plasma citraté Cong
x_LBA, Pulmonaire, Pleural, LCR, Urine
x_Sérum SS Cong < 2h Abri lum
x_Sang Total Hép. SS
x_Plasma Hép. GEL à décanter
x_Plasma Hép. sans GEL
x_Sang Total (Tube Bleu Roi)
xxx_OLD_Calculs Temp. Ambiante
x_Urines 1ère miction (2 Aliq) Cong <1h
x_Plasma Citraté Cong
x_Sérum SS 2 tubes Cong < 2h
xxx_OLD_Liquide de ponction CLFD
x_Sérum SS
x_Sérum GEL 2 tubes T°amb
x_Plasma Hép. SS 2 tubes Cong <1h
x_Urines fraiches 50 ml (pot stérile) CO
x_Urines fraiches
x_Plasma Hép. GEL Cong <1h
x_Plasma Citraté 5 Aliq. Cong < 6h
x_Sang Total EDTA 3 tubes T°amb
x_Sang Total Citrate T°amb
xxx_OLD_Liquide de ponction décanté/cong
x_Liquide de ponction   Pot / Tube Blanc
x_Sang Total EDTA 2 tubes Cong
x_Urines 1ère miction ou Diurèse 24h
x_Selles de 24h (totalité)
x_LCR T°amb
x_Moelle EDTA+Sérum gel+Sg EDTA
x_Sg Total/Moëlle/Biopsie EDTA x3 T°amb
x_Sérum SS Cong
x_Plasma Hép. SS ou     Sérum SS   Cong
x_Plasma (Tube Bleu Roi) Cong
x_LBA pot stérile
x_Sérum GEL Cong < 1h
x_LCR PP -80°C
x_w_ESSAI_ABCDEFGHIJKLMNOPQRSTUVWXYZ1234
x_Urines Fraîches Cong <1h
x_Plasma EDTA + Aprotinine Cong
x_Urines 1ère miction Abri lumière
xxx_OLD_LCR_CLFD
x_LCR_Frigo +4°C
x_Biopsie,Ponction,LCR -20°C
x_Plasma Citraté 2 Aliq. centri 37°C
x_Sérum SS 2 tubes 37°C
x_Calcul urinaire-vésical Pot stérile
x_Sang Total EDTA 2 tubes
x_Urines fraiches 2 tubes Cong
x_Sérum GEL T°amb
x_Sérum GEL à décanter Cong < 4h
x_PCR, Sang total EDTA  Cong
xxx_OLD_Liquide de ponction à décanter e
x_PCR, Sang total EDTA
x_PCR, Plasma EDTA  Cong
x_Sang Total EDTA + Plasma EDTA x2 Cong
"""
lst = from_clipboard.split("\n")
print(lst)

for line in lst:
    print (line)
    pyperclip.copy(line)

    sleep(5)





