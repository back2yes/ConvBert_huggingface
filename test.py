import torch
from convbert_huggingface import ConvBertModel, ElectraTokenizer

tokenizer = ElectraTokenizer.from_pretrained("weights/convbert_base")
text = "it is a sunny day, i want to go out!"
for model_size in ["small", "medium-small", "base"]:
    model = ConvBertModel.from_pretrained(f"weights/convbert_{model_size}")
    with torch.no_grad():
        x = tokenizer(text, return_tensors="pt")
        pt_out = model(**x)[0]
    tf_out = torch.load(f"./tf_{model_size}_output.pt")
    print(f"{model_size} max difference is :",
          (tf_out - pt_out).abs().max().item())
