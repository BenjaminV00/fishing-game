class Equipment:
    def __init__(self, str=0, speed=0, mana=0, hp=0, armor=0, special=0, type="armor", name="", desc="", equip_type="pet"):
        self.str = str
        self.speed = speed
        self.mana = mana
        self.hp = hp 
        self.armor = armor 
        self.special = special 
        self.type = type 
        self.name = name
        self.desc = desc
        self.equip_type 



lion_sword = Equipment(str=10, type="weapon", name="lion sword", desc="sword of the lion", equip_type="pet")
lion_armor = Equipment(str=2, armor=10, special=4, type="armor", name="lion armor", desc="Lion skin merge into a armor", equip_type="pet") #You get a buff that is caled lions rawr that boosts up your armor and dmg by 5%
Aqua_spear = Equipment(str=5, mana=3, type="weapon", name="Aqua spear", desc="A spear from the kraken its self", equip_type="pet") #Summons massive waves that can do a high to mid level attack (Goes well with the deep sea armor)
Deep_sea_armor = Equipment(armor=7, hp=3, mana=2, type="armor", name="Deep sea armor", desc="A armor no man has found", equip_type="pet") #If having the Aqua spear equip with the deep sea armor on you gain a moderate special boost at the start ofa ll the fights
Bass_armor = Equipment(armor=5, hp=3, type="armor", name="Bass armor", desc="The many scales it took to make this is sad", equip_type="pet") 
Big_mama_sword = Equipment(str=11, speed= -2, type="weapon", name="Big mama sword", desc="A real life story", equip_type="pet") 
Puffer_fish_armor = Equipment(armor=1, special=2, speed=4, type="armor", name="Puffer fish armor", desc="Carful dont poke yourself", equip_type="pet") #Poisons enemy if hit with a str attack draining 3% of their hp slwoly each turn but ending around the 7-10th turn(Mana attacks doesnt trigger the effect)
Eel_sword = Equipment(str=4, special=3, mana=3, type="weapon", equip_type="pet", name="Eel sword", desc="Thats a very shocking fish") #Shocks enemy dealing 5% of their max hp
life_drinker_ring = Equipment(special=5, type= "armor", equip_type="pet", name="life drinker ring", desc="DIY vampire") #stealing hp from enemy every 5 turns (4%)
#Anything above here are high level gear
#Anything down here is low to moderate gear 
Two_hand_axe = Equipment(str=4, speed= -1, type="weapon", equip_type="pet", name="Two hand axe", desc="Very heavy but packs a huge punch" )
Swat_armor = Equipment(armor=3, speed=1, name="Swat armor", type="armor", equip_type="pet",  desc="A decent armor that can be a bit flexible to move around in")
Black_steel_katana = Equipment(str=2, speed=3, type="weapon", equip_type="pet", name="Black steel katana", desc="forged with the finest steel")
Spear_gun = Equipment(Str=2, speed=2, type="weapon", equip_type="pet", name="Spear gun", desc="packs a decent punch but take a turn to reload")
Samurai_armor = Equipment(armor=3, speed=2, hp=1, type="armor", equip_type="pet", name="Samurai armor", desc="Passes down generations to generations")
Rifle = Equipment(str=3, speed=2, type="weapon", equip_type="pet", name="Rifle", desc="Takes a turn to reload." )
#Anything down here are low lvl items and anything above are moderate
Sling_shot = Equipment(str=1, speed=3, equip_type="pet", type="weapon", name="sling shot", desc="pew pew")
chain_armor = Equipment(armor=2, speed=2, type="armor", equip_type="pet", name="Chain armor", desc="Forged from a blacksmith very light and a mid level gear")
One_handed_axe = Equipment(str=3, speed= -1, type="weapon", equip_type="pet", name="Two hand axe", desc="Heavy but packs a huge punch" )
Toilet_shield = Equipment(armor=1, hp=1, type="armor", equip_type="pet", name="Toilet shield", desc="Uhh where did you get this...")
The_blue_gill_armor = Equipment(speed=1, hp=2, type="armor", equip_type="pet", name="Blue gill armor", desc="50 bluegills to make this how is that possible...")
Broken_warrior_gear = Equipment(armor=2, health=1, special=3, type= "armor", equip_type="pet", name="Broken warrior armor", desc="Such a brave fish") #When you have this gear on you'll be granted iron will boosting your str by 2%
Rusted_iron_sword = Equipment(str=3, type= "weapon", equip_type="pet", name="Rusted iron sword", desc="Plain old iron sword")
Novice_mage_robe = Equipment(armor=1, mana=2, special=2, type= "armor", equip_type="pet", name="Novice magic robe", desc="Magic robe") #As wearing this armor you get a 3% mana boost
Newbie_wand = Equipment(str=1, mana=3, speed=1, type= "weapon", equip_type="pet", name="Newbie wand", desc="Just a wand")
stick = Equipment(str=1, type="weapon", equip_type="pet", name="Stick", desc="Really a stick come on stick to a better weapon")
Slime_ring = Equipment(Str=1, type="armor", equip_type="pet", desc="Ugh a slimy ring why bother to wear it")
stone_ring = Equipment(armor=1 , type="armor", equip_type="pet", name="Stone ring", desc="Surprising not heavy.")
