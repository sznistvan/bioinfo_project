import sys
from Bio.Seq import Seq
from translaterror import TranslatError

try:
	if(len(sys.argv[1])>=3 & len(sys.argv[1])%3 == 0):
		dna_seq = Seq(sys.argv[1])
		print("DNA seq: {}".format(dna_seq))
		rna_seq = dna_seq.transcribe()
		print("mRNA seq: {}".format(rna_seq))
		prot_seq = dna_seq.translate()
		print("Protein seq: {}".format(prot_seq))
	else:
		raise TranslatError("Something is wrong, check sequence!")

except TranslatError as te:
	print(te)
	print("Translation did not happen!")

