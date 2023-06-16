import subprocess
import os


#output_prefix = "results"

dir_path= "./pseudomonas_phage"

for fasta_file in os.listdir(dir_path):
    results = fasta_file[:-6] 
    command = f'python3 acranker.py ./pseudomonas_phage/{fasta_file} ./pseudomonas_result/{results}'
    print(command)
    result = subprocess.Popen(command, shell=True).communicate()
    #print(result)

#stdout, stderr = result.communicate()
