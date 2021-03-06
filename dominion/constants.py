
SVG_SCHEMA = "http://www.w3.org/Graphics/SVG/1.2/rng/"

DISPOSITIONS = (
    (0, 'Garrison'),
    (1, 'Planetary Defense'), # used
    (2, 'Scout'),     # used
    (3, 'Screen'),    # used
    (4, 'Diplomacy'),
    (5, 'Attack'),    # used
    (6, 'Colonize'),  # used
    (7, 'Patrol'),    # used  
    (8, 'Trade'),     # used
    (9, 'Piracy'),    # used
    (10, 'Planetary Assault'),
    (11, 'Helium Harvesting'),
    (12, 'Long Haul Trade')
    )
TRADE_DISPOSITIONS = [8,12]
TRADE_SHIPTYPES = ['merchantmen','bulkfreighters','longhaulmerchants']

PAID_TYPES = (
    (0, '3 Months Basic Membership'),
    (1, '6 Months Basic Membership + Tshirt'),
    (2, '6 Months + UFE + Tshirt'),
    (3, 'Lifetime + UFE + Tshirt'),
    )
TWENTYMIL = 20000000
instrumentalitytypes = [
  {'name': 'Long Range Sensors 1',
   'shortid': 'lrs1',
   'type': 0,
   'description': "Increases the radius over which this planet's sensors " +
                  "can see by .5 G.U.'s.  Does not increase sensor ranges " +
                  "for fleets.",
   'requires': -1,
   'minsociety': 10,
   'upkeep': .01,
   'minupkeep': 500,
   'minenergy': 50,
   'energypercapita': 0,
   'maxpercapita': 0,
   'priority': 5,
   'required':   {'people': 1000, 'food': 1000, 'steel': 150, 
                 'antimatter': 5, 'quatloos': 400, 'hydrocarbon': 500,
                 'unobtanium':0, 'krellmetal':0}},

  {'name': 'Long Range Sensors 2',
   'shortid': 'lrs2',
   'type': 1,
   'description': "Increases the radius over which this planet's sensors " +
                  " can see by another .5 G.U.'s beyond the added range " +
                  "given by Long Range Sensors 1.",
   'requires': 0,
   'minsociety': 20,
   'upkeep': .02,
   'minupkeep': 1000,
   'minenergy': 100,
   'energypercapita': 0,
   'maxpercapita': 0,
   'priority': 4,
   'required':   {'people': 1000, 'food': 1000, 'steel': 300, 
                 'antimatter': 10, 'quatloos': 600, 'hydrocarbon': 1000,
                 'unobtanium':0, 'krellmetal':0}},

  {'name': 'Trade Incentives',
   'shortid': 'tradeincentives',
   'type': 2,
   'description': "Promotes trade by reducing the price of " +
                  "commodities that are in surplus, and raising the prices of " +
                  "commodities that are needed.  The Government subsidizes the difference " +
                  "in prices through its treasury.",
   'requires': -1,
   'minsociety': 1,
   'upkeep': .01,
   'minupkeep': 0,
   'minenergy': 0,
   'energypercapita': 0,
   'maxpercapita': 0,
   'priority': 10,
   'required':   {'people': 100, 'food': 100, 'steel': 10, 
                 'antimatter': 0, 'quatloos': 100,
                 'unobtanium':0, 'krellmetal':0}},

  {'name': 'Regional Government',
   'shortid': 'rglgvt',
   'type': 3,
   'description': "Allows this planet to collect taxes from it's neighbors.  This tax is " +
                  "fixed at 5%, and please note that if you set all your planets as " +
                  "regional goverments, you're just moving a lot of money around with no " +
                  "advantage.",
   'requires': -1,
   'minsociety': 30,
   'upkeep': .02,
   'minupkeep': 2000,
   'minenergy': 10,
   'energypercapita': 0,
   'maxpercapita': 0,
   'priority': 3,
   'required':   {'people': 5000, 'food': 5000, 'steel': 500, 
                 'antimatter': 200, 'quatloos': 10000, 'hydrocarbon': 1000,
                 'unobtanium':0, 'krellmetal':0}},

  {'name': 'Mind Control',
   'shortid': 'mindcontrol',
   'type': 4,
   'description': "Every inhabitant of this planet is issued an antenna " +
                  "beanie that turns them into a mindless automaton.  The " + 
                  "consequences of this enbeaniement are that the level of " +
                  "society on the planet does not change.  Naturally this " +
                  "technology is not looked upon favorably by the international " +
                  "community.  Also, certain elements in society resist the wearing " +
                  "of their handsome new headgear, and will have to be...eliminated.",
   'requires': -1,
   'minsociety': 40,
   'upkeep': .2,
   'minupkeep': 50000,
   'minenergy': 200,
   'energypercapita': 500/TWENTYMIL,
   'maxpercapita': 0,
   'priority': 15,
   'required':   {'people': 20000, 'food': 500, 'steel': 2000, 
                 'antimatter': 10, 'quatloos': 5000,
                 'unobtanium':0, 'krellmetal':0}},

  {'name': 'Matter Synth 1',
   'shortid': 'mattersynth1',
   'type': 5,
   'description': "A matter synthesizer allows you to produce the artificial " +
                  "element *Krellenium*, (Krell Metal), which is used in building " +
                  "military ships beyond the most basic types.  If you wish to build " +
                  "these kinds of ships on this planet you will also need to build a " +
                  "military base.",
   'requires': -1,
   'minsociety': 35,
   'upkeep': .025,
   'minupkeep': 3000,
   'minenergy': 100,
   'energypercapita': 0,
   'maxpercapita': 0,
   'priority': 3,
   'required':   {'people': 5000, 'food': 5000, 'steel': 1000, 
                 'antimatter': 500, 'quatloos': 10000,
                 'unobtanium':0, 'krellmetal':0}},

  {'name': 'Matter Synth 2',
   'shortid': 'mattersynth2',
   'type': 6,
   'description': "Adds an Unobtanium extractor to the matter synthesizer " +
                  "already located on this planet.  Unobtanium is used in " + 
                  "the production of larger military ships.",
   'requires': 5,
   'minsociety': 45,
   'upkeep': .1,
   'minupkeep': 5000,
   'minenergy': 150,
   'energypercapita': 0,
   'maxpercapita': 0,
   'priority': 3,
   'required':   {'people': 5000, 'food': 5000, 'steel': 2000, 
                 'antimatter': 1000, 'quatloos': 20000,
                 'unobtanium':0, 'krellmetal':0}},

  {'name': 'Military Base',
   'shortid': 'militarybase',
   'type': 7,
   'description': "A military base, along with a matter synthesizer, allows you " +
                  "to build larger warships on this planet.",
   'requires': 5,
   'minsociety': 40,
   'upkeep': .15,
   'minupkeep': 25000,
   'minenergy': 100,
   'maxpercapita': 0,
   'energypercapita': 0,
   'priority': 2,
   'required':   {'people': 2000, 'food': 2000, 'steel': 1000, 
                 'antimatter': 100, 'quatloos': 10000,
                 'unobtanium':0, 'krellmetal':0}},

  {'name': 'Slingshot',
   'shortid': 'slingshot',
   'type': 8,
   'description': "A slingshot gives a speed boost to any fleet leaving this planet. ",
                  
   'requires': -1,
   'minsociety': 25,
   'upkeep': .1,
   'minupkeep': 10000,
   'minenergy': 150,
   'maxpercapita': 0,
   'energypercapita': 0,
   'priority': 8,
   'required':   {'people': 100, 'food': 100, 'steel': 500, 
                 'antimatter': 10, 'quatloos': 1000,
                 'unobtanium':0, 'krellmetal':0}},
                 
  {'name': 'Farm Subsidies',
   'shortid': 'farmsubsidies',
   'type': 9,
   'description': "Farm subsidies promote the growing of crops over the production of other "+
                  "commodities.  80% of resources that would normally go towards the production "+
                  "of other commodities, go towards farming instead.  Younger citizens tend to "+
                  "move away from farming colonies because of lack of opportunities.",
                  
   'requires': -1,
   'minsociety': 1,
   'upkeep': .4,
   'minupkeep': 15000,
   'minenergy': 0,
   'maxpercapita': 0,
   'energypercapita': 200/TWENTYMIL,
   'priority': 20,
   'required':   {'people': 100, 'food': 0, 'steel': 500, 
                 'antimatter': 0, 'quatloos': 1000,
                 'unobtanium':0, 'krellmetal':0}},
  
  {'name': 'Drilling Subsidies',
   'shortid': 'drillingsubsidies',
   'type': 10,
   'description': "Drilling subsidies promote the drilling of oil wells over the production of other "+
                  "commodities.  80% of resources that would normally go towards the production "+
                  "of other commodities, go towards drilling instead.  Drilling degrades the" +
                  "environment, and retards population growth.",
                  
   'requires': -1,
   'minsociety': 1,
   'upkeep': .4,
   'minupkeep': 30000,
   'minenergy': 0,
   'maxpercapita': 0,
   'energypercapita': 200/TWENTYMIL,
   'priority': 20,
   'required':   {'people': 100, 'food': 100, 'steel': 500, 
                 'antimatter': 0, 'quatloos': 1000,
                 'unobtanium':0, 'krellmetal':0}},
  
  {'name': 'Planetary Defense 1',
   'shortid': 'planetarydefense1',
   'type': 11,
   'description': "A planet based area defense weapon.  Very expensive, but able to defend "+
                  "a quite large area.  Can accept targeting information from any fleet or " +
                  "planet in it's area of effectiveness.  Does more damage the closer the " +
                  "enemy fleet gets to it.",
                  
   'requires': 5,
   'minsociety': 50,
   'upkeep': .3,
   'minupkeep': 20000,
   'minenergy': 300,
   'maxpercapita': 0,
   'energypercapita': 0,
   'priority': 1,
   'required':   {'people': 50000, 'food': 50000, 'steel': 5000, 
                 'antimatter': 100, 'quatloos': 100000,
                 'unobtanium':0, 'krellmetal':20}},
                 
  {'name': 'Petrochemical Power Plant',
   'shortid': 'powerplant1',
   'type': 12,
   'description': "A power plant that converts hydrocarbon (oil, coal, "+
                  "natural gas...) into electrical energy.  Produces a maximum of 200-700 "+
                  "Gigawatts of power, with the  commensurate amount of polution.  "+
                  "produces 1 gigawatt per unit of hydrocarbon consumed.",
                  
   'requires': -1,
   'minsociety': 20,
   'upkeep': .1,
   'minupkeep': 5000,
   'minenergy': -200,
   'fuel': 'hydrocarbon',
   'fuelconversion': .2, 
   'energypercapita': -500/TWENTYMIL,
   'maxpercapita': -500,
   'priority': 2,
   'required':   {'people': 3000, 'food': 3000, 'steel': 5000, 
                 'antimatter': 100, 'quatloos': 5000,
                 'unobtanium':0, 'krellmetal':20}},
  
  {'name': 'Fusion Power Plant',
   'shortid': 'powerplant2',
   'type': 13,
   'description': "A power plant that converts helium 3 "+
                  "into electrical energy.  Produces 600-1000 "+
                  "Gigawatts of power.  Produces 1 gigawatt of power "+
                  "for every 4 units of helium 3 consumed.",
                  
   'requires': -1,
   'minsociety': 30,
   'upkeep': .1,
   'minupkeep': 5000,
   'minenergy': -600,
   'fuel': 'helium3',
   'fuelconversion': .25,
   'priority': 2,
   'energypercapita': -400/TWENTYMIL,
   'maxpercapita': -400,
   'required':   {'people': 8000, 'food': 8000, 'steel': 5000, 
                 'antimatter': 100, 'quatloos': 8000,
                 'unobtanium':0, 'krellmetal':20}},
  
  {'name': 'Antimatter Power Plant',
   'shortid': 'powerplant3',
   'type': 14,
   'description': "A power plant that converts antimatter "+
                  "into electrical energy.  Produces 200-700 "+
                  "Gigawatts of power, but causes huge amounts of "+
                  "devastation if damaged.  It produces 1 megawatt "+
                  "of energy per unit of antimatter consumed.",
                  
   'requires': -1,
   'minsociety': 45,
   'upkeep': .1,
   'minupkeep': 5000,
   'minenergy': -200,
   'fuel': 'antimatter',
   'fuelconversion': 1,
   'energypercapita': -500/TWENTYMIL,
   'maxpercapita': -500,
   'priority': 2,
   'required':   {'people': 30000, 'food': 30000, 'steel': 5000, 
                 'antimatter': 100, 'quatloos': 20000,
                 'unobtanium':0, 'krellmetal':20}},


]



