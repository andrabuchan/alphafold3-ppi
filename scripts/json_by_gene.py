#!/usr/bin/python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input")
parser.add_argument("-o", "--output_dir")
args = parser.parse_args()
	
infile = args.input
outdir = args.output_dir

seqdict={}
key=""
val=""

with open(infile, 'r') as faa:
	for line in faa:
		if line.startswith(">") and len(val) == 0:
			key = line[1:].strip()
		elif not line.startswith(">") and len(key) != 0:	
			val += line.strip()
		elif (line.startswith(">") or False) and len(val) > 0:
			val = val.strip("*")
			seqdict.update({key:val})
			key = line[1:].strip()
			val=""

def makejson(filename, key1, seq1):
	outfile = f"{outdir}/{filename}.json"
	with open(outfile, 'w') as output:
		output.write("{\n")
		output.write(f"  \"name\": \"{key1}\",\n")
		output.write("  \"sequences\": [\n")
		output.write("    {\n")
		output.write("      \"protein\": {\n")
		output.write(f"        \"id\": [\"A\"],\n")
		output.write(f"        \"sequence\": \"{seq1}\"\n")
		output.write("      }\n")
		output.write("    }\n")
		output.write("  ],\n")
		output.write("  \"modelSeeds\": [1],\n")
		output.write("  \"dialect\": \"alphafold3\",\n")
		output.write("  \"version\": 1\n")
		output.write("}\n")

for i in range(0, len(seqdict)):
	i_key = list(seqdict.keys())[i]
	i_val = list(seqdict.values())[i]
	out = "contig_" + str(i+1)
	makejson(out, i_key, i_val)
