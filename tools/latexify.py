import json,sys
R=[(': : ',': '),
('Q = mL',r'$Q = mL$'),('Eg = mgΔh',r'$E_g = mg\Delta h$'),
('1/R = 1/R1 + 1/R2 + …',r'$\frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_2} + \dots$'),
('Requivalent = R1 + R2 + … + Rn',r'$R_{eq} = R_1 + R_2 + \dots + R_n$'),
('Ek = ½mv²',r'$E_k = \tfrac{1}{2}mv^2$'),('Q = mcΔT',r'$Q = mc\Delta T$'),
('n1\xa0sin\xa0(θ1) = n2\xa0sin(θ2) and n1v1 = n2v2',r'$n_1\sin\theta_1 = n_2\sin\theta_2$ and $n_1v_1 = n_2v_2$'),
('applications:n1\xa0sin\xa0(θc) = n2\xa0sin\xa0(90°)',r'applications: $n_1\sin\theta_c = n_2\sin 90^\circ$'),
('R = constant',r'$R$ = constant'),('Es = ½kx²',r'$E_s = \tfrac{1}{2}kx^2$'),
('W = F\xa0s\xa0cos\xa0θ',r'$W = Fs\cos\theta$'),
('v = u + at, v² = u² + 2as, s = ½(u + v)t, s = ut + ½at², s = vt – ½at²',r'$v = u + at$, $v^2 = u^2 + 2as$, $s = \tfrac{1}{2}(u + v)t$, $s = ut + \tfrac{1}{2}at^2$, $s = vt - \tfrac{1}{2}at^2$'),
('FΔt = mΔv',r'$F\Delta t = m\Delta v$'),('P = E/t',r'$P = \frac{E}{t}$'),
('a = Fnet/m, Fon A by B = –Fon B by A',r'$a = \frac{F_{net}}{m}$, $F_{\text{on A by B}} = -F_{\text{on B by A}}$'),
('Fon A by B = –Fon B by A',r'$F_{\text{on A by B}} = -F_{\text{on B by A}}$'),
('p = mv',r'$p = mv$'),('η = useful energy out / total energy in',r'$\eta = \frac{\text{useful energy out}}{\text{total energy in}}$'),
('λmaxT = constant',r'$\lambda_{max}T = \text{constant}$'),('v = fλ = λ/T',r'$v = f\lambda = \frac{\lambda}{T}$'),
('τ = r⊥F',r'$\tau = r_\perp F$'),('Δp = Fnet',r'$\Delta p = F_{net}\Delta t$'),('F = –kx',r'$F = -kx$'),
('V = IR, P = VI, R(series) = R1 + R2 + …',r'$V = IR$, $P = VI$, $R_{series} = R_1 + R_2 + \dots$'),
('use of V = IR and P = VI',r'use of $V = IR$ and $P = VI$'),
('Fon body by Earth = mg',r'$F_{\text{on body by Earth}} = mg$'),('9.8\xa0N\xa0kg–1',r'$9.8\ \text{N kg}^{-1}$'),
(', Fg,',r', $F_g$,'),('speed, c,',r'speed, $c$,')]
p=sys.argv[1];d=json.load(open(p))
for l in d['lessons']:
  out=[]
  for k in l['keyKnowledge']:
    for a,b in R:
      if a in k: k=k.replace(a,b)
    out.append(k)
  l['keyKnowledge']=out
json.dump(d,open(p,'w'),indent=1,ensure_ascii=False)
left={k for l in d['lessons'] for k in l['keyKnowledge'] if ('=' in k and '$' not in k)}
print('unconverted:',left)
