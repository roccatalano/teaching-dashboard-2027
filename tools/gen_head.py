import json,re
raw=json.load(open('/tmp/build/raw.json'))
CAM={2:1,3:1,4:2,5:2,6:3,7:4,8:5,9:6,10:7,11:7,12:8,13:9,14:9}
AOS={ (1,1):("U1 AoS1","How are light and heat explained?",12),
      (1,2):("U1 AoS2","How is energy from the nucleus utilised?",12),
      (1,3):("U1 AoS3","How can electricity be used to transfer energy?",21),
      (2,1):("U2 AoS1","How is motion understood?",30)}
def lines(s): return [l.strip(' •\t') for l in s.split('\n') if l.strip(' •\t')]
FIX=[('speed of travel of waves using:','speed of travel of waves using: v = fλ = λ/T'),
 ('using the relationships: , ,','using the relationships: V = IR, P = VI, R(series) = R1 + R2 + …'),
 ('arrangements in parallel:','arrangements in parallel: 1/R = 1/R1 + 1/R2 + …'),
 ('restricted to use of and P = VI','restricted to use of V = IR and P = VI'),
 ('s = (u + v)t, s = ut + at2, s = vt – at2','s = ½(u + v)t, s = ut + ½at², s = vt – ½at²'),
 ('v2 = u2 + 2as','v² = u² + 2as'),(': :',':'),
 ('a = , F','a = Fnet/m, F'),('Es = kx2','Es = ½kx²'),('Ek = mv2','Ek = ½mv²'),
 ('using power: P =','using power: P = E/t'),('efficiency of an energy transfer system:','efficiency of an energy transfer system: η = useful energy out / total energy in')]
def fixk(l):
  for a,b in FIX:
    if a in l and b not in l: l=l.replace(a,b)
  l=l.strip()
  return '    – '+l[1:].strip() if l.startswith('–') else l
def kk(s): return [fixk(l) for l in lines(s) if len(l)>3][:10]
