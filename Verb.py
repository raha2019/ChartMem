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
ego.singular.nominative.append([''])
ego.singular.genitive.append([''])
ego.singular.dative.append([''])
ego.singular.accusative.append([''])
ego.singular.ablative.append([''])

ego.plural.nominative.append([''])
ego.plural.genitive.append([''])
ego.plural.dative.append([''])
ego.plural.accusative.append([''])
ego.plural.ablative.append([''])

sē.singular.nominative.append([''])
sē.singular.genitive.append([''])
sē.singular.dative.append([''])
sē.singular.accusative.append([''])
sē.singular.ablative.append([''])

sē.plural.nominative.append([''])
sē.plural.genitive.append([''])
sē.plural.dative.append([''])
sē.plural.accusative.append([''])
sē.plural.ablative.append([''])

hesheit.singular.nominative.append([''])
hesheit.singular.genitive.append([''])
hesheit.singular.dative.append([''])
hesheit.singular.accusative.append([''])
hesheit.singular.ablative.append([''])

hesheit.plural.nominative.append([''])
hesheit.plural.genitive.append([''])
hesheit.plural.dative.append([''])
hesheit.plural.accusative.append([''])
hesheit.plural.ablative.append([''])

hic.singular.nominative.append([''])
hic.singular.genitive.append([''])
hic.singular.dative.append([''])
hic.singular.accusative.append([''])
hic.singular.ablative.append([''])

hic.plural.nominative.append([''])
hic.plural.genitive.append([''])
hic.plural.dative.append([''])
hic.plural.accusative.append([''])
hic.plural.ablative.append([''])

ille.singular.nominative.append([''])
ille.singular.genitive.append([''])
ille.singular.dative.append([''])
ille.singular.accusative.append([''])
ille.singular.ablative.append([''])

ille.plural.nominative.append([''])
ille.plural.genitive.append([''])
ille.plural.dative.append([''])
ille.plural.accusative.append([''])
ille.plural.ablative.append([''])

ipse.singular.nominative.append([''])
ipse.singular.genitive.append([''])
ipse.singular.dative.append([''])
ipse.singular.accusative.append([''])
ipse.singular.ablative.append([''])

ipse.plural.nominative.append([''])
ipse.plural.genitive.append([''])
ipse.plural.dative.append([''])
ipse.plural.accusative.append([''])
ipse.plural.ablative.append([''])

īdem.singular.nominative.append([''])
īdem.singular.genitive.append([''])
īdem.singular.dative.append([''])
īdem.singular.accusative.append([''])
īdem.singular.ablative.append([''])

īdem.plural.nominative.append([''])
īdem.plural.genitive.append([''])
īdem.plural.dative.append([''])
īdem.plural.accusative.append([''])
īdem.plural.ablative.append([''])

quī.singular.nominative.append([''])
quī.singular.genitive.append([''])
quī.singular.dative.append([''])
quī.singular.accusative.append([''])
quī.singular.ablative.append([''])

quī.plural.nominative.append([''])
quī.plural.genitive.append([''])
quī.plural.dative.append([''])
quī.plural.accusative.append([''])
quī.plural.ablative.append([''])

#Verb Data

#Checked
RegularActive.present.me = ['portō', 'doceō', 'trahō', 'audiō']
RegularActive.present.yous = ['portās', 'docēs', 'trahis', 'audīs']
RegularActive.present.it.append(['portat', 'docet', 'trahit', 'audit'])
RegularActive.present.we.append(['portāmus', 'docēmus', 'trahimus', 'audīmus'])
RegularActive.present.youpl.append(['portātis', 'docētis', 'trahitis', 'audītis'])
RegularActive.present.they.append(['portant', 'docent', 'trahunt', 'audiunt'])

#
RegularActive.imperfect.me.append(['portābam', 'docēbam', 'trahēbam', 'audiēbam'])
RegularActive.imperfect.yous.append(['portābās', 'docēbās', 'trahēbās', 'audiēbās'])
RegularActive.imperfect.it.append(['portābat', 'docēbat', 'trahēbat', 'audiēbat'])
RegularActive.imperfect.we.append(['portābāmus', 'docēbāmus', 'trahēbāmus', 'audiēbāmus'])
RegularActive.imperfect.youpl.append(['portābātis', 'docēbātis', 'trahēbātis', 'audiēbātis'])
RegularActive.imperfect.they.append(['portābant', 'docēbant', 'trahēbant', 'audiēbant'])

#
RegularActive.future.me.append(['portābō', 'docēbō', 'traham', 'audiam'])
RegularActive.future.yous.append(['portābis', 'docēbis', 'trahēs', 'audiēs'])
RegularActive.future.it.append(['portābit', 'docēbit', 'trahet', 'audiet'])
RegularActive.future.we.append(['portābimus', 'docēbimus', 'trahētis', 'audiētis'])
RegularActive.future.youpl.append(['portābitis', 'docēbitis', 'trahētis', 'audiētis'])
RegularActive.future.they.append(['portābunt', 'docēbunt', 'trahent', 'audient'])

#
RegularActive.perfect.me.append([''])
RegularActive.perfect.yous.append([''])
RegularActive.perfect.it.append


RegularPassive.present.me.append(['portor', 'doceor', 'trahor', 'audior'])

Deponent.present.me.append(['cōnor', 'vereor', 'loquor', 'orior'])

print(RegularActive.present.me)

#Algorithm
user_input = RegularActive.present

# print(RegularActive.present)

# print(RegularActive.present.me)
# print(RegularActive.imperfect.me)
