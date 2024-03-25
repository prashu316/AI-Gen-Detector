import pandas as pd
import os
import re

# Get the current working directory
current_directory = os.getcwd()

# Define the file path relative to the current directory
file_path = os.path.join(current_directory, "datasets", "reviews_music.xml")

# Initialize lists to store data
review_texts = []

# Parse XML data
with open(file_path, "r", encoding="ISO-8859-1") as file:
    for line in file:
        if line.strip().startswith('<review>'):
            # Start parsing a new review
            review_text = []
            review_text.append(line.strip())
        elif line.strip().startswith('</review>'):
            # End parsing the review, append the review text to the list
            review_text.append(line.strip())
            review_texts.append("".join(review_text))
        elif review_text:
            # Continue parsing review text
            review_text.append(line.strip())

# Create pandas DataFrame
df = pd.DataFrame({"Review Text": review_texts})

# Function to extract text between review text tags
def extract_review_text(text):
    # Regular expression to match text between review text tags
    match = re.search(r'<review_text>(.*?)</review_text>', text, re.DOTALL)
    if match:
        return match.group(1)
    else:
        return None

# Apply the function to every entry in the DataFrame
df["Review Text"] = df["Review Text"].apply(extract_review_text)

# Display DataFrame
print(df)

#df.to_csv("datasets/processed_xml_reviews_human_music.csv")