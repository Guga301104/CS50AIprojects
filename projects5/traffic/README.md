# Traffic

O dataset [GTSRB](https://cdn.cs50.net/ai/2023/x/projects/5/gtsrb.zip) não está no repositório por causa do tamanho. Baixe, extraia nesta pasta e rode:

```
pip install -r requirements.txt
python traffic.py gtsrb [model.h5]
```

## Modelo

- Normalização dos pixels (`Rescaling 1/255`)
- 2 blocos `Conv2D` (32 e 64 filtros, 3x3, ReLU) + `MaxPooling2D` 2x2
- `Flatten` → `Dense(128, ReLU)` → `Dropout(0.5)`
- Saída `Dense(43, softmax)`, otimizador Adam e `categorical_crossentropy`

Duas camadas convolucionais extraem bordas e formas das placas, o pooling reduz a dimensionalidade e o dropout ajuda a evitar overfitting na camada densa.
