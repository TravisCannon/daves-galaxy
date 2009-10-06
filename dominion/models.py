from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db import models
from django.core.mail import send_mail
from django.db.models import Q
import datetime
import math
import operator
import random
0,1,2,3,5,7,9
SVG_SCHEMA = "http://www.w3.org/Graphics/SVG/1.2/rng/"
DISPOSITIONS = (
    ('0', 'Garrison'),
    ('1', 'Planetary Defense'),
    ('2', 'Scout'),
    ('3', 'Screen'),
    ('4', 'Diplomacy'),
    ('5', 'Attack'),
    ('6', 'Colonize'),
    ('7', 'Move'),
    ('8', 'Trade'),
    ('9', 'Piracy'),
    )

INSTRUMENTALITIES = (
    ('0', 'Sensor Array'),
    ('1', 'Planetary Defense Network'),
    ('2', 'International Port'),
    ('3', 'Regional Government'),
    )

scouts_info  = "<b>Scouts</b> are fast, lightly armed and armored ships.  "
scouts_info += "ideal for watching over trade routes, or keeping tabs on your neighbors."

arcs_info    = "<b>Arcs</b> are large hulks of ships, the only type of ship able to colonize "
arcs_info   += "another planet.  Upon arrival at an unoccupied planet, the colonists "
arcs_info   += "will cannibalize the arc to provide the materials needed to start a "
arcs_info   += "colony."

merchantmen_info  = "<b>Merchants</b> go from planet to planet, buying and selling goods on the "
merchantmen_info += "local market, and then moving on to the next planet.  Once a certain "
merchantmen_info += "level of profit is reached, they return to their home port and render "
merchantmen_info += "a profit to their owners (and taxes to the planetary government)."

fighters_info     = "<b>Fighters</b> are small unpiloted drones incapable of interplanetary travel.  "
fighters_info    += "They can be used as a cheap planetary defense, and can be carried between "
fighters_info    += "planets by a <b>Carrier</b>."

frigates_info     = "<b>Frigates</b> are the smallest effective military unit.  Designed for use "
frigates_info    += "as convoy escorts, and as a screen for larger military units."

destroyers_info   = "<b>Destroyers</b> are the workhorse of military units.  Relatively cheap and "
destroyers_info  += "quick, they are lightly armored and relatively expendable."

cruisers_info     = "<b>Cruisers</b> are the smallest of the capital ships.  They are the smallest "
cruisers_info    += "ship that require the use of scarce commodities (1 unit of Krellmetal) to "
cruisers_info    += "build.  Cruisers can accelerate at the same rate as Destroyers, but are much "
cruisers_info    += "more powerful in the attack."

battleships_info  = "<b>Battleships</b> are larger and more powerful than cruisers, having a much "
battleships_info += "better defense capability.  They are a little slower than cruisers however, and "
battleships_info += "are much more expensive."

superbattleships_info = "Like battleships, but bigger, faster, more expensive..."

carriers_info = "<b>Carriers</b> are large, thinly armored ships designed to carry fighters around.  "
carriers_info += "ideally suited for attacking heavily defended targets (as long as they are "
carriers_info += "carrying fighters...)"

buildfleettooltips = [
  {'id': '#info-scouts', 'tip': scouts_info},
  {'id': '#info-arcs', 'tip': arcs_info},
  {'id': '#info-merchantmen', 'tip': merchantmen_info},
  {'id': '#info-fighters', 'tip': fighters_info},
  {'id': '#info-frigates', 'tip': frigates_info},
  {'id': '#info-cruisers', 'tip': cruisers_info},
  {'id': '#info-battleships', 'tip': battleships_info},
  {'id': '#info-superbattleships', 'tip': superbattleships_info},
  {'id': '#info-carriers', 'tip': carriers_info},
  {'id': '#info-destroyers', 'tip': destroyers_info}]

