from Bio import SeqIO
import sys

#Check argomenti
if len(sys.argv)!=3:
    print("Argomenti non validi")

#Argomenti passati
print("Analisi file: ", sys.argv[1])
print("Soglia qualità: ", sys.argv[2])

#Read Totali
count = 0
for rec in SeqIO.parse(sys.argv[1], "fastq"):
    count += 1
print("Read Totali: ", count)

#Read filtrati
good_reads = (rec for rec in SeqIO.parse(sys.argv[1], "fastq") if min(rec.letter_annotations["phred_quality"]) >= int(sys.argv[2]))
good_count = SeqIO.write(good_reads, "good_quality.fastq", "fastq")
print("Salvati %i reads" % good_count)