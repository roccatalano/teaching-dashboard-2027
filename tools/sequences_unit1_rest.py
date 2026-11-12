import json,sys
d=json.load(open(sys.argv[1]));L={l['id']:l for l in d['lessons']}
def S(m,p,t,dt,r=None): return dict(min=m,phase=p,title=t,detail=dt,**({'resource':r} if r else {}))
def dn(a,b,c,bn=None,cn=None):
  return [dict(when='Last lesson',q=a),dict(when='Last week',q=b,**({'note':bn} if bn else {})),dict(when='Last term',q=c,**({'note':cn} if cn else {}))]
def T(lid,goals,vocab,donow,apk,nk_t,nk,nk_r,guided,exit,video=None):
  l=L[lid];cf=l.get('cfat');qs='; '.join(l['questions'])
  st=[]
  if cf: st.append(S(20,'CFAT',f"{cf['id']}: {cf['title']}",f"{cf['id']} replaces the do-now today. Students sit it as they arrive (closed book, about 20 min). Collect for marking."))
  else: st.append(S(8,'Do-now','Retrieval practice','Three do-now questions done independently, then self-marked.'))
  st.append(S(2,'Learning goals','Share the goals','Read the “I can” statements together.'))
  st.append(S(5 if cf else 7,'APK',apk[0],apk[1]))
  st.append(S(18 if cf else 20,'New knowledge',nk_t,nk,nk_r))
  if video: st.append(S(5,'Video',video[0],video[1],'Pearson video'))
  st.append(S(10,'Guided practice','We do',guided))
  used=sum(s['min'] for s in st)+8
  st.append(S(79-used,'Apply','Independent practice',f"Pearson {l['section']} {qs.replace('Key questions','Key questions',1)}. Finish for homework.",f"Pearson SB {l['section']}"))
  st.append(S(8,'Exit ticket','Goals revisited',exit+' Red/amber/green on each goal.'))
  l['sequence']=dict(length=79,goals=goals,vocab=vocab,doNow=[] if cf else donow,steps=st)
def P(lid,goals,vocab,donow,brief,run,analysis,exit):
  l=L[lid];p=l['prac']
  st=[S(6,'Do-now','Retrieval practice','Three do-now questions done independently, then self-marked.'),
      S(10,'Pre-lab briefing','Aim, method and risks',brief,f"{p['code']} teacher notes and risk assessment"),
      S(35,'Prac',p['title'],run,f"{p['code']} {'SPARKlab (students open in the eBook)' if p['kind']=='SPARKlab' else 'student sheet (also in the eBook)'}"),
      S(15,'Analysis','Process the results',analysis),
      S(8,'Exit ticket','Logbook check',exit+' Teacher sights and initials each logbook.'),
      S(5,'Pack-up','Return equipment','Equipment back and benches cleared.')]
  l['sequence']=dict(length=79,goals=goals,vocab=vocab,doNow=donow,steps=st)
def X(lid,goals,vocab,donow,steps):
  assert sum(s['min'] for s in steps)==79,(lid,sum(s['min'] for s in steps))
  L[lid]['sequence']=dict(length=79,goals=goals,vocab=vocab,doNow=donow,steps=steps)
I=lambda n:f'p11-u1-l{n:02d}'

# ======================= AoS1 (Weeks 3–7) =======================
T(I(7),['Explain dispersion of white light in a prism in terms of refractive index varying with wavelength','Explain how rainbows and mirages form','Describe polarisation as evidence that light is a transverse wave'],
 ['dispersion','spectrum','total internal reflection','critical angle','mirage','polarisation'],
 dn('Light enters glass ($n = 1.5$) from air at $40^\\circ$. Find the angle of refraction.','Which EM radiation has the highest frequency?','What is the speed of sound in air, roughly? (OE 2.2.1)',bn='Lesson 4',cn='Week 2 prac'),
 ('Refraction recap','Prerequisite: Snell’s law and “toward/away from the normal”. Two quick sketches on the guided sheet: ray entering glass, ray leaving glass.'),
 'Dispersion, rainbows, mirages and polarisation','Refractive index depends on wavelength, so colours refract by different amounts (violet most). Prism and rainbow ray diagrams. Total internal reflection and critical angle: $n_1\\sin\\theta_c = n_2\\sin 90^\\circ$; optical fibres. Mirages from refraction through air layers of different temperature. Polarisation only happens to transverse waves.','Pearson SB 3.2',
 'Critical angle for glass ($n = 1.5$) to air; then explain in words why the sky looks blue or the ocean blue (link to the video).',
 '“Why does a prism split white light? Which colour bends most?”',video=('Why is the ocean blue?','Play the video; students note how scattering and absorption depend on wavelength.'))
