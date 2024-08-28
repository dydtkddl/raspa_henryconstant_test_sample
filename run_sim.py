import pandas as pd 
import numpy as np 
import os 
import subprocess
import ast 

df = pd.read_csv("test_input_sample.csv")
l = []
for i in range(len(df)):
    row = df.iloc[i]
    with open("Input_HenryCoefficient.txt", "r") as f:
        txt = f.read()
    ASRCIF = row["ASRCIF"]
    ASRCIF_UCELL = row["ASR_UCELL"].replace("(", "").replace(")", "").replace("," , "")
    txt = txt.replace("{Forcefield}", row["FORCE_FIELD_DIR"])
    txt = txt.replace("{MoleculeDefinition}", ast.literal_eval(row["MOLECULEDIR"])["CO2"])
    txt = txt.replace("{MOF}", ASRCIF)
    txt = txt.replace("{countABC}", ASRCIF_UCELL)
    ## 서브프로세스
    with open("simulation.input", "w") as f:
        f.write(txt)
    subprocess.run("sh run simulation.input")
    with open("Input_HenryCoefficient.txt", "r") as f:
        txt = f.read()
    FSRCIF = row["FSRCIF"]
    FSRCIF_UCELL = row["FSR_UCELL"].replace("(", "").replace(")", "").replace("," , "")
    txt = txt.replace("{Forcefield}", row["FORCE_FIELD_DIR"])
    txt = txt.replace("{MoleculeDefinition}", ast.literal_eval(row["MOLECULEDIR"])["CO2"])
    txt = txt.replace("{MOF}", FSRCIF)
    txt = txt.replace("{countABC}",FSRCIF_UCELL)
    ## 서브프로세스    
    with open("simulation.input", "w") as f:
        f.write(txt)
    subprocess.run("sh run simulation.input")
    