shiptypes = {
  'scouts':           {'singular': 'scout', 'plural': 'scouts',
                       'accel': .4, 'att': 1, 'def': 10, 
                       'sense': .5, 'effrange': .5,
                       'required':
                         {'people': 5, 'food': 5, 'steel': 1, 
                         'antimatter': 1, 'quatloos': 10,
                         'unobtanium':0, 'krellmetal':0}
                      },
  'arcs':             {'singular': 'arc', 'plural': 'arcs',
                       'accel': .25, 'att': 0, 'def': 2, 
                       'sense': .2, 'effrange': .25,
                       'required':
                         {'people': 500, 'food': 1000, 'steel': 200, 
                         'antimatter': 10, 'quatloos': 200,
                         'unobtanium':0, 'krellmetal':0}
                      },

  'merchantmen':      {'singular': 'merchantman', 'plural': 'merchantmen',
                       'accel': .28, 'att': 0, 'def': 2, 
                       'sense': .2, 'effrange': .25,
                       'required':
                         {'people': 20, 'food': 20, 'steel': 30, 
                         'antimatter': 2, 'quatloos': 10,
                         'unobtanium':0, 'krellmetal':0}
                      },
  'fighters':         {'singular': 'fighter', 'plural': 'fighters',
                       'accel': 0.0,
                       'att': 5, 'def': 1, 
                       'sense': 1.0, 'effrange': 2.0,
                       'required':
                         {'people': 0, 'food': 0, 'steel': 1, 
                         'antimatter': 0, 'quatloos': 10,
                         'unobtanium':0, 'krellmetal':0}
                      },
  'frigates':         {'singular': 'frigate', 'plural': 'frigates',
                       'accel': .35, 'att': 10, 'def': 8, 
                       'sense': .4, 'effrange': 1.0,
                       'required':
                         {'people': 50, 'food': 50, 'steel': 50, 
                         'antimatter': 10, 'quatloos': 100,
                         'unobtanium':0, 'krellmetal':0}
                      },
  'destroyers':       {'singular': 'destroyer', 'plural': 'destroyer',
                       'accel':.32, 'att': 15, 'def': 7, 
                       'sense': .5, 'effrange': 1.2,
                       'required':
                         {
                         'people': 70, 'food': 70, 'steel': 100, 
                         'antimatter': 12, 'quatloos': 150,
                         'unobtanium':0, 'krellmetal':0}
                      },
  'cruisers':         {'singular': 'cruiser', 'plural': 'cruisers',
                       'accel': .32, 'att': 30, 'def': 6, 
                       'sense': .7, 'effrange': 1.8,
                       'required':
                         {
                         'people': 100, 'food': 100, 'steel': 200, 
                         'antimatter': 20, 'quatloos': 500,
                         'unobtanium':0, 'krellmetal':1}
                      },
  'battleships':      {'singular': 'battleship', 'plural': 'battleships',
                       'accel': .25, 'att': 50, 'def': 10, 
                       'sense': .7, 'effrange': 2.0,
                       'required':
                         {
                         'people': 200, 'food': 200, 'steel': 1000, 
                         'antimatter': 50, 'quatloos': 2000,
                         'unobtanium':0, 'krellmetal':3}
                      },
  'superbattleships': {'singular': 'super battleship', 'plural': 'super battleships',
                       'accel': .24, 'att': 100, 'def': 20, 
                       'sense': 1.0, 'effrange': 2.0,
                       'required':
                         {
                         'people': 300, 'food': 300, 'steel': 5000, 
                         'antimatter': 150, 'quatloos': 5000,
                         'unobtanium':1, 'krellmetal':5}
                      },
  'carriers':         {'singular': 'carrier', 'plural': 'carriers',
                       'accel': .2, 'att': 0, 'def': 10, 
                       'sense': 1.2, 'effrange': .5,
                       'required':
                         {
                         'people': 500, 'food': 500, 'steel': 7500, 
                         'antimatter': 180, 'quatloos': 6000,
                         'unobtanium':5, 'krellmetal':10} 
                       }
  }
  
productionrates = {'people': {'baserate': 1.2, 'socmodifier': -0.0028, 'initial': 50000},
                   'quatloos': {'baserate': 1.0, 'socmodifier': 0.0, 'initial': 1000},
                   'food': {'baserate': 1.1, 'socmodifier': -.0013, 'initial': 5000},
                   'consumergoods': {'baserate': .9999, 'socmodifier': .0000045, 'initial': 2000},
                   'steel': {'baserate': 1.001, 'socmodifier': 0.0, 'initial': 500},
                   'unobtanium': {'baserate': .99999, 'socmodifier': .00000025, 'initial': 0},
                   'krellmetal': {'baserate': .999995, 'socmodifier':.0000003, 'initial': 0},
                   'antimatter': {'baserate': .9999, 'socmodifier': .000008, 'initial': 50},
                   'hydrocarbon': {'baserate': 1.01, 'socmodifier': -.00018, 'initial': 1000}
                  }


class Instrumentality(models.Model):
  planet = models.ForeignKey('Planet')
  type = models.PositiveIntegerField(default=0, choices = INSTRUMENTALITIES)
  state = models.PositiveIntegerField(default=0)

class Player(models.Model):
  def __unicode__(self):
      return self.user.username
  user = models.ForeignKey(User, unique=True)
  lastactivity = models.DateTimeField(auto_now=True)
  capital = models.ForeignKey('Planet', unique=True)
  color = models.CharField(max_length=15)

  appearance = models.XMLField(blank=True, schema_path=SVG_SCHEMA)
  friends = models.ManyToManyField("self")
  enemies = models.ManyToManyField("self")
  def getpoliticalrelation(self,otherid):
    if otherid in self.enemies.all():
      return "enemy"
    elif otherid in self.friends.all():
      return "friend"
    else:
      return "neutral"
  def setpoliticalrelation(self,otherid,state):
    if state in ["neutral","none"]:
      self.friends.remove(otherid)
      self.enemies.remove(otherid)
    elif state=="friend":
      self.enemies.remove(otherid)
      self.friends.add(otherid)
    elif state=="enemy":
      self.enemies.add(otherid)
      self.friends.remove(otherid)
  def create(self):
    if len(self.user.planet_set.all()) > 0:
      # cheeky fellow
      return
    narrative = []
    self.lastactivity = datetime.datetime.now()
    userlist = User.objects.exclude(id=self.user.id)
    random.seed()
    userorder = range(len(userlist))
    random.shuffle(userorder)
    for uid in userorder:
      narrative.append("looking at user " + str(uid))
      curuser= userlist[uid]
      planetlist = curuser.planet_set.all()
      if len(planetlist):
        planetorder = range(len(planetlist))
        random.shuffle(planetorder)
        for pid in planetorder:
          narrative.append("looking at planet " + str(pid) + "(" + str(planetlist[pid].id) + ")")
          curplanet = planetlist[pid]
          distantplanets = nearbysortedthings(Planet,curplanet)
          distantplanets.reverse()
          if len(distantplanets) < 6:
            narrative.append("not enough distant planets")
            continue
          for distantplanet in distantplanets:
            suitable = True
            #look at the 'distant planet' and its 5 closest 
            # neighbors and see if they are available
            if distantplanet.owner is not None:
              narrative.append("distant owner not none")
              continue 
            nearcandidates = nearbysortedthings(Planet,distantplanet)
            # make sure the 5 closest planets are free
            for nearcandidate in nearcandidates[:5]:
              if nearcandidate.owner is not None:
                narrative.append("near candidate not none")
                suitable = False
                break
            #if there is a nearby inhabited planet closer than 7
            #units away, continue...
            for nearcandidate in nearcandidates:
              distance = getdistanceobj(nearcandidate,distantplanet)
              narrative.append("d = " + str(distance))
              if nearcandidate.owner is not None:
                narrative.append("distance less than 7 owner = " + str(nearcandidate.owner))
                suitable = False
                break
              if distance > 7.9:
                break
                
            if suitable:
              narrative.append("found suitable")
              distantplanet.owner = self.user
              self.capital = distantplanet
              #self.color = "#ff0000"
              self.color = "#" + hex(((random.randint(64,255) << 16) + 
                            (random.randint(64,255) << 8) + 
                            (random.randint(64,255))))[2:]
              self.save()
              distantplanet.populate()
              distantplanet.save()
              return
    message = []
    message.append('Could not create new player planet for user: ')
    message.append(self.user.username + "("+str(self.user.id)+")")
    message.append('error follows...')
    message.append(' ')
    message.append("\n".join(narrative))
    message = "\n".join(message)
    print "---"
    print message
    print "---"
    send_mail("Dave's Galaxy Problem!", 
              message,
              'support@davesgalaxy.com',
              ['dav3xor@gmail.com'])

    print "did not find suitable"
