import re

# Read the original sequence
with open("preproinsulin-seq.txt", "r") as file:
    sequence = file.read()

# Keep only lowercase amino-acid letters
clean_sequence = re.sub(r"[^a-z]", "", sequence)

# Verify the length
print("Preproinsulin length:", len(clean_sequence))

if len(clean_sequence) == 110:
    print("Success: sequence contains 110 amino acids.")
else:
    print("Error: sequence should contain 110 amino acids.")

# Save the cleaned sequence
with open("preproinsulin-seq-clean.txt", "w") as file:
    file.write(clean_sequence)

# Extract the insulin chains
lsinsulin = clean_sequence[0:24]
binsulin = clean_sequence[24:54]
cinsulin = clean_sequence[54:89]
ainsulin = clean_sequence[89:110]

# Save each sequence
with open("lsinsulin-seq-clean.txt", "w") as file:
    file.write(lsinsulin)

with open("binsulin-seq-clean.txt", "w") as file:
    file.write(binsulin)

with open("cinsulin-seq-clean.txt", "w") as file:
    file.write(cinsulin)

with open("ainsulin-seq-clean.txt", "w") as file:
    file.write(ainsulin)

# Verify lengths
print("lsinsulin:", len(lsinsulin))
print("binsulin:", len(binsulin))
print("cinsulin:", len(cinsulin))
print("ainsulin:", len(ainsulin))