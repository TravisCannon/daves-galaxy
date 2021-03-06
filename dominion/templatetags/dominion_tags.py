from django import template
from newdominion import settings
import hashlib


register = template.Library()
counter = 1 

class TestPoint(object):
  def __init__(self):
    self.x = 1.5
    self.y = 2.1


def incrementcounter():
  global counter
  counter = (counter%10000)+1
  return counter



@register.filter
def get_attr(obj, val):
  return getattr(obj, val)

@register.simple_tag
def protocolversion():
  return str(settings.PROTOCOL_VERSION)

@register.simple_tag
def cssversion():
  return str(settings.CSS_VERSION)

@register.simple_tag
def playerbadge(badge):
  global counter
  output = """
  <img class="noborder" title="%(title)s"
       id="%(id)s"       src="/site_media/badges/%(image)ssmall.png"/>
  <script>
  $('#%(id)s').bt('<img class="noborder" width="150" height="150" src="/site_media/badges/%(image)s.png"/>',
    {padding:10, width:150, margin:0, height:170, strokeWidth:2, strokeStyle: 'white',
     fill:'#224433',
     cornerRadius: 10, spikeGirth: 20});
  </script>
  """ % {'title' :str(badge)+' badge',
         'id'    :str(badge)+'-badge-'+str(counter),
         'image' :str(badge)}
  counter = (counter%10000)+1
  return output

@register.simple_tag
def playerinfobutton(player):
  """
  >>> hashlib.md5(playerinfobutton(1)).hexdigest()
  '3b457ee6004cb182e5cef4931b4b3d60'
  >>> hashlib.md5(playerinfobutton(1)).hexdigest()
  '4142ccc320f31cfc776707c06100b33e'
  """
  return infopopup('playerinfo', 'player info',
                    '/players/%s/info/'%player)

@register.simple_tag
def shipinfobutton(shiptype):
  """
  >>> hashlib.md5(playerinfobutton(1)).hexdigest()
  '3b457ee6004cb182e5cef4931b4b3d60'
  >>> hashlib.md5(playerinfobutton(1)).hexdigest()
  '4142ccc320f31cfc776707c06100b33e'
  """
  return infopopup('shiptypeinfo', 'ship info',
                    '/help/simple/%s/'%shiptype)


@register.simple_tag
def instrumentalityinfobutton(instrumentalitytype):
  """
  >>> hashlib.md5(playerinfobutton(1)).hexdigest()
  '3b457ee6004cb182e5cef4931b4b3d60'
  >>> hashlib.md5(playerinfobutton(1)).hexdigest()
  '4142ccc320f31cfc776707c06100b33e'
  """
  return infopopup('instrumentalityinfo', 'instrumentality info',
                    '/help/simple/%s/'%instrumentalitytype,400)


@register.simple_tag
def infopopup(objid,title,url,width=380):
  """
  >>> hashlib.md5(playerinfobutton(1)).hexdigest()
  '3b457ee6004cb182e5cef4931b4b3d60'
  >>> hashlib.md5(playerinfobutton(1)).hexdigest()
  '4142ccc320f31cfc776707c06100b33e'
  """
  global counter
  output = """
  <img class="noborder" title="%s"
                       id="%s%d"
                       src="/site_media/infobutton.png"/>
  <script>
    loadtooltip('#%s%d',
                '%s',
                %d,'click');
  </script>
  """ % (title,objid,counter,objid,counter,url,width)
  counter = (counter%10000)+1
  return output




@register.simple_tag
def planetinfobutton(planet):
  """
  >>> hashlib.md5(planetinfobutton(1)).hexdigest()
  '7c2af7a2269a9279bed2afd3db1d4317'
  >>> hashlib.md5(planetinfobutton(1)).hexdigest()
  '9e8da88e996315d973d9aeb06cead8ba'
  """
  global counter
  output = """
  <img class="noborder" title="planet info"
                       id="planetinfo%d"
                       src="/site_media/infobutton.png"/>
  <script>
    $('#planetinfo%d').click(
      function(event){
        handlebutton('planetmanagertab%d',
                     'planetmanager%d',
                     'planetinfotab%d',
                     'ManagePlanet',
                     '/planets/%d/manager/0/',
                     '/planets/%d/info/');
      });
  </script>
  """ % (counter,counter,planet,planet,planet,planet,planet)
  counter = (counter%10000)+1
  return output




@register.simple_tag
def planetmanagebutton(planet):
  """
  >>> hashlib.md5(planetmanagebutton(1)).hexdigest()
  '2d4c0ee7bee16d2ad1e7b7046778dffd'
  >>> hashlib.md5(planetmanagebutton(1)).hexdigest()
  '024cc2910f2100e7da98f9902fe6edc3'
  """
  global counter
  output = """
  <img class="infobutton" title="Manage" 
                 id="planetmanage%d"
                 src="/site_media/manage.png"/>
  <script>
    $('#planetmanage%d').click(
      function(event){
        handlebutton('planetmanagertab%d',
                     'planetmanager%d',
                     'planetmanagetab%d',
                     'ManagePlanet',
                     '/planets/%d/manager/1/',
                     '/planets/%d/manage/');
      });
  </script>
  """ % (counter,counter,planet,planet,planet,planet,planet)
  counter = (counter%10000)+1
  return output



@register.simple_tag
def planetupgradebutton(planet):
  """
  >>> hashlib.md5(planetupgradebutton(1)).hexdigest()
  '20dda3a904bbff80799a82e485d65ffb'
  >>> hashlib.md5(planetupgradebutton(1)).hexdigest()
  '4f0e536be2d9f14d543cf053605407a5'
  """
  global counter
  output = """
  <img class="infobutton" title="Upgrade" 
                 id="planetupgrade%d"
                 src="/site_media/upgradebutton.png"/>
  <script>
    $('#planetupgrade%d').click(
      function(event){
        handlebutton('planetmanagertab%d',
                     'planetmanager%d',
                     'planetupgradestab%d',
                     'ManagePlanet',
                     '/planets/%d/manager/3/',
                     '/planets/%d/upgradelist/');
      });
  </script>
  """ % (counter,counter,planet,planet,planet,planet,planet)
  counter = (counter%10000)+1
  return output



@register.simple_tag
def buildfleetbutton(planet):
  """
  >>> hashlib.md5(buildfleetbutton(1)).hexdigest()
  '324f0b3532f6f851226b11a74876833b'
  >>> hashlib.md5(buildfleetbutton(1)).hexdigest()
  'ac16dd18c3e7f93f814d7e90a11807bb'
  """
  global counter
  if planet.canbuildships:
    output = """
    <img class="infobutton" title="Construct Fleet" 
           id="planetbuildfleet%d"
           src="/site_media/construct.png"/>
    <script>
      $('#planetbuildfleet%d').click(
        function(event){
          if(!transienttabs.alreadyopen('buildfleet%d')){
            transienttabs.pushtab('buildfleet%d','Build Fleet','',false);
            transienttabs.gettaburl('buildfleet%d',
                                    '/planets/%d/buildfleet/');
            transienttabs.displaytab('buildfleet%d');
          } else {
            transienttabs.removetab('buildfleet%d');
          }
        });
    </script>
    """ % (counter,counter,planet.id,planet.id,planet.id,planet.id,planet.id,planet.id)
  else:
    output = ""
  counter = (counter%10000)+1
  return output



@register.simple_tag
def fleetinfobutton(fleet):
  """
  >>> hashlib.md5(fleetinfobutton(1)).hexdigest()
  '7c2af7a2269a9279bed2afd3db1d4317'
  >>> hashlib.md5(fleetinfobutton(1)).hexdigest()
  '9e8da88e996315d973d9aeb06cead8ba'
  """
  return infopopup('fleetinfo', 'fleet info',
                    '/fleets/%d/info/'%fleet)



@register.simple_tag
def fleetdestinationbutton(fleet):
  """
  >>> hashlib.md5(fleetdestinationbutton(1)).hexdigest()
  '7c2af7a2269a9279bed2afd3db1d4317'
  >>> hashlib.md5(fleetdestinationbutton(1)).hexdigest()
  '9e8da88e996315d973d9aeb06cead8ba'
  """
  global counter
  output = """
  <img class="noborder" title="set destination" 
                 src="/site_media/goto.png"
                 onmouseup="buildanother=0;
                            routebuilder.startdirectto({'i':'%d',
                                                        'x':%f,
                                                        'y':%f});"/>
  """ % (fleet.id,fleet.x,fleet.y)
  return output



@register.simple_tag
def fleetscrapbutton(fleet, listtype = 'all', page='1'):
  """
  >>> hashlib.md5(fleetdestinationbutton(1)).hexdigest()
  '7c2af7a2269a9279bed2afd3db1d4317'
  >>> hashlib.md5(fleetdestinationbutton(1)).hexdigest()
  '9e8da88e996315d973d9aeb06cead8ba'
  """
  if fleet.inport():
    output = """
    <img title="scrap fleet" 
         onclick="loadtab('#%sfleetstab',
                          '/fleets/list/%s/%d/',
                          '#fleetview',
                          {'scrapfleet':%d});"
         class="noborder" src="/site_media/scrap.png"/>

    """ % (listtype,listtype,page,fleet.id)
  else:
    output = ""
  return output



@register.simple_tag
def ajaxformbutton(url, text, key, value):
  """
  >>> a = TestPoint()
  >>> hashlib.md5(gotobutton(a)).hexdigest()
  '0e7daee6644f42d2d3730daca55acac9'
  """
  output = """

<input 
  onclick="sendrequest(handleserverresponse,
                       '%s',
                       'POST',
                       {'%s':%s});"
  type="button" 
  value="%s"/>
  """ % (url,key,value,text)
  return output