shiptypes = {
  'scouts':           {'singular': 'scout', 'plural': 'scouts', 
                       'nice': 'Scouts', 'rank': 11,
                       'accel': .4, 'att': 2, 'def': 0,'requiresbase':False, 
                       'sense': .5, 'effrange': .5, 'capitalship': False,
                       'passengers': 0, 'numholds': 0,
                       'upkeep':
                         {'food': 1, 'quatloos': 20},
                       'required':
                         {'people': 5, 'food': 5, 'steel': 250, 
                         'antimatter': 25, 'quatloos': 250,
                         'unobtanium':0, 'krellmetal':0}
                      },
  'blackbirds':       {'singular': 'blackbird', 'plural': 'blackbirds', 
                       'nice': 'Blackbirds', 'rank': 10,
                       'accel': .8, 'att': 0, 'def': 10,'requiresbase':False, 
                       'sense': 1.0, 'effrange': .5, 'capitalship': False,
                       'passengers': 0, 'numholds': 0,
                       'upkeep':
                         {'food': 1, 'quatloos': 400},
                       'required':
                         {'people': 5, 'food': 5, 'steel': 500, 
                         'antimatter': 125, 'quatloos': 10000,
                         'unobtanium':25, 'krellmetal':50}
                      },
  'arcs':             {'singular': 'arc', 'plural': 'arcs', 
                       'nice': 'Arcs', 'rank': 12,
                       'accel': .25, 'att': 0, 'def': 1, 'requiresbase':False,
                       'sense': .2, 'effrange': .25, 'capitalship': False,
                       'passengers': 0, 'numholds': 0,
                       'upkeep':
                         {'food': 1, 'quatloos': 30},
                       'required':
                         {'people': 2000, 'food': 1000, 'steel': 10000, 
                         'antimatter': 500, 'quatloos': 10000,
                         'unobtanium':0, 'krellmetal':0}
                      },

  'merchantmen':      {'singular': 'merchantman', 'plural': 'merchantmen', 
                       'nice': 'Merchantmen', 'rank': 9,
                       'accel': .28, 'att': 0, 'def': 1, 'requiresbase':False,
                       'sense': .2, 'effrange': .25, 'capitalship': False,
                       'passengers': 1000, 'numholds': 500,
                       'upkeep':
                         {'food': 4, 'quatloos': -20},
                       'required':
                         {'people': 20, 'food': 20, 'steel': 750, 
                         'antimatter': 50, 'quatloos': 6000,
                         'unobtanium':0, 'krellmetal':0}
                      },
  
  'longhaulmerchants': {'singular': 'long haul freighter', 'plural': 'long haul freighters', 
                         'nice': 'Long Haul Freighters', 'rank': 9,
                         'accel': .35, 'att': 0, 'def': 1, 'requiresbase':False,
                         'sense': .2, 'effrange': .25, 'capitalship': False,
                         'passengers': 1000, 'numholds': 300,
                         'upkeep':
                           {'food': 4, 'quatloos': -20},
                         'required':
                           {'people': 15, 'food': 15, 'steel': 350, 
                           'antimatter': 80, 'quatloos': 6000,
                           'unobtanium':0, 'krellmetal':5}
                      },

  'bulkfreighters':   {'singular': 'bulkfreighter', 'plural': 'bulkfreighters', 
                       'nice': 'Bulk Freighters', 'rank': 8,
                       'accel': .25, 'att': 0, 'def': 1, 'requiresbase':False,
                       'sense': .2, 'effrange': .25, 'capitalship': False,
                       'passengers': 2000, 'numholds': 1000,
                       'upkeep':
                         {'food': 4, 'quatloos': -30},
                       'required':
                         {'people': 20, 'food': 20, 'steel': 2500, 
                         'antimatter': 50, 'quatloos': 6500,
                         'unobtanium':0, 'krellmetal':0}
                      },
  'harvesters':   {'singular': 'harvester', 'plural': 'harvesters', 
                       'nice': 'Helium Harvesters', 'rank': 12,
                       'accel': .25, 'att': 0, 'def': 1, 'requiresbase':False,
                       'sense': .2, 'effrange': .25, 'capitalship': False,
                       'passengers': 0, 'numholds': 0,
                       'upkeep':
                         {'food': 4, 'quatloos': -30},
                       'required':
                         {'people': 25, 'food': 20, 'steel': 5000, 
                         'antimatter': 50, 'quatloos': 6500,
                         'unobtanium':0, 'krellmetal':0}
                      },
  'fighters':         {'singular': 'fighter', 'plural': 'fighters', 
                       'nice': 'Fighters', 'rank': 7,
                       'accel': 0.0, 'numholds': 0,
                       'att': 5, 'def': 1, 'requiresbase':True,
                       'sense': 1.0, 'effrange': 2.0, 'capitalship': False,
                       'passengers': 0,
                       'upkeep':
                         {'quatloos': 2},
                       'required':
                         {'people': 0, 'food': 0, 'steel': 25, 
                         'antimatter': 0, 'quatloos': 250,
                         'unobtanium':0, 'krellmetal':0}
                      },
  'subspacers':       {'singular': 'subspacer', 'plural': 'subspacers', 
                       'nice': 'Sub Spacers', 'rank': 6,
                       'accel': .3, 'att': 8, 'def': 2, 'requiresbase':False,
                       'sense': .8, 'effrange': 1.0, 'capitalship': False,
                       'passengers': 0, 'numholds': 0,
                       'upkeep':
                         {'food': 1, 'quatloos': 60},
                       'required':
                         {'people': 50, 'food': 50, 'steel': 625, 
                         'antimatter': 250, 'quatloos': 12500,
                         'unobtanium':0, 'krellmetal':16}
                      },
  'frigates':         {'singular': 'frigate', 'plural': 'frigates', 
                       'nice': 'Frigates', 'rank': 5,
                       'accel': .35, 'att': 6, 'def': 2, 'requiresbase':False,
                       'sense': .4, 'effrange': 1.0, 'capitalship': False,
                       'passengers': 0, 'numholds': 0,
                       'upkeep':
                         {'food': 10, 'quatloos': 40},
                       'required':
                         {'people': 50, 'food': 50, 'steel': 950, 
                         'antimatter': 200, 'quatloos': 1250,
                         'unobtanium':0, 'krellmetal':0}
                      },
  'destroyers':       {'singular': 'destroyer', 'plural': 'destroyer', 
                       'nice': 'Destroyers', 'rank': 4,
                       'accel':.32, 'att': 9, 'def': 3, 'requiresbase':False,
                       'sense': .5, 'effrange': 1.2, 'capitalship': False,
                       'passengers': 0, 'numholds': 0,
                       'upkeep':
                         {'food': 12, 'quatloos': 50},
                       'required':
                         {
                         'people': 60, 'food': 70, 'steel': 1200, 
                         'antimatter': 276, 'quatloos': 5020,
                         'unobtanium':0, 'krellmetal':0}
                      },
  'cruisers':         {'singular': 'cruiser', 'plural': 'cruisers', 
                       'nice': 'Cruisers', 'rank': 3,
                       'accel': .5, 'att': 14, 'def': 4, 'requiresbase':True,
                       'sense': .7, 'effrange': 1.8, 'capitalship': True,
                       'passengers': 0, 'numholds': 0,
                       'upkeep':
                         {'food': 16, 'quatloos': 60},
                       'required':
                         {
                         'people': 80, 'food': 100, 'steel': 1625, 
                         'antimatter': 385, 'quatloos': 15000,
                         'unobtanium':0, 'krellmetal':67}
                      },
  'battleships':      {'singular': 'battleship', 'plural': 'battleships', 
                       'nice': 'Battleships', 'rank': 2,
                       'accel': .25, 'att': 20, 'def': 9, 'requiresbase':True,
                       'sense': .7, 'effrange': 2.0, 'capitalship': True,
                       'passengers': 0, 'numholds': 0,
                       'upkeep':
                         {'food': 21, 'quatloos': 80},
                       'required':
                         {
                         'people': 110, 'food': 200, 'steel': 4000, 
                         'antimatter': 655, 'quatloos': 25000,
                         'unobtanium':20, 'krellmetal':155}
                      },
  'superbattleships': {'singular': 'super battleship', 'plural': 'super battleships', 
                       'nice': 'Super Battleships', 'rank': 1,
                       'accel': .24, 'att': 27, 'def': 14, 'requiresbase':True,
                       'sense': 1.0, 'effrange': 2.0, 'capitalship': True,
                       'passengers': 0, 'numholds': 0,
                       'upkeep':
                         {'food': 30, 'quatloos': 100},
                       'required':
                         {
                         'people': 150, 'food': 300, 'steel': 8000, 
                         'antimatter': 1050, 'quatloos': 75000,
                         'unobtanium':102, 'krellmetal':290}
                      },
  # TODO: need to re-do required resources for carriers (when implemented...)
  'carriers':         {'singular': 'carrier', 'plural': 'carriers', 
                       'nice': 'Carriers', 'rank': 1,
                       'accel': .2, 'att': 0, 'def': 10, 'requiresbase':True,
                       'sense': 1.2, 'effrange': .5, 'capitalship': True,
                       'passengers': 0, 'numholds': 0,
                       'upkeep':
                         {'food': 100, 'quatloos': 200},
                       'required':
                         {
                         'people': 500, 'food': 500, 'steel': 1875, 
                         'antimatter': 2250, 'quatloos': 125000,
                         'unobtanium':187, 'krellmetal':312} 
                       }
  }

