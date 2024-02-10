# Hilbert

![hilbert_curve](https://github.com/michbogos/hilbert/blob/main/hilbert_curve.png?raw=true)

This is a quick and dirty implementation of a Lindenmayer System for drawing fractals.

It uses a replacement rule which it applies a couple of times. The generated instructions are then interpreted as turtle commands.

```
    Alphabet : A, B
    Constants : F + −
    Axiom : A
    Production rules:
        A → +BF−AFA−FB+
        B → −AF+BFB+FA−
```