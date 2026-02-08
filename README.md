# Genome Annotation and RNA-seq Analysis Project  
---

## How to Run the Code

### 1. Gene Count & Common/Specific Genes Analysis
Run the following command after placing GTF files in the `data/` directory:

bash
python scripts/gene_count.py

### Week-by-Week Bioinformatics Workflow (8 Weeks)

## Project Overview
This repository documents a week-by-week bioinformatics workflow focused on
RNA-seq data processing and large-scale genome annotation across multiple species.
The project involves quality control of sequencing data, genome preparation,
chromosome-level scaffolding, and reference-based gene annotation using established
bioinformatics tools.

This work was carried out as part of a research internship/training at  
**National Institute of Animal Biotechnology (NIAB), Hyderabad**,  
under the guidance of **Dr. Shailesh Sharma (Scientist F)**.

---

## Dataset Summary
- Chicken genomes analyzed: 45–50
- Sheep genomes analyzed: multiple breeds
- Genome assembly levels:
  - Chromosome-level assemblies
  - Non-chromosome-level assemblies (scaffolded where required)

---

## Tools & Software Used
- FastQC – RNA-seq quality assessment  
- fastp – Read preprocessing and quality filtering  
- RagTag – Chromosome-level scaffolding  
- Liftoff – Reference-based gene annotation transfer  
- Linux command line  
- Excel – Metadata and annotation availability tracking  

---

## Week-wise Work Summary

### Week 1 – RNA-seq Data Preparation (21 December)
- Downloaded and extracted RNA-seq sample data
- Performed quality assessment using FastQC
- Reviewed FastQC reports to evaluate read quality
- Installed fastp for read preprocessing
- Downloaded chicken reference genome
- Compiled an Excel sheet of livestock genomes and GTF annotation availability
- Explored tools and resources for GTF file generation

---

### Week 2 – Annotation Planning & Preprocessing (28 December)
- Continued RNA-seq data handling and quality analysis
- Explored fastp for read preprocessing
- Organized reference genome files
- Investigated annotation availability across livestock genomes
- Studied tools and workflows for generating missing GTF files
- Planned read mapping and annotation steps

---

### Week 3 – Chromosome Scaffolding & Liftoff Testing (4 January)
- Analyzed assembly status of 45 chicken genomes
- Identified non-chromosome-level assembled breeds
- Performed chromosome-level scaffolding using RagTag
  - Fayoumi genome scaffolded using Red Jungle Fowl and White Leghorn references
  - Consistent result of 34 chromosomes obtained
- Ran Liftoff successfully on chromosome 1 (Red Jungle Fowl → White Leghorn)
- Identified system resource limitations and planned chromosome-wise execution

---

### Week 4 – Large-scale Chicken Genome Annotation (11 January)
- Identified 19 chromosome-level assembled chicken breeds
- Completed Liftoff annotation for all 19 breeds
- Generated GTF files for 6 chicken breeds lacking annotations
  using an alternative reference genome (pig)
- Validated cross-reference annotation strategy

---

### Week 5 – Multi-species Genome Annotation (18 January)
- Generated unique GTF/GFF3 annotation files for 20 chromosome-level chicken breeds
- Extended the annotation workflow to sheep genomes
- Used sheep reference genome and GTF files to annotate 7 sheep breeds
- Established a reusable cross-species genome annotation pipeline

---

### Week 6 – Genome Annotation Expansion (25 January)

- Generated GTF/GFF3 annotation files for all sheep breeds with available chromosome-level genome assemblies  
- Completed reference-based annotation transfer for sheep genomes  
- Generated GTF/GFF3 files for 10 goat breeds using goat reference FASTA and GTF files  
- Prepared annotated datasets for downstream comparative analysis  

---

### Week 7 – Gene-Level Comparative Analysis (1 February)

- Generated GTF files for 22 goat species  
- Developed a custom Python script for gene-level analysis  
- Performed:
  - Total gene count calculation per species  
  - Identification of common genes across species  
  - Identification of breed/species-specific genes  
  - Extraction and recording of gene names  
- Compiled all outputs into structured Excel files  
- Generated an UpSet plot to visualize total, common, and breed-specific gene distributions  

---

### Week 8 – Multi-Species Analysis & Visualization Refinement (7 February)

- Generated GTF files for different goat breeds  
- Performed gene count analysis for pig, identifying common and species-specific genes  
- Organized all results into Excel datasets  
- Generated an UpSet plot for gene overlap visualization  
- Identified limitations in the current visualization and initiated refinement  
- Extended the workflow to sheep and goat comparative analysis  
- Initiated GTF file generation for cow and buffalo datasets
---

## Key Outcomes
- Established a complete RNA-seq preprocessing and genome annotation workflow
- Generated GTF/GFF3 files for multiple chicken and sheep breeds
- Successfully applied chromosome-level scaffolding and annotation transfer
- Maintained detailed week-by-week documentation for reproducibility

---

## Current Status

✔ Genome annotation and GTF/GFF3 generation completed for multiple livestock species (chicken, sheep, goat, pig)  
✔ Chromosome-level genome assemblies successfully utilized where available  
✔ Gene-level analysis performed to identify total, common, and species-specific genes  
✔ Results systematically compiled into Excel datasets for interpretation  
✔ UpSet plots generated to visualize gene overlaps across species  
✔ A reusable multi-species genome annotation and analysis workflow established

---

## Future Work

• Extend genome annotation and comparative analysis to additional livestock species (cow, buffalo)  
• Refine and optimize UpSet and other visualization methods for clearer interpretation  
• Integrate downstream RNA-seq analysis with comparative genomics results  
• Perform functional annotation and biological interpretation of common and species-specific genes  
• Prepare the workflow and results for publication-quality analysis

---

## Author & Affiliation
**Anisha Vishwakarma**  
MSc Biotechnology | Aspiring Bioinformatician  

**Affiliation:**  
National Institute of Animal Biotechnology (NIAB), Hyderabad  

**Supervisor:**  
Dr. Shailesh Sharma, Scientist F  