productionrates = {'people':        {'baseprice': 100, 'pricemod':.003, 'nice': 'People', 
                                     'baserate': 1.12, 'socmodifier': -0.00002, 'neededupgrade': -1,
                                     'initial': 8000000, 'maxsurplus': 20000000, 'distancemod':1.0},
                                     
                   'quatloos':      {'baseprice': 1, 'pricemod':1.0,  'nice': 'Quatloos',
                                     'baserate': 1.0, 'socmodifier': 0.0, 'neededupgrade': -1,
                                     'initial': 500000, 'maxsurplus': 100000000, 'distancemod':1.0},

                   'food':          {'baseprice': 10, 'pricemod':-.00002,  'nice': 'Food',
                                     'baserate': 1.09, 'socmodifier': -.00108, 'neededupgrade': -1,
                                     'initial': 250000, 'maxsurplus': 300000, 'distancemod':1.0},

                   'consumergoods': {'baseprice': 30, 'pricemod':.02,  'nice': 'Consumer Goods',
                                     'baserate': .9999, 'socmodifier': .0000045, 'neededupgrade': -1,
                                     'initial': 100000, 'maxsurplus': 250000, 'distancemod':1.5},

                   'steel':         {'baseprice': 100, 'pricemod':-.05,  'nice': 'Steel',
                                     'baserate': 1.0022, 'socmodifier': 0.0, 'neededupgrade': -1,
                                     'initial': 25000, 'maxsurplus': 1000000, 'distancemod':1.0},

                   'unobtanium':    {'baseprice': 20000, 'pricemod':10000.0, 'nice': 'Unobtanium',
                                     'baserate': .99999, 'socmodifier': .00000035, 
                                     'neededupgrade': 6, #Instrumentality.MATTERSYNTH2
                                     'initial': 100, 'maxsurplus': 40000, 'distancemod':1.0},

                   'krellmetal':    {'baseprice': 10000, 'pricemod':100.0,  'nice': 'Krell Metal',
                                     'baserate': .999995, 'socmodifier':.0000008, 
                                     'neededupgrade': 5, #Instrumentality.MATTERSYNTH1
                                     'initial': 500, 'maxsurplus': 70000, 'distancemod':1.0},

                   'antimatter':    {'baseprice': 5000, 'pricemod':4.0,  'nice': 'Antimatter',
                                     'baserate': .9999, 'socmodifier': .000008, 'neededupgrade': -1,
                                     'initial': 2500, 'maxsurplus': 500000, 'distancemod':1.0},

                   'hydrocarbon':   {'baseprice': 100, 'pricemod':-.009,  'nice': 'Hydrocarbon',
                                     'baserate': 1.013, 'socmodifier': -.00014, 'neededupgrade': -1,
                                     'initial': 50000, 'maxsurplus': 300000, 'distancemod':1.0},
                   #nebulae
                   'helium3':       {'baseprice': 12000, 'pricemod':1000,  'nice': 'Helium-3',
                                     'baserate': 1.0, 'socmodifier': 0.0, 'neededupgrade': -1,
                                     'initial': 0, 'maxsurplus': 0, 'distancemod':1.0},
                   # red giants
                   'strangeness':   {'baseprice': 100, 'pricemod':0.0,  'nice': 'Strangeness',
                                     'baserate': 1.0, 'socmodifier': 0.0, 'neededupgrade': -1,
                                     'initial': 0, 'maxsurplus': 0, 'distancemod':1.0},
                   # yellow stars                  
                   'charm':         {'baseprice': 100, 'pricemod':0.0,  'nice': 'Charm',
                                     'baserate': 1.0, 'socmodifier': 0.0, 'neededupgrade': -1,
                                     'initial': 0, 'maxsurplus': 0, 'distancemod':1.0}
                  }