class Manifest(models.Model):
  people = models.PositiveIntegerField(default=0)
  food = models.PositiveIntegerField(default=0)
  consumergoods = models.PositiveIntegerField(default=0)
  steel = models.PositiveIntegerField(default=0)
  krellmetal = models.PositiveIntegerField(default=0)
  unobtanium = models.PositiveIntegerField(default=0)
  antimatter = models.PositiveIntegerField(default=0)
  hydrocarbon = models.PositiveIntegerField(default=0)
  quatloos = models.PositiveIntegerField(default=0)
  def manifestlist(self, skip):
    mlist = {}
    for field in self._meta.fields:
      if field.name not in skip: 
        mlist[field.name] = getattr(self,field.name)
    return mlist

class Fleet(models.Model):
  def __unicode__(self):
    numships = self.numships()
    return '(' + str(self.id) + ') '+ str(numships) + ' ship' + ('' if numships == 1 else 's')
  owner = models.ForeignKey(User)
  disposition = models.PositiveIntegerField(default=0, choices = DISPOSITIONS)
  homeport = models.ForeignKey("Planet", null=True, related_name="home_port", editable=False)
  trade_manifest = models.ForeignKey("Manifest", null=True, editable=False)
  sector = models.ForeignKey("Sector", editable=False)
  speed = models.FloatField(default=0)
  direction = models.FloatField(default=0, editable=False)
  x = models.FloatField(default=0, editable=False)
  y = models.FloatField(default=0, editable=False)

  destination = models.ForeignKey("Planet", related_name="destination_port", null=True, editable=False)
  dx = models.FloatField(default=0, editable=False)
  dy = models.FloatField(default=0, editable=False)
  
  scouts = models.PositiveIntegerField(default=0)
  arcs = models.PositiveIntegerField(default=0)
  merchantmen = models.PositiveIntegerField(default=0)
  fighters = models.PositiveIntegerField(default=0)
  frigates = models.PositiveIntegerField(default=0)
  destroyers = models.PositiveIntegerField(default=0)
  cruisers = models.PositiveIntegerField(default=0)
  battleships = models.PositiveIntegerField(default=0)
  superbattleships = models.PositiveIntegerField(default=0)
  carriers = models.PositiveIntegerField(default=0)
  def shiplistreport(self):
    output = []
    for type in self.shiptypeslist():
      numships = getattr(self, type.name)
      if numships == 0:
        continue
      name = type.name
      if numships == 1:
        name = shiptypes[name]['singular']
      output.append(name + ": " + str(numships))
    return "\n".join(output)
  def shortdescription(self, html=1):
    description = "Fleet #"+str(self.id)+", "
    curshiptypes = self.shiptypeslist()
    if len(curshiptypes) == 1:
      if getattr(self,curshiptypes[0].name) == 1:
        if html==1:
          description += "<span class=\"fleetnum\">" 
        description += str(getattr(self,curshiptypes[0].name))
        if html==1:
          description += "</span>"
        description += " " + shiptypes[curshiptypes[0].name]['singular']
      else:
        if html==1:
          description += "<span class=\"fleetnum\">" 
        description += str(getattr(self,curshiptypes[0].name))
        if html==1:
          description += "</span>"
        description += " " + shiptypes[curshiptypes[0].name]['plural']
    else:
      if html==1:
        description += "<span class=\"fleetnum\">" 
      description += str(self.numships())
      if html==1:
        description += "</span>" + " mixed ships"
    return description
  def description(self):
    desc = []
    desc.append(self.__unicode__() + ":")
    for type in self.shiptypeslist():
      desc.append(str(getattr(self,type.name)) + " --> " + type.name)
    desc.append("acceleration = " + str(self.acceleration()))
    desc.append("attack = " + str(self.numattacks()) + " defense = " + str(self.numdefenses()))
    return "\n".join(desc)
  def json(self, playersship=0):
    json = {}
    json['x'] = self.x
    json['y'] = self.y
    json['i'] = self.id
    json['c'] = self.owner.get_profile().color
    json['s'] = self.senserange()
    if playersship == 1:
      json['ps'] = 1
    if self.dx:
      distanceleft = getdistance(self.x,self.y,self.dx,self.dy)
      angle = math.atan2(self.x-self.dx,self.y-self.dy)
      if distanceleft > .2:
        x2 = self.x - math.sin(angle) * (distanceleft-.2)
        y2 = self.y - math.cos(angle) * (distanceleft-.2)
      else:
        x2 = self.dx
        y2 = self.dy
      json['x2'] = x2
      json['y2'] = y2
    else:
      json['x2'] = 0
      json['y2'] = 0

    return json

  def gotoplanet(self,destination):
    self.direction = math.atan2(self.x-destination.x,self.y-destination.y)
    self.dx = destination.x
    self.dy = destination.y
    self.destination = destination
    self.sector = Sector.objects.get(pk=int(self.x/5.0) * 1000 + int(self.y/5.0))
    self.save()
  def gotoloc(self,dx,dy):
    self.dx = float(dx)
    self.dy = float(dy)
    self.direction = math.atan2(self.x-self.dx,self.y-self.dy)
    self.destination = None
    self.sector = Sector.objects.get(pk=int(self.x/5.0) * 1000 + int(self.y/5.0))
    self.save()
  def arrive(self):
    self.speed=0
    self.x = self.dx
    self.y = self.dy
    self.save()
  def validdispositions(self):
    
    valid = []
    if self.arcs > 0:
      valid.append(DISPOSITIONS[6])
    if self.merchantmen > 0:
      valid.append(DISPOSITIONS[8])

    if self.numcombatants():
      valid.append(DISPOSITIONS[1])
      valid.append(DISPOSITIONS[2])
      valid.append(DISPOSITIONS[5])
      valid.append(DISPOSITIONS[9])
    return tuple(valid)


  def defenselevel(self,shiptype):
    if type(shiptype) is str:
      return shiptypes[shiptype]['def']
    elif type(shiptype) is models.PositiveIntegerField and shiptype.name != 'disposition':
      
      return shiptypes[shiptype.name]['def']
    else:
      return -1

  def attacklevel(self,shiptype):
    if type(shiptype) is str:
      return shiptypes[shiptype]['att']
    elif type(shiptype) is models.PositiveIntegerField and shiptype.name != 'disposition':
      
      return shiptypes[shiptype.name]['att']
    else:
      return -1

  def hasshiptype(self, shiptype):
    typestr = ""
    if type(shiptype) is str:
      typestr = shiptype
    else:
      typestr = shiptype.name
    if not shiptypes.has_key(typestr):
      return False
    if getattr(self,typestr) > 0:
      return True
    else:
      return False
  def shiptypeslist(self):
    return filter(lambda x: self.hasshiptype(x), self._meta.fields)
  def acceleration(self):
    try:
      accel =  min([shiptypes[x.name]['accel'] for x in self.shiptypeslist()])
      accel += min([self.homeport.society*.001, .1])
    except ValueError: 
      return 0
    return accel
  def numdefenses(self):
    return sum([getattr(self,x.name)*shiptypes[x.name]['def'] for x in self.shiptypeslist()])
  def numattacks(self):
    return sum([getattr(self,x.name)*shiptypes[x.name]['att'] for x in self.shiptypeslist()])
  def numcombatants(self):
    return sum([getattr(self,x.name) for x in filter(lambda y: self.attacklevel(y)>0, self.shiptypeslist())])
  def numnoncombatants(self):
    return sum([getattr(self,x.name) for x in filter(lambda y: self.attacklevel(y)==0, self.shiptypeslist())])
  def senserange(self):
    range = 0
    if not self.owner:
      return range
    if self.numships() > 0:
      range =  max([shiptypes[x.name]['sense'] for x in self.shiptypeslist()])
      range += min([self.homeport.society*.002, .2])
      range += min([self.numships()*.01, .2])
    return range
  def numships(self):
    return sum([getattr(self,x.name) for x in self.shiptypeslist()]) 
   
  def dotrade(self,report):
    replinestart = "  Trading at " + self.destination.name + " ("+str(self.destination.id)+") "
    if self.trade_manifest is None:
      report.append(replinestart+"can't trade without trade goods.")
      return
    if self.destination.resources is None:
      report.append(replinestart+"planet doesn't support trade.")
      return
    # sell whatever is in the hold
    m = self.trade_manifest
    curplanet = self.destination
    curprices = curplanet.getprices()
    shipsmanifest = m.manifestlist(['id','quatloos'])
    r = curplanet.resources
    for line in shipsmanifest:
      numtosell = getattr(m,line)
      if(numtosell > 0):
        profit = curplanet.getprice(line) * numtosell
        if line == 'people':
          report.append(replinestart + 
                        " disembarking " + str(numtosell) + " passengers.")
        else:
          report.append(replinestart + 
                        " selling " + str(numtosell) + " " + str(line) +
                        " for " + str(profit) + ".")
        setattr(m,'quatloos',getattr(m,'quatloos')+profit)
        setattr(m,line,0)
        setattr(r,line,numtosell)
        if r.quatloos - profit < 0:
          r.quatloos = 0
        else:
          setattr(r,'quatloos',getattr(r,'quatloos')-profit)
    m.save()
    r.save()

    # look for next destination (most profitable...)
    
    # reset curprices to only ones that are available to sell...
    curprices = curplanet.getavailableprices()

    bestdif = -10000.0
    bestplanet = 0
    bestcommodity = 0 

    # should we pay taxes?
    if m.quatloos > 20000 and self.destination == self.homeport:
      self.homeport.resources.quatloos += m.quatloos - 5000
      m.quatloos = 5000
      m.save()
      self.homeport.resources.save()

    # first see if we need to go home...
    if m.quatloos > 20000 and self.destination != self.homeport:
      report.append(replinestart + 
                    " going home!")
      distance = getdistanceobj(self,self.homeport)
      bestplanet = self.homeport
      bestcommodity, bestdif = findbestdeal(curprices,
                                            self.homeport.getprices(),
                                            m.quatloos)
    else: 
      # first build a list of nearby planets, sorted by distance
      plist = nearbysortedthings(Planet,self)[1:]
      
      for destplanet in plist:
        distance = getdistanceobj(self,destplanet)
        if destplanet == self.destination:
          print "shouldn't happen"
          continue
        if destplanet.owner == None:
          continue
        if not (destplanet.opentrade or destplanet.owner == self.owner):
          continue
        if destplanet.resources == None:
          continue
        if self.owner.get_profile().getpoliticalrelation(destplanet.owner.get_profile()) == "enemy":
          continue

        commodity = "food"
        differential = -10000

        if destplanet.resources.food <= 0 and curplanet.resources.food > 0 and \
           Fleet.objects.filter(destination=destplanet, disposition=8).count() < 3:
          #drop everything and do famine relief
          report.append(replinestart + 
                        " initiating famine relief mission to planet " +
                        str(destplanet.name)+
                        " (" + str(destplanet.id) + ")")
          bestplanet = destplanet
          bestcommodity = "food"
          break
        else:
          destprices = destplanet.getprices()
          commodity, differential = findbestdeal(curprices,
                                                 destprices,
                                                 m.quatloos)
          differential -= distance*.05
          #attempt to get ships to go between more than the 2 most
          #convenient planets...
          if destplanet.society < curplanet.society:
            competition = Fleet.objects.filter(destination=destplanet, disposition=8).count()
            differential -= competition*.1
          if differential > bestdif:
            bestdif = differential 
            bestplanet = destplanet
            bestcommodity = commodity

    if bestplanet:
      self.gotoplanet(bestplanet)
      numbuyable = m.quatloos/curprices[bestcommodity]
      if numbuyable > 500 * self.merchantmen:
        # we have officially bulked out!
        numbuyable = 500 * self.merchantmen
      cost = numbuyable*curprices[bestcommodity]
      leftover = m.quatloos - numbuyable*curprices[bestcommodity]
      setattr(m, bestcommodity, 
              getattr(m, bestcommodity) + numbuyable)
      if m.quatloos - cost < 0:
        m.quatloos = 0
      else:
        m.quatloos -= cost
      m.save()
      r.quatloos += cost
      setattr(r, bestcommodity, 
              getattr(r, bestcommodity) - numbuyable)
      r.save()
      self.save()
      if bestcommodity == 'people':
        report.append(replinestart + "took on " + str(getattr(m,bestcommodity)) + " passengers.")
      else:
        report.append(replinestart + "bought " + str(getattr(m,bestcommodity)) + " " + bestcommodity)
      report.append(replinestart + "leftover quatloos = " + str(m.quatloos))
      report.append(replinestart + "new destination = " + str(bestplanet.id))
    # disembark passengers (if they want to disembark here, otherwise
    # they wait until the next destination)

  def newfleetsetup(self,planet,ships):
    buildableships = planet.buildableships()
    notspent = buildableships['commodities']
    for shiptype in ships:
      if not buildableships['types'].has_key(shiptype):
        print "cannot build type " + shiptype
        continue
      for commodity in buildableships['types'][shiptype]:
        notspent[commodity] -= buildableships['types'][shiptype][commodity]*ships[shiptype]
      for commodity in notspent:
        if notspent[commodity] < 0:
          return "Not enough " + commodity + " to build fleet..."
    for shiptype in ships:
      setattr(self, shiptype, ships[shiptype])
    for commodity in notspent:
      setattr(planet.resources, commodity, notspent[commodity])
    planet.save()
    planet.resources.save()

    self.homeport = planet
    self.x = planet.x
    self.y = planet.y
    self.dx = planet.x
    self.dy = planet.y
    self.sector = planet.sector
    self.owner = planet.owner
    
    if self.arcs > 0:
      self.disposition = 6
    elif self.merchantmen > 0:
      self.disposition = 8
      manifest = Manifest()
      manifest.quatloos = 1000 * self.merchantmen
      manifest.save()
      self.trade_manifest = manifest
      #self.trade_manifest.save() 
    self.save()
    return self
    
  def move(self):
    accel = self.acceleration()
    distancetodest = getdistance(self.x,self.y,self.dx,self.dy)
    if accel and distancetodest:
      daystostop = (math.ceil(self.speed/accel))
      distancetostop = .5*(self.speed)*(daystostop) # classic kinetics...
      if(distancetodest<=distancetostop):
        self.speed -= accel
        if self.speed <= 0:
          self.speed = 0
      elif self.speed < 5.0:
        self.speed += accel
        if self.speed > 5.0:
          self.speed = 5.0
      #now actually move the fleet...
      self.x = self.x - math.sin(self.direction)*self.speed
      self.y = self.y - math.cos(self.direction)*self.speed
      sectorkey = int(self.x/5.0)*1000 + int(self.y/5.0)
      self.sector = Sector.objects.get(pk=sectorkey)
      self.save()
  def doassault(self,destination,report):
    replinestart = "  Assaulting Planet " + self.destination.name + " ("+str(self.destination.id)+")"
    nf = nearbysortedthings(Fleet,self)
    for f in nf:
      if f == self:
        continue
      if f.numcombatants() == 0:
        continue
      distance = getdistanceobj(f,self)
      if distance < self.senserange() or distance < f.senserange():
        report.append(replinestart + "unsuccessful assault -- planet currently defended")
        # can't assault when there's a defender nearby...
        return
    # ok, we've made it through any defenders...
    if destination.resources:
      report.append(replinestart + "assault in progress -- raining death from space")
      potentialloss = self.numattacks()/1000.0
      if potentialloss > .5:
        potentialloss = .5
      for key in destination.resources.manifestlist([]):
        curvalue = getattr(destination.resources,key)
        if curvalue > 0:
          newvalue = curvalue - (curvalue*(random.random()*potentialloss))
          setattr(destination.resources,key,newvalue)
      destination.save()
    if random.random() < .2:
      report.append(replinestart + "planetary assault -- capitulation!")
      #capitulation -- planet gets new owner...
      destination.owner = self.owner
      destination.save()
        
  def doturn(self,report):
    replinestart = "Fleet: " + self.shortdescription(html=0) + " (" + str(self.id) + ") "
    # see if we need to move the fleet...
    distancetodest = getdistance(self.x,self.y,self.dx,self.dy)
    # figure out how fast the fleet can go
    
    if distancetodest < self.speed: 
      # we have arrived at our destination
      if self.destination:
        report.append(replinestart +
                      "Arrived at " +
                      self.destination.name + 
                      " ("+str(self.destination.id)+")")
      else:
        report.append(replinestart +
                      "Arrived at X = " + str(self.dx) +
                      " Y = " + str(self.dy))
        
      self.arrive()

      if self.disposition == 6 and self.arcs > 0:
        self.destination.colonize(self)
      # handle trade disposition
      if self.disposition == 8 and self.destination and self.trade_manifest:   
        self.dotrade(report)
    elif distancetodest != 0.0:
      report.append(replinestart + 
                    "enroute -- distance = " + 
                    str(distancetodest) + 
                    " speed = " + 
                    str(self.speed))
    if distancetodest < .05 and self.destination and self.destination.owner:
      # always do the following if nearby, not just when arriving
      if self.owner.get_profile().getpoliticalrelation(self.destination.owner.get_profile())=='enemy':
        if self.disposition in [0,1,2,3,5,7,9]:
          self.doassault(self.destination, report)
        else:
          self.gotoplanet(self.homeport)
          

    else:
      self.move()
      
