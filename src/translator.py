import sys
from Bio.Seq import Seq
from translaterror import TranslatError


def Sequences(input_dna_seq):
	try:
		if(len(input_dna_seq)>=3 & len(input_dna_seq)%3 == 0):
			dna_seq = Seq(input_dna_seq)
			print("DNA seq: {}".format(dna_seq))
			rna_seq = dna_seq.transcribe()
			print("mRNA seq: {}".format(rna_seq))
			prot_seq = dna_seq.translate()
			print("Protein seq: {}".format(prot_seq))
			return prot_seq
		else:
			raise TranslatError("Something is wrong, check sequence!")

	except TranslatError as te:
		print(te)
		print("Translation did not happen!")


def main():
	Sequences(sys.argv[1])

if __name__ == '__main__':
	main()