@register.simple_tag
def playerpicture(player, width, height, background="none"):
  rectid = incrementcounter()
  lineargradient1 = incrementcounter()            #3163
  lineargradient2 = incrementcounter()            #3175
  lineargradient3 = incrementcounter()            #3157
  radialgradient1 = incrementcounter()            #3181

  backgrounds = {'none': '',
                 'normal': """
      <g
         id="layer1">
        <rect
           width="120"
           height="170"
           x="0"
           y="0"
           id="rect%d"
           style="opacity:1;
                  fill:url(#linearGradient%d);
                  fill-opacity:1;stroke:#000000;
                  stroke-width:3;stroke-linecap:butt;
                  stroke-linejoin:miter;
                  stroke-miterlimit:4;
                  stroke-dasharray:none;
                  stroke-opacity:1" />
        <path
           d="M 5,165 L 20,140 L 100,140 L 115,165 L 5,165 z"
           id="path3165"
           style="fill:url(#radialGradient%d);
                  fill-opacity:1;
                  fill-rule:evenodd;
                  stroke:#000000;
                  stroke-width:1px;
                  stroke-linecap:butt;
                  stroke-linejoin:miter;
                  stroke-opacity:1" />
      </g>
      """ %(rectid,lineargradient1,radialgradient1)}
  output = """
    <svg
       xmlns:svg="http://www.w3.org/2000/svg"
       xmlns="http://www.w3.org/2000/svg"
       xmlns:xlink="http://www.w3.org/1999/xlink"
       version="1.0"
       viewBox="0 0 120 170"
       width="%d"
       height="%d"
       id="svg2">
      <defs>
        <linearGradient
           id="linearGradient%d">
          <stop
             style="stop-color:#000000;stop-opacity:1"
             offset="0" />
          <stop
             style="stop-color:#323232;stop-opacity:0.98275864"
             offset="1" />
        </linearGradient>
        <linearGradient
           id="linearGradient%d">
          <stop
             style="stop-color:#000000;stop-opacity:1"
             offset="0" />
          <stop
             style="stop-color:#808041;stop-opacity:1"
             offset="1" />
        </linearGradient>
        <linearGradient
           x1="55"
           y1="-20"
           x2="55"
           y2="170"
           id="linearGradient%d"
           xlink:href="#linearGradient%d"
           gradientUnits="userSpaceOnUse" />
        <radialGradient
           cx="34.583031"
           cy="172.07823"
           r="55.5"
           fx="34.583031"
           fy="172.07823"
           id="radialGradient%d"
           xlink:href="#linearGradient%d"
           gradientUnits="userSpaceOnUse"
           gradientTransform="matrix(1.9641997,-1.0614772,0.6414687,1.1870022,-138.20927,-15.073515)" />
      </defs>
      %s
      %s
    </svg>
  """ % (width, height, 
         lineargradient2, lineargradient3, lineargradient1, lineargradient3, radialgradient1, lineargradient2, 
         backgrounds[background], player.player.appearance)
  return output

@register.simple_tag
def gotodestinationbutton(x,y):
  """
  >>> a = TestPoint()
  >>> hashlib.md5(gotobutton(a)).hexdigest()
  '0e7daee6644f42d2d3730daca55acac9'
  """
  output = """
  <img src="/site_media/center.png" 
                       class="noborder"
                       onclick="gm.centermap(%f,%f);"
                       title="center on location"/>
  """ % (x,y)
  return output

@register.simple_tag
def gotobutton(location, type):
  """
  >>> a = TestPoint()
  >>> hashlib.md5(gotobutton(a)).hexdigest()
  '0e7daee6644f42d2d3730daca55acac9'
  """
  output = """
  <img src="/site_media/center.png" 
                       class="noborder"
                       onclick="gm.centermap(%f,%f);"
                       title="center on %s"/>
  """ % (location.x, location.y, type)
  return output

@register.simple_tag
def transferbutton(player, neighbor):
  """
  >>> a = TestPoint()
  >>> hashlib.md5(gotobutton(a)).hexdigest()
  '0e7daee6644f42d2d3730daca55acac9'
  """
  output = """
  <img src="/site_media/money.png" 
                       class="noborder"
                       onclick="stringprompt({'title': 'Transer Money', 
                                             'headline': 'How Much?',
                                             'subhead': %(maxtransfer)d + ' Quatloos Available',
                                             'numeric': true,
                                             'min': 0,
                                             'max': %(maxtransfer)d,
                                             'maxlen': 20,
                                             'text': '0',
                                             'submitfunction': function (stuff, string){
                                               sendrequest(handleserverresponse,
                                                           '/transferto/',
                                                           'POST', 
                                                           {'otherplayer': %(neighborid)d,
                                                            'transfertype': 'currency',
                                                            'transferamount': string})
                                             },
                                             'cancelfunction': function(){},
                                             'submit': 'Transfer Money',
                                             'cancel': 'Cancel'});"
                       title="transfer money"/>
  """ % {'neighborid':neighbor.user.id, 'maxtransfer':player.capital.resources.quatloos}
  return output

if __name__ == '__main__':
  import doctest
  doctest.testmod()