class Message(models.Model):
  def __unicode__(self):
      return self.subject
  subject = models.CharField(max_length=80)
  message = models.TextField()
  fromplayer = models.ForeignKey(User, related_name='from_player')
  toplayer = models.ForeignKey(User, related_name='to_player')
  
class Sector(models.Model):
  def __unicode__(self):
      return str(self.key)
  key = models.IntegerField(primary_key=True)
  controllingplayer = models.ForeignKey(User, null=True)
  x = models.IntegerField()
  y = models.IntegerField()

class Planet(models.Model):
  def __unicode__(self):
      return self.name + "-" + str(self.id)
  name = models.CharField('Planet Name', max_length=50)
  owner = models.ForeignKey(User, null=True)
  sector = models.ForeignKey('Sector')
  x = models.FloatField()
  y = models.FloatField()
  r = models.FloatField()
  color = models.PositiveIntegerField()
  society = models.PositiveIntegerField()

  resources = models.ForeignKey('Manifest', null=True)
  tariffrate = models.FloatField('External Tariff Rate', default=0)
  inctaxrate = models.FloatField('Income Tax Rate', default=0)
  openshipyard = models.BooleanField('Allow Others to Build Ships', default=False)
  opencommodities = models.BooleanField('Allow Trading of Rare Commodities',default=False)
  opentrade = models.BooleanField('Allow Others to Trade Here',default=False)
  def colonize(self, fleet):
    if self.owner != None:
      # colonization doesn't happen if the planet is already colonized
      # (someone beat you to it, sorry...)
      fleet.gotoplanet(fleet.homeport)
      msg = Message(toplayer=fleet.owner, fromplayer=fleet.owner,
                    subject="Colonization Fleet " + str(fleet.id) + " Report",
                    message="We must sadly report that planet " + str(self.id) +
                    "(" + self.name + ") is already populated.\n\n We " +
                    "are currently " +
                    "returning to our home port, but could easily be diverted to a " +
                    "new destination on your orders.")
      msg.save()
    resources = Manifest()
    if self.resources == None:
      resources = Manifest()
    else:
      resources = Manifest()
    numarcs = fleet.arcs
    for commodity in shiptypes['arcs']['required']:
      setattr(resources,commodity,shiptypes['arcs']['required'][commodity]*numarcs)
    # some of the steel is wasted in the process
    # (stops people from colonizing, and then building
    # an arc and going to the next planet...)
    resources.steel = resources.steel-5
    self.owner = fleet.owner
    resources.save()
    self.resources = resources
    fleet.arcs = 0
    fleet.save()
    self.save()
  def buildableships(self):
    buildable = {}
    buildable['types'] = {}
    buildable['commodities'] = {}
    buildable['available'] = []
    # this is a big imperative mess, but it's somewhat readable
    # (woohoo!)
    for type in shiptypes:
      isbuildable = True
      # turn off fighters for now, too confusing...
      if type == 'fighters':
        isbuildable = False
      for needed in shiptypes[type]['required']:
        if shiptypes[type]['required'][needed] > getattr(self.resources,needed):
          isbuildable = False
          break 
      if isbuildable:
        for needed in shiptypes[type]['required']:
          if shiptypes[type]['required'][needed] != 0 and needed not in  buildable['commodities']:
            buildable['commodities'][needed] = getattr(self.resources,needed)
            #buildable['available'].append(getattr(self.resources,needed))
        buildable['types'][type] = {} 

    for type in buildable['types']:
      for i in buildable['commodities'].keys():
        buildable['types'][type][i]=shiptypes[type]['required'][i]
    return buildable
    

  def populate(self):
    # populate builds a new capital (i.e. a player's first
    # planet, the one he comes from...)
    if self.resources == None:
      resources = Manifest()
    else:
      resources = self.resources
    for resource in productionrates:
      setattr(resources,resource,productionrates[resource]['initial'])
    resources.save()

    self.society = 50
    self.inctaxrate = .07
    self.tariffrate = 0.0
    self.openshipyard = False
    self.opencommodities = False
    self.opentrade = False
    self.resources = resources
    self.save()
  def senserange(self):
    if not self.owner:
      return 0 
    range = .5 
    range += min(self.society*.01, 1.0)
    return range
  def getprice(self,commodity):
    basevalue = 1/(1-productionrates[commodity]['baserate'])
    if self.society*productionrates[commodity]['socmodifier'] != 0.0:
      cursocmodifier = 1/(self.society*productionrates[commodity]['socmodifier'])
    else:
      cursocmodifier = 0.0
    unitprice = (15000 + basevalue + cursocmodifier)/1000.0
    return int(round(10.0 * unitprice))

  def getprices(self):
    pricelist = {}
    if self.resources != None:
      resourcelist = self.resources.manifestlist(['id','quatloos'])
      for resource in resourcelist:
        pricelist[resource] = self.getprice(resource) 
    return pricelist 

  def getavailableprices(self):
    pricelist = {}
    if self.resources != None:
      resourcelist = self.resources.manifestlist(['id','quatloos'])
      for resource in resourcelist:
        if getattr(self.resources,resource)>0:
          pricelist[resource] = self.getprice(resource) 
    return pricelist

  def json(self,playersplanet=0):
    json = {}

    if self.owner:
      json['h'] = self.owner.get_profile().color
      if self.owner.get_profile().capital == self:
        json['cap'] = "1"
      json['s'] = self.senserange()
    else:
      json['h'] = 0
    
    json['x'] = self.x
    json['y'] = self.y
    json['c'] = "#" + hex(self.color)[2:]
    json['r'] = self.r
    json['i'] = self.id
    if playersplanet == 1:
      json['pp'] = 1
    return json


  def nextproduction(self,resource, population):
    produced = ((productionrates[resource]['baserate']+
                (productionrates[resource]['socmodifier']*self.society))*population)
    if resource in ['food']:
      aftertax = produced * (1-(self.inctaxrate/15.0))
    else:
      aftertax = produced
    return aftertax
  def resourcereport(self):
    report = []
    if self.resources:
      mlist = self.resources.manifestlist(['people','id','quatloos'])
      for resource in mlist:
        res = {}
        res['name'] = resource
        res['amount'] = mlist[resource]
        res['nextproduction'] = self.nextproduction(resource,self.resources.people)
        res['nextproduction'] = int(res['nextproduction'] -
                                    self.resources.people)
        if res['nextproduction'] < 0:
          res['negative'] = 1
        else:
          res['negative'] = 0
        report.append(res)
    return report    
  def doturn(self, report):
    replinestart = "Planet: " + str(self.name) + " (" + str(self.id) + ") "
    # only owned planets produce
    if self.owner != None and self.resources != None:
      curpopulation = self.resources.people
      popgrowth = productionrates['food']['socmodifier']*self.society
      if self.resources.food > 0 or popgrowth > 1.0:
        for resource in productionrates.keys():
          # 'baserate': 1.2, 'socmodifier'
          stats = productionrates[resource]
          oldval = getattr(self.resources, resource)
          aftertax = self.nextproduction(resource,curpopulation)
          newval = max([0,oldval+aftertax-curpopulation])
          setattr(self.resources, resource, newval)
      elif productionrates['food']['socmodifier']*self.society < 1.0:
        # uhoh, famine...
        report.append(replinestart + "Reports Famine!")
        self.population = int(curpopulation * .95)
      
      # increase the planet's treasury through taxation
      self.resources.quatloos += (self.resources.people * self.inctaxrate)/6.0
      
      # increase the society count if the player has played
      # in the last 2 days.
      
      if self.owner.get_profile().lastactivity >  datetime.datetime.today() - datetime.timedelta(hours=36):
        self.society += 1
      else:
        # limit population growth on absentee landlords... ;)
        if popgrowth > 1.0:
          self.resources.people = curpopulation * (popgrowth*.9)
      self.save()
      self.resources.save()
