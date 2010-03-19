from newdominion.dominion.models import *
import datetime



disownplanets = Planet.objects.filter(owner__player__lastactivity__lt = 
                                      (datetime.datetime.today()-datetime.timedelta(days=30)))


for p in disownplanets:
  print p.name + " -- " + str(p.society) + " -- " + p.owner.username
  

deleteusers = User.objects.filter(player__lastactivity__lt = (datetime.datetime.today()-datetime.timedelta(days=30)))

print str(deleteusers)


