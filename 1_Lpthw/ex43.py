# -- coding: utf-8 --

from sys import exit
from random import randint


class Scene(object):
    
    def enter(self):
        print "This sceneis not yet configured. Subclass it and implement erter()."
        exit(1)


class Engine(object):
    
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while  current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
        "You mom would be proud...if she were samrter.",
        "Such a luser.",
        "I have a samll puppy that's better at this."
    ]
    
    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):
    
    def enter(self):
        print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
        print "your entire crew. You are the last suiviving member and you last"
        print "mission is to get the neutron destruct bomb from the Weapon Armory,"
        print "put it in the bridge, and blow the ship up after getting to an"
        print "escape pod.\n"
        print "You're running down the central corridor to the Weapons Armory whe"
        print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costum"
        print "flowing around his hate filled body. He's blocking the door to the"
        print "Armory and about to pulla weapon to blast you."

        action = raw_input(">")
        
        if action == 'shout!':
            print "Quick on the draw you yank out your blaster and fire it at the Gothon."
            print "His clown constume is flowing and moving around his body, which throws"
            print "off your aim. Your laser hits his costume but misses him entirely. This"
            print "completely ruins his brand new costume his mother bought him, which"
            print "makes him fly into an insane rage and blast you repeatedly in the face until"
            print "you are dead. Then he eats you."
            return 'death'

        elif action == 'dodge!':
            print "Like a world class boxer you dodge, weave, slipp and slide right"
            print "as the Gothon's blaster cranks a laser past your head."
            print "In the middle of you artful dodge  your foot slops and you"
            print "bang your head on the metal wall and pass out."
            print "You wake up shourtly after only to die as the Gothon stomps on"
            print "your head and eats you."
            return 'death'

        elif action == 'tell a joke':
            print """
	Lucky for you they made you learn Gothon insults in the academy.
	You tell the one Gothon joke you know:
	Lbhe zbgure vf sng, jura fur fvgf nebhaq gur ubhgr, fur fvgf nebhaq gurubhfr.
	The Gothon stops, tries not to laugh, then busts out laughing and can't move.
	While he's laughing you run up and shoot him square in the head"
	putting him down, then jump through the Weapon Armory door.
            """
            return 'laser_weapon_armory'

        else:
            print "Does not compute!"
            return 'central_corridor'

class LaserWeaponArmory(Scene):
    
    def enter(self):
        print """
    You do a dive roll into  the Weapon Armory, crouch and scan the room
    for more Gothons that might be hiding. It's dead quiet, too quiet.
    You stand up and run to the far side of the room and find the
    neutron bomb in its container. There's a keypad lock on the box
    and you need the code to get the bomb out. If you get the code
    wrong 10 times the the lock closes forever and you can't get
    bomb. The code is 3 digits.
        """
        code = randint(0,999)
        guess = int(raw_input("[keypad]>"))
        guesses = 0
        
        while guess!= code and guesses < 10:
            if guess < code:
                print "too small"
            else:
                print "too large"
            guesses += 1
            guess = int(raw_input("[keypad]>"))

	
        if guess == code:
            print """
    The container clicks open and the seal breaks, letting gas out.
    You grab the neutron bomb and run as fast as you can to the
    bridge where you must place it in the right spot.
            """
            return 'the_bridge' 
        else:
            print """
    The lock buzzes one last time and the you hear a sickening
    metlting sound as the mechanism is fused together.
    You decide to sit there, and finally the Gothons blow up the
    ship from there ship and you die."
            """
            return 'death'

class TheBridge(Scene):
    
    def enter(self):
        print """
    You burst onto the Bridge with the netron destruct bomb
    under your arm and surprise 5 Gothons who are trying to
    take control of the ship. Each of them has an even uglier
    clown costume than the last. They haven't pulled their
    weapons out yet, as they see the active bomb under your
    arm and don't want to set if off.
        """
        action = raw_input(">")
        
        if action == "throw the bomb":
            print """
    In a panic you throw the bomb at the group of Gothons
    and  make a leap for the door. Right as you drop it a
    Gothon shoots you right in the back killing you.
    As you die you dee another Gothon frantically try to disarm the bomb.
    You die knowing they wil probably blow up when it goes off.
            """
            return 'death'
        
        elif action == "slowly place the bomb":
            print """
    You point your blaster at the bomb under you arm
    and the Gothons put their hands up and start to sweat.
    You inch backward to the door, open it, and the carefully
    place the bomb on the floor, pointing your blaster at it.
    You then junp back through the door, punch the close button
    and blast the lock so the Gothons can't get out.
    Now that the bomb is placed you run to the escape pod to 
    get off this tin can.
            """
            return 'escape_pod'
        else:
            print "Does not compute!"
            return 'the_bridge'

class EscapePod(Scene):
    
    def enter(self):
        print """
    You rush through the ship desperately trying to make it to
    the escape pod before the whole ship explodes. It seams like
    hardly any Gothons are on the ship, so your runis clear of interference.
    You get to the chamber with the escape pods, and now need to pick one to 
    take. Some of them could be damaged but you don't have time to look.
    There's 5 pods, which one do you take
        """
        good_pod = randint(1, 5)
        guess = raw_input("[pod #]> ")
        
        print "You jump into pod %s and hit the eject button."%guess
        
        if int(guess) != good_pod:
            print """
    The pod escapes out into the void of space, then
    implodes as the hull ruptures, crushing your body to jam jelly.
            """ 
            return 'death'
        else:
            print """
    The pod easil slides out into space heading to the planet below.
    As it flies to the planet, you look back and see your ship implode
    then explode like a bright star, taking out the Gothon ship at the
    same time. You won!"
            """
            return 'finished'

class Finished(Scene):
    
    def enter(self):
        print "You won! Good job."
        return 'finished'

class Map(object):
    
    scenes = {
        'central_corridor':CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)    
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
