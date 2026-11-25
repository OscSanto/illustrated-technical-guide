import numpy as np

def softmax_temperature(logits, temperature=1.0):
    z = np.asarray(logits, dtype=np.float64) / temperature
    z -= z.max()
    e = np.exp(z)
    return e / e.sum()

def average_orders(original_logits, reversed_logits, temperature=1.0):
    p1 = softmax_temperature(original_logits, temperature)
    p2 = softmax_temperature(reversed_logits, temperature)[::-1]
    return (p1 + p2) / 2

p = average_orders([2., 1., 0.], [0., 1., 2.])
assert np.isclose(p.sum(), 1.)
assert np.all(p >= 0)
assert np.allclose(p, softmax_temperature([2.,1.,0.]))
assert np.isclose(-np.log(p[0]), 0.4076059644)
print('PASS: normalization, nonnegativity, reverse mapping, cross entropy')