def nearbythings(thing,x,y):
  sx = int(x)/5
  sy = int(y)/5
  return thing.objects.filter(
    Q(sector=((sx-1)*1000)+sy-1)|
    Q(sector=((sx-1)*1000)+sy-1)|
    Q(sector=((sx-2)*1000)+sy)|
    Q(sector=((sx-1)*1000)+sy)|
    Q(sector=((sx-1)*1000)+sy+1)|
    Q(sector=(sx*1000)+sy-2)|
    Q(sector=(sx*1000)+sy-1)|
    Q(sector=(sx*1000)+sy)|
    Q(sector=(sx*1000)+sy+1)|
    Q(sector=(sx*1000)+sy+2)|
    Q(sector=((sx+1)*1000)+sy-1)|
    Q(sector=((sx+2)*1000)+sy)|
    Q(sector=((sx+1)*1000)+sy)|
    Q(sector=((sx+1)*1000)+sy+1))

class Announcement(models.Model):
  def __unicode__(self):
      return self.subject
  time = models.DateTimeField(auto_now_add=True)
  subject = models.CharField(max_length=50)
  message = models.TextField()

class Event(models.Model):
  def __unicode__(self):
      return self.event[:20]
  time = models.DateTimeField(auto_now_add=True)
  event = models.TextField()

