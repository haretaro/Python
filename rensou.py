import word2vec
import random
model = word2vec.load('entity_vector.model.bin', newLines=False)
with open('model.bin', 'rb') as f:
  model = pickle

index = random.randrange(len(model.vocab))

print(model.vocab[index])
while True:
    indexes, _ = model.cosine(model.vocab[index])
    index = indexes[0]
    print(model.vocab[index])
