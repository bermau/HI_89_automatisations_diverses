
import pyperclip

from_clipboard  = """X_5FU_CLFD
X_5FUU_CLFD
X_AMISU_CLFD
X_AMOX_CLFD
X_CARB_CLFD
X_CEFA_CLFD
X_CEFO_CLFD
X_CITA_CLFD
X_CLOXA_CLFD
X_CLOZ_CLFD
X_FLUOX_CLFD
X_GUANI_CLFD
X_HYDREA_CLFD
X_ISAVU_CLFD
X_LAMO_CLFD
X_METS_CLFD
X_MIAN_CLFD
X_MIRT_CLFD
X_OLAN_CLFD
X_PHENO_CLFD
X_VENLA_CLFD
"""
lst = from_clipboard.split("\n")
print(lst)

for line in lst:
    print (line)
    pyperclip.copy(line)
    input("next...")