def getdistanceobj(o1,o2):
  return getdistance(o1.x,o1.y,o2.x,o2.y)
def getdistance(x1,y1,x2,y2):
  return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

def nearbysortedthings(Thing,curthing):
  nearby = list(nearbythings(Thing,curthing.x,curthing.y))
  nearby.sort(lambda x,y:int((getdistanceobj(curthing,x) -
                              getdistanceobj(curthing,y))*100000 ))
  return nearby

def setextents(x,y,extents):
  x *= 5
  y *= 5
  if x < extents[0]:
    extents[0] = x
  if x > extents[2]:
    extents[2] = x
  if y < extents[1]:
    extents[1] = y
  if y > extents[3]:
    extents[3] = y
  return extents


def cullneighborhood(neighborhood):
  player = neighborhood['player']
  neighborhood['fbys'] = {}
  playersensers = []
  for planet in neighborhood['planets']:
    if planet.owner and planet.owner.id == player.id:
      playersensers.append({'x': planet.x, 'y': planet.y, 'r': planet.senserange()})

  for fleet in neighborhood['fleets']:
    if fleet.owner == player:
      playersensers.append({'x': fleet.x, 'y': fleet.y, 'r': fleet.senserange()})
    
  for f in neighborhood['fleets']:
    f.keep=0
    if f.owner == player:
      f.keep=1
      continue
    f.keep=0
    for s in playersensers:
      d = math.sqrt((s['x']-f.x)**2 + (s['y']-f.y)**2)
      if d < s['r']:
        f.keep=1
  
  for f in neighborhood['fleets']:
    if f.keep == 1:
      if f.sector.key not in neighborhood['fbys']:
        neighborhood['fbys'][f.sector.key] = []
      neighborhood['fbys'][f.sector.key].append(f)
  return neighborhood