T(I(8),['Distinguish between heat, temperature and internal energy','Describe temperature as the average translational kinetic energy of particles','Convert between Celsius and kelvin'],
 ['temperature','heat','internal energy','kinetic theory','kelvin','absolute zero','thermal equilibrium'],
 [],('States of matter','Prerequisite: particle model from Year 9–10. On the guided sheet: “Sketch particles in a solid, liquid and gas. What is different about their motion?”'),
 'Heat, temperature and internal energy','Kinetic particle model. Temperature as average translational kinetic energy; internal energy as total kinetic + potential energy of particles. Heat is energy transferred because of a temperature difference. Kelvin scale: $T(\\text{K}) = T(^\\circ\\text{C}) + 273$; absolute zero. Thermal equilibrium.','Pearson SB 4.1',
 'Convert 25 °C, −196 °C and 373 K. Then: two blocks at different temperatures touch; describe what happens to their particles until equilibrium.',
 '“What is the difference between heat and temperature? Convert 15 °C to kelvin.”')
P(I(9),['Observe and measure refraction of light through a glass block or prism','Observe dispersion of white light into a spectrum','Use measured angles to calculate refractive index'],
 ['incident angle','refracted angle','refractive index','dispersion','protractor','uncertainty'],
 dn('Convert 300 K to °C.','Why does a prism split white light?','State the wave equation.',bn='Lesson 7',cn='Week 1'),
 'Walk through PA2: ray box, glass block or prism, protractor; measuring angles from the normal. Risks: hot ray-box globes, glass edges, working in a dimmed room.',
 'Groups trace rays through the block at several angles of incidence, record $\\theta_1$ and $\\theta_2$, then use a prism to produce a spectrum and note the order of colours.',
 'Calculate $n$ for each trial with Snell’s law, then find the mean. Optional: graph $\\sin\\theta_1$ vs $\\sin\\theta_2$; the gradient is $n$. Discuss sources of error in reading angles.',
 'Conclusion: your value of $n$ and one improvement to the method.')
T(I(10),['Define specific heat capacity','Use $Q = mc\\Delta T$ to calculate energy, mass or temperature change','Explain why water moderates climate'],
 ['specific heat capacity, $c$','energy, $Q$','temperature change, $\\Delta T$','joule'],
 dn('What is the difference between heat and temperature?','Calculate the refractive index if $\\theta_1 = 45^\\circ$ and $\\theta_2 = 28^\\circ$.','Rearrange $v = f\\lambda$ for $f$.',bn='Week 3 prac',cn='Week 1'),
 ('Rearranging three-variable formulas','Prerequisite: rearranging formulas like $Q = mc\\Delta T$ and working out $\\Delta T$ as final minus initial. Two quick examples.'),
 'Specific heat capacity','Define $c$ as energy to raise 1 kg by 1 K. $Q = mc\\Delta T$ with units. Water’s very high $c$ and its effect on coastal climates. Worked examples from the student book.','Pearson SB 4.2',
 'Heat 2.0 kg of water from 20 °C to 80 °C ($c = 4200$ J kg$^{-1}$ K$^{-1}$). Then find $\\Delta T$ when 50 kJ is added to 1.0 kg of aluminium.',
 '“How much energy heats 0.5 kg of water by 10 °C?”')
T(I(11),['Define latent heat of fusion and vaporisation','Use $Q = mL$ to calculate energy for a change of state','Explain cooling by evaporation using the kinetic model'],
 ['latent heat','fusion','vaporisation','change of state','evaporation','heating curve'],
 dn('State $Q = mc\\Delta T$ and the meaning of each symbol.','Convert −40 °C to kelvin.','What is a compression in a longitudinal wave?',bn='Lesson 8',cn='Week 1'),
 ('Heating curves','Prerequisite: reading a graph. Show a heating curve for ice to steam; ask what is happening on the flat sections.'),
 'Latent heat','During a change of state, energy breaks bonds (potential energy) rather than raising temperature. $Q = mL$; latent heat of fusion vs vaporisation. Multi-step problems combining $Q = mc\\Delta T$ and $Q = mL$. Evaporation removes the fastest particles, so the liquid cools (sweating).','Pearson SB 4.3',
 'Energy to turn 0.2 kg of ice at 0 °C into water at 20 °C (two steps).',
 '“Why does sweating cool you down?”')
P(I(12),['Measure the specific heat capacity of a substance','Identify energy losses as a source of systematic error','Compare an experimental value with an accepted value'],
 ['specific heat capacity','electrical energy','insulation','systematic error','percentage difference'],
 dn('Energy to melt 0.1 kg of ice? ($L_f = 3.34 \\times 10^5$ J kg$^{-1}$)','What is a temperature of 0 K?','State Snell’s law.',bn='Lesson 8',cn='Week 2'),
 'Walk through PA5: heating a known mass with a known energy input (heater or immersion coil), recording temperature over time. Risks: hot water and heaters, electrical safety near water.',
 'Groups heat the substance, logging temperature against time and the energy supplied (from $E = VIt$ or the heater rating).',
 'Calculate $c$ from $Q = mc\\Delta T$; compare with the accepted value and calculate percentage difference. Discuss heat loss to surroundings and how insulation would help.',
 'Conclusion: your value of $c$, and whether heat loss makes it too high or too low.')
