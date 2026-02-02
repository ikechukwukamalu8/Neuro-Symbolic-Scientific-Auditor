import re, pdfplumber, pandas as pd, glob
from transformers import pipeline, AutoTokenizer, AutoModelForTokenClassification

class ScientificAuditor:
    def __init__(self, kb_path, device=-1):
        self.kb = pd.read_csv(kb_path)
        # Initialize SciBERT
        self.tokenizer = AutoTokenizer.from_pretrained("allenai/scibert_scivocab_uncased")
        self.model = AutoModelForTokenClassification.from_pretrained("allenai/scibert_scivocab_uncased")
        self.ner_nlp = pipeline("ner", model=self.model, tokenizer=self.tokenizer, 
                                aggregation_strategy="simple", device=device)

    def run_audit(self, reports_folder):
        results = []
        files = glob.glob(f"{reports_folder}/*.pdf")
        for file in files:
            with pdfplumber.open(file) as pdf:
                text = "\n".join(p.extract_text() for p in pdf.pages)
                # Find the tech mentioned in the PDF
                tech = next((t for t in self.kb['panel_type'] if t.lower() in text.lower()), "Unknown")
                limit = self.kb[self.kb['panel_type'] == tech]['theoretical_limit'].values[0]
                # Extract % values
                found = [float(x) for x in re.findall(r"(\d{1,2}\.?\d?)\s?%", text)]
                for val in found:
                    results.append({
                        'File': file.split('/')[-1],
                        'Tech': tech,
                        'Claimed_%': val,
                        'Status': 'VALID' if val <= limit else 'IMPOSSIBLE'
                    })
        return pd.DataFrame(results)