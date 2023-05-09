import torch
from transformers import BertTokenizer, BertModel
import os
import numpy as np


class BERTEmebddingGenerator():
    def __init__(self,model, device):
        self.model=model
        self.device=device
    
    def get_embeddings(self,text):
        tokenizer=BertTokenizer.from_pretrained(self.model)
        model=BertModel.from_pretrained(self.model)
        tokens=tokenizer.encode_plus(
        text,
        add_special_tokens=True,
        padding='max_length',
        max_length=128,
        truncation=True,
        return_tensors='pt'
        )
        tokens=tokens.to(self.device)
        model=model.to(self.device)
        with torch.no_grad():
            outputs=model(**tokens)

        embeddings=outputs.last_hidden_state.squeeze(0)
        return embeddings.cpu().numpy()

if __name__=="__main__":
    generic=os.listdir('./data/generic')
    relevant=os.listdir('./data/relevant')
    device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model='bert-base-uncased'
    bert_embedder=BERTEmebddingGenerator(model,device)
    for page in generic:
        path=os.path.join('data','generic',page)
        with open(path, 'r') as text_file:
            text=text_file.read()
        embeddings=bert_embedder.get_embeddings(text)
        save_path=os.path.join('embeddings','generic',f'{page[:-4]}.npy')
        np.save(save_path,embeddings)

    for page in relevant:
        path=os.path.join('data','relevant',page)
        with open(path, 'r') as text_file:
            text=text_file.read()
        embeddings=bert_embedder.get_embeddings(text)
        save_path=os.path.join('embeddings','relevant',f'{page[:-4]}.npy')
        np.save(save_path,embeddings)

    print("Saved embeddings at ./embeddings :)")







