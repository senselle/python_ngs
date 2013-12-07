#!/usr/bin/python
import sys
import os


#ssh s_elle@195.70.204.3

#dobi2014

def pipeline(SRR):
  name=os.path.basename(SRR[:-4])
  steps=[ 
   'wget %s' % SRR,
   'fastq-dump --split-files %s' % os.path.basename(SRR),
   '/home/akomissarov/libs/FastQC/fastqc -t 30 -o /home/bioinf/public/results/sc %s%s %s%s' % (name, "-1.fastq", name, "-2.fastq"),
   'java -jar /home/akomissarov/libs/Trimmomatic-0.30/trimmomatic-0.30.jar PE -phred33 %s%s %s%s %s%s %s%s %s%s %s%s %s' \
            % (name, "-1.fastq", name, "-2.fastq", name, "_1_paired.fq.gz", name, "_1_unpaired.fq.gz", name, "_2_paired.fq.gz", name, "_2_unpaired.fq.gz", \
             "ILLUMINACLIP:/home/akomissarov/libs/Trimmomatic-0.30/adapters/TruSeq3-PE.fa:2:30:10 TRAILING:20 MINLEN:36"),
   '/home/akomissarov/libs/FastQC/fastqc -t 30 -o /home/bioinf/public/results/sc %s%s %s%s' % (name, "-1.fastq", name, "-2.fastq"),
   'gunzip %s%s' % (name, "_1_unpaired.fq.gz"),
   'gunzip %s%s' % (name, "_2_unpaired.fq.gz"),
   'cat %s%s %s%s %s %s%s' % (name, "_1_unpaired.fq", name, "_1_unpaired.fq", ">", name, "_unpaired_merged.fastq"),
   '/home/akomissarov/libs/FastQC/fastqc -t 30 -o /home/bioinf/public/results/sc %s%s' % (name, "_unpaired_merged.fastq"),
   'tophat -o %s%s %s %s%s %s%s %s%s' % (name, ".sam", "/home/s_elle/bt2_S288C/bt2_S288C", name, "_1_paired.fq.gz", name, "_2_paired.fq.gz", name, "_unpaired_merged.fastq")]


  for i in steps: 
   #os.system(i)
   print i
  return()

if  __name__ == '__main__':
#pipeline(sys.argv[1])

 pipeline("ftp://ftp-trace.ncbi.nlm.nih.gov/sra/sra-instant/reads/ByRun/sra/SRR/SRR453/SRR453569/SRR453569.sra")