T(I(13),['Distinguish conduction, convection and radiation','Explain heat transfer within and between systems','Apply heat transfer ideas to insulation and everyday examples'],
 ['conduction','convection','radiation','insulator','conductor','convection current'],
 dn('Energy to raise 0.3 kg of water by 15 °C?','State $Q = mL$ and explain why temperature is constant during melting.','What is the order of the EM spectrum from radio to gamma?',bn='Lesson 11',cn='Week 2'),
 ('Particle collisions','Prerequisite: kinetic model. Quick question: “Why does a metal spoon in hot soup get hot all the way up?”'),
 'Conduction, convection and radiation','Conduction by particle collisions (metals also by free electrons); convection by bulk movement of fluid driven by density differences; radiation as EM (mainly infrared), needing no medium. Insulation reduces each one. Everyday examples: double glazing, a thermos, ceiling insulation.','Pearson SB 4.4',
 'Classify ten everyday examples as conduction, convection or radiation, with a reason for each.',
 '“Explain how a thermos flask reduces all three types of heat transfer.”')
T(I(14),['Describe black-body radiation curves at different temperatures','Use Wien’s law, $\\lambda_{max}T = \\text{constant}$','Compare the total energy radiated by hot and cooler objects'],
 ['black body','peak wavelength','Wien’s law','emission spectrum','infrared'],
 [],('Graph reading','Prerequisite: reading peaks off a curve and scientific notation. Show one black-body curve and ask students to read the peak wavelength.'),
 'Black-body radiation and Wien’s law','All objects emit EM radiation; hotter objects emit more in total and peak at shorter wavelengths. Wien’s law $\\lambda_{max}T = 2.9 \\times 10^{-3}$ m K. Worked examples: the Sun (about 5800 K) and the human body (about 310 K). Link to why hot objects glow red then white.','Pearson SB 5.1',
 'Peak wavelength of a star at 10 000 K; temperature of an object peaking at 10 µm.',
 '“A star peaks at 500 nm. Estimate its surface temperature.”',video=('What is fire?','Play the video; link the colour of a flame to temperature.'))
P(I(15),['Measure the latent heat of fusion of ice','Account for energy transferred from the surroundings','Use $Q = mL$ with experimental data'],
 ['latent heat of fusion','calorimeter','energy balance','uncertainty'],
 dn('State Wien’s law in words.','Name the three types of heat transfer.','A wave has $T = 0.01$ s. Find $f$.',bn='Lesson 13',cn='Week 1'),
 'Walk through PA6: melting a known mass of ice in water (or with a heater) and measuring the temperature change and energy supplied. Risks: electrical equipment near water, hot water.',
 'Groups record masses and temperatures before and after the ice melts, logging data in the logbook as they go.',
 'Calculate $L_f$ from the energy balance; compare with $3.34 \\times 10^5$ J kg$^{-1}$. Discuss sources of error (heat from the room, water on the ice).',
 'Conclusion: your value of $L_f$ and the biggest source of error.')
T(I(16),['Explain the greenhouse effect','Distinguish the natural from the enhanced greenhouse effect','Apply energy transfer ideas to climate change and global warming'],
 ['greenhouse effect','enhanced greenhouse effect','albedo','greenhouse gas','radiative balance'],
 dn('An object peaks at 10 µm. Estimate its temperature.','Explain convection in a pot of water.','What is $Q = mc\\Delta T$ used for?',bn='Lesson 13',cn='Week 4'),
 ('Energy in, energy out','Prerequisite: Earth receives mainly visible/UV from the Sun and emits infrared (Wien’s law). Quick sketch of energy arrows in and out of Earth.'),
 'The greenhouse effect','Incoming short-wavelength radiation, outgoing long-wavelength infrared. Greenhouse gases absorb and re-emit IR. Natural vs enhanced effect; feedback loops (ice albedo, water vapour); role of oceans’ high specific heat capacity.','Pearson SB 5.2',
 'Annotate an energy-flow diagram of Earth’s atmosphere together.',
 '“Explain in three sentences how extra CO₂ leads to warming.”',video=('The greenhouse effect and global warming','Play the video; students note one feedback loop.'))
X(I(17),['Recall and apply all AoS1 key knowledge','Identify my own gaps before SAC 1'],['(all AoS1 vocabulary)'],[],
 [S(20,'CFAT','CFAT 4: SAC 1 readiness check','CFAT 4 (Ch 5) replaces the do-now. Mark quickly in class or collect: it tells you what to re-teach today.'),
  S(2,'Learning goals','Share the goals','Review lesson: find and fix gaps before SAC 1.'),
  S(12,'Re-teach','Common errors','Re-teach the two or three most-missed ideas so far (CFATs 1–4): typically the two kinds of wave graph, Snell’s law setup, and $Q = mc\\Delta T$ vs $Q = mL$.'),
  S(37,'Apply','AoS1 review questions','Students work through the student book AoS1 review, self-marking against the fully worked solutions you release partway through.','Pearson SB AoS1 review; AoS1 Review fully worked solutions (teacher)'),
  S(8,'Exit ticket','SAC plan','Each student writes the three topics they will revise before SAC 1.')])
