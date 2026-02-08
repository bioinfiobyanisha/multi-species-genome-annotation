import matplotlib.pyplot as plt
from upsetplot import UpSet, from_contents

def extract_genes(gtf_file):
    genes = set()
    with open(gtf_file) as f:
        for line in f:
            if line.startswith("#"):
                continue
            fields = line.strip().split("\t")
            if fields[2] == "gene":
                for attr in fields[8].split(";"):
                    if "gene_id" in attr:
                        genes.add(attr.split('"')[1])
    return genes


gtf_files = {
    "Chicken": "data/chicken.gtf",
    "Sheep": "data/sheep.gtf",
    "Goat": "data/goat.gtf",
    "Pig": "data/pig.gtf"
}

gene_data = {sp: extract_genes(gtf) for sp, gtf in gtf_files.items()}

upset_data = from_contents(gene_data)

plt.figure(figsize=(10, 6))
UpSet(
    upset_data,
    show_counts=True,
    sort_by="cardinality"
).plot()

plt.title("Gene Overlap Across Species")
plt.savefig("results/upset_plot.png", dpi=300)
plt.show()

print("📊 UpSet plot generated")
