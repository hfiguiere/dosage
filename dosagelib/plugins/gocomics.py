# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012 Bastian Kleineidam

from re import compile
from ..scraper import make_scraper
from ..util import tagre, asciify

def add(name, repl=''):
    baseUrl = 'http://www.gocomics.com/'
    comicname = asciify(name)
    shortname = name.lower().replace(' ', repl)
    classname = 'GoComics_%s' % comicname

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        prefix, year, month, day = pageUrl.split('/', 3)
        return "%s_%s%s%s.gif" % (shortname, year, month, day)

    globals()[classname] = make_scraper(classname,
        latestUrl=baseUrl + shortname,
        name='GoComics/' + comicname,
        stripUrl=baseUrl + shortname + '/%s',
        imageSearch=compile(tagre("img", "src", r'(http://assets\.amuniversal\.com/[0-9a-f]+)')),
        prevSearch=compile(tagre("a", "href", r'(/[^"]+/\d+/\d+/\d+)', after="prev")),
        help='Index format: yyyy/mm/dd',
        namer=namer,
    )


# http://www.gocomics.com/features
# note that comics from creators.com are not repeated here
add('2 Cows and a Chicken')
add('9 Chickweed Lane')
add('9 to 5')
add('The Academia Waltz')
add('Adam at Home')
add('Agnes')
add('Alley Oop', repl='-')
add('Andertoons')
add('Andy Capp')
add('Angry Little Girls', repl='-')
add('Animal Crackers')
add('Annie')
add('The Argyle Sweater')
add('Arlo and Janis')
add('Ask Shagg')
add('BC')
add('Back in the Day')
add('Bad Reporter')
add('Baldo')
add('Ballard Street')
add('Banana Triangle', repl='-')
add('Barkeater Lake')
add('The Barn')
add('Barney and Clyde')
add('Basic Instructions')
add('Beardo')
add('Ben')
add('Berger and Wyse', repl='-')
add('Betty')
add('Bewley')
add('Biff and Riley', repl='-')
add('Big Nate')
add('The Big Picture')
add('Big Top')
add('Biographic')
add('Birdbrains')
add('Bliss')
add('Bloom County')
add('Bo Nanas')
add('Bob the Squirrel')
add('Boomerangs')
add('The Boondocks')
add('The Born Loser')
add('Bottomliners')
add('Bound and Gagged')
add('Break of Day')
add('Brevity')
add('Brewster Rockit')
add('Broom Hilda')
add('The Buckets')
add('Buni')
add('Cafe con Leche')
add('Calvin and Hobbes')
add('Candorville')
add('Cathy')
add('Cest la Vie')
add('Cheap Thrills Cuisine', repl='-')
add('Chuckle Bros')
add('Citizen Dog')
add('The City')
add('Cleats')
add('Close to Home')
add('Committed')
add('Compu-toon')
add('Cornered')
add('Cow and Boy')
add('CowTown')
add('Crumb')
add('Cul de Sac')
add('Daddys Home')
add('Dark Side of the Horse')
add('Deep Cover')
add('Diamond Lil')
add('Dick Tracy')
add('The Dinette Set')
add('Dixie Drive', repl='-')
add('Dog Eat Doug')
add('Dogs of C Kennel')
add('Domestic Abuse')
add('Doonesbury')
add('The Doozies')
add('Drabble')
add('DudeDude')
add('The Duplex')
add('Eek')
add('The Elderberries')
add('Endtown')
add('Eric the Circle', repl='-')
add('F Minus')
add('Family Tree')
add('Farcus')
add('Fat Cats', repl='-')
add('Flo and Friends')
add('The Flying McCoys')
add('Foolish Mortals', repl='-')
add('For Better or For Worse')
add('For Heavens Sake')
add('Fort Knox')
add('FoxTrot')
add('FoxTrot Classics')
add('Frank and Ernest')
add('Frazz')
add('Fred Basset')
add('Free Range')
add('Freshly Squeezed')
add('Frog Applause')
add('The Fusco Brothers')
add('Garfield')
add('Garfield Minus Garfield')
add('Gasoline Alley')
add('Geech')
add('Get a Life')
add('Get Fuzzy')
add('Gil Thorp')
add('Ginger Meggs')
add('Gor Dominical')
add('Graffiti')
add('Grand Avenue')
add('Gray Matters')
add('The Grizzwells')
add('Haiku Ewe')
add('Ham Shears')
add('Health Capsules')
add('Heart of the City')
add('Heathcliff')
add('Heavenly Nostrils')
add('Herb and Jamaal')
add('Herman')
add('Home and Away')
add('HUBRIS!')
add('The Humble Stumble')
add('Imagine This')
add('In the Bleachers')
add('In the Sticks')
add('Incidental Comics')
add('Ink Pen')
add('Inspector Dangers Crime Quiz')
add('Its All About You')
add('Janes World')
add('Jims Journal')
add('Joe Vanilla')
add('Jump Start')
add('The K Chronicles')
add('KidCity')
add('KidSpot')
add('Kit N Carlyle')
add('Kitchen Capers')
add('Kliban')
add('Klibans Cats')
add('The Knight Life')
add('La Cucaracha')
add('Last Kiss')
add('The LeftyBosco Picture Show')
add('Legend of Bill')
add('Liberty Meadows')
add('Lil Abner')
add('Lio')
add('Little Dog Lost')
add('Lola')
add('Loose Parts')
add('The Lost Bear')
add('Lost Side of Suburbia')
add('Love Is...')
add('Luann')
add('Lucky Cow')
add('Mac')
add('Magic in a Minute')
add('Maintaining')
add('Marias Day')
add('Marmaduke')
add('McArroni')
add('The Meaning of Lila')
add('Medium Large')
add('Meg Classics')
add('The Middletons')
add('Mike du Jour')
add('Minimum Security')
add('Moderately Confused')
add('Molly and the Bear')
add('Momma')
add('Monty')
add('Motley Classics')
add('Mr. Gigi and the Squid')
add('Mutt and Jeff')
add('My Cage')
add('MythTickle')
add('Nancy')
add('Nest Heads')
add('NEUROTICA')
add('New Adventures of Queen Victoria')
add('Non Sequitur')
add('The Norm Classics')
add('Nothing is Not Something')
add('Off the Mark')
add('Ollie and Quentin')
add('On A Claire Day')
add('One Big Happy')
add('Ordinary Bill')
add('The Other Coast')
add('Out of the Gene Pool Re-Runs')
add('Over the Hedge')
add('Overboard')
add('Oyster War')
add('PC and Pixel')
add('Peanuts')
add('Pearls Before Swine')
add('Pibgorn')
add('Pibgorn Sketches')
add('Pickles')
add('Pinkerton')
add('Pluggers')
add('Pooch Cafe')
add('PreTeena')
add('Prickly City')
add('Rabbits Against Magic')
add('Raising Duncan')
add('Real Life Adventures')
add('Reality Check')
add('Red and Rover')
add('Red Meat')
add('Reply All')
add('Rip Haywire')
add('Ripleys Believe It or Not')
add('Rose is Rose')
add('Rubes')
add('Rudy Park')
add('Savage Chickens')
add('Scary Gary')
add('Shirley and Son Classics')
add('Shoe')
add('Shoecabbage')
add('Shortcuts')
add('Skin Horse')
add('Skippy')
add('Slowpoke')
add('Soup to Nutz')
add('Speed Bump')
add('Spot the Frog')
add('Starslip')
add('Stone Soup')
add('Strange Brew')
add('The Sunshine Club')
add('Sylvia')
add('Tank McNamara')
add('Tarzan')
add('Ten Cats')
add('Tales of TerraTopia')
add('That is Priceless')
add('Thats Life')
add('Thatababy')
add('Thin Lines')
add('Tiny Sepuku')
add('TOBY')
add('Todays Dogg')
add('Tom the Dancing Bug')
add('Too Much Coffee Man')
add('Trivquiz')
add('Twaggies')
add('Uncle Arts Funland')
add('Unstrange Phenomena')
add('U.S. Acres')
add('Viivi and Wagner')
add('Watch Your Head')
add('Wee Pals')
add('Wizard of Id')
add('Working Daze')
add('Working It Out')
add('W.T. Duck')
add('Zack Hill')
add('Ziggy')

# http://www.gocomics.com/explore/editorial_list
# XXX

# http://www.gocomics.com/explore/sherpa_list
# XXX