P(I(18),['Investigate how insulating materials affect the rate of heat loss','Control variables in a comparative experiment','Graph cooling curves and compare rates'],
 ['insulation','independent variable','dependent variable','controlled variable','cooling curve','rate'],
 dn('Explain the enhanced greenhouse effect.','Energy to melt 0.2 kg of ice?','What is dispersion?',bn='Lesson 11',cn='Week 3'),
 'Walk through OE 4.4.2: identical containers of hot water wrapped in different insulators, temperature recorded over time. Identify the variables. Risks: hot water.',
 'Groups set up containers with different insulators and record temperature every minute.',
 'Plot cooling curves on one set of axes; compare initial rates of cooling. Rank the insulators and link to conduction, convection and radiation.',
 'Conclusion: the best insulator, with evidence from your graph.')
X(I(19),['Demonstrate Outcome 1 under SAC conditions'],['(all AoS1 vocabulary)'],[],
 [S(5,'Setup','SAC conditions','Seat students, hand out the SAC and formula sheet; read the instructions and permitted materials.'),
  S(65,'SAC','SAC 1: Light and heat','Students complete SAC 1 under test conditions.','SAC 1 (to be written: see Assessment plan)'),
  S(9,'Wrap-up','Collect and reflect','Collect all materials. Students note in one sentence how they think it went.')])
# ======================= AoS2 (Weeks 7–10) =======================
T(I(20),['Describe the structure of the atom and nucleus','Use nuclear notation for isotopes','Explain nuclear stability in terms of the forces in the nucleus'],
 ['nucleon','proton','neutron','isotope','radioisotope','atomic number','mass number','strong nuclear force'],
 dn('How did you go in SAC 1? Name one topic you’ll keep practising.','What does Wien’s law describe?','What is a transverse wave?',bn='Week 5',cn='Week 1'),
 ('Atomic structure','Prerequisite: Year 9–10 atomic model. On the guided sheet: “Draw a lithium atom. Where is most of its mass?”'),
 'Atoms, isotopes and nuclear stability','Nuclear notation $^A_ZX$; isotopes; the strong nuclear force vs electrostatic repulsion; the weak nuclear force; the band of stability (N vs Z graph).','Pearson SB 6.1',
 'Write nuclear notation for carbon-14 and uranium-238; use the N–Z graph to predict whether three isotopes are stable.',
 '“Why don’t the protons in a nucleus fly apart?” (Start the lesson with 15 min of SAC 1 feedback if the SACs are marked: shorten Apply.)')
T(I(21),['Describe the properties of alpha, beta and gamma radiation','Write balanced decay equations','Compare penetrating and ionising ability'],
 ['alpha','beta-minus','beta-plus','gamma','ionising','penetrating','decay equation','positron','neutrino'],
 dn('Write the notation for an isotope with 6 protons and 8 neutrons.','Explain the greenhouse effect.','What is specific heat capacity?',bn='Lesson 16',cn='Week 4'),
 ('Conservation','Prerequisite: balancing totals. Quick puzzle: balance top and bottom numbers in a simple nuclear equation.'),
 'Radioactivity and decay equations','Alpha, beta-minus, beta-plus and gamma: what each is, charge, mass, penetration, ionisation. Balancing A and Z in decay equations. Decay series.','Pearson SB 6.2',
 'Write decay equations for alpha decay of U-238 and beta-minus decay of C-14 together.',
 '“Which radiation is stopped by paper? Write the alpha decay of Po-210.”',video=('Alpha, beta and gamma radiation','Play the video; students note penetration for each.'))
T(I(22),['Define half-life and model random decay','Calculate amounts remaining after whole half-lives','Interpret decay series diagrams'],
 ['half-life','activity','becquerel','random decay','decay series','daughter nucleus'],
 dn('Write the beta-minus decay of C-14.','Write the notation for U-235.','Explain cooling by evaporation.',bn='Lesson 20',cn='Week 4'),
 ('Halving','Prerequisite: repeated halving and fractions. “Halve 80 four times. What fraction is left after 3 halvings?”'),
 'Half-life','Decay is random for an individual nucleus but predictable for large numbers. Half-life; activity in Bq; decay curves; whole half-life calculations only; decay series diagrams.','Pearson SB 6.3',
 'A 64 g sample has a half-life of 8 days. How much remains after 24 days? Then read a half-life off a decay curve.',
 '“A source has a half-life of 5 years. What fraction is left after 15 years?”')
T(I(23),['Calculate absorbed, equivalent and effective dose','Explain short- and long-term effects of radiation','Evaluate the use of medical radioisotopes'],
 ['absorbed dose (Gy)','equivalent dose (Sv)','effective dose (Sv)','radiation weighting factor','tissue weighting factor','radioisotope therapy'],
 dn('What fraction of a sample remains after 4 half-lives?','Which radiation is most ionising?','Convert 50 °C to kelvin.',bn='Lesson 21',cn='Week 3'),
 ('Energy per kilogram','Prerequisite: dividing energy by mass and multiplying by factors. Quick numeric warm-up.'),
 'Radiation and the human body','Absorbed dose (Gy) = energy/mass; equivalent dose (Sv) with radiation weighting factors; effective dose with tissue weighting factors. Deterministic vs stochastic effects. Medical uses: diagnosis and therapy.','Pearson SB 6.4',
 'Work out absorbed, then equivalent dose for 0.02 J of alpha radiation absorbed by 2 kg of tissue.',
 '“Why is alpha radiation more dangerous inside the body than outside it?”')
