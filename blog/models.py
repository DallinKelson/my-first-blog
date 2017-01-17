from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Question(models.Model):
    q_text = models.TextField()

    def print_self(self):
        return str(self.q_text)

    def print_answers(self):
        return self.choice_set.all()

    def __str__(self):
        return self.q_text
    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length=200)
    q_link = models.IntegerField(null=True)

    def print_self(self):
        return str(self.choice_text)

    def __str__(self):
        return self.choice_text

directions_dict = {
    "AYou are in a vast, boring, empty room. Where to from here?":[("North",2),("East",4),("West",3),("South",5)],
    "BA bear is blocking the east. He looks mean. Also he stands on the banks of a large river, which is also foreboding.":[("West",6),("North",7),("South",1)],
    "CA troll is eating dinner to the south and really doesn't want to be disturbed. A witch is yelling drunken obscenities at you from the north.":[("East",1),("West",8)],
    "DA river surrounds this area on the north and east. It is quite wet, as rivers tend to be.":[("West",1),("South",9)],
    "ETwelve wolves invite you to play poker to the south. They seem sketchy so you decline.":[("East",9),("West",10),("North",1)],
    "FA drunken witch to the south gives you a sword. You are grateful but can't help noticing the whiskey on her breath.":[("East",2),("North",12),("West",11)],
    "GThe river flows to the north and east of you. If it weren't so dark you might see a bridge somewhere. Oh wait, it's daytime. There's a bridge to the east.":[("East",13),("West",12),("South",2)],
    "HAn ominous barbed wire sign to the west, with a sign that reads 'Electric fence, touch only in case of suicide.' You're in a good mood today.":[("North",11),("South",14),("East",3)],
    "IAnother boring stretch of forest, with nothing around. You nap for awhile and continue on.":[("North",4),("East",16),("South",15),("West",5)],
    "JYou'd go north if that troll wasn't hogging the entire road with his picnic. He's a real impediment to traffic.":[("West",14),("East",5),("South",17)],
    "KA huge barbed wire fence to the west. It sizzles when you spit on it.":[("North",18),("East",12),("South",8)],
    "LThe river continues to the north, and the mermaids swimming at this stretch of it are throwing rocks at you.":[("West",18),("South",6),("East",7)],
    "MA sweet smell emanates from either the east or south. To the north a waterfall dashes an unwitting canoe against the rocks.":[("East",19),("South",20),("West",7)],
    "NA barbed wire fence on the west, with landscape beyond it that you wouldn't visit if you could: the people seem to be having some kind of Justin Bieber festival.":[("South",21),("East",10),("North",8)],
    "OTo the south of you is the land of the giants. Giants can be real jerks sometimes, and you just really don't feel like putting up with their crap today.":[("East",22),("West",23),("North",9)],
    "PThe great river rises to the east, up the side of a mountain somehow. It's a fantasy world, I guess gravity is weaker or something. You also can't go north. No particular reason.":[("South",22),("West",9)],
    "QYou don't want to go south, towards the land of the giants, where the tempers are as big as the feet, and twice as smelly.":[("East",23),("North",10),("West",21)],
    "RIn the distance, to the northwest, the river runs into the electric barbed-wire fence, which was clearly a mistake of engineering on behalf of either the designer of the fence or the designer of the river. You decide to steer very clear of the whole area.":[("South",11),("East",12)],
    "SThe mountains to the east and north look climbable, but you honestly just don't feel like it. You've been walking all day, for crying out loud!":[("West",13),("South",24)],
    "TThe river is to the south and west of you now, which is really disorienting. Not Tilt-A-Whirl disorienting, but definitely Shampoo-On-The-Wrong-Shelf disorienting.":[("North",13),("East",24)],
    "UWorkers are touching up the barbed wire fence to the west, and they yell at you not to head south because of a riot. Turns out the dwarves are getting really sick of short jokes and they're gonna do something about it.":[("North",14),("East",17)],
    "VAn old man brandishing a machine gun politely tells you to go the hell back the way you came, so you oblige.":[("West",15),("North",16)],
    "WTo the north is the legendary tribe of degenerate wolf gamblers, whom you steer clear of since they always cheat. To the south is the less than legendary tribe of angry giants, whom you avoid just on principle.":[("East",15),("West",17)],
    "XYou should just go south. You've made it this far.":[("South",25)],
    "YThere's a tablet on the ground.":[("Read it",26)],
    "ZCan I have the honor of marrying your daughter, Anna Hoffmann?":[("Yes!",27)]
}