def buildneighborhood(player):
  sectors = Sector.objects.filter(planet__owner=player)
  neighborhood = {}
  neighborhood['sectors'] = []
  neighborhood['fleets'] = []
  neighborhood['planets'] = []
  neighborhood['neighbors'] = []
  neighborhood['viewable'] = []
  neighborhood['player'] = player

  extents = [2001,2001,-1,-1]
  allsectors = []
  for sector in sectors:
    if sector.key not in allsectors:
      allsectors.append(sector.key)

    testsector = (sector.x-1)*1000 + sector.y
    if testsector not in allsectors:
      allsectors.append(testsector)

    testsector = (sector.x-1)*1000 + sector.y-1
    if testsector not in allsectors:
      allsectors.append(testsector)

    testsector = (sector.x-1)*1000 + sector.y+1
    if testsector not in allsectors:
      allsectors.append(testsector)

    testsector = (sector.x)*1000 + sector.y-1
    if testsector not in allsectors:
      allsectors.append(testsector)

    testsector = (sector.x)*1000 + sector.y+1
    if testsector not in allsectors:
      allsectors.append(testsector)

    testsector = (sector.x+1)*1000 + sector.y-1
    if testsector not in allsectors:
      allsectors.append(testsector)

    testsector = (sector.x+1)*1000 + sector.y
    if testsector not in allsectors:
      allsectors.append(testsector)
    
    testsector = (sector.x+1)*1000 + sector.y+1
    if testsector not in allsectors:
      allsectors.append(testsector)
  neighborhood['sectors'] = Sector.objects.filter(key__in=allsectors)

  for sector in neighborhood['sectors']:
    for fleet in sector.fleet_set.all():
      neighborhood['fleets'].append(fleet)  
    for planet in sector.planet_set.all():
      if planet.owner is not None:
        if planet.owner not in neighborhood['neighbors']:
          planet.owner.relation = player.get_profile().getpoliticalrelation(planet.owner.get_profile())
          neighborhood['neighbors'].append(planet.owner)
      neighborhood['planets'].append(planet)
    extents=setextents(sector.x,sector.y,extents)
  extent = 0
  if extents[2]-extents[0] > extents[3]-extents[1]:
    extent = extents[2]-extents[0]+5
  else:
    extent = extents[3]-extents[1]+5

  neighborhood['viewable'] = (extents[0],extents[1],extent,extent)

  return neighborhood 

def findbestdeal(curprices, destprices, quatloos):
  #print "---"
  #print str(curprices)
  #print str(destprices)
  #print "---"
  bestdif = -10000.0
  bestitem = "none"
  for item in destprices:
    if not curprices.has_key(item):
      continue
    elif curprices[item] > quatloos:
      continue
    #    10                  8
    else:
      curdif = float(destprices[item])/float(curprices[item])
      if curdif > bestdif:
        bestdif = curdif
        bestitem = item
  #print "bi=" + str(bestitem) + " bd=" + str(bestdif)
  return bestitem, bestdif
