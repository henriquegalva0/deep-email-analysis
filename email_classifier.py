import pandas as pd
from datasets import Dataset
from transformers import BertTokenizerFast, BertForSequenceClassification, Trainer, TrainingArguments
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

tokenizer = BertTokenizerFast.from_pretrained("bert-base-uncased")

# 1. Carregar o dataset
df = pd.read_csv("data/emails.csv")
le = LabelEncoder()
df['label'] = le.fit_transform(df['label'])  # phishing = 1, legitimo = 0

# Corrigir tipo de texto
df['body'] = df['body'].astype(str)

# Separar
train_df, test_df = train_test_split(df, test_size=0.2)
train_ds = Dataset.from_pandas(train_df[["body", "label"]])
test_ds = Dataset.from_pandas(test_df[["body", "label"]])

# Tokenização segura
def tokenize(batch):
    textos = [str(x) for x in batch["body"]]
    return tokenizer(textos, padding="max_length", truncation=True, max_length=256)

train_ds = train_ds.map(tokenize, batched=True)
test_ds = test_ds.map(tokenize, batched=True)


# 5. Modelo
model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)

# 6. Argumentos de treinamento
training_args = TrainingArguments(
    output_dir="model/",
    evaluation_strategy="epoch",
    save_strategy="epoch",
    logging_dir="./logs",
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=2,
    weight_decay=0.01,
    logging_steps=10,
    save_total_limit=2,
)

# 7. Treinamento
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_ds,
    eval_dataset=test_ds,
)

trainer.train()

# 8. Salvar modelo
model.save_pretrained("model/")
tokenizer.save_pretrained("model/")