import torch
from torch import nn


class GRU(nn.Module):
    def __init__(self, config):
        super(GRU, self).__init__()

        self.num_tokens = config['num_tokens']
        self.embedding_size = config['embedding_size']
        self.hidden_size = config['hidden_size']
        self.num_layers = config['num_layers']
        self.bidirectional = config['bidirectional']
        self.dropout = config['dropout']

        self.embedding = nn.Embedding(self.num_tokens, self.embedding_size)
        self.gru = nn.GRU(self.embedding_size, self.hidden_size, self.num_layers, batch_first=True, bidirectional=self.bidirectional, dropout=self.dropout)
        self.fc = nn.Linear(self.hidden_size * (2 if self.bidirectional else 1), self.num_tokens)

    def forward(self, src, tgt):
        src = self.embedding(src)
        out, _ = self.gru(src)
        out = self.fc(out[:, -1, :])
        return out