distanceaffected = { 'food': 1, 'consumergoods':1 }

fleetdata = [
  'id',
  'owner_id',
  'sector_id',
  'name',
  'x',
  'y',
  'dx',
  'dy',
  'direction',
  'speed',
  'sensorrange',
  'shiplist',
  'homeport_id',
  'source_id',
  'destination_id',
  'route_id',
  'curleg',
  'society',
  'disposition',
  'flags']

fddict = {fleetdata[i]:i for i in xrange(len(fleetdata))}

planetdata = ['id',
              'owner_id',
              'sector_id',
              'name',
              'society',
              'sensorrange',
              'hexcolor',
              'r',
              'resourcelist',
              'inctaxrate',
              'tariffrate',
              'x',
              'y',
              'flags']

pddict = {planetdata[i]:i for i in xrange(len(planetdata))}




shiptypesordered = [
  'scouts',
  'blackbirds',
  'arcs',
  'merchantmen',
  'longhaulmerchants',
  'bulkfreighters',
  'harvesters',
  'fighters',
  'subspacers',
  'frigates',
  'destroyers',
  'cruisers',
  'battleships',
  'superbattleships',
  'carriers']

sddict = {shiptypesordered[i]:i for i in xrange(len(shiptypesordered))}

manifestdata = sorted(productionrates.keys())

mddict = {manifestdata[i]:i for i in xrange(len(manifestdata))}

pfdict = {
  'food_subsidy':          1,
  'famine':                2,
  'rgl_govt':              4,
  'matter_synth1':         8 ,
  'military_base':         16,
  'matter_synth2':         32,
  'open_trade':            64,
  'player_owned':          128,
  'planetary_defense':     256,
  'farm_subsidies':        512,
  'drilling_subsidies':    1024,
  'damaged':               2048,
  'can_build_ships':       4096,
  'in_nebulae':            8192}

ffdict = {
  'destroyed':    1,
  'damaged':      2,
  'scout':        4,
  'colonization': 8,
  'merchant':     16,
  'military':     32,
  'pirated':      64,
  'inport':       128
}



