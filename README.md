# 🧬 DNA ORF Finder

A lightweight Python tool to analyze DNA sequences and identify **Open Reading Frames (ORFs)**.

Whether you're studying genetics, learning bioinformatics, or building something scientific, this tool helps you classify sequences and find possible protein-coding regions with clarity.

---

## 🚀 Features

- ✅ Reads DNA sequences from a file  
- ✅ Detects and classifies DNA vs. RNA  
- ✅ Finds the **first valid ORF** (from ATG to a stop codon)  
- ✅ Scans for **all potential ORFs** across the sequence  
- ✅ Skips duplicates, allows overlaps  
- ✅ Handles invalid input gracefully  

---

## 🧪 How It Works

1. Input a plain text file with a raw DNA sequence.
2. The script:
   - Strips whitespace
   - Validates content
   - Locates ATG start codons and TAA/TAG/TGA stop codons
   - Outputs positions and sequences of found ORFs

---

📌 Notes
Only uppercase DNA letters (A, T, G, C) are considered valid.

Make sure your file is clean: no FASTA formatting or weird characters.

Stop codons must be in-frame with the start codon to count.

---

## 📂 Example Usage

```bash
$ python orf_finder.py
Enter the full path to the DNA sequence file: ./sample_sequence.txt
```

👩‍🔬 Created By
Elif M. — a biomedical scientist with a love for code 🧬💻