P(I(24),['Model random radioactive decay using a physical analogue','Determine a half-life from a graph','Explain why decay is random but predictable'],
 ['random','model','half-life','decay curve','sample size'],
 dn('Calculate the equivalent dose for 2 mGy of alpha radiation ($w_R = 20$).','Write the alpha decay of Ra-226.','What is Wien’s law?',bn='Lesson 21',cn='Week 5'),
 'Walk through PA8: “nuclei” (dice, coins or similar) are “decayed” by chance each round. Discuss what one roll represents. Minimal risk.',
 'Groups run repeated rounds, removing decayed nuclei each time and recording the number remaining.',
 'Plot number remaining vs round; read the half-life from the graph. Compare groups and discuss why larger samples give smoother curves.',
 'Conclusion: the half-life from your graph, and one limitation of the model.')
T(I(25),['Explain mass–energy equivalence','Use $E = mc^2$ to calculate energy released','Explain binding energy using the binding energy curve'],
 ['mass–energy equivalence','mass defect','binding energy','binding energy curve','MeV'],
 [],('Very large and very small numbers','Prerequisite: scientific notation with $c^2 = 9 \\times 10^{16}$. Quick calculator check.'),
 'Energy from mass','$E = mc^2$ qualitatively and quantitatively. Mass defect and binding energy. The binding energy per nucleon curve: why fusion of light nuclei and fission of heavy nuclei both release energy.','Pearson SB 7.1',
 'Energy released when 1 g of mass is converted. Then use the binding energy curve to explain why iron is the most stable.',
 '“Why do both fission and fusion release energy?”')
T(I(26),['Explain fission chain reactions, criticality and moderation','Compare fission and fusion','Evaluate the viability of nuclear energy for Australia'],
 ['fission','fusion','chain reaction','critical mass','moderator','control rods','enrichment'],
 dn('What is a mass defect?','What is a half-life?','Name the three types of heat transfer.',bn='Lesson 22',cn='Week 5'),
 ('Chain reactions','Prerequisite: exponential growth. “One person tells two people, who each tell two more… How many after 10 rounds?”'),
 'Fission, fusion and nuclear energy in Australia','Neutron-induced fission of U-235; chain reactions; effect of mass and shape on criticality; moderation and absorption. Fusion in stars and reactors. Arguments for and against nuclear power in Australia.','Pearson SB 7.2',
 'Annotate a fission reactor diagram together, labelling the fuel, moderator, control rods and coolant.',
 '“Give one argument for and one against nuclear power in Australia, using physics.”',video=('Thermonuclear fusion (eBook interactive)','Run the eBook interactive; students note the conditions needed for fusion.'))
P(I(27),['Detect background and source radiation with a G-M tube','Investigate how absorbers affect count rate','Account for background radiation in data'],
 ['Geiger–Müller tube','count rate','background radiation','absorber','inverse square'],
 dn('Explain how control rods work.','What is half-life?','What is an absorbed dose?',bn='Lesson 21',cn='Lesson 23'),
 'Walk through PA7: measuring background count, then count rate with different absorbers and distances. Risks: sealed sources handled only with tongs by the teacher; follow the school’s radiation safety rules strictly.',
 'Groups record background count, then count rates for paper, aluminium and lead, and at different distances.',
 'Subtract background; identify each source type from absorption; plot count rate vs distance. Link to ionising and penetrating ability.',
 'Conclusion: which radiation the source emits, with evidence. (Check with your lab tech that the school has sources and G-M tubes; if not, use OE 6.3.2 data analysis instead.)')
X(I(28),['Recall and apply all AoS2 key knowledge','Identify my own gaps before SAC 2'],['(all AoS2 vocabulary)'],[],
 [S(20,'CFAT','CFAT 6: SAC 2 readiness check','CFAT 6 (Ch 7) replaces the do-now. Mark quickly in class: it tells you what to re-teach today.'),
  S(2,'Learning goals','Share the goals','Review lesson: find and fix gaps before SAC 2.'),
  S(12,'Re-teach','Common errors','Re-teach the most-missed ideas from CFATs 5–6: typically balancing decay equations, dose calculations and the binding energy curve.'),
  S(37,'Apply','AoS2 review questions','Students work through the student book AoS2 review, self-marking against the fully worked solutions.','Pearson SB AoS2 review; AoS2 Review fully worked solutions (teacher)'),
  S(8,'Exit ticket','SAC plan','Each student writes the three topics they will revise before SAC 2.')])
X(I(29),['Demonstrate Outcome 2 under SAC conditions'],['(all AoS2 vocabulary)'],[],
 [S(5,'Setup','SAC conditions','Seat students, hand out the SAC and formula sheet; read the instructions.'),
  S(65,'SAC','SAC 2: Nuclear','Students complete SAC 2 under test conditions.','SAC 2 (to be written: see Assessment plan)'),
  S(9,'Wrap-up','Collect and reflect','Collect all materials. Students note one thing they found hard.')])
