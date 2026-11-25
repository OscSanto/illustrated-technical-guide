import math

def softmax(xs):
    m=max(xs); e=[math.exp(x-m) for x in xs]
    return [v/sum(e) for v in e]
p=softmax([2,1,0]); assert abs(p[0]-.6652409558)<1e-8
assert abs(sum(p)-1)<1e-12
grad=[p[i]-(i==0) for i in range(3)]
updated=[z-.1*g for z,g in zip([2,1,0],grad)]
assert -math.log(softmax(updated)[0]) < -math.log(p[0])
scores=softmax([0,1,2]); assert abs(sum(i*v for i,v in enumerate(scores))-1.5752103826)<1e-8
assert abs(.5*sum(abs(a-b) for a,b in zip([.7,.2,.1],[.5,.3,.2]))-.2)<1e-12
assert abs(20/21-.9523809524)<1e-8
print('PASS: 6 numerical invariants')
