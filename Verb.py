import random

class Verb:
  def __init__(self, value):
    self.value = value
    self.present = Tense()
    self.imperfect = Tense()
    self.future = Tense()
    self.perfect = Tense()
    self.pluperfect = Tense()
    self.future_perfect = Tense()

  def get_declaination(self, dec):
    decs = {}
    for key, tense in self.pack().items():
      declination = [v[dec - 1] for v in tense.pack()]
      decs[key] = declination
    return decs

  def pack(self):
    return {
      'present': self.present,
      'imperfect': self.imperfect,
      'future': self.future,
      'perfect': self.perfect,
      'pluperfect': self.pluperfect,
      'future_perfect': self.future_perfect
    }

class Nounadj:
  def __init__(self, value):
    self.value = value
    self.singular = POS()
    self.plural = POS()


class Tense:
  def __init__(self):
    self.me = []
    self.yous = []
    self.it = []
    self.we = []
    self.youpl = []
    self.they = []

  def pack(self):
    return self.me, self.yous, self.it, self.we, self.youpl, self.they


class POS:
  def __init__(self):
    self.nominative = []
    self.genitive = []
    self.dative = []
    self.accusative = []
    self.ablative = []

RegularActive = Verb("RegularActive")
RegularPassive = Verb("RegularPassive")
Deponent = Verb("Deponent")

ego = Nounadj("ego")
sē = Nounadj("sē")
hesheit = Nounadj("hesheit")
hic = Nounadj("hic")
ille = Nounadj("ille")
ipse = Nounadj("ipse")
īdem = Nounadj("īdem")
quī = Nounadj("quī")


#Nounadj Data
ego.singular.nominative = ['', '', '', '']
ego.singular.genitive = ['', '', '', '']
ego.singular.dative = ['', '', '', '']
ego.singular.accusative = ['', '', '', '']
ego.singular.ablative = ['', '', '', '']

ego.plural.nominative = ['', '', '', '']
ego.plural.genitive = ['', '', '', '']
ego.plural.dative = ['', '', '', '']
ego.plural.accusative = ['', '', '', '']
ego.plural.ablative = ['', '', '', '']

sē.singular.nominative = ['', '', '', '']
sē.singular.genitive = ['', '', '', '']
sē.singular.dative = ['', '', '', '']
sē.singular.accusative = ['', '', '', '']
sē.singular.ablative = ['', '', '', '']

sē.plural.nominative = ['', '', '', '']
sē.plural.genitive = ['', '', '', '']
sē.plural.dative = ['', '', '', '']
sē.plural.accusative = ['', '', '', '']
sē.plural.ablative = ['', '', '', '']

hesheit.singular.nominative = ['', '', '', '']
hesheit.singular.genitive = ['', '', '', '']
hesheit.singular.dative = ['', '', '', '']
hesheit.singular.accusative = ['', '', '', '']
hesheit.singular.ablative = ['', '', '', '']

hesheit.plural.nominative = ['', '', '', '']
hesheit.plural.genitive = ['', '', '', '']
hesheit.plural.dative = ['', '', '', '']
hesheit.plural.accusative = ['', '', '', '']
hesheit.plural.ablative = ['', '', '', '']

hic.singular.nominative = ['', '', '', '']
hic.singular.genitive = ['', '', '', '']
hic.singular.dative = ['', '', '', '']
hic.singular.accusative = ['', '', '', '']
hic.singular.ablative = ['', '', '', '']

hic.plural.nominative = ['', '', '', '']
hic.plural.genitive = ['', '', '', '']
hic.plural.dative = ['', '', '', '']
hic.plural.accusative = ['', '', '', '']
hic.plural.ablative = ['', '', '', '']

ille.singular.nominative = ['', '', '', '']
ille.singular.genitive = ['', '', '', '']
ille.singular.dative = ['', '', '', '']
ille.singular.accusative = ['', '', '', '']
ille.singular.ablative = ['', '', '', '']

ille.plural.nominative = ['', '', '', '']
ille.plural.genitive = ['', '', '', '']
ille.plural.dative = ['', '', '', '']
ille.plural.accusative = ['', '', '', '']
ille.plural.ablative = ['', '', '', '']

ipse.singular.nominative = ['', '', '', '']
ipse.singular.genitive = ['', '', '', '']
ipse.singular.dative = ['', '', '', '']
ipse.singular.accusative = ['', '', '', '']
ipse.singular.ablative = ['', '', '', '']