X(I(30),['Understand my SAC 2 results and the model responses','Improve my weakest areas'],['(AoS2 vocabulary)'],[],
 [S(10,'Return','SAC 2 returned','Return marked SACs with the marking scheme.'),
  S(25,'Feedback','Model responses','Go through the model answers and the most common errors as a class.'),
  S(36,'Apply','Corrections and redemption','Students correct errors in their logbook or book; eligible students sit the redemption task.','SAC 2 redemption (to be written)'),
  S(8,'Exit ticket','Next steps','Students write two skills to improve before SAC 3.')])
# ======================= AoS3 (Weeks 11–15) =======================
T(I(31),['Describe charge and the forces between charges','Explain conductors and insulators in terms of free electrons','Use the unit of charge, the coulomb'],
 ['charge','coulomb','electron','conductor','insulator','electrostatic force'],
 dn('What was your weakest area in SAC 2?','Write the beta-minus decay of Sr-90.','Convert 1.5 kJ to J.',bn='Week 8',cn='Week 1'),
 ('Atoms and electrons','Prerequisite: atomic structure (from AoS2). Ask: “Which particle moves when an object becomes charged?”'),
 'Behaviour of charged particles','Like charges repel, unlike attract. Charge is measured in coulombs; the electron charge is $1.6 \\times 10^{-19}$ C. Conductors have free electrons; insulators don’t. Charging by friction and contact.','Pearson SB 8.1',
 'How many electrons make up −1 C of charge? Explain why a balloon sticks to a wall.',
 '“Why do metals conduct electricity but plastic doesn’t?”')
T(I(32),['Define current as rate of flow of charge, $I = \\frac{Q}{t}$','Define potential difference as energy per charge, $V = \\frac{E}{Q}$','Draw circuit diagrams and place ammeters and voltmeters correctly'],
 ['current','ampere','potential difference','volt','ammeter','voltmeter','circuit diagram','conventional current'],
 dn('How many electrons in −2 C of charge?','What is a conductor?','State $Q = mc\\Delta T$.',bn='Lesson 31',cn='Week 4'),
 ('Rates','Prerequisite: “per second” and “per unit”. Quick examples: litres per second; dollars per item.'),
 'Current and potential difference','$I = \\frac{Q}{t}$; $V = \\frac{E}{Q}$. Conventional current vs electron flow. Circuit symbols. Ammeters in series (low resistance), voltmeters in parallel (high resistance). Analogies for circuits and their limits.','Pearson SB 8.2',
 '3.0 C passes in 1.5 s: find the current. 12 J delivered to 2.0 C: find the voltage. Draw where the meters go in a simple circuit.',
 '“Where do you connect an ammeter, and why?”',video=('Flow of charge through a conductor','Play the video; students note the difference between drift speed and signal speed.'))
P(I(33),['Connect ammeters and voltmeters correctly','Measure current and voltage in simple circuits','Practise safe circuit-building'],
 ['ammeter','voltmeter','series','parallel','power supply','circuit diagram'],
 dn('Find the current when 6 C passes in 3 s.','Explain the difference between conductors and insulators.','What is the strong nuclear force?',bn='Lesson 31',cn='Week 7'),
 'Walk through OE 8.2.1 and 8.2.2: building a simple circuit, placing the ammeter in series and the voltmeter in parallel, reading scales. Risks: low-voltage supplies only; check the circuit before switching on; hot resistors.',
 'Groups build circuits from the diagrams and record current and voltage readings for each setup.',
 'Check the readings for consistency (e.g. the same current everywhere in a series loop). Discuss what happens if a meter is connected the wrong way.',
 'Conclusion: one rule for each meter, with evidence from today.')
T(I(34),['Calculate energy and power in circuits, $P = VI$ and $E = VIt$','Use the kilowatt-hour as a unit of energy','Calculate the cost of running appliances'],
 ['power','watt','energy','kilowatt-hour','efficiency'],
 dn('Why must a voltmeter be connected in parallel?','Find $V$ if 24 J is given to 3 C.','What is an effective dose?',bn='Lesson 32',cn='Week 8'),
 ('Units of time and energy','Prerequisite: converting hours to seconds and J to kJ. Quick drill.'),
 'Energy in electric circuits','$P = VI$; $P = \\frac{E}{t}$; $E = VIt$. The kWh as a unit of energy; cost calculations from power bills.','Pearson SB 8.3',
 'A 2000 W heater runs for 3 h: energy in kWh, then in J, then the cost at 30c per kWh.',
 '“Find the power of a 240 V appliance drawing 5 A.”')
T(I(35),['Define resistance, $R = \\frac{V}{I}$','Distinguish ohmic and non-ohmic devices from I–V graphs','Describe the behaviour of diodes, LEDs, thermistors and LDRs'],
 ['resistance','ohm','ohmic','non-ohmic','I–V graph','diode','thermistor','LDR'],
 dn('Cost of running a 1.5 kW heater for 4 h at 30c per kWh?','Draw a circuit with an ammeter and voltmeter on a resistor.','What is a chain reaction?',bn='Lesson 33',cn='Week 9'),
 ('Gradients','Prerequisite: finding the gradient of a straight line. Quick example on a V–I graph.'),
 'Resistance','$R = \\frac{V}{I}$; ohmic devices have a straight-line I–V graph through the origin. Non-ohmic: filament lamp, diode, LED. Thermistors and LDRs as sensors.','Pearson SB 8.4',
 'Find $R$ from three V–I data points; sketch I–V graphs for a resistor, a lamp and a diode.',
 '“Sketch the I–V graph of a filament lamp and explain its shape.”')
