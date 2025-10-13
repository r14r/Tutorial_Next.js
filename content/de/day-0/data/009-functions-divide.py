## functions-divide
def teile(a, b):
    """Gibt den Quotienten und Rest der Division von a durch b zurück."""
    return a // b, a % b

# Beispielaufruf
quotient, rest = teile(17, 5)
print("Quotient:", quotient)
print("Rest:", rest)