ipse.plural.nominative = ['', '', '', '']
ipse.plural.genitive = ['', '', '', '']
ipse.plural.dative = ['', '', '', '']
ipse.plural.accusative = ['', '', '', '']
ipse.plural.ablative = ['', '', '', '']

īdem.singular.nominative = ['', '', '', '']
īdem.singular.genitive = ['', '', '', '']
īdem.singular.dative = ['', '', '', '']
īdem.singular.accusative = ['', '', '', '']
īdem.singular.ablative = ['', '', '', '']

īdem.plural.nominative = ['', '', '', '']
īdem.plural.genitive = ['', '', '', '']
īdem.plural.dative = ['', '', '', '']
īdem.plural.accusative = ['', '', '', '']
īdem.plural.ablative = ['', '', '', '']

quī.singular.nominative = ['', '', '', '']
quī.singular.genitive = ['', '', '', '']
quī.singular.dative = ['', '', '', '']
quī.singular.accusative = ['', '', '', '']
quī.singular.ablative = ['', '', '', '']

quī.plural.nominative = ['', '', '', '']
quī.plural.genitive = ['', '', '', '']
quī.plural.dative = ['', '', '', '']
quī.plural.accusative = ['', '', '', '']
quī.plural.ablative = ['', '', '', '']

#Verb Data 

#Checked
RegularActive.present.me = ['portō', 'doceō', 'trahō', 'audiō']
RegularActive.present.yous = ['portās', 'docēs', 'trahis', 'audīs']
RegularActive.present.it = ['portat', 'docet', 'trahit', 'audit']
RegularActive.present.we = ['portāmus', 'docēmus', 'trahimus', 'audīmus']
RegularActive.present.youpl = ['portātis', 'docētis', 'trahitis', 'audītis']
RegularActive.present.they = ['portant', 'docent', 'trahunt', 'audiunt']

#
RegularActive.imperfect.me = ['portābam', 'docēbam', 'trahēbam', 'audiēbam']
RegularActive.imperfect.yous = ['portābās', 'docēbās', 'trahēbās', 'audiēbās']
RegularActive.imperfect.it = ['portābat', 'docēbat', 'trahēbat', 'audiēbat']
RegularActive.imperfect.we = ['portābāmus', 'docēbāmus', 'trahēbāmus', 'audiēbāmus']
RegularActive.imperfect.youpl = ['portābātis', 'docēbātis', 'trahēbātis', 'audiēbātis']
RegularActive.imperfect.they = ['portābant', 'docēbant', 'trahēbant', 'audiēbant']

#
RegularActive.future.me = ['portābō', 'docēbō', 'traham', 'audiam']
RegularActive.future.yous = ['portābis', 'docēbis', 'trahēs', 'audiēs']
RegularActive.future.it = ['portābit', 'docēbit', 'trahet', 'audiet']
RegularActive.future.we = ['portābimus', 'docēbimus', 'trahētis', 'audiētis']
RegularActive.future.youpl = ['portābitis', 'docēbitis', 'trahētis', 'audiētis']
RegularActive.future.they = ['portābunt', 'docēbunt', 'trahent', 'audient']

#
RegularActive.perfect.me = ['portāvī', 'docuī', 'trāxī', 'audīvī']
RegularActive.perfect.yous = ['portāvistī', 'docuistī', 'trāxistī', 'audīvistī']
RegularActive.perfect.it = ['portāvit', '', '', '']
RegularActive.perfect.we = ['', '', '', '']
RegularActive.perfect.youpl = ['', '', '', '']
RegularActive.perfect.they = ['', '', '', '']

RegularActive.pluperfect.me = ['', '', '', '']
RegularActive.pluperfect.yous = ['', '', '', '']
RegularActive.pluperfect.it = ['', '', '', '']
RegularActive.pluperfect.we = ['', '', '', '']
RegularActive.pluperfect.youpl = ['', '', '', '']
RegularActive.pluperfect.they = ['', '', '', '']

RegularActive.future_perfect.me = ['', '', '', '']
RegularActive.future_perfect.yous = ['', '', '', '']
RegularActive.future_perfect.it = ['', '', '', '']
RegularActive.future_perfect.we = ['', '', '', '']
RegularActive.future_perfect.youpl = ['', '', '', '']
RegularActive.future_perfect.they = ['', '', '', '']