P(I(36),['Collect V–I data for a resistor and a filament lamp','Plot I–V graphs and classify devices as ohmic or non-ohmic','Explain non-ohmic behaviour'],
 ['ohmic','non-ohmic','I–V graph','variable resistor','line of best fit'],
 dn('Find $R$ if $V = 6$ V and $I = 0.2$ A.','Find the power of a 12 V, 2 A device.','Define half-life.',bn='Lesson 34',cn='Week 8'),
 'Walk through PA11: varying the voltage across a resistor, then a lamp, recording current. Risks: hot lamp filaments; keep below rated voltages.',
 'Groups collect at least six V–I readings for each device.',
 'Plot I–V graphs for both devices; find $R$ from the resistor’s gradient; explain the lamp’s curve in terms of temperature.',
 'Conclusion: which device is ohmic, with evidence from your graphs.')
T(I(37),['Calculate equivalent resistance in series and parallel','Apply current and voltage rules in series and parallel circuits','Explain why household circuits are wired in parallel'],
 ['series','parallel','equivalent resistance','voltage divider','combination circuit'],
 [],('Fractions','Prerequisite: adding reciprocals. Quick drill: $\\frac{1}{2} + \\frac{1}{3}$; then the reciprocal of the answer.'),
 'Series and parallel circuits','Series: same current, voltages add, $R_{eq} = R_1 + R_2 + \\dots$. Parallel: same voltage, currents add, $\\frac{1}{R_{eq}} = \\frac{1}{R_1} + \\frac{1}{R_2} + \\dots$. Combination circuits step by step. Voltage dividers.','Pearson SB 9.1',
 'Find the total resistance and current for 2 Ω and 4 Ω in series, then in parallel, on a 12 V supply.',
 '“Why are homes wired in parallel?”',video=('Series and parallel circuits','Play both short videos; students note one difference.'))
T(I(38),['Model household electricity as a simple DC circuit','Calculate power and energy use in household circuits','Compare power transfers in series and parallel circuits'],
 ['active','neutral','earth','load','household circuit','power rating'],
 dn('Find $R_{eq}$ for 3 Ω and 6 Ω in parallel.','Sketch the I–V graph for a diode.','Explain the enhanced greenhouse effect.',bn='Lesson 35',cn='Week 6'),
 ('Power formulas','Prerequisite: $P = VI$ and $V = IR$. Quick substitution practice.'),
 'Using electricity','Household circuits modelled as DC: active, neutral, earth wires; appliances in parallel; total current drawn as more appliances switch on. Power loss in wiring.','Pearson SB 9.2',
 'A 240 V circuit runs a 2400 W heater and a 1200 W kettle: total current. Is a 15 A circuit enough?',
 '“Why does switching on more appliances increase the current from the supply?”')
P(I(39),['Build series and parallel circuits','Measure current and voltage at different points','Verify the series and parallel rules experimentally'],
 ['series','parallel','equivalent resistance','current rule','voltage rule'],
 dn('Total current drawn by a 2000 W heater on 240 V?','Find $R$ for a device with $V = 9$ V and $I = 0.3$ A.','State $E = mc^2$ in words.',bn='Lesson 36',cn='Week 9'),
 'Walk through PA13: building series and parallel circuits with two or three resistors and measuring currents and voltages. Risks: low-voltage supplies; check before switching on.',
 'Groups build each circuit and record readings at every point.',
 'Check the readings against the series and parallel rules; calculate $R_{eq}$ from $V$ and $I$ and compare with the formula.',
 'Conclusion: one rule for series and one for parallel, with evidence.')
T(I(40),['Compare fuses, circuit breakers and RCDs','Describe the causes and effects of electric shock and first aid','Identify danger thresholds for current and duration'],
 ['fuse','circuit breaker','residual current device (RCD)','earthing','electric shock','double insulation'],
 dn('Is a 15 A circuit enough for a 3000 W load on 240 V?','Find $R_{eq}$ for 10 Ω and 10 Ω in parallel.','What does a moderator do in a reactor?',bn='Lesson 37',cn='Week 9'),
 ('Current and the body','Prerequisite: $I = \\frac{V}{R}$. “Dry skin is about 100 kΩ; wet skin about 1 kΩ. Find the current at 240 V for each.”'),
 'Electrical safety','How fuses, circuit breakers and RCDs work and what each protects against. Earthing and double insulation. Effects of current on the body, danger thresholds and first aid (DRSABCD).','Pearson SB 9.3',
 'Scenario cards: for each fault, which safety device acts first and why?',
 '“An RCD trips but the fuse doesn’t. What kind of fault happened?”')
