# Pearson worked examples (each followed by its "Worked example: Try yourself") for the We do step.
# Refs only: number, short label, printed student-book page. Usage: python we_pearson.py classes/physics-11.json
import json,sys
WE={
 '2.2':[('2.2.1','displacement–distance graph',65),('2.2.2','displacement–time graph',66),('2.2.3','the wave equation',68),('2.2.4','the wave equation',69)],
 '2.3':[('2.3.1','wave equation with EM radiation',73)],
 '3.1':[('3.1.1','applying Huygens’ principle',83),('3.1.2','calculating refractive index',86),('3.1.3','change in speed of light',87),('3.1.4','using Snell’s law',87),('3.1.5','calculating critical angle',88)],
 '3.2':[('3.2.1','range of angles for dispersion',94)],
 '4.1':[('4.1.1','change in internal energy',107)],
 '4.2':[('4.2.1','calculations using specific heat capacity',111),('4.2.2','comparing specific heat capacities',111)],
 '4.3':[('4.3.1','latent heat of fusion',114),('4.3.2','change in temperature and state',115)],
 '5.1':[('5.1.1','Wien’s law',130)],
 '5.2':[('5.2.1','re-radiated energy from Earth',133)],
 '6.1':[('6.1.1','working with isotopes',154)],
 '6.2':[('6.2.1','radioactive decay',159)],
 '6.3':[('6.3.1','half-life',168)],
 '6.4':[('6.4.1','treating tumours',177),('6.4.2','calculating effective dose',178)],
 '7.1':[('7.1.1','the electron volt',189),('7.1.2','calculating binding energy',191)],
 '7.2':[('7.2.1','neutrons released in fission',195)],
 '8.1':[('8.1.1','charge on a group of electrons',211),('8.1.2','number of electrons in a given charge',211)],
 '8.2':[('8.2.1','using I = Q/t',217)],
 '8.3':[('8.3.1','definition of potential difference',223),('8.3.2','using E = VIt',225),('8.3.3','using P = VI',226),('9.3.1','cost of electricity (from 9.3)',268)],
 '8.4':[('8.4.1','Ohm’s law: resistance',231),('8.4.2','Ohm’s law: resistance, current and PD',232),('8.4.3','resistance of a non-ohmic conductor',233),('8.4.4','Ohm’s law: current',236),('8.4.5','Ohm’s law: potential difference',236)],
 '9.1':[('9.1.1','equivalent series resistance',244),('9.1.2','series circuit analysis',245),('9.1.3','equivalent parallel resistance',247),('9.1.4','parallel circuit analysis',248),('9.1.5','complex circuit analysis',249),('9.1.6','power in series vs parallel',252)],
 '9.2':[('9.2.1','voltage divider',256),('9.2.2','thermistor in a voltage divider',258),('9.2.3','LDR in a voltage divider',260),('9.2.4','diodes',261),('9.2.5','LEDs',263)],
}
d=json.load(open(sys.argv[1]));n=0
for l in d['lessons']:
  s=l.get('sequence')
  if l['type']!='lesson' or not s: continue
  s.pop('weRefs',None)
  if l['section'] in WE:
    s['weRefs']=[dict(n=a,label=b,page=c) for a,b,c in WE[l['section']]];n+=1
json.dump(d,open(sys.argv[1],'w'),indent=1,ensure_ascii=False)
print('lessons with worked examples',n)