#Regular Passive Verb Data
RegularPassive.present.me = ['portor', 'doceor', 'trahor', 'audior']
RegularPassive.present.yous = ['', '', '', '']
RegularPassive.present.it = ['', '', '', '']
RegularPassive.present.we = ['', '', '', '']
RegularPassive.present.youpl = ['', '', '', '']
RegularPassive.present.they = ['', '', '', '']

RegularPassive.imperfect.me = ['', '', '', '']
RegularPassive.imperfect.yous = ['', '', '', '']
RegularPassive.imperfect.it = ['', '', '', '']
RegularPassive.imperfect.we = ['', '', '', '']
RegularPassive.imperfect.youpl = ['', '', '', '']
RegularPassive.imperfect.they = ['', '', '', '']

RegularPassive.future.me = ['', '', '', '']
RegularPassive.future.yous = ['', '', '', '']
RegularPassive.future.it = ['', '', '', '']
RegularPassive.future.we = ['', '', '', '']
RegularPassive.future.youpl = ['', '', '', '']
RegularPassive.future.they = ['', '', '', '']

RegularPassive.perfect.me = ['', '', '', '']
RegularPassive.perfect.yous = ['', '', '', '']
RegularPassive.perfect.it = ['', '', '', '']
RegularPassive.perfect.we = ['', '', '', '']
RegularPassive.perfect.youpl = ['', '', '', '']
RegularPassive.perfect.they = ['', '', '', '']

RegularPassive.pluperfect.me = ['', '', '', '']
RegularPassive.pluperfect.yous = ['', '', '', '']
RegularPassive.pluperfect.it = ['', '', '', '']
RegularPassive.pluperfect.we = ['', '', '', '']
RegularPassive.pluperfect.youpl = ['', '', '', '']
RegularPassive.pluperfect.they = ['', '', '', '']

RegularPassive.future_perfect.me = ['', '', '', '']
RegularPassive.future_perfect.yous = ['', '', '', '']
RegularPassive.future_perfect.it = ['', '', '', '']
RegularPassive.future_perfect.we = ['', '', '', '']
RegularPassive.future_perfect.youpl = ['', '', '', '']
RegularPassive.future_perfect.they = ['', '', '', '']

#Deponent Verbs

Deponent.present.me = ['cōnor', 'vereor', 'loquor', 'orior']
Deponent.present.yous = ['', '', '', '']
Deponent.present.it = ['', '', '', '']
Deponent.present.we = ['', '', '', '']
Deponent.present.youpl = ['', '', '', '']
Deponent.present.they = ['', '', '', '']

Deponent.imperfect.me = ['', '', '', '']
Deponent.imperfect.yous = ['', '', '', '']
Deponent.imperfect.it = ['', '', '', '']
Deponent.imperfect.we = ['', '', '', '']
Deponent.imperfect.youpl = ['', '', '', '']
Deponent.imperfect.they = ['', '', '', '']

Deponent.future.me = ['', '', '', '']
Deponent.future.yous = ['', '', '', '']
Deponent.future.it = ['', '', '', '']
Deponent.future.we = ['', '', '', '']
Deponent.future.youpl = ['', '', '', '']
Deponent.future.they = ['', '', '', '']

Deponent.perfect.me = ['', '', '', '']
Deponent.perfect.yous = ['', '', '', '']
Deponent.perfect.it = ['', '', '', '']
Deponent.perfect.we = ['', '', '', '']
Deponent.perfect.youpl = ['', '', '', '']
Deponent.perfect.they = ['', '', '', '']

Deponent.pluperfect.me = ['', '', '', '']
Deponent.pluperfect.yous = ['', '', '', '']
Deponent.pluperfect.it = ['', '', '', '']
Deponent.pluperfect.we = ['', '', '', '']
Deponent.pluperfect.youpl = ['', '', '', '']
Deponent.pluperfect.they = ['', '', '', '']

Deponent.future_perfect.me = ['', '', '', '']
Deponent.future_perfect.yous = ['', '', '', '']
Deponent.future_perfect.it = ['', '', '', '']
Deponent.future_perfect.we = ['', '', '', '']
Deponent.future_perfect.youpl = ['', '', '', '']
Deponent.future_perfect.they = ['', '', '', '']

#print(RegularActive.present.me)

#Algorithm
user_input = RegularActive.present

# print(RegularActive.present)

print(RegularActive.get_declaination(1))

# print(RegularActive.present.me)
# print(RegularActive.imperfect.me)
# x = 0
# for i in range(0, len(user_input))
#   print(RegularActive.future.me[x])
#   x+=1