X(I(41),['Recall and apply all AoS3 key knowledge','Identify my own gaps before SAC 3'],['(all AoS3 vocabulary)'],[],
 [S(20,'CFAT','CFAT 8: SAC 3 readiness check','CFAT 8 (Ch 9) replaces the do-now. Mark quickly in class: it tells you what to re-teach today.'),
  S(2,'Learning goals','Share the goals','Review lesson: find and fix gaps before SAC 3.'),
  S(12,'Re-teach','Common errors','Re-teach the most-missed ideas from CFATs 7–8: typically meter placement, parallel resistance and power calculations.'),
  S(37,'Apply','AoS3 review questions','Students work through the student book AoS3 review, self-marking against the fully worked solutions.','Pearson SB AoS3 review; AoS3 Review fully worked solutions (teacher)'),
  S(8,'Exit ticket','SAC plan','Each student writes the three topics they will revise before SAC 3.')])
P(I(42),['Measure the electrical energy supplied to water','Compare electrical energy in with thermal energy gained','Calculate the efficiency of the energy transfer'],
 ['electrical energy','thermal energy','efficiency','energy transfer'],
 dn('What does an RCD detect?','Find total resistance of 5 Ω and 5 Ω in series.','Use $Q = mc\\Delta T$: 0.5 kg water, 20 °C rise.',bn='Lesson 38',cn='Week 4'),
 'Walk through PA14: an immersion heater in water, measuring $V$, $I$, $t$ and the temperature rise. Risks: electricity near water (low-voltage heater only), hot water.',
 'Groups record $V$, $I$, time and temperatures for a known mass of water.',
 'Calculate $E = VIt$ and $Q = mc\\Delta T$; compare and find the efficiency. Discuss where the “lost” energy went.',
 'Conclusion: the efficiency you measured, and the main energy loss.')
X(I(43),['Demonstrate Outcome 3 under SAC conditions'],['(all AoS3 vocabulary)'],[],
 [S(5,'Setup','SAC conditions','Seat students, hand out the SAC and formula sheet; read the instructions.'),
  S(65,'SAC','SAC 3: Electricity','Students complete SAC 3 under test conditions.','SAC 3 (to be written: see Assessment plan)'),
  S(9,'Wrap-up','Collect and reflect','Collect all materials. Students note one thing they found hard.')])
X(I(44),['Understand my SAC 3 results and the model responses','Improve my weakest areas'],['(AoS3 vocabulary)'],[],
 [S(10,'Return','SAC 3 returned','Return marked SACs with the marking scheme.'),
  S(25,'Feedback','Model responses','Go through the model answers and the most common errors.'),
  S(36,'Apply','Corrections and redemption','Students correct their errors; eligible students sit the redemption task.','SAC 3 redemption (to be written)'),
  S(8,'Exit ticket','Next steps','Students write the two topics they’ll focus on for the exam.')])
X(I(45),['Complete any missed prac and its logbook entry','Have my logbook signed off for Unit 1'],['logbook','authentication'],[],
 [S(5,'Setup','Who needs what','Check the prac tracker: who missed which prac.'),
  S(55,'Prac','Catch-up pracs','Students who missed a prac complete it now (set up 2–3 stations). Others complete outstanding logbook analysis and reflections.'),
  S(14,'Logbook','Sign-off','Teacher checks every logbook for all 12 pracs, then signs and dates it (needed for satisfactory completion).'),
  S(5,'Pack-up','Return equipment','Equipment back.')])
# ======================= Week 16 =======================
for n,focus in [(46,'AoS1 Light and heat and AoS2 Nuclear'),(47,'AoS3 Electricity and mixed exam practice')]:
  X(I(n),[f'Revise {focus}','Practise exam technique: command words and timing'],['explain','calculate','compare','evaluate'],[],
   [S(8,'Do-now','Mixed retrieval','Five quick questions, one from each chapter.'),
    S(12,'Exam technique','Command words and timing','Model how to answer “explain”, “calculate”, “compare”, “evaluate”; about 1 mark per minute.'),
    S(51,'Apply','Revision questions',f'Targeted revision on {focus}: chapter review questions for the weakest areas from CFATs and SACs.','Pearson SB chapter reviews; Unit 1 fully worked solutions (teacher)'),
    S(8,'Exit ticket','Revision plan','Students list the three topics they’ll revise before the exam.')])
X(I(48),['Attempt a full practice exam under exam conditions'],['(all Unit 1 vocabulary)'],[],
 [S(5,'Setup','Exam conditions','Hand out the Unit 1 questions from the Pearson practice exam and the formula sheet.'),
  S(65,'Practice exam','Pearson practice exam (Unit 1 questions)','Students complete it under timed conditions. Use the mapping document to choose the Unit 1 questions.','Pearson Units 1 and 2 practice exam; mapping document'),
  S(9,'Wrap-up','Self-mark plan','Collect papers; answers released next lesson or at the start of the exam period.')])
json.dump(d,open(sys.argv[1],'w'),indent=1,ensure_ascii=False)
bad=[(k,sum(s['min'] for s in v['sequence']['steps'])) for k,v in L.items() if v.get('sequence') and sum(s['min'] for s in v['sequence']['steps'])!=79]
print('missing',[k for k,v in L.items() if not v.get('sequence')],'bad',bad)
