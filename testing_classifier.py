from transformers import BertTokenizerFast, BertForSequenceClassification
import torch

# Carregar modelo
tokenizer = BertTokenizerFast.from_pretrained("model/")
model = BertForSequenceClassification.from_pretrained("model/")
model.eval()

def classificar_email(texto):
    inputs = tokenizer(texto, return_tensors="pt", truncation=True, padding="max_length", max_length=256)
    with torch.no_grad():
        outputs = model(**inputs)
    probs = torch.nn.functional.softmax(outputs.logits, dim=1)
    classe = torch.argmax(probs).item()
    return "phishing" if classe == 1 else "legítimo"

email_teste=""

# Teste
print(classificar_email(email_teste))