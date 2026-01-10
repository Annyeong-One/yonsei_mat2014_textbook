# Training Loops

Training a neural network consists of repeatedly applying a **training loop** that updates model parameters to minimize a loss function.

---

## 1. The standard training loop

A canonical training step in PyTorch:

```python
for x, y in dataloader:
    optimizer.zero_grad()
    pred = model(x)
    loss = loss_fn(pred, y)
    loss.backward()
    optimizer.step()
```

This loop performs one gradient-based update per batch.

---

## 2. Epochs and batches

- **Batch**: a subset of data used for one update
- **Epoch**: one full pass over the dataset

```python
for epoch in range(num_epochs):
    train_one_epoch()
```

---

## 3. Training vs evaluation mode

Some modules behave differently during training:

```python
model.train()
model.eval()
```

Examples:
- Dropout
- Batch Normalization

---

## 4. Monitoring training

Typical quantities to monitor:
- training loss,
- validation loss,
- gradient norms.

```python
loss.item()
```

---

## 5. Financial calibration context

Training loops are used for:
- fitting surrogate pricing models,
- calibrating neural networks to market data,
- learning hedging strategies.

---

## Key takeaways

- Training loops follow a fixed pattern.
- Separate training and evaluation modes.
- Monitoring prevents silent failures.
