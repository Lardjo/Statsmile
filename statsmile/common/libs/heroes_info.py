#!/usr/bin/env python3
# All right reserved 2013
# Description: Dota 2 Library (Heroes Full Information)
# URL: http://github.com/Lardjo

heroes_info = {

    1: {'name': 'Anti-Mage',
        'role': 'Carry, Escape',
        'radiant': 'true',
        'class': 'Agility',
        'bio': '<strong>Anti-Mage</strong> is a fast melee Agility Carry with an emphasis on disabling and killing '
               'high-mana enemies. He has notably high agility and low base attack time, giving him high damage and '
               'scaling with his basic attacks. His signature ability is Mana Break, a passive attack modifier that '
               'makes him a huge threat to mana-reliant heroes, mainly Intelligence-based casters. In addition to '
               'granting substantial bonus damage on each attacks, its mana burn sets enemies up to be devastated by '
               'his ultimate ability, Mana Void. Blink is a highly versatile ability that allows Anti-Mage to '
               'instantly teleport short distances, thereby allowing him to escape, chase, and even farm with ease. '
               'Combined with his high base movement speed, this makes Anti-Mage a highly mobile hero at all points '
               'in the game. Spell Shield greatly increases Anti-Mage\'s magic resistance, allowing him to sustain '
               'more damage from enemy casters. Finally, Mana Void finishes off targets after their mana has been '
               'burnt, inflicting heavy damage to both the target and enemies surrounding the target. The damage '
               'Mana Void can potentially deal scales extremely well into the late game, as enemies\' mana pools only '
               'grow larger over time. His naturally fast basic attacks combined with his powerful abilities make him '
               'extremely dangerous in the late game, allowing him to devastate enemies with ease if he is allowed to '
               'farm as a hard carry.',
        'quote': 'I bring an end to magic.',
        'strength': '20 + 1.2',
        'agility': '22 + 2.8',
        'intelligence': '15 + 1.8',
        'ms': '315',
        'tr': '0.5',
        'sr': '1800 / 800',
        'ar': 'Melee',
        'miss_s': 'Instant',
        'ad': '0.3 + 0.6',
        'cd': '0.3 + 0.47',
        'bat': '1.45',
        'avatar': 'img/dota/heroes/antimage.png'},

    2: {'name': 'Axe',
        'role': 'Durable, Initiator, Disabler, Jungler',
        'radiant': 'false',
        'class': 'Strength',
        'bio': '<strong>Mogul Khan</strong> the <strong>Axe</strong> is a savage melee strength hero, infamous for '
               'creating chaos in battle and thriving off of it. He is commonly played as an initiator with a large '
               'semi-carry presence that quickly transitions into a support role later in the game. His fighting style '
               'demands that he gets up close and very personal. He can taunt enemies into targeting him and counters '
               'those who try to strike him with a sweeping Counter Helix that slashes all enemies at melee range. '
               'Axe has a tendency to draw opponents so deep in the fight that they do not have a chance to escape, '
               'each soul he draws infusing his own love of war; his ultimate, Culling Blade bolsters that talent '
               'with an attack that unconditionally kills a unit with low health.',
        'quote': 'Axe is all the reinforcement this army needs!',
        'strength': '25 + 2.5',
        'agility': '20 + 2.2',
        'intelligence': '18 + 1.6',
        'ms': '290',
        'tr':'0.6',
        'sr':'1800 / 800',
        'ar':'Melee',
        'miss_s':'Instant',
        'ad':'0.5 + 0.5',
        'cd':'0.3 + 0.51',
        'bat':'1.7',
        'avatar': 'img/dota/heroes/axe.png'
    },

    3: {'name': 'Bane',
        'role': 'Disabler, Nuker, Support',
        'radiant': 'false',
        'class': 'Intelligence',
        'bio': '<strong>Atropos</strong> the <strong>Bane Elemental</strong>, also known simply as Bane, is a ranged '
               'intelligence Hero, possessing dark and nightmarish abilities that give him strong disabling, ganking, '
               'and nuking prowess. Mostly played as a support, he has some of the highest starting stats of any hero, '
               'yet is unique in the sense that all his attributes and stat growths are equivalent. In addition, he '
               'possesses four highly potent single-target spells, which if used properly can more than make up for '
               'his complete lack of area of effect presence and pushing power. Enfeeble reduces the target\'s attack '
               'damage by a tremendous amount, which can highly reduce an attack-reliant enemy hero\'s effectiveness '
               'from as early as the laning stage all the way to the endgame. Brain Sap is a nuke that deals hefty '
               'pure damage to the target, healing himself for the same amount as well. Nightmare puts a unit to '
               'sleep, completely disabling for several seconds and dealing minor damage per second. If the slept '
               'target is physically attacked, it wakes up and the spell transfers to the attacker (spells will also '
               'wake the target up, but will not transfer the effect to the caster). Finally, Bane\'s Fiend\'s Grip is '
               'a channeling spell that completely disables the target for several seconds, dealing heavy damage per '
               'second and giving Bane some mana back as well. Bane\'s debilitating lockdown abilities are what make '
               'him an invaluable support to allies, and a feared one for enemies.',
        'quote': 'I dreamt a field of war... and woke to find myself upon it.',
        'strength': '22 + 2.1',
        'agility': '22 + 2.1',
        'intelligence': '22 + 2.1',
        'ms': '315',
        'tr': '0.6',
        'sr': '1800 / 800',
        'ar': '400',
        'miss_s': '900',
        'ad': '0.3 + 0.7',
        'cd': '0.5 + 0.51',
        'bat': '1.7',
        'avatar': 'img/dota/heroes/bane.png'
    },

    4: {'name': 'Bloodseeker',
        'role': 'Carry, Jungler',
        'radiant': 'false',
        'class': 'Agility',
        'bio': '<strong>Strygwyr</strong> the <strong>Bloodseeker</strong> is a melee agility hero imbued with '
               'dreadful powers to fuel violence and rip enemies apart in the heat of close combat. He can drive '
               'targets into a maddened Bloodrage, increasing the damage of their attacks, preventing them to cast '
               'spells and bleeding their life in the frenzy. His speed is unmatched when he senses the blood of the '
               'dying, and from this perception none can escape. His own health is never a problem, as he can salve '
               'his wounds merely by bathing in the blood of the fallen. His ultimate, Rupture, sunders the skin of '
               'his victims, causing them to trail their life force behind if they dare to flee.',
        'quote': 'You should be honored to bleed so that the Flayed ones may live.',
        'strength': '23 + 2',
        'agility': '24 + 3',
        'intelligence': '18 + 1.7',
        'ms': '300',
        'tr': '0.5',
        'sr': '1800 / 800',
        'ar': 'Melee',
        'miss_s': 'Instant',
        'ad': '0.43 + 0.74',
        'cd': '0.6 + 1.4',
        'bat': '0.7',
        'avatar': 'img/dota/heroes/bloodseeker.png'
    },

    5: {'name': 'Crystal Maiden',
        'role': 'Support, Disabler, Nuker, Lane Support',
        'radiant': 'true',
        'class': 'Intelligence',
        'bio': '<strong>Rylai</strong> the <strong>Crystal Maiden</strong> is a ranged intelligence Hero used as a '
               'hard support and disabler. She is perhaps best known for her powerful global mana regeneration aura. '
               'This aura allows mana dependent allies to excel during the early to mid game and the laning phase, and '
               'allows her to constantly activate her own spells without needing to worry much about the mana costs. '
               'She also has a high amount of early game presence with just a few points in her Crystal Nova and '
               'Frostbite abilities. Crystal Nova is a powerful area-of-effect nuke that slows both attack and '
               'movement speeds of enemies within an area for several seconds, while Frostbite encases an enemy in a '
               'block of ice for several seconds, immobilizing it and doing moderate damage per second. Combining '
               'these two abilities together along with a laning partner\'s own spells often results in the quick '
               'death of an enemy hero. Although her strong early game presence is quickly lost due to her extreme '
               'frailty and poor mobility, she can still inflict a heavy amount of damage in teamfights later on if '
               'she is able to channel her deadly ultimate, Freezing Field. Her Arcane Aura, strong disabling and '
               'nuking prowess, relative ease of usage, and almost complete lack of item dependence makes her a '
               'reliable support caster that can be useful in any team.',
        'quote': 'When Hell freezes over, I\'ll start calling it Heaven.',
        'strength': '16 + 1.7',
        'agility': '16 + 1.6',
        'intelligence': '19 + 2.9',
        'ms': '280',
        'tr': '0.5',
        'sr': '1800 / 800',
        'ar': '600',
        'miss_s': '900',
        'ad': '0.55 + 0',
        'cd': '0.3 + 2.4',
        'bat': '1.7',
        'avatar': 'img/dota/heroes/crystal_maiden.png'
    },

    6: {'name': 'Drow Ranger',
        'role': 'Carry',
        'radiant': 'true',
        'class': 'Agility',
        'bio': '<p><strong>Traxex</strong> the <strong>Drow Ranger</strong> is a ranged agility hero whose greatest '
               'assets are her incredible damage and ability to keep threats at bay. Traxex is a carry who, though '
               'lacking survivability, provides a worthwhile contribution through her damage alone. The Drow Ranger '
               'can be extremely powerful at any given point in the game.</p><p>As an agility hero, Traxex\'s damage '
               'is based largely off her auto attacks and is among the greatest largely due to the massive amounts of '
               'agility she gains from her passive ultimate, Marksmanship. The Drow Ranger also adds ranged damage to '
               'teammates with her global Precision Aura. Despite her lack of escape spells, Drow Ranger can keep '
               'herself relatively safe from enemy spellcasters and melee heroes using her Silence and her Frost '
               'Arrows, respectively. Frost Arrows infuses her attacks with ice cold, greatly slowing down her '
               'enemies. Since it can be manually cast, Frost Arrows can be used to harass her foes in the early game '
               'without drawing the creeps\' attention. Silence is a great counter to enemy spellcasters who might '
               'threaten her life in battles. Position is of utmost importance as Traxex is quite vulnerable in close '
               'combat and the agility bonus from Marksmanship is removed when enemies come near her. This means she '
               'struggles against melee dps heroes with high mobility, such as Anti-Mage and Faceless Void.</p>',
        'quote': 'I walk alone, but the shadows are company enough.',
        'strength': '17 + 1.9',
        'agility': '26 + 1.9',
        'intelligence': '15 + 1.4',
        'ms': '300',
        'tr': '0.6',
        'sr': '1800 / 800',
        'ar': '625',
        'miss_s': '1250',
        'ad': '0.7 + 0.3',
        'cd': '0.4 + 0.5',
        'bat': '1.7',
        'avatar': 'img/dota/heroes/drow_ranger.png'
    },

    7: {'name': 'Earthshaker',
        'role': 'Initiator, Disabler, Support, Lane Support',
        'radiant': 'true',
        'class': 'Strength',
        'bio': '<strong>Raigor Stonehoof</strong> the <strong>Earthshaker</strong> is a melee Strength Hero with '
               'several area of effect disables, commonly played as a ganker or initiator. Unlike most Strength '
               'heroes, he is played more like an Intelligence caster hero and is almost entirely reliant on his '
               'spells to inflict heavy damage. His Fissure is a versatile spell that affects enemies in a line, '
               'used to stun, inflict decent damage, and create an impassable wall of earth for a significant '
               'duration. Good usage of this can cut off chokepoints, leaving enemies with no escape routes or '
               'preventing them from chasing after endangered allies. Enchant Totem massively boosts his attack '
               'damage for one attack, and has a very short cooldown. Aftershock lets the Earthshaker deal '
               'additional damage and stun in a small area around him everytime he uses one of his spells, and '
               'combos particularly well with Enchant Totem. Earthshaker\'s heavy AoE-centric kit is most '
               'powerful when his enemies are in large numbers and in close proximity. With his Echo Slam, '
               'he can deal heavy damage to clusters of enemies. All of Earthshaker\'s spells (with the exception '
               'of his ultimate) have a long casting animation, but with proper positioning, an adept Earthshaker '
               'can wreak havoc with his area-of-effect spells. Blink Dagger is an essential item for Earthshaker '
               'to be able to properly land Echo Slam within a cluster of enemies. At the same time, because of the '
               'high mana costs of his spells, he needs some form of mana sustenance. With his tremendous seismic '
               'power, the Earthshaker is never one that should be taken lightly even when he is heavily outnumbered.',
        'quote': 'There may be many earths, but there\'s only one Earthshaker.',
        'strength': '22 + 2.5',
        'agility': '12 + 1.5',
        'intelligence': '16 + 1.8',
        'ms': '300',
        'tr': '0.6',
        'sr': '1800 / 800',
        'ar': 'Melee',
        'miss_s': 'Instant',
        'ad': '0.467 + 0.863',
        'cd': '0.69 + 0.5',
        'bat': '1.7',
        'avatar': 'img/dota/heroes/earthshaker.png'
    },

    8: {'name': 'Juggernaut',
        'role': 'Carry, Pusher',
        'radiant': 'true',
        'bio': '<strong>Yurnero</strong> the <strong>Juggernaut</strong> is a melee agility hero whose abilities allow '
               'him to sprint into battle and '
               'recklessly devastate enemies in an impenetrable flurry of blades. His skills grant invulnerability '
               'and magic immunity, turning him into an unstoppable force on a hairpin. Juggernaut is strong both '
               'offensively and defensively, and deals heavy damage both physical and magical with his Blade Fury '
               'and Omnislash ultimate, but he possesses below average strength and intelligence attributes, so he '
               'does not have as much health and mana as other heroes and is vulnerable when his abilities are on '
               'cooldown. For this reason, although his abilities make him powerful even in the early game, he cannot '
               'charge into forces without restraint until farmed and is usually played as a carry.',
        'quote': 'By the Visage of Vengeance, which drowned in the Isle of Masks, '
                 'I will carry on the rites of the Faceless Ones.',
        'class': 'Agility',
        'strength': '20 + 1.9',
        'agility': '20 + 2.85',
        'intelligence': '14 + 1.4',
        'ms': '305',
        'tr':'0.6',
        'sr':'1800 / 800',
        'ar':'Melee',
        'miss_s':'Instant',
        'ad':'0.33 + 0.84',
        'cd':'0.3 + 0.51',
        'bat':'1.6',
        'avatar': 'img/dota/heroes/juggernaut.png'
    },

    9: {'name': 'Mirana',
        'role': 'Carry, Nuker, Disabler, Escape',
        'radiant': 'true',
        'class': 'Agility',
        'bio': '<strong>Mirana</strong> the <strong>Princess of the Moon</strong>, is a ranged Agility Hero that uses '
               'her abilities to surprise, chase, and assault enemies. She is an excellent huntress and widely known '
               'for her Sacred Arrow which stuns her victim with deadly precision. The arrow stuns longer when its '
               'fired from a farther distance. Mirana can bring down the stars with Starstorm to damage nearby enemies '
               'and an additional star to cast down on her one unfortunate target. Mounting with her trusted tiger '
               'Sagan, Mirana can Leap forward over a distance, to escape or chase, and enhancing her allies with a '
               'roar, increasing their attack and movement speed. Invoking the power of her moon goddess, Mirana uses '
               'her ultimate, Moonlight Shadow to cloak all allied heroes and herself with invisibility. At any time, '
               'Mirana and her allies can break out of their hiding with an ambush and fade into the shadows again '
               'during the duration of the spell. With an array of mighty and supportive skills, Mirana is a versatile '
               'heroine that can excel early in the game as a mobile ganker. She is not much heavily reliant on '
               'luxurious items but she can benefit from almost any item that gives her presence in the battlefield.',
        'quote': ' How long must we ride before we\'re summoned again to the Nightsilver Woods?',
        'strength': '17 + 1.85',
        'agility': '20 + 2.75',
        'intelligence': '17 + 1.65',
        'ms': '300',
        'tr': '0.4',
        'sr': '1800 / 800',
        'ar': '600',
        'miss_s': '900',
        'ad': '0.3 + 0.7',
        'cd': '0.5 + 0.83',
        'bat': '1.7',
        'avatar': 'img/dota/heroes/mirana.png'
    },

    10: {'name': 'Morphling',
         'role': 'Carry, Escape, Initiator, Nuker',
         'radiant': 'true',
         'class': 'Agility',
         'bio': '<strong>Morphling</strong> is a ranged agility hero that has many flexible skills and item builds and '
                'is skilled as a very strong hard carry. He relies strongly on his attributes, and is an effective '
                'ganker. Unlike other agility carries who rely on physical attacks, he relies on his powerful abilities '
                'to initiate and shift into a state from which he can make a kill. Waveform lets him surge directly '
                'forward to a location, damaging enemies on his path, working both as a nuke or an escape. Adaptive '
                'Strike is an interesting scaling skill that blasts enemies with magical water while also stunning, '
                'knocking back, and dealing damage. Its power is based on either Agility or Strength. Morph allows him '
                'to edit his physical being, switching it from Agility or Strength, transforming him into a strong '
                'damage dealer or a tank. His ultimate, Replicate, creates a copy of either an ally or an enemy. At '
                'will, he can take on the place of that Replicate and instantly surprise enemies.',
         'quote': 'You only miss the water when the well runs dry.',
         'strength': '19 + 2',
         'agility': '24 + 3',
         'intelligence': '17 + 1.5',
         'ms': '285',
         'tr': '0.6',
         'sr': '1800 / 800',
         'ar': '350',
         'miss_s': '1300',
         'ad': '0.5 + 0.5',
         'cd': '0.25 + 0.51',
         'bat': '1.6',
         'avatar': 'img/dota/heroes/morphling.png'
    },

    11: {'name': 'Shadow Fiend',
         'role': 'Carry, Nuker',
         'radiant': 'false',
         'class': 'Agility',
         'bio': '<strong>Nevermore</strong> the <strong>Shadow Fiend</strong> is a ranged agility Hero possessing '
                'abilities that inflict superb burst damage from varying distances. Whether near or far, Shadow Fiend '
                'is able to release incredible offensive power, both physical and magical. Shadow Fiend\'s true power '
                'comes from the souls he takes, thus, he is more dangerous every time he kills. With enough souls, he '
                'can release all of the captured souls in a devastating burst, dealing more damage to enemies that '
                'are closer to him. Shadow Fiend is a carry who is powerful at all stages of the game, a trait most '
                'carries don\'t share. He can harass and conquer early game, set out and kill unsuspecting Heroes '
                'during the mid stages, and unleash more power and dominate other Heroes late game.',
         'quote': 'So, you\'re curious where I come from? There\'s one easy way to find out for yourself.',
         'strength': '15 + 2',
         'agility': '20 + 2.9',
         'intelligence': '18 + 2',
         'ms': '305',
         'tr': '1.0',
         'sr': '1800 / 800',
         'ar': '500',
         'miss_s': '1200',
         'ad': '0.5 + 0.54',
         'cd': '0.67 + 0.4',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/nevermore.png'
    },

    12: {'name': 'Phantom Lancer',
         'role': 'Carry, Escape, Pusher',
         'radiant': 'true',
         'class': 'Agility',
         'bio': '<strong>Azwraith</strong> the <strong>Phantom Lancer</strong> is a melee agility hard carry and '
                'pusher because of his capability of constantly generating multiple illusions in a matter of seconds. '
                'He requires deep cunning, positioning, and most importantly, great micromanagement as his illusions '
                'might just get in the way rather than help the situation if not utilized correctly. All of his '
                'abilities help him in his creation of images, allowing him to always have a companion. He has a nuke '
                'skill that deals high damage, slows the target, and creates an illusion at his target\'s location. '
                'His escape skill allows him to turn invisible while creating an illusion to take his place, possibly '
                'tricking enemies into wasting their spells and time in trying to kill said illusion. His passive '
                'allows him to generate an illusion of himself which procs during an attack. His ultimate gives him '
                'magic resistance, an improvement to his skill Juxtapose, but most importantly allows his illusions '
                'to generate their own illusions.',
         'quote': 'We outnumbered you. We outnumber them all!',
         'strength': '18 + 1.7',
         'agility': '23 + 4.2',
         'intelligence': '21 + 2',
         'ms': '290',
         'tr': '0.6',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.5 + 0.5',
         'cd': '0.3 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/phantom_lancer.png'
    },

    13: {'name': 'Puck',
         'role': 'Initiator, Nuker, Disabler, Escape',
         'radiant': 'true',
         'class': 'Intelligence',
         'bio': '<strong>Puck</strong> the <strong>Faerie Dragon</strong> is a highly mobile ranged intelligence hero '
                'best known for being an extremely unpredictable and slippery target. Puck is commonly played as an '
                'initiator and ganker, with spells that are equally useful for super-aggressive maneuvers as well as '
                'daring escapes. Expert use of Puck\'s abilities will let you appear out of nowhere, suddenly leave '
                'your enemies crippled and disadvantaged, and get away in the blink of an eye - but mess up your '
                'timing or misjudge the situation, and there is little left to save this fragile Hero from death.',
         'quote': 'I find myself strangely drawn to this odd configuration of activity.',
         'strength': '15 + 1.7',
         'agility': '22 + 1.7',
         'intelligence': '25 + 2.4',
         'ms': '295',
         'tr': '0.4',
         'sr': '1800 / 800',
         'ar': '550',
         'miss_s': '900',
         'ad': '0.5 + 0.8',
         'cd': '0.1 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/puck.png'
    },

    14: {'name': 'Pudge',
         'role': 'Durable, Disabler',
         'radiant': 'false',
         'class': 'Strength',
         'bio': '<strong>Pudge</strong> the <strong>Butcher</strong> is a melee strength hero feared for his '
                'incredible gank prowess. Though he may not look like it, he is one of the strongest solo-killing '
                'gankers in the entire game, with one combo of his three active abilities proving more than sufficient '
                'to kill fragile enemy heroes in the early and midgame. His signature ability, Meat Hook, which '
                'requires intuition, guesswork, and good timing to land, is thrown out in a straight line a long '
                'distance away. If it snags a unit, it will drag it back to Pudge, dealing enormous damage to it if '
                'it was an enemy. It thus serves as a powerful ganking and initation tool, and also has the utility '
                'of being able to save an endangered ally. He can then follow up with his ultimate, Dismember, which '
                'deals further damage to the target over a few seconds, as well as disabling it. During this period, '
                'he can toggle on his Rot to damage his enemy further while hurting himself as well, and use it to '
                'slow and finish off the hero if he or she survived the initial assault. To supplement his killing '
                'power is Flesh Heap, which provides him some magic resistance to reduce the damage he takes from Rot '
                'as well as from other enemy spells. The scariest aspect of Flesh Heap though is that it provides him '
                'permanent Strength with every kill that he participates in, giving him the potential to permanently '
                'increase his vitality (and physical damage) to monolithic proportions, thereby becoming a formidable '
                'tank. In the hands of a skilled player who can land his deadly Meat Hook with high accuracy, Pudge '
                'is both one of the most rewarding and fun heroes to play and one of the most fearsome opponents to '
                'be up against.',
         'quote': 'When I\'m through with these vermin, they\'ll be fit for a pie.',
         'strength': '25 + 3.2',
         'agility': '14 + 1.5',
         'intelligence': '14 + 1.5',
         'ms': '285',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.5 + 1.17',
         'cd': '0.3 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/pudge.png'
    },

    15: {'name': 'Razor',
         'role': 'Carry, Durable, Nuker',
         'radiant': 'false',
         'class': 'Agility',
         'bio': '<strong>Razor</strong> the <strong>Lightning Revenant</strong> is a ranged position-based agility '
                'tank/carry that employs his abilities to deal massive damage in a relatively short amount of time, '
                'chase down the fleeing injured with his speed, and inflict debuffs on more powerful foes. Razor '
                'prefers to keep his position or kite his enemies allowing his spells to unleash its full potential. '
                'Known for being one of the Anti-carry heroes, Razor specializes in using his opponent\'s own powers '
                'against them, draining them of their damage and using it to smite them, as well as damaging, '
                'slowing, and purging them of buffs should they dare cast a spell on him. His ultimate, Eye of the '
                'Storm, further enhances his carry-killing powers by inflicting constant, armor-shattering, lightning '
                'strikes on the foe with the lowest HP within a 500 radius. For those who rely on their pure brute '
                'force alone to fight, there is truly no escape from the Underscape.',
         'quote': 'I bring my lightning whip not to punish souls, but only to hasten them toward the inevitable exit.',
         'strength': '21 + 1.7',
         'agility': '22 + 2',
         'intelligence': '19 + 1.8',
         'ms': '295',
         'tr': '0.4',
         'sr': '1800 / 800',
         'ar': '475',
         'miss_s': '2000',
         'ad': '0.3 + 0.7',
         'cd': '0.5 + 0.125',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/razor.png'
    },

    16: {'name': 'Sand King',
         'role': 'Initiator, Disabler, Nuker',
         'radiant': 'false',
         'class': 'Strength',
         'bio': '<strong>Crixalis</strong> the <strong>Sand King</strong> is a melee strength hero with one of the '
                'highest area of effect damage outputs in the entire game. All four of his abilities can affect '
                'multiple enemy units, and can combo quite well with each other. He is one of the most versatile '
                'Heroes in the game as he can push, initiate, support, roam, gank, and even semi-carry if he does '
                'well. Late game his effectiveness diminishes as none of his abilities scale, but he can still '
                'function to support carries with Burrowstrike and Epicenter\'s slows. He is also versatile enough to '
                'be able to go to any lane with at least moderate success. He works well as a participant in a dual '
                'lane or trilane, but can also solo very effectively against melee enemies as Caustic Finale inhibits '
                'enemies from approaching the creeps. His main role in the team is to deliver a devastating '
                'initiation, delivering both stuns and slows to the enemy team. Crixalis is also very effective at '
                'escaping and dodging with two low cost, low cool down abilities that disjoin projectiles and can '
                'escape enemy damage. Burrowstrike allows him to tunnel underground and resurface in a short line, '
                'dealing damage and stunning all targets it hits. Sandstorm is used as escape mechanism and to do '
                'area of effect damage. Caustic Finale serves as a strong harassing tool against enemy melee heroes '
                'or as a followup after he Burrowstrikes a creep wave, allowing him to farm quite effectively. '
                'Finally, his ultimate, after a short channeling time, delivers a vast amount of area of effect damage '
                'and slow centered around himself, which necessitates a safe way to channel the ability like the '
                'purchase of a Blink Dagger. A Sand King that is played effectively is one that grinds the entire '
                'enemy team into dust.',
         'quote': 'I will show you fear in a handful of sand...',
         'strength': '18 + 2.6',
         'agility': '19 + 2.1',
         'intelligence': '16 + 1.8',
         'ms': '300',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.53 + 0.47',
         'cd': '0 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/sand_king.png'
    },

    17: {'name': 'Storm Spirit',
         'role': 'Carry, Initiator, Escape, Disabler',
         'radiant': 'true',
         'class': 'Intelligence',
         'bio': '<p><strong>Raijin Thunderkeg</strong>, the <strong>Storm Spirit</strong>, is a ranged Intelligence '
                'hero who wields the elemental power of lightning. He has high mobility, strong ganking and carrying '
                'potential, and very good synergy between his hero abilities.</p><p>Static Remnant creates an immobile '
                'clone of himself that, upon contact with an enemy, shocks all enemies in a small area for damage. It '
                'has a very low cooldown, making it a good farming skill. Electric Vortex binds an enemy to himself, '
                'drawing it in slowly; at higher levels of the skill, it will always be able to pull the target into '
                'a Static Remnant. Overload further supplements this combo by harnessing the excess charge whenever '
                'Raijin casts a spell, adding it in the form of magical damage to his next attack and zapping enemies '
                'in a radius around the target. Finally, Storm Spirit\'s ultimate and signature skill is Ball '
                'Lightning, in which he transforms into pure energy, sacrificing his own mana to dash quickly around '
                'the map in an invulnerable state, inflicting minor damage to foes he impacts as well as giving him '
                'an Overload charge. It can be used to initiate and escape long distances with ease.</p>',
         'quote': 'Everyone complains about the weather...well, I\'m doing something about it!',
         'strength': '19 + 1.5',
         'agility': '22 + 1.8',
         'intelligence': '23 + 2.6',
         'ms': '295',
         'tr': '0.6',
         'sr': '1800 / 800',
         'ar': '480',
         'miss_s': '1100',
         'ad': '0.5 + 0.3',
         'cd': '0.3 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/storm_spirit.png'
    },

    18: {'name': 'Sven',
         'role': 'Disabler, Initiator, Carry, Support',
         'radiant': 'true',
         'class': 'Strength',
         'bio': '<strong>Sven</strong> the <strong>Rogue Knight</strong> is a versatile melee strength Hero with '
                'superior physical power yet is coupled with various abilities that provide various utility. He can '
                'fulfill various roles, but is often played as a support or a semi-carry due to his high utility even '
                'without items. He possess a versatile arsenal, from shouts that grant armor both for escaping and '
                'pushing to throwable gauntlets that disorient enemies around the target unit. With enough items, '
                'Sven has the potential to be a strong late-game carry due to his ultimate which increases his damage '
                'and his passive which allows him to hit multiple targets at once. He is a formidable foe and his '
                'versatility makes the Rogue Knight a great asset to any team.',
         'quote': 'May my enemies share the fate of the Shattered Helm.',
         'strength': '23 + 2.7',
         'agility': '21 + 2',
         'intelligence': '14 + 1.3',
         'ms': '295',
         'tr': '0.6',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.4 + 0.3',
         'cd': '0.3 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/sven.png'
    },

    19: {'name': 'Tiny',
         'role': 'Disabler, Nuker, Initiator, Durable',
         'class': 'Strength',
         'radiant': 'true',
         'bio': '<strong>Tiny</strong> the <strong>Stone Giant</strong> is a melee Strength hero with powerful ganking '
                'and killing '
                'potential. Although he starts off vulnerable in lane with his pitiful mana pool and almost '
                'non-existent armor, with a few levels, he gets considerably stronger. His killing power in the '
                'early and midgame comes from comboing his two active abilities. Avalanche engulfs an area in a '
                'wave of stones, dealing respectable damage and stunning enemies. Toss allows Tiny to pick up a '
                'random unit near himself and launch it at the designated location, dealing damage to all enemies '
                'at the location as well as additional damage to the thrown unit if an enemy. It can be used to '
                'displace an ally within the enemy team, but is mostly used on enemies themselves to deliver '
                'massive damage. If chained immediately with Avalanche, it will also double the damage the target '
                'takes from Avalanche, allowing Tiny to easily dispatch fragile enemy heroes in a matter of seconds. '
                'Although his nuking potential with his two active abilities is already considerable, his passives, '
                'Craggy Exterior and Grow turn Tiny into a formidable physical combatant as well. Craggy Exterior '
                'provides Tiny with some much needed armor, and gives him a chance to stun enemies that attack him '
                'from too close, making Tiny a potent counter to fast-attacking melee heroes. Grow increases Tiny\'s '
                'size and provides him a massive boost to his attack damage, movespeed, and Toss damage, at the cost '
                'of some attack speed. Aghanim\'s Scepter is an almost essential item on Tiny since it allows him to '
                'permanently equip a tree, giving him extra attack range as well as a powerful cleaving attack. '
                'Although Tiny initially lives up to his name by starting off small and weak, much like an avalanche, '
                'he quickly grows in size and strength until he becomes a hulking behemoth with enormous health and '
                'damage output.',
         'quote': 'My enemies break upon me like surf upon the stone.',
         'strength': '24 + 3.0',
         'agility': '9 + 0.9',
         'intelligence': '14 + 1.6',
         'ms': '285',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.49 + 1',
         'cd': '0.001 + 0',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/tiny.png'
    },

    20: {'name': 'Vengeful Spirit',
         'role': 'Support, Disabler, Lane Support, Initiator',
         'radiant': 'true',
         'class': 'Agility',
         'bio': 'Shendelzare the Vengeful Spirit is a ranged Agility Hero excelling in ganks, disabling and kill '
                'hunts. She is one of the most potent supporters in the game and being item-independent, she serves as '
                'the team warder. Effective from early to late game, Vengeful Spirit is typically seen roaming the '
                'battlefield, searching for targets to prey on, hitting them with a powerful stun with Magic Missile '
                'and reducing their armor and scouting ahead with Wave of Terror. Motivated by her determined '
                'vengeance, her Vengeance Aura boosts her bonus attack damage not only for herself, but her allies as '
                'well. This makes her an ideal partner for physical gankers and carries, and what makes her a '
                'potential Carry herself. Her ultimate Nether Swap switches your position with another hero; ally or '
                'enemy. This allows Shendel to swap an enemy key hero making him/her vulnerable or sacrificing herself '
                'to save an important ally from death which may be essential to win a clash, or perhaps the entire '
                'game. Her unusual reliance on Agility (rather than Intelligence, like most supports) results in her '
                'offensive capabilities being remarkably high, at the cost of having a lower mana pool. She needs '
                'items perhaps less than any other hero in the game, and as such can be played with great '
                'recklessness, as her death is only a slight inconvenience. Shendel requires very selfless and '
                'skilled play to operate well, and relies on the competence of teammates as much as herself.',
         'quote': 'I will slake my thirst for revenge.',
         'strength': '18 + 2.6',
         'agility': '27 + 2.8',
         'intelligence': '15 + 1.75',
         'ms': '295',
         'tr': '0.6',
         'sr': '1800 / 800',
         'ar': '400',
         'miss_s': '1500',
         'ad': '0.33 + 0.64',
         'cd': '0.3 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/vengefulspirit.png'
    },

    21: {'name': 'Windranger',
         'role': 'Disabler, Nuker, Support, Escape',
         'radiant': 'true',
         'class': 'Intelligence',
         'bio': '<strong>Lyralei</strong> the <strong>Windranger</strong> is a ranged intelligence hero that uses '
                'powerful abilities in conjunction with her physical attack to take down enemies. Despite being an '
                'intelligence Hero, Windranger\'s playstyle resembles that of an agility Hero, due in large part to '
                'her skillset. Windranger is most often played as an offlane solo due to her escape, long range '
                'harass, and farm capability; however, she is quite versatile and can be fielded as a midlaner, '
                'roamer, lane support, or even a carry, if the game calls for it. She is famous for her immense '
                'utility and versatility, and as such, she is one of the most common picks of experienced players.',
         'quote': 'If at first you don\'t succeed, stand closer, shoot again.',
         'strength': '15 + 2.5',
         'agility': '17 + 1.4',
         'intelligence': '22 + 2.6',
         'ms': '295',
         'tr': '0.6',
         'sr': '1800 / 800',
         'ar': '600',
         'miss_s': '1250',
         'ad': '0.4 + 0.3',
         'cd': '0.3 + 0.5',
         'bat': '1.5',
         'avatar': 'img/dota/heroes/windrunner.png'
    },

    22: {'name': 'Zeus',
         'role': 'Nuker, Support',
         'radiant': 'true',
         'class': 'Intelligence',
         'bio': '<strong>Zeus</strong> the <strong>Lord of Heaven</strong> is a ranged intelligence Hero who functions '
                'almost solely as a nuker. He is usually played as a semi-carry ganker type hero, who instead of '
                'utilizing disables, focuses solely on delivering tremendous amounts of magical damage to his foes. '
                'With the high cast range and low cooldown on his spells, he is able to deliver the most superb and '
                'consistent magical damage of any hero in the game. Arc Lightning is a highly spammable nuke that '
                'creates a stream of lightning that bounces between enemy foes (up to fifteen times at max level), '
                'dealing minor damage. Lightning Bolt is more focused, dealing heavy damage to a single target, also '
                'on a very low cooldown. Static Field is a potent passive ability that allows Zeus\'s magical damage '
                'to scale into late game, dealing damage to all enemies within a decent AoE equal to a certain '
                'percentage of nearby targets\' health whenever he casts a spell. Finally, his ultimate Thundergod\'s '
                'Wrath allows him to strike all enemy heroes with a bolt of lightning, no matter their position, '
                'inflicting heavy damage. It can be used for multiple purposes: to finish off low-health enemy '
                'heroes limping away, to soften up the entire enemy team during a teamfight, or even to scout out the '
                'enemy\'s position. With the ability to strike down enemies both near and afar, the Lord of Heaven '
                'ensures that nobody can escape his wrath.',
         'quote': 'Immortality was overrated. This is much more interesting.',
         'strength': '19 + 2.3',
         'agility': '11 + 1.2',
         'intelligence': '20 + 2.7',
         'ms': '295',
         'tr': '0.6',
         'sr': '1800 / 800',
         'ar': '350',
         'miss_s': '1100',
         'ad': '0.633 + 0.366',
         'cd': '0.4 + 0.5',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/zuus.png'
    },

    23: {'name': 'Kunkka',
         'role': 'Disabler, Initiator, Carry, Durable',
         'radiant': 'true',
         'class': 'Strength',
         'bio': '<strong>Kunkka</strong> the <strong>Admiral</strong> is a versatile melee Strength hero built with an '
                'arsenal of powerful area-of-effect spells. Two of his active spells are nukes that have long reaction '
                'time, but can disable and disrupt the enemies\' position. He is mostly played as a carry or an '
                'initiator or even a spell nuker. He is known for his Tidebringer sword, which magically gives him '
                'the ability to cleave a large area around him on his attack with heavy potential damage on his next '
                'attack, which refreshes at a given period of time. Torrent calls upon the element of water to rise '
                'and burst out, dealing damage, disabling them up high, and slowing them on impact. There\'s a delay '
                'on this skill before it activates, so Kunkka must be wise in using this ability. X Marks the Spot '
                'targets any hero or Admiral himself to be marked on their current position, and after a few seconds '
                'delay, instantly returns to the marked spot. Useful in setting up tricky spells, escape prevention, '
                'or even saving allies, X Marks the Spot makes the Admiral a great battle strategist. His ultimate '
                'lets him summon a Ghost Ship, which travels on ground, until it crashes a set distance away, '
                'stunning and damaging enemy armies on that location. The Ghost Ship also bolsters allies with '
                'Kunkka\'s Rum, granting them bonus movement speed and numbness to damage. Ghost Ship is difficult '
                'to land, due to the fixed distance of its cast point and the crash site of the ship. However, a '
                'good Ghost Ship absolutely cripples an enemy team. Capable of inflicting high burst damage with his '
                'spells, controlling their position while able to survive the mayhem when his spells are used '
                'properly, Kunkka is a mighty offensive team fighter, built with strong physical and magical damage '
                'output, who can indeed turn the tide of a battle.',
         'quote': 'Step lively now, your Admiral is on board!',
         'strength': '24 + 3',
         'agility': '14 + 1.3',
         'intelligence': '18 + 1.5',
         'ms': '300',
         'tr': '0.6',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.4 + 0.3',
         'cd': '0.4 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/kunkka.png'
    },

    25: {'name': 'Lina',
         'role': 'Nuker, Disabler, Support',
         'radiant': 'true',
         'class': 'Intelligence',
         'bio': '<strong>Lina</strong> the <strong>Slayer</strong> is a ranged Intelligence hero, adept at destroying '
                'enemy heroes fast and delivering massive bursts of magical damage, making her one of the most '
                'effective gankers in the game. She possesses immense damaging capabilities all throughout the game, '
                'but is very fragile. Two of her fiery spells are her main source of damage, Dragon Slave sends a wave '
                'of fire to burn enemies in her path while Light Strike Array stuns them with a concentrated pillar '
                'of solar flame. Each of her spells deals great damage early on and has a low cooldown. Her Fiery Soul '
                'bolsters her attack and movement speed exponentially every time she casts a spell, which gives her '
                'scaling damage for the later game. Laguna Blade, her ultimate, is her ace in the hole. Lina fires off '
                'a huge bolt of lightning at a single target, dealing colossal damage. Laguna Blade\'s damage is '
                'staggering in early-mid game, and late game is still enough to destroy frail enemy heroes. Dragon '
                'Slave, Light Strike Array, and Laguna Blade are incredible flaming nukes that can incinerate her '
                'target instantly, and Fiery Soul allows her to transition into a strong and fast physical attacker. '
                'Though her power falls from its peak late game, mana-boosting and damage-increasing items can be '
                'purchased to keep herself up, serving as the team\'s magical semi-carry, dishing out intense burning '
                'damage with her attacks and spells.',
         'quote': 'One little spark and before you know it, the whole world is burning.',
         'strength': '18 + 1.5',
         'agility': '16 + 1.5',
         'intelligence': '27 + 3.2',
         'ms': '295',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': '650',
         'miss_s': '900',
         'ad': '0.75 + 0.78',
         'cd': '0.45 + 1.08',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/lina.png'
    },

    26: {'name': 'Lion',
         'role': 'Disabler, Nuker, Lane Support, Support',
         'radiant': 'false',
         'class': 'Intelligence',
         'bio': '<strong>Lion</strong> the <strong>Demon Witch</strong> is a ranged intelligence hero who is adept at '
                'disabling and nuking his enemies, as well as being a strong lane support. Although his abilities do '
                'not scale into the lategame, his offensive power can destroy enemies during the early game and '
                'remain somewhat useful throughout the later game. Lion is famous for his outstanding ability combos, '
                'making him a solid and versatile choice in any team composition. He has the ability to drain mana '
                'from enemy heroes with his Mana Drain skill and his complement of disables makes him an effective '
                'team-fighter and support in any stage of the game.',
         'quote': 'I don\'t fear Hell; Hell fears me.',
         'strength': '16 + 1.7',
         'agility': '15 + 1.5',
         'intelligence': '22 + 3',
         'ms': '290',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': '600',
         'miss_s': '900',
         'ad': '0.43 + 0.74',
         'cd': '0.3 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/lion.png'
    },

    27: {'name': 'Shadow Shaman',
         'role': 'Pusher, Disabler, Nuker, Support',
         'radiant': 'true',
         'class': 'Intelligence',
         'bio': 'Rhasta the Shadow Shaman is a ranged intelligence Hero mostly used as a pusher and disabler, wielding '
                'abilities that make pushing lanes more efficient. He is also capable of disabling multiple enemy '
                'heroes, allowing him to initiate encounters as well. Though very supportive in nature, until the late '
                'game Rhasta is capable of killing lone enemy heroes with the use of his entire skillset; meaning he '
                'is more difficult to gank than most other supports. Playing Rhasta well requires good knowledge of '
                'target priority and timing; and some minor micromanagement. His peak is mid-game, but he can continue '
                'to wreak havoc on enemies all throughout the match.',
         'quote': 'I am the intermediary between life and death.',
         'strength': '19 + 1.6',
         'agility': '16 + 1.6',
         'intelligence': '21 + 3',
         'ms': '285',
         'tr': '0.4',
         'sr': '1800 / 800',
         'ar': '500',
         'miss_s': '900',
         'ad': '0.3 + 0.5',
         'cd': '0.3 + 1.07',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/shadow_shaman.png'
    },

    28: {'name': 'Slardar',
         'role': 'Carry, Durable, Disabler, Initiator',
         'radiant': 'false',
         'class': 'Strength',
         'bio': 'Slardar the Slithereen Guard is a melee strength hero who uses brute force, low cooldown spells, and '
                'high physical strength to bring his enemies to their knees. He excels and thrives in close combat '
                'situations, and has high mobility, strong initiation and ganking abilities, and good synergy between '
                'his skills. Sprint greatly increases Slardar\'s movespeed for a lengthy duration, and allows him to '
                'chase down heroes and escape with ease. It does increase the damage Slardar takes, so it must be used '
                'with extreme caution. Sprint is used to get right next to enemies so Slardar can use Slithereen '
                'Crush, which delivers an area of effect stun to nearby enemies followed by a minor slow afterwards, '
                'all on a very low cooldown. This allows Slardar to take on multiple opponents simultaneously and '
                'deliver a potent initiation. Bash serves as a strong steroid, locking enemies in place while Slardar '
                'whacks at them with impunity. Finally, his ultimate Amplify Damage greatly reduces a target\'s armor '
                'and reveals him/her for the duration, making Slardar very potent against tanks and invisible heroes '
                'alike; it will also increase the damage dealt by his Crush and Bash. Although a strength hero, he '
                'has high physical damage output and an agility growth and armor value that rivals that of most '
                'agility heroes, allowing him to carry quite well if the situation calls for it. Chasing enemies '
                'relentlessly and pummeling them into the ground, Slardar is a fearsome opponent to be next to.',
         'quote': 'I guard what slumbers in the deeps.',
         'strength': '21 + 2.8',
         'agility': '17 + 2.4',
         'intelligence': '15 + 1.5',
         'ms': '300',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.36 + 0.64',
         'cd': '0.35 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/slardar.png'
    },

    29: {'name': 'Tidehunter',
         'role': 'Initiator, Durable, Disabler, Support',
         'radiant': 'false',
         'class': 'Strength',
         'bio': '<p><strong>Leviathan</strong> the <strong>Tidehunter</strong> is a melee strength hero who is '
                'formidable due to his uncommonly tough hide and his ocean spells that sweep enemies upward. He is a '
                'support hero whose greatest strengths lie in being able to take heavy amounts of damage in the early '
                'game and the disabling powers of his spells.</p><p>Though he does not deal especially high damage at '
                'any point in the game, his spells can have a devastating effect on the enemy without expending much '
                'mana. He is able to send forth a spray of water to slow down the enemy retreat and his outrageous '
                'ultimate, Ravage, throttles enemies in a massive area around him. The durability of his Kraken Shell '
                'allows him to shrug off damage for absurd survivability against low damage attacks. Tidehunter\'s '
                'ability to scrub off damage and his enormous strength gain makes him very durable, and the power of '
                'his spells means he is a tank the enemy very much needs to target.</p>',
         'quote': 'You can\'t hide from the tide.',
         'strength': '22 + 3',
         'agility': '15 + 1.5',
         'intelligence': '16 + 1.7',
         'ms': '310',
         'tr': '0.4',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.6 + 0.56',
         'cd': '0.3 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/tidehunter.png'
    },

    30: {'name': 'Witch Doctor',
         'role': 'Support, Disabler',
         'radiant': 'false',
         'class': 'Intelligence',
         'bio': '<strong>Zharvakko</strong> the <strong>Witch Doctor</strong> is a ranged intelligence Hero who can '
                'take on the role of a support or a ganker. A master of voodoo curses and healing arts, he possesses '
                'several positioning-dependant crowd control/damage spells as well as a heal that scales well into '
                'the late game. Maledict is one of the most powerful damaging spells in the game, and is fittingly '
                'enough quite hard to hit properly - but when applied at the right time, Malediction can curse someone '
                'to suffer a slow, humiliating death as they limp back towards safety.',
         'quote': 'Do no harm. Chaaah! What fun is that?',
         'strength': '16 + 1.8',
         'agility': '13 + 1.4',
         'intelligence': '24 + 2.9',
         'ms': '305',
         'tr': '0.4',
         'sr': '1800 / 800',
         'ar': '600',
         'miss_s': '1200',
         'ad': '0.4 + 0.5',
         'cd': '0.35 + 0.52',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/witch_doctor.png'
    },

    31: {'name': 'Lich',
         'role': 'Support, Lane Support, Nuker',
         'radiant': 'false',
         'class': 'Intelligence',
         'bio': 'Ethreain the Lich is a ranged intelligence Hero that uses his abilities to slow his enemies down with '
                'his ice-based attacks, as well as giving a boost to ally defenses, and serves as a great teamfight '
                'ganker with his powerful ultimate. He can use Sacrifice to easily level up and keep his mana high, '
                'making him very good at harassing in the early stages of the game. While a relatively frail hero and '
                'mostly known as a support, he can prove to be a force to be reckoned and mighty foe to stand with as '
                'he can render the attempts of multiple enemies futile with his ultimate, Chain Frost. Lich is a '
                'powerful crowd controller and can easily turn a teamfight, or dominate in a lane.',
         'quote': 'For the greater good-mine!',
         'strength': '18 + 1.55',
         'agility': '15 + 2',
         'intelligence': '18 + 3.25',
         'ms': '315',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': '550',
         'miss_s': '900',
         'ad': '0.46 + 0.54',
         'cd': '0.4 + 1.1',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/lich.png'
    },

    32: {'name': 'Riki',
         'role': 'Carry, Escape',
         'radiant': 'true',
         'class': 'Agility',
         'bio': '<strong>Riki</strong> the <strong>Stealth Assassin</strong> is a melee agility hero that uses stealth '
                'in order to surprise enemies and quickly kill them. His trademark ability, Permanent Invisibility, '
                'allows him to sneak into the shadows to hide and slip by without giving himself away. This allows '
                'him to close in on the enemy and drop his devastating Smoke Screen, which cripples fighter and '
                'spellcaster alike. Blink Strike allows Riki to chase with impunity, and Backstab makes running '
                'from him even more dangerous.',
         'quote': 'There are none so stabbed as those who will not see.',
         'strength': '17 + 2',
         'agility': '34 + 2.9',
         'intelligence': '14 + 1.3',
         'ms': '300',
         'tr': '0.6',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.3 + 0.3',
         'cd': '0.4 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/riki.png'
    },

    33: {'name': 'Enigma',
         'role': 'Disabler, Initiator, Jungler, Pusher',
         'radiant': 'false',
         'class': 'Intelligence',
         'bio': 'Enigma',
         'quote': 'Chaos hunts the spark of endless suns, whose light will die in my crushing grasp.',
         'strength': '17 + 2.1',
         'agility': '14 + 1',
         'intelligence': '20 + 3.4',
         'ms': '300',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': '500',
         'miss_s': '900',
         'ad': '0.4 + 0.77',
         'cd': '0.3 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/enigma.png'
    },

    34: {'name': 'Tinker',
         'role': 'Nuker, Pusher',
         'radiant': 'true',
         'class': 'Intelligence',
         'bio': 'Boush the Tinker is a ranged intelligence Hero who relies heavily on his assortment of nukes for '
                'ganking and pushing. He is able to reset the cooldown on his abilities, which in conjunction with '
                'Boots of Travel gives Tinker global mobility rivaled only by Nature\'s Prophet, making him a constant '
                'threat. His abilities\' mana costs are very high, so he must constantly use his ultimate, Rearm, and '
                'Boots of Travel to go back to base to heal. Tinker must acquire Boots of Travel, they are not '
                'optional; and if he acquires them early with a level advantage he will make short work of the enemy. '
                'Tinker is also the only hero in the game with two abilities that can be upgraded with an '
                'Aghanim\'s Scepter.',
         'quote': 'You can keep your magic, I have laser beams!',
         'strength': '17 + 2',
         'agility': '13 + 1.2',
         'intelligence': '27 + 2.2',
         'ms': '305',
         'tr': '0.6',
         'sr': '1800 / 800',
         'ar': '500',
         'miss_s': '900',
         'ad': '0.35 + 0.65',
         'cd': '0.53 + 0.5',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/tinker.png'
    },

    35: {'name': 'Sniper',
         'role': 'Carry',
         'class': 'Agility',
         'radiant': 'true',
         'bio': '<strong>Kardel Sharpeye</strong> the <strong>Sniper</strong> is a ranged agility hard carry who '
                'excels at dealing heavy damage at an incredible range. His third ability, Take Aim, allows him '
                'to deal high DPS at a safe distance, and avoiding damage as he is relatively frail. He also excels '
                'at harassing enemies due to his second ability, Headshot, which gives him a chance to do extra '
                'damage and mini-stun, and his first ability, Shrapnel, which slows and deals damage over time '
                'in an area. While he can be a nuisance to lane against, he is also extremely squishy early-game '
                'and requires supports to lane effectively. He scales extremely hard into the late game, dealing '
                'a remarkable amount of dps while sitting outside of harm\'s reach, almost permastunning heroes '
                'with his headshot. Though he is a rather frail hero, his potential in the hands of a good player '
                'and team is high.',
         'quote': 'Killing is the last resort, true. But the other resorts don\'t even have a pool.',
         'strength': '16 + 1.7',
         'agility': '21 + 2.9',
         'intelligence': '15 + 2.6',
         'ms': '290',
         'tr': '0.6',
         'sr': '1800 / 1000',
         'ar': '550',
         'miss_s': '3000',
         'ad': '0.17 + 0.7',
         'cd': '0.3 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/sniper.png'
    },

    36: {'name': 'Necrophos',
         'role': 'Support, Durable, Carry',
         'radiant': 'false',
         'class': 'Intelligence',
         'bio': 'Rotund\'jere the Necrophos is a ranged intelligence hero who typically plays as a mid-game carry. His '
                'skills are most effective in team fights where he can damage enemies and heal allies simultaneously, '
                'while picking off key enemy heroes with his ultimate. Necrophos is most dangerous when his enemy is '
                'severely injured, instantly killing them with his ultimate while recovering over time after killing '
                'his foe. Necrophos is naturally fragile, but his mechanics require him to stay in the midst of '
                'encounters; it is for this reason that he depends on items to prevent his death. Ideally, by casting '
                'Death Pulse repeatedly, he and his team are able to stay alive while the enemy team\'s health is '
                'gradually sapped by Heartstopper Aura, which reduces enemy HP by a small percentage each second. '
                'Because his abilities are suited to prolonged encounters, he must build items which allow him to '
                'survive for as long as possible against his enemies. His ultimate, Reaper\'s Scythe, has its damage '
                'increased by how much of their maximum HP the target is missing; meaning that an enemy that is close '
                'to death will be killed outright by it. Upon attaining a kill, Sadist restores Necrophos\'s mana and '
                'HP over a short time, allowing him to continue fulfilling his role in encounters. Necrophos is best '
                'understood as a hero who is weak at the beginning of a fight but becomes more dangerous with each '
                'passing second.',
         'quote': 'Rot starts at the head.',
         'strength': '1.6 + 2.0',
         'agility': '15 + 1.7',
         'intelligence': '22 + 2.5',
         'ms': '290',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': '550',
         'miss_s': '900',
         'ad': '0.53 + 0.77',
         'cd': '0.7 + 0.8',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/necrolyte.png'
    },

    37: {'name': 'Warlock',
         'role': 'Initiator, Support, Lane Support, Disabler',
         'radiant': 'false',
         'class': 'Intelligence',
         'bio': '<strong>Demnok Lannik</strong> the <strong>Warlock</strong> is a ranged intelligence hero and a good '
                'support. His Shadow Word ability makes for an excellent heal as well as a decent harassment tool, '
                'and his physical attack helps him to ward off any enemies and keep his friends safe. He also '
                'possesses a considerable presence in team fights, as Fatal Bonds spreads damage dealt by his allies '
                'to all enemies affected by it and his Upheaval is a channelled Area of Effect spell that slows foes '
                'caught in it by up to 84%. His ultimate, Chaotic Offering allows him to summon a massive Golem to do '
                'his bidding, stunning anyone caught in a large area when it is summoned.',
         'quote': 'Chaos comes at my command!',
         'strength': '18 + 2.5',
         'agility': '10 + 1',
         'intelligence': '24 + 2.7',
         'ms': '295',
         'tr': '0.4',
         'sr': '1800 / 800',
         'ar': '600',
         'miss_s': '1200',
         'ad': '0.3 + 0.3',
         'cd': '0.5 + 0.5',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/warlock.png'
    },


    38: {'name': 'Beastmaster',
         'role': 'Initiator, Disabler, Durable',
         'radiant': 'true',
         'class': 'Strength',
         'bio': 'Karroch the Beastmaster is a melee strength hero whose unique power takes the form of summons with '
                'exaggerated unit utility. His thralls provide extreme amounts of sight and have ability to reduce the '
                'attackspeed of targeted units. In addition, he has the longest lasting single reliable stun in the '
                'game. He is an effective support with good disabling ability in team fights. His strengths lie '
                'primarily in the slow debuff his Boar inflicts and ability to easily provide vision at crucial '
                'locations on the map. His ultimate, the stunning Primal Roar and Wild Axes allow him to deal massive '
                'damage at a distance. Though he is able to easily take down undefended targets in the early game, '
                'most of his abilities do not directly combo with each other, although the debiliating effects he '
                'brings to a fight can greatly assist allies (along with his passive attack speed boost aura).',
         'quote': 'I run with the rabbit and hunt with the hounds.',
         'strength': '23 + 2.2',
         'agility': '18 + 1.6',
         'intelligence': '16 + 1.9',
         'ms': '310',
         'tr': '0.4',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.3 + 0.7',
         'cd': '0.5 + 0.5',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/beastmaster.png'
    },

    39: {'name': 'Queen of Pain',
         'role': 'Nuker, Escape, Carry',
         'radiant': 'false',
         'class': 'Intelligence',
         'bio': '<strong>Akasha</strong> the <strong>Queen of Pain</strong> is a ranged intelligence hero who uses her '
                'abilities to close in and deal huge area damage to the enemy. She is typically played as a ganker '
                'with her ability to appear in battle and deal damage in quick succession, as well as hunt down '
                'fleeing heroes with ease. Her Blink ability is the lynchpin of her skillset, allowing her to enter '
                'and leave fights at her whim. Once in position to attack, Akasha can unleash her Scream of Pain and '
                'Sonic Wave, able to devastate an entire team at once. Chasing down straggling prey is another of her '
                'fortes, with Shadow Strike crippling their ability to escape. Akasha is very adept at getting kills '
                'early in the game, and transitions very well into a semi-carry if she acquires the proper items.',
         'quote': 'They say pain is all in the mind, but they\'re wrong: It\'s all in my hands.',
         'strength': '16 + 1.7',
         'agility': '18 + 2',
         'intelligence': '24 + 2.5',
         'ms': '300',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': '550',
         'miss_s': '1500',
         'ad': '0.56 + 0.41',
         'cd': '0.452 + 1.008',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/queenofpain.png'
    },

    40: {'name': 'Venomancer',
         'role': 'Support, Nuker, Initiator, Pusher',
         'radiant': 'false',
         'class': 'Agility',
         'bio': '<strong>Lesale Deathbringer</strong> the <strong>Venomancer</strong> is a ranged agility hero who is '
                'focused on dealing damage over time and slowing enemies down. He is not granted with a big amount of '
                'base attack and attribute gain, but he can bring enormous area damage with his poisonous abilities. '
                'Venomancer can unleash a Venomous Gale to enemies in a straight line, infecting them, damaging and '
                'slowing them over time. His attacks are hazardous thanks to his lethal Poison Sting, which adds a '
                'toxic effect to his normal attacks, poisoning opposing Heroes for a duration. Plague Ward, his next '
                'ability, lets him summon a sentient ward to a targeted point, which attacks enemies or structures. '
                'While weak on first use its power grows in numbers, which means the more the wards are placed the '
                'deadlier they become. This gives him good versatility, providing vision, pushing power, and a helpful '
                'block, preventing enemies from running away when trapped in a sticky situation. Venomancer\'s most '
                'dangerous ability is Poison Nova, though it isn\'t lethal and won\'t kill an enemy, the damage it '
                'inflicts is tremendous, the duration is very long, and it affects an area around him. It is mostly '
                'used to initiate battles, since Poison Nova isn\'t a killing type spell. When used altogether, the '
                'Venomancer is a powerful killing machine, like a virus, slowly killing enemies with venom and '
                'poisons. Despite being considered by most players as a support, because of his slowing capabilities, '
                'extra ward vision, and being item independent, this doesn\'t hinder his power to gank and kill '
                'enemies, especially in the earliest parts of the game, and with enough kills, farm, and domination, '
                'Venomancer can transition into a semi-carry, with formidable venomous power and deadly specialties.',
         'quote': 'No necromancer shall raise what the venomancer puts down.',
         'strength': '18 + 1.85',
         'agility': '22 + 2.6',
         'intelligence': '15 + 1.75',
         'ms': '285',
         'tr': '0.4',
         'sr': '1800 / 800',
         'ar': '450',
         'miss_s': '900',
         'ad': '0.3 + 0.7',
         'cd': '0 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/venomancer.png'
    },


    41: {'name': 'Faceless Void',
         'role': 'Carry, Initiator, Disabler, Escape',
         'class': 'Agility',
         'radiant': 'false',
         'bio': '<strong>Darkterror</strong> the <strong>Faceless Void</strong> is a melee agility hard carry hero. '
                'Given a little time, he becomes a terrifyingly powerful hero capable of destroying entire enemy '
                'teams. Wielding his cosmically powered mace, each hit can lock his foes in time, stopping them '
                'in place. He can jump into or out of combat using Time Walk, and passively can avoid any damage '
                'with Backtrack which even works against Monkey King Bar. His ultimate, Chronosphere, locks time '
                'for everything within its area of effect, giving him time to strike down any enemies caught within '
                'with near impunity for several seconds. Faceless Void is a hard carry and, as such, scales heavily '
                'from items and reaches his full potential in late game, growing into one of the most powerful and '
                'destructive Heroes.',
         'quote': 'From a place beyond time, and time beyond counting.',
         'strength': '23 + 1.6',
         'agility': '21 + 2.65',
         'intelligence': '15 + 1.5',
         'ms': '300',
         'tr':'0.5',
         'sr':'1800 / 800',
         'ar':'Melee',
         'miss_s':'Instant',
         'ad':'0.5 + 0.56',
         'cd':'0.35 + 0.51',
         'bat':'1.7',
         'avatar': 'img/dota/heroes/faceless_void.png'
    },

    42: {'name': 'Wraith King',
         'role': 'Durable, Carry, Disabler',
         'radiant': 'false',
         'class': 'Strength',
         'bio': '<strong>Ostarion</strong> the <strong>Wraith King</strong> is a melee strength hero, a carry and tank '
                'capable of both dealing and taking plenty of damage. His infamous Reincarnation allows the Wraith '
                'King to rise again after death, acting like an Aegis of the Immortal, making him especially difficult '
                'to kill. But if left alive, the Wraith King can wreak havoc upon his enemies; his Wraithfire Blast '
                'provides reliable damage and a stun on a short cooldown, Vampiric Aura grants his team sizeable '
                'lifesteal, and Mortal Strike helps make short work of foes.',
         'quote': 'Purer than flesh, stronger than bone, imperishable is the essence of the wraith.',
         'strength': '22 + 2.9',
         'agility': '18 + 1.7',
         'intelligence': '18 + 1.6',
         'ms': '300',
         'tr': '0.4',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.56 + 0.44',
         'cd': '0.35 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/wraith_king.png'
    },

    43: {'name': 'Death Prophet',
         'role': 'Pusher, Nuker, Durable',
         'radiant': 'false',
         'class': 'Intelligence',
         'bio': 'Krobelus the Death Prophet is a ranged intelligence Hero who excels at pushing lanes. Like other '
                'casters, her abilities allow her to be less item dependent during the early game. As she learns '
                'Exorcism, Death Prophet can deal a huge amount of damage to towers and lone heroes alike, while '
                'healing at the end of the duration. Despite being a caster, Death Prophet has a relatively high '
                'Strength compared to other intelligence Heroes and she is mostly built as a tank. Her passive '
                'ability, Witchcraft, both grants her bonus movement speed and an increase her other abilities '
                'effectiveness, making her a formidable ganker as well.',
         'quote': 'What I\'ve seen goes far beyond death.',
         'strength': '19 + 2.2',
         'agility': '14 + 1.4',
         'intelligence': '20 + 3',
         'ms': '280',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': '600',
         'miss_s': '1000',
         'ad': '0.56 + 0.51',
         'cd': '0.5 + 0.83',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/death_prophet.png'
    },

    44: {'name': 'Phantom Assassin',
         'role': 'Carry, Escape',
         'radiant': 'false',
         'class': 'Agility',
         'bio': '<strong>Mortred</strong> the <strong>Phantom Assassin</strong> is a melee agility Hero fitting the '
                'role of hard carry. Mortred is best-known, and infamous for, her ability to inflict staggering '
                'damage with single strikes. Her abilities synergise supremely well with each other, rendering her '
                'an extremely formidable foe once she has acquired the items she requires. She is a very '
                'farm-dependent melee Hero, but she farms creeps with much more ease than many of her fellow '
                'carries, using her Stifling Dagger for last hitting. Besides eliminating the weakness most melee '
                'Heroes have in their farming, it also saves her from expending gold on important melee carry '
                'items like Quelling Blade. Her second ability, Phantom Strike, acts as both her escape and '
                'initiate, while Blur gives her an edge against other Heroes that depend on their physical attacks '
                'by evading them; giving her partial damage immunity to many carries. Her ultimate, the strongest '
                'critical strike in the game, is what connects Mortred with four-digit damage and what gives her a '
                'place amongst the very best support killers in the late game, since they usually fall instantly '
                'from the divine strike her ultimate provides.',
         'quote': 'I\'m here to blur the line between life and death.',
         'strength': '20 + 1.85',
         'agility': '23 + 3.15',
         'intelligence': '13 + 1',
         'ms': '310',
         'tr': '0.4',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.3 + 0.7',
         'cd': '0.3 + 0.5',
         'bat': '0.7',
         'avatar': 'img/dota/heroes/phantom_assassin.png'
    },

    45: {'name': 'Pugna',
         'role': 'Nuker, Pusher, Support',
         'radiant': 'false',
         'class': 'Intelligence',
         'bio': 'Pugna the Oblivion is a ranged Intelligence Hero who possesses powerful abilities which give him '
                'great versatility and offensive capabilities. He has a high base Movement Speed and also has the '
                'highest Intelligence gain per level in the game. Nether Blast is an AOE nuke which also deals damage '
                'to buildings, giving Pugna good pushing capabilities and teamfighting presence. Decrepify can disable '
                'enemy carries or save allies from physical attacks, while amplifying magical damage done to the '
                'target. Nether Ward is an excellent teamfight ability which deals damage to enemies based on the '
                'manacost of abilities, making Pugna a counter to casters. Pugna\'s ultimate ability, Life Drain, is a '
                'channeling ability which saps enemy health and grants it to himself, somewhat making up for his low '
                'durability.',
         'quote': 'Who needs a blade when you have oblivion?',
         'strength': '17 + 1.2',
         'agility': '16 + 1',
         'intelligence': '26 + 4',
         'ms': '320',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': '600',
         'miss_s': '900',
         'ad': '0.5 + 0.5',
         'cd': '0.2 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/pugna.png'
    },

    46: {'name': 'Templar Assassin',
         'role': 'Carry, Escape',
         'radiant': 'true',
         'class': 'Agility',
         'bio': '<p><strong>Lanaya</strong> the <strong>Templar Assassin</strong> is a short-ranged Agility hero '
                'capable of dealing huge bursts of Physical damage to swathes of enemies with expert positioning and '
                'timing. Unlike most physical damage dealers, Lanaya reaches her damage potential quite early and then '
                'scales up from that point with carry items, letting her gank with impunity throughout the '
                'mid-game, and her range changes from a melee hero to a ranged hero with short reach as '
                'she levels Psi Blades.</p><p>Her Psionic Traps provide map control and the ability to chase down '
                'fleeing heroes from up to 2000 range, and Refraction and Meld lets you shrug off high-damage nukes '
                'and disjoint projectiles. With a Blink Dagger, Lanaya can quickly materialize in the enemy team\'s '
                'weakest flank and shred several heroes at once with her Meld and Psi Blades.</p>',
         'quote': 'My body is a temple for which I will kill.',
         'strength': '18 + 2.1',
         'agility': '23 + 2.7',
         'intelligence': '20 + 2',
         'ms': '305',
         'tr': '0.7',
         'sr': '1800 / 800',
         'ar': '140',
         'miss_s': '900',
         'ad': '0.3 + 0.5',
         'cd': '0.3 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/templar_assassin.png',
    },

    47: {'name': 'Viper',
         'role': 'Carry, Durable',
         'radiant': 'false',
         'class': 'Agility',
         'bio': '<strong>Viper</strong> the <strong>Netherdrake</strong> is a ranged agility Hero who can function as '
                'an excellent ganker and carry due to his slowing auto-attacks and his low cooldown ultimate. Although '
                'ganking is often made easier with Viper\'s presence, his true carry potential is revealed with sheer '
                'item power. Farming with Viper is relatively easy; while he has no area of effect abilities to clear '
                'waves, Nethertoxin makes last-hitting a cinch. However, active participation in ganking is very '
                'important before his ganking power wears out in mid-late game, due to enemy heroes playing more '
                'cautiously and obtaining better items. Poison Attack makes Viper very potent in hero harassing.',
         'quote': 'None forget the bite of Viper.',
         'strength': '20 + 1.9',
         'agility': '21 + 2.5',
         'intelligence': '15 + 1.8',
         'ms': '285',
         'tr': '0.4',
         'sr': '1800 / 800',
         'ar': '575',
         'miss_s': '1200',
         'ad': '0.33 + 1',
         'cd': '0.3 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/viper.png'
    },

    48: {'name': 'Luna',
         'role': 'Carry, Nuker',
         'radiant': 'true',
         'class': 'Agility',
         'bio': '<strong>Luna</strong> the <strong>Moon Rider</strong> is a Ranged Agility carry hero. Even though '
                'she can be seen as a tempting target for enemy heroes, Luna possesses solid early game laning '
                'presence due to her Lucent Beams, a cheap, low-cooldown nuke, and her Lunar Blessing aura, which '
                'grants all nearby allied heroes increased damage. In mid-game, she becomes far more formidable with '
                'Moon Glaives, allowing her to kill entire creep waves with two to three attacks, and Eclipse, which '
                'can instantly kill a hero if that hero is unfortunate to catch its full blast. Luna is a very common '
                'pick in professional matches; owing to her unique status as a hard carry who is also a dangerous '
                'nuker. Her Achilles\' Heel is her fragility; she has no escape abilities and cannot handle a lot of '
                'punishment, relying on her enormous movement speed to keep her out of harm\'s way. Luna begins and '
                'ends a match dangerous, and if carefully and skilfully played will destroy '
                'anybody who stands against her.',
         'quote': 'I would water the trees with their entrails if Selemene would smile on me.',
         'strength': '15 + 1.9',
         'agility': '22 + 2.8',
         'intelligence': '16 + 1.85',
         'ms': '330',
         'tr': '0.4',
         'sr': '1800 / 800',
         'ar': '330',
         'miss_s': '900',
         'ad': '0.46 + 0.54',
         'cd': '0.6 + 0.4',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/luna.png'
    },

    49: {'name': 'Dragon Knight',
         'role': 'Carry, Durable, Disabler, Pusher',
         'radiant': 'true',
         'class': 'Strength',
         'bio': 'Davion the Dragon Knight is a very tough melee strength hero with a relatively versatile skill set. '
                'Dragon Knight has a nuke and a stun, giving him an advantage in ganks. Dragon Knight has no real '
                'escape ability, though his Dragon Blood ability and armor make him capable of withstanding strong '
                'hits and recovering quickly. He is still very vulnerable in the early game, however, and needs to '
                'farm and stay alive in order to be effective in later stages. If he has enough levels and farm, '
                'Dragon Knight is very formidable late game due to his strong ultimate, transforming into a '
                'legendary dragon, turning him into one of the most dangerous beasts in late game, capable of '
                'eliminating multiple enemies at once.',
         'quote': 'The Dragon Slyrak sleeps within this armor, and the knight within the Dragon waits. Beware you do '
                  'not wake them both.',
         'strength': '19 + 2.8',
         'agility': '19 + 2.2',
         'intelligence': '15 + 1.7',
         'ms': '290',
         'tr': '0.6',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.5 + 0.5',
         'cd': '0 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/dragon_knight.png'},

    50: {'name': 'Dazzle',
         'role': 'Support, Lane Support',
         'radiant': 'false',
         'class': 'Intelligence',
         'bio': '<strong>Dazzle</strong> the <strong>Shadow Priest</strong> is a ranged intelligence Hero exhibiting '
                'abilities that bend the sustainability of both his allies and enemies, making him a viable support. '
                'While frail, he is capable of keeping his allies and himself from dying, causing his foes to waste '
                'time in a fruitless endeavor. Similarly to Slardar, Dazzle boasts abilities that deal physical '
                'damage instead of the usual magical. His first ability, Poison Touch, is a strong spammable '
                'disable, though mediocre in effects in the first levels. Out of all his abilities, Poison Touch '
                'is the only one that cannot pass through Magic immunity, will it sustain itself when magic immunity '
                'is granted after the buff is placed. Shallow Grave is a solid survivability spell, allowing your '
                'allied targets to escape during serious encounters. Though it only prevents fatal damage, it cannot '
                'be purged, making it a full guarantee that Dazzle\'s target will survive for the duration. Shadow '
                'Wave is a chaining healing ability that dissipates the health gained to damage nearby enemies, '
                'having a potential of delivering a huge damage output when good positioning comes to play. His '
                'ultimate, Weave, is a large armor bending ability that not only increases his allies\' armor, but '
                'also decreases his enemies. With the fact that his abilities deal physical damage and that Dazzle '
                'himself has large attack damage, the chaotic combination with armor reduction really makes '
                'Dazzle a devastating Hero to go against.',
         'quote': 'Where my shadow falls, there falls my foe.',
         'strength': '16 + 1.85',
         'agility': '21 + 1.7',
         'intelligence': '27 + 3.4',
         'ms': '305',
         'tr': '0.6',
         'sr': '1800 / 800',
         'ar': '500',
         'miss_s': '1200',
         'ad': '0.3 + 0.3',
         'cd': '0.3 + 0.5',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/dazzle.png'
    },

    51: {'name': 'Clockwerk',
         'role': 'Initiator, Durable',
         'radiant': 'true',
         'class': 'Strength',
         'bio': '<strong>Rattletrap</strong> the <strong>Clockwerk</strong> is a melee strength hero commonly played '
                'as an initiator or ganker. As an initiator, his main purpose is crowd control. However, he also does '
                'secondary jobs such as chasing and map control. His abilities are centered around isolating and '
                'killing enemies one by one. He does not deal reliable area damage like most initiators, but still he '
                'is capable of doing a surprising and devastating entrance. Usually Clockwerk players should initiate '
                'onto low health support heroes or enemy heroes with strong team fight ability, such as Warlock, '
                'hampering their ability to land solid teamfight spells. Clockwerk can also initiate onto enemy carry '
                'heroes, in order to isolate them away from the team fight by forcing them to remain in cogs.',
         'quote': 'A good offense is the best armor. Good armor is also good armor.',
         'strength': '24 + 2.7',
         'agility': '13 + 2.3',
         'intelligence': '17 + 1.3',
         'ms': '315',
         'tr': '0.6',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.33 + 0.64',
         'cd': '0.3 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/rattletrap.png'
    },

    52: {'name': 'Leshrac',
         'role': 'Nuker, Pusher, Disabler, Support',
         'radiant': 'false',
         'class': 'Intelligence',
         'bio': 'Leshrac the Tormented Soul is an intelligence hero who is known for his massively damaging spells. '
                'He can easily destroy Creeps and Towers with his abilities, which deal damage at the expense of Mana. '
                'His power is balanced by his lack of an escape mechanism, while his only disable, Split Earth, '
                'takes time to cast and needs good planning to land successfully. Without expert positioning and '
                'powerful items, Leshrac is an easy target for physical attackers late-game, but he can easily hamper '
                'those same enemies by destroying towers and dealing damage in the midgame. If Leshrac is encountered '
                'outside the lanes early on, there are very few opponents who can stand against the power of Diabolic '
                'Edict and live.',
         'quote': 'An end to it all is all I desire, that I might learn what worse mysteries the Impurities veil.',
         'strength': '16 + 1.5',
         'agility': '23 + 1.7',
         'intelligence': '26 + 3',
         'ms': '315',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': '600',
         'miss_s': '900',
         'ad': '0.4 + 0.77',
         'cd': '0.7 + 0.8',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/leshrac.png'
    },

    53: {'name': 'Nature\'s Prophet',
         'class': 'Intelligence',
         'role': 'Jungler, Pusher, Carry, Escape',
         'radiant': 'true',
         'bio': '<strong>Nature\'s Prophet</strong> is a ranged Intelligence hero, whose play style is removed '
                'from most Intelligence heroes, because he can be almost anywhere at any given time with his '
                'Teleportation. This ability allows him participate in most ganks and pushes at a moment\'s '
                'notice. With Sprout, he creates a ring of trees, trapping anyone within them in place, serving '
                'to disable anyone caught within them. The trees around him serve as his objects of power; using '
                'them, he summons sentient tree beings known as Treants from trees on the map with his Nature\'s '
                'Call ability. Wrath of Nature is his main and only directly damaging spell in his arsenal, '
                'but it can potentially be very powerful, as it can inflict increased damage with each bounce '
                'off subsequent enemies and can clear out multiple creep waves with its moderate cooldown and '
                'mana cost. Commonly played as a ganker, offlaner and jungler and known as a strong pusher, '
                'Nature\'s Prophet has superb farming capabilities and global presence, giving him the power '
                'to be anywhere on the map and aid his allies in need.',
         'quote': 'I woke within the seed and saw my destiny, and many were its branches.',
         'strength': '19 + 1.8',
         'agility': '18 + 1.9',
         'intelligence': '21 + 2.9',
         'ms': '295',
         'tr': '0.6',
         'sr': '1800 / 800',
         'ar': '600',
         'miss_s': '1125',
         'ad': '0.4 + 0.77',
         'cd': '0.5 + 1.17',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/furion.png'
    },

    54: {'name': 'Lifestealer',
         'role': 'Carry, Durable, Jungler, Escape',
         'radiant': 'false',
         'class': 'Strength',
         'bio': '<strong>N\'aix</strong> the <strong>Lifestealer</strong> is a vicious melee Strength hero whose '
                'abilities give him the power to bring down durable heroes quickly, while sustaining his health '
                'from absorbing the very life of his enemies. The main role of the Lifestealer is to fulfill the '
                'job as a formidable carry, able to restore his life thanks to his skills. Feast is his passive '
                'ability and his signature, every attack he lands deals extra physical damage and consumes the flesh '
                'and blood of his victim, regenerating his health. With Feast, he can munch down tough and strong '
                'tanks. N\'aix can send himself into a bloody Rage, increasing his attack speed and a short period '
                'of magic immunity. Open Wounds tears the enemy, causing the prey\'s wounds to open, bleeding their '
                'life essence, allowing him and his allies to feast down as well as greatly slowing them to a crawl. '
                'Rage and Open Wounds allows the Lifestealer to brutally rip his victim apart, feasting on their '
                'health in the process. When in need, N\'aix can use Infest to hide himself inside of his allies '
                'or any non-hero units, laying dormant, until he is ready to come out, devouring the flesh from '
                'the inside, killing the non-hero unit, and bursting out the chunks of flesh and bones of his '
                'unfortunate host, damaging his foes around him, and ambushing them with carnivorous savagery. '
                'The Lifestealer is a monstrous beast of gluttony and greed, bent on stealing the lives of every '
                'living creature he encounters, violently killing them to sate the Lifestealer\'s terrifying thirst '
                'and hunger.',
         'quote': 'Oh Master, behold all these lives for the taking!',
         'strength': '25 + 2.4',
         'agility': '18 + 1.9',
         'intelligence': '15 + 1.75',
         'ms': '315',
         'tr': '1.0',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.39 + 0.44',
         'cd': '0.2 + 0.01',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/life_stealer.png'
    },

    55: {'name': 'Dark Seer',
         'role': 'Initiator, Nuker, Escape',
         'radiant': 'false',
         'class': 'Intelligence',
         'bio': 'Ish\'kafel the Dark Seer is a melee intelligence hero with versatile abilities that allow him to '
                'assist allies and greatly change the conditions of combat. His Vacuum in particular affects enemies '
                'in a large area and is a powerful crowd-control. It not only disorients and damages enemies, but '
                'also pushes them into a small area to follow up with area spells or to trigger other abilities, such '
                'as his Wall of Replica ultimate that turns the very power of enemies against them in the form of '
                'illusions that replicate their statistics. His other spells focus on buffing allies with speed, or '
                'in the case of his Ion Shell, granting an aura that radiates damage onto enemies who venture '
                'within it.',
         'quote': 'If your enemy is equal, prepare for him. If greater, elude him. If weaker, crush him.',
         'strength': '22 + 2.3',
         'agility': '12 + 1.2',
         'intelligence': '29 + 2.7',
         'ms': '300',
         'tr': '0.6',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.59 + 0.58',
         'cd': '0.4 + 0.67',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/dark_seer.png'
    },

    56: {'name': 'Clinkz',
         'role': 'Carry, Escape',
         'radiant': 'false',
         'class': 'Agility',
         'bio': '<strong>Clinkz</strong> the <strong>Bone Fletcher</strong> is a ranged agility carry specializing in '
                'ambushing lone Heroes with high physical damage and incredible speed. Though frail and easy to kill, '
                'Skeleton Walk grants Clinkz stealth and haste to escape and re-position himself. This assassin '
                'Strafes around the enemy, launching a flurry of Searing Arrows that greatly injure enemies. To aid '
                'his assault, Clinkz can form a Death Pact and absorb a creature\'s life for greater damage and '
                'health, making him not only able to take more hits, but hit harder as well.',
         'quote': 'An arrow says what words cannot.',
         'strength': '15 + 1.6',
         'agility': '22 + 3',
         'intelligence': '16 + 1.55',
         'ms': '300',
         'tr': '0.4',
         'sr': '1800 / 800',
         'ar': '600',
         'miss_s': '900',
         'ad': '0.7 + 0.3',
         'cd': '0.5 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/clinkz.png'
    },

    57: {'name': 'Omniknight',
         'role': 'Durable, Lane Support, Support',
         'radiant': 'true',
         'class': 'Strength',
         'bio': '<strong>Purist Thunderwrath</strong> the <strong>Omniknight</strong> is a versatile melee strength '
                'hero who can take on the role of a support or, occasionally, a semi-carry, depending on the player\'s '
                'play style. A holy and courageous Hero, Omniknight possesses abilities that excel at protecting and '
                'aiding friendly heroes. His heal doubles as a nuke and he can grant any friend Magic Immunity, as '
                'well as blessing allies with a physical invulnerability and regeneration. Few can escape the mighty '
                'and heavenly power of the Omniknight and he is a powerful ally in team fights. He is a mighty tank, '
                'and one of the most difficult heroes to kill.',
         'quote': 'I have gazed into the Omniscience, and it has gazed into me.',
         'strength': '20 + 2.65',
         'agility': '15 + 1.75',
         'intelligence': '17 + 1.8',
         'ms': '305',
         'tr': '0.6',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.433 + 0.567',
         'cd': '0.5 + 1.67',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/omniknight.png'},

    58: {'name': 'Enchantress',
         'role': 'Support, Pusher, Durable, Jungler',
         'radiant': 'true',
         'class': 'Intelligence',
         'bio': 'Aiushtha the Enchantress is a ranged intelligence Hero who uses her abilities to push through lanes '
                'and gank with relative ease. Enchantress works well as a jungler in the early game, as it maximizes '
                'the effectiveness of her Enchant and Untouchable abilities. On first glance, she may be just a '
                'support, serving her allies with powerful heals, creep abilities and slows, but as time goes on, '
                'her power increases and once she has her ultimate, Enchantress regular attacks are strong enough to '
                'kill most heroes with a couple of attacks, if they stand far enough, and make her a potential carry.',
         'quote': 'You know what I love? Everything!',
         'strength': '16 + 1',
         'agility': '19 + 1.8',
         'intelligence': '16 + 2.8',
         'ms': '310',
         'tr': '0.4',
         'sr': '1800 / 800',
         'ar': '550',
         'miss_s': '900',
         'ad': '0.3 + 0.7',
         'cd': '0.3 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/enchantress.png'
    },

    59: {'name': 'Huskar',
         'role': 'Carry, Initiator, Durable',
         'radiant': 'true',
         'class': 'Strength',
         'bio': 'Huskar the Sacred Warrior is a ranged Strength hero who is an effective ganker and carry, with both '
                'great benefits and risks offered. He is known to be a powerful adversary in most games, as his damage '
                'per second can easily kill other heroes at any point in the game assuming no one is near by to save '
                'them. Unlike most heroes, he doesn\'t use mana much to use his abilities, rather, he sacrifices his '
                'own health to inflict the highest damage possible. His passive Berserker\'s Blood defines the power '
                'of sacrifice; he gets more dangerous the more he gets hurt. This gives him increased magic resistance'
                'and attack speed depending how much life is missing, and the given magic resistance and attack speed '
                'are staggering, potentially having the highest damage output in the earliest stage. Huskar can use '
                'his own life force to attack using Burning Spears which scorches foes and gives him an advantage '
                'early on. Due to the health cost of Burning Spears, his Berserker\'s Blood sets on, granting him '
                'power to decimate any target. Inner Vitality magically heals Huskar after he is injured, regenerating '
                'health each second based upon its primary attribute, and heals more when the health is on a critical '
                'level. It can be used to heal allies as well. His Life Break is his most dangerous ability and a '
                'risky one too. Charging towards his target, Huskar sheds a large amount of life force to cut a '
                'target\'s current HP to fractions. This is great to use as an initiation spell, as it deals immense '
                'damage based on the target\'s current health, breaking it down, allowing Huskar and his allies to '
                'feel the pain that the Sacred Warrior felt. Courageous and fearless, Huskar is powerful at any stage '
                'of the game, and is willing to suffer and face death, for him to contribute and deliver a marvelous '
                'victory to his team.',
         'quote': 'Those who are given more in life must not cling to it but risk it all in every moment.',
         'strength': '21 + 2.4',
         'agility': '15 + 1.4',
         'intelligence': '18 + 1.5',
         'ms': '300',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': '400',
         'miss_s': '1400',
         'ad': '0.4 + 0.5',
         'cd': '0.3 + 2.4',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/huskar.png'},

    60: {'name': 'Night Stalker',
         'role': 'Durable, Initiator',
         'radiant': 'false',
         'class': 'Strength',
         'bio': '<strong>Balanar</strong> the <strong>Night Stalker</strong> is a unique melee Strength hero in that '
                'his skills are affected by the time of day during the game. During daytime, he is weaker than a hero '
                'of an equal level, especially in the early game. But once the sun goes down, Balanar\'s real power '
                'is unleashed, becoming the beast known as the Night Stalker. His Void damages and slows his target '
                'to a crawl as he pursues them. Crippling Fear prevents his enemy from attacking Balanar, silencing '
                'them and causing their attacks to miss, making him an effective counter against spellcasters and '
                'physical attackers. Hunter in the Night is what defines the Night Stalker. He becomes a brutal and '
                'merciless hunter during the night, with supernatural attack speed and movement speed, which allows '
                'Balanar to chase and savagely attack his victim. Darkness creates a period of darkness for the Night '
                'Stalker to enjoy and use his abilities to the fullest.',
         'quote': 'I feed the darkness and the darkness feeds me.',
         'strength': '23 + 2.8',
         'agility': '18 + 2.25',
         'intelligence': '16 + 1.6',
         'ms': '295',
         'tr': '0.5',
         'sr': '1200 / 1800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.55 + 0.55',
         'cd': '0.3 + 0.3',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/night_stalker.png'},

    61: {'name': 'Broodmother',
         'role': 'Pusher, Carry, Escape',
         'radiant': 'false',
         'class': 'Agility',
         'bio': 'Black Arachnia the Broodmother is a melee agility hero who is a notably powerful pusher. Her '
                'trademark spiderlings, as both an asset and a liability, define her play style. While a possible '
                'additional source of income, experience and lane pushes, spiderlings can easily feed opponents when '
                'not handled with deft micro and great awareness. Broodmother\'s abilities allow her to summon those '
                'spiderlings to do her bidding, to conceal herself and her spiderlings in an area, and to slow and '
                'kill heroes with relative ease if caught off guard, all while staying as elusive as possible with '
                'her webs and passives. She spends most of the early game pressuring a lane with little concern, due '
                'to her spiderlings and her invisibility/added HP regeneration, but she can also transition into a '
                'difficult to kill melee carry, which can dive in on and rapidly kill lone enemies with the right '
                'items later on.',
         'quote': 'I\'ve promised you to my children.',
         'strength': '17 + 2.5',
         'agility': '18 + 2.2',
         'intelligence': '18 + 2',
         'ms': '295',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s':'Instant',
         'ad': '0.4 + 0.5',
         'cd': '0.2 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/broodmother.png'
    },

    62: {'name': 'Bounty Hunter',
         'role': 'Carry, Escape, Nuker',
         'radiant': 'true',
         'class': 'Agility',
         'bio': '<strong>Gondar</strong> the <strong>Bounty Hunter</strong> is a melee agility Hero that excels in '
                'dealing high amounts of damage to single targets. Bounty Hunter can easily gank other lanes, using '
                'his Shadow Walk to sneak up on enemies and get easy kills. Shadow Walk also allows him to escape '
                'from dangerous situations, making him very elusive. Bounty Hunter can be played as a carry, though '
                'it is not recommended, as Bounty Hunter is also extremely deadly as an offlaner. thanks to Track, '
                'which will grant True Sight, movement speed, and bonus gold, allowing him and his team to farm and '
                'earn powerful items faster than other carries and Jinada which amplifies the damage of his next '
                'attack every few seconds.',
         'quote': 'For the right price, anything.',
         'ms': '315',
         'tr': '0.6',
         'sr': '1800 / 1000',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.59 + 0.59',
         'cd': '0.3 + 0.51',
         'bat': '1.7',
         'strength': '17 + 1.8',
         'agility': '21 + 3',
         'intelligence': '19 + 1.4',
         'avatar': 'img/dota/heroes/bounty_hunter.png'
    },

    63: {'name': 'Weaver',
         'role': 'Carry, Escape',
         'radiant': 'false',
         'class': 'Agility',
         'bio': 'Skitskurr the Weaver is a ranged agility hero, who isn\'t capable of being in the center of a battle, '
                'but can really annoy and harass his enemies in the lane. His abilities allow him to evade damage that '
                'would be dealt or was already dealt to him. Weaver is a carry who can surprise wounded foes running '
                'away from the battle, hunt them down and disappear, avoiding the focus of the enemy team.',
         'quote': 'The threads of fate are mine to weave.',
         'strength': '15 + 1.5',
         'agility': '14 + 2.5',
         'intelligence': '15 + 1.8',
         'ms': '290',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': '425',
         'miss_s': '900',
         'ad': '0.64 + 0.36',
         'cd': '0.3 + 0.51',
         'bat': '1.8',
         'avatar': 'img/dota/heroes/weaver.png'
    },

    64: {'name': 'Jakiro',
         'role': 'Nuker, Pusher, Lane Support, Disabler',
         'radiant': 'true',
         'class': 'Intelligence',
         'bio': 'Jakiro the Twin Head Dragon is a ranged intelligence hero who utilises powers over ice and fire in '
                'powerful linear area spells. He can freeze enemies in place or slow them down, and is capable of '
                'dealing heavy damage throughout the game by locking enemies inside his Macropyre. With high base '
                'intelligence, strength, and statistics gain and relatively low mana costs, he requires few items to '
                'be effective. Jakiro is a support who can continually turn battles in his favor with good '
                'positioning. His high strength gain makes him a bit tougher than most spellcasters and his low '
                'cooldowns ensure that his downtime is very miniscule, making him a great hero for ganks, pushes and '
                'clashes across the battlefield.',
         'quote': 'Two sides of the same coin.',
         'strength': '24 + 2.3',
         'agility': '10 + 1.2',
         'intelligence': '28 + 2.8',
         'ms': '290',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': '400',
         'miss_s': '1100',
         'ad': '0.4 + 0.5',
         'cd': '0.65 + 0.3',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/jakiro.png'
    },

    65: {'name': 'Batrider',
         'role': 'Initiator, Disabler, Nuker, Escape',
         'radiant': 'false',
         'class': 'Intelligence',
         'bio': 'Batrider is a ranged intelligence hero who excels in lane control and harassing enemies, especially '
                'in the early phase of the game. Usually Batrider is played as a heavy support, items are not needed '
                'to utilise his abilties. Batrider is a mobile burst damage raider, capable of dealing enormous '
                'amounts of damage on stacks, at a risky close range. Before moving in for the kill, the Batrider '
                'hinders his targets with Sticky Napalm, a stacking debuff skill that slows his enemies and amplifies '
                'the damage taken from Batrider himself, be it with attacks, spells, or items. When his enemies are '
                'greatly crippled, he is ready to attack. With Flamebreak, he launches an explosive cocktail which '
                'damages and knocks back enemies in a targeted area. Then, the Batrider activates his Firefly ability, '
                'allowing the Batrider to fly high in the sky, creating a burning trail of liquid fire, scorching '
                'enemies who dare to go in his path, while giving him the ability to cross and phase through '
                'impassable grounds. With Sticky Napalm stacked, he is capable of amplifying and inflicting massive '
                'damage quickly, burning them with Flamebreak and Firefly. The Batrider then uses his ultimate, '
                'Flaming Lasso, which catches a target with a lasso, shackling and pulling them to his Firefly trail '
                'or to the clutches of his merciless allies. When these spells are used altogether, the Batrider is a '
                'dangerous enemy that enemies should be aware of, risking his own safety, but enough to cause fiery '
                'chaos and mass destruction.',
         'quote': 'It\'s not the bat you gotta worry about. She eats fruit.',
         'strength': '23 + 2.4',
         'agility': '15 + 1.5',
         'intelligence': '24 + 2.5',
         'ms': '290',
         'tr': '1.0',
         'sr': '1200 / 800',
         'ar': '375',
         'miss_s': '900',
         'ad': '0.3 + 0.54',
         'cd': '0.2 + 0.7',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/batrider.png'
    },

    66: {'name': 'Chen',
         'role': 'Support, Jungler, Pusher',
         'radiant': 'true',
         'class': 'Intelligence',
         'bio': 'Chen the Holy Knight has gameplay that is different than most other heroes. Holy Persuasion lets him '
                'convert creeps to his side, including powerful neutral creeps. As a result, Chen is usually found in '
                'the forest searching for creeps to convert. When he finds a strong creep or two, he descends on his '
                'unwary enemies, using both his own spells and the abilities of his persuaded creeps to take them out. '
                'When ambushing enemies, Chen generally uses his Penitence ability, which slows the target and causes '
                'them to take extra damage from Chen\'s flock. Test of Faith can be used to finish off enemies and '
                'also teleport any ally to the fountain after a short delay with a subability. Chen\'s support '
                'abilities are rounded out by Hand of God, a healing spell which instantly restores a set amount of HP '
                'to all allied Heroes and fully heals his controlled creeps across the battlefield.',
         'quote': 'You can learn faith at the end of a sword.',
         'strength': '20 + 1.5',
         'agility': '15 + 2.1',
         'intelligence': '21 + 2.8',
         'ms': '300',
         'tr': '0.6',
         'sr': '1800 / 800',
         'ar': '600',
         'miss_s': '1100',
         'ad': '0.5 + 0.5',
         'cd': '0.3 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/chen.png'
    },

    67: {'name': 'Spectre',
         'role': 'Carry, Durable',
         'radiant': 'false',
         'class': 'Agility',
         'bio': '<strong>Mercurial</strong> the <strong>Spectre</strong> is a melee Agility hero adept at dealing pure '
                'damage to lone targets and is powerful, both offensively and defensively. Spectral Dagger provides '
                'her with a significant amount of mobility, allowing her to pass through objects, units and terrain '
                'while slowing her foes that came in contact with the shadowy path left by her Spectral Dagger. '
                'Desolate allows her to inflict high pure damage to enemy heroes when she catches them alone. '
                'Dispersion reduces and reflects all damage, whether by attacks or spells, to an area around her as '
                'pure damage. Dispersion gives her great durability, especially when equipped with items that provide '
                'health, armor, and damage block. Finally, her Haunt creates a malevolent spectral illusion to all '
                'enemy heroes in the map. Haunt lets Spectre wreak havoc in clashes and ganks, while her allies take '
                'advantage of the confusion. Spectre can use Reality during the Haunt, instantly teleporting her to '
                'her illusion to take its form. This lets her hound her victim anywhere on the map. Mercurial is a '
                'dangerous supernatural being, relentless as she can chase and stalk down her victim to a global '
                'range, unhindered by boundaries. Her kit allows her to play the role of the team\'s hard carry by '
                'applying an immense amount of pressure in late game team fights. More specifically, the pure damage '
                'reflection from Dispersion makes it disadvantageous for teams to focus her. Her abilities have a '
                'complex nature, and newer players should generally not play Spectre as she is extremely farm and '
                'level dependent. It is best to face Spectre with allied help and strength, as encountering her '
                'alone isn\'t always the best option.',
         'quote': 'Can no one understand me?',
         'strength': '19 + 2',
         'agility': '23 + 2.2',
         'intelligence': '16 + 1.9',
         'ms': '295',
         'tr': '0.4',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.3 + 0.7',
         'cd': '0.3 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/spectre.png'
    },

    68: {'name': 'Ancient Apparition',
         'role': 'Support, Disabler',
         'radiant': 'false',
         'class': 'Intelligence',
         'bio': '<strong>Kaldr</strong> the <strong>Ancient Apparition</strong> is a ranged intelligence hero. This '
                'spell-caster elemental being possesses high range, great attributes and strong semi-spammable spells. '
                'He is commonly played as a ganker or support role and due to his high agility and an attack enhancing '
                'spell, he can be played as a Semi-Carry too. His ultimate is one of the most devastating spells in '
                'the game as it can hit multiple units, has global range, freezes health regeneration, and instantly '
                'kill units if low on life.',
         'quote': 'One day, ice will cover these lands, and it will be as if this war never happened.',
         'strength': '18 + 1.4',
         'agility': '20 + 22',
         'intelligence': '25 + 2.6',
         'ms': '295',
         'tr': '0.6',
         'sr': '1800 / 800',
         'ar': '600',
         'miss_s': '1250',
         'ad': '0.45 + 0.3',
         'cd': '0.01 + 0.75',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/ancient_apparition.png'},

    69: {'name': 'Doom',
         'role': 'Durable, Carry, Nuker',
         'radiant': 'false',
         'class': 'Strength',
         'bio': '<strong>Lucifer</strong> the <strong>Doom</strong> is a melee strength Hero with strong farming '
                'capabilities, good versatility, and one of the strongest single-target spells in the game. His very '
                'low starting armor makes him vulnerable to harassment, but his abilities and high health allow him '
                'to lane or even jungle quite effectively. A ruthless demon, he possesses malicious abilities '
                'revolving around greed, fire, and death. His Devour ability allows him to consume creeps, providing '
                'additional gold and allowing him to absorb any powers that creep had, which potentially allows him '
                'to have up to six total hero skills. Because there are numerous neutral creep abilities to choose '
                'from to supplement his other skills, the role that he chooses to play is quite flexible. Scorched '
                'Earth serves numerous purposes, allowing him to chase, escape, regenerate, and slowly burn his '
                'enemies all at once. LVL? Death is a spammable nuke that does either modest or massive damage to the '
                'enemy, depending on the enemy\'s level. Finally, his namesake ult Doom serves as one of the strongest '
                'single target lockdown abilities in the game. A unit afflicted with Doom takes intense damage over a '
                'lengthy duration, while having all his active abilities - even those from items - completely '
                'silenced. With numerous expensive items in his arsenal and a key enemy hero rendered useless for a '
                'teamfight, a farmed Doom ensures that nobody can extinguish his flame.',
         'quote': 'You\'re doomed.',
         'strength': '26 + 3.2',
         'agility': '11 + 0.9',
         'intelligence': '13 + 2.1',
         'ms': '290',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.5 + 0.7',
         'cd': '0.3 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/doom_bringer.png'},

    70: {'name': 'Ursa',
         'role': 'Carry, Jungler, Durable',
         'radiant': 'true',
         'class': 'Agility',
         'bio': '<p><strong>Ulfsaar</strong> the <strong>Ursa Warrior</strong> is a melee agility hero whose '
                'abilities\' main focus is the increase of autoattack damage, allowing for some of the most '
                'impressive sustained damage in the entire game.</p><p>He specializes in increasing damage against one '
                'target. His abilities allow him to attack at up to maximum speed (400 IAS) and gain bonus damage '
                'with each consecutive hit on a single target. With these abilities—Overpower and Fury Swipes—Ursa '
                'can savage beefy targets for as much as 700 damage per hit. He is a ferocious jungler and '
                'straightforward attacker, able to solo even Roshan at low levels if he has Vladmir\'s Offering or '
                'another lifesteal. Ursa is a carry who can snowball if he is farmed, but the array of anti-melee '
                'abilities existing even by the early game and his lack of any counterspells, especially to strong '
                'nukers and heroes with the ability to evade him make him a hero reliant on other spells on his team. '
                'Although an agility hero, Ursa\'s strength gain makes him very durable, and his ultimate allows his '
                'damage to scale by building strength items.</p>',
         'quote': 'It is my spirit that keeps me safe, and not mere armor.',
         'strength': '23 + 2.9',
         'agility': '18 + 2.1',
         'intelligence': '16 + 1.5',
         'ms': '310',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.3 + 0.3',
         'cd': '0.3 + 0',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/ursa.png'
    },

    71: {'name': 'Spirit Breaker',
         'role': 'Durable, Carry, Initiator, Disabler',
         'radiant': 'false',
         'class': 'Strength',
         'bio': '<strong>Barathrum</strong> the <strong>Spirit Breaker</strong> is a powerful ganker type melee '
                'strength Hero that concentrates on taking out single targets, while lacking in larger team fights. '
                'His Charge of Darkness lets him charge towards any target available, while knocking off all enemies '
                'in his path. If you see the charge coming, it may already be too late. He is picked mostly for his '
                'high damage given by his Greater Bash which crushes the life out of his hapless victims. Barathrum '
                'can instantly and quickly move to his enemy via Nether '
                'Strike and shock them with a soul-bashing blow.',
         'quote': 'I\'ll break their spirits and their backs.',
         'strength': '29 + 2.4',
         'agility': '17 + 1.7',
         'intelligence': '14 + 1.8',
         'ms': '290',
         'tr': '0.4',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.6 + 0.3',
         'cd': '0.47 + 0.8',
         'bat': '1.9',
         'avatar': 'img/dota/heroes/spirit_breaker.png'},

    72: {'name': 'Gyrocopter',
         'role': 'Disabler, Initiator, Nuker',
         'radiant': 'true',
         'class': 'Agility',
         'bio': 'Aurel the Gyrocopter is a ranged agility Hero, capable of outputting a lot of single target and area '
                'of effect damage at a multitude of ranges. Early game Gyrocopter is a strong ganker, with Rocket '
                'Barrage able to output a lot of damage in a short amount of time if he and his target are alone. His '
                'second ability, Homing Missile, is a long range projectile that forces opponents to either stop and '
                'engage to take out the missile, or run to a safe location before being stunned. Thanks to his third '
                'ability, Flak Cannon, he is also an excellent pusher, and with it can farm up big items in the '
                'midgame as his spells start to fall off in damage. Flak Cannon also allows him to hit everyone in a '
                'teamfight with his autoattack, and with enough damage items he can inflict a lot of damage to the '
                'entire enemy team. Call Down is a useful ultimate with a low cooldown, and with an Aghanim\'s Scepter '
                'Gyrocopter can become a global presence, able to push or gank from anywhere on the map. With the '
                'right items, he can also transition into a semi-carry role.',
         'quote': 'They\'re like ants from up here.',
         'strength': '18 + 1.8',
         'agility': '24 + 2.8',
         'intelligence': '23 + 2.1',
         'ms': '315',
         'tr': '0.6',
         'sr': '1800 / 800',
         'ar': '365',
         'miss_s': '3000',
         'ad': '0.2 + 0.97',
         'cd': '0.3 + 0.5',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/gyrocopter.png'
    },

    73: {'name': 'Alchemist',
         'role': 'Durable, Carry, Disabler',
         'radiant': 'true',
         'class': 'Strength',
         'bio': '<strong>Razzil Darkbrew</strong> the <strong>Alchemist</strong> is a melee strength hero who utilises '
                'his alchemical prowess as a '
                'strange but versatile fighter. He is an unusual carry based upon transmuting fallen enemies into '
                'large amounts of bonus gold, with both an early game and late game presence due to his large health '
                'pool and the first strike nature of his spells. His balanced statistics and the sure promise of gold '
                'for items means he can be one of the most disparately built heroes in the game. Unstable Concoction '
                'is his main contribution early on, dealing good damage and a lengthy stun. Acid Spray allows him to '
                'rapidly clear waves of creeps for his Greevil\'s Greed to contribute massive amounts of extra income. '
                'A well-equipped Alchemist can then use Chemical Rage to its fullest effect, as the incredible '
                'regeneration and base attack time reduction make it one of the best steroid abilities in the game.',
         'quote': 'I\'m the brains! And I\'m the brawn!',
         'strength': '25 + 1.8',
         'agility': '11 + 1.2',
         'intelligence': '25 + 1.8',
         'ms': '295',
         'tr': '0.6',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.35 + 0.65',
         'cd': '0.2 + 0.5',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/alchemist.png'},

    74: {'name': 'Invoker',
         'role': 'Carry, Nuker, Initiator, Escape',
         'radiant': 'false',
         'class': 'Intelligence',
         'bio': '<strong>Invoker</strong> is a ranged intelligence Hero who is considered one of the most difficult '
                'hero in the game to master. He is unique in that he possesses a total of 14 abilities in his arsenal; '
                'three of them - Quas, Wex, and Exort - are reagents and one is his special ultimate Invoke. The three '
                'abilities he learns throughout leveling up can have three instances, which serve as the basic '
                'ingredients or components for him to create a new ability using his ultimate. Once the reagents or '
                'elements are combined, he can invoke one out of ten different abilities. All of his invoked abilities '
                'are capable of a multitude of actions, from damaging enemies to aiding his allies, and even saving '
                'himself from danger. His three reagents can be upgraded up to level 7 which determines the power and '
                'potency of his invoked abilities, making it more powerful than an ordinary spell. Because of this, he '
                'can be played in almost any role possible. Invoker can be a carry, semi-carry, ganker, pusher, '
                'initiator or even support. He is also the only hero who doesn\'t have Attribute Bonuses, thus he has '
                'average attributes. However, his three reagents provide passive attributes with each level, and each '
                'instance of his reagents provides a passive bonus, allowing for specialization at early levels and '
                'situational boosts at later levels. His extremely flexible nature allows him to use many different '
                'combinations of items effectively but also make him dependent on solid builds and a good '
                'gold advantage.',
         'quote': 'What joy it is beholding me!',
         'strength': '19 + 1.7',
         'agility': '20 + 1.9',
         'intelligence': '22 + 2.5',
         'ms': '280',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': '600',
         'miss_s': '900',
         'ad': '0.4 + 0.7',
         'cd': '0 + 0',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/invoker.png'
    },

    75: {'name': 'Silencer',
         'role': 'Support, Carry, Initiator',
         'radiant': 'true',
         'class': 'Intelligence',
         'bio': '<strong>Nortrom</strong> the <strong>Silencer</strong> is a ranged Intelligence hero who can be '
                'played as a Support, Carry or Initiator. He is one of the minority of Intelligence heroes who truly '
                'benefits from Intelligence items and is effective against Heroes who rely mostly on spells, as he can '
                'silence them while stealing their Intelligence and adding it to his own. He is a notorious anti-caster '
                'hero who can disrupt the magical abilities of his enemies and cripple spellcasters throughout the '
                'game. Curse of the Silent causes enemies to lose health and mana until the end of the duration or '
                'until the enemy casts a spell. Last Word places a curse on Nortrom\'s target that damages and '
                'silences for a long duration if the target casts a spell. If the target does not cast a spell before '
                'the curse\'s duration ends they will be damaged, silenced, and disarmed. Glaives of Wisdom is a '
                'Unique Attack Modifier that deals a percentage of Nortrom\'s intelligence as pure damage. Glaives '
                'of Wisdom also includes a passive component that permanently steals the intelligence of enemy heroes '
                'that die near Nortrom. Nortrom\'s ultimate, Global Silence, silences all enemy units on the map for '
                'a few seconds. A well-timed Global Silence can be used to save yourself or an ally, initiate a '
                'teamfight, or ruin the enemy\'s initiation.',
         'quote': 'Quiet as the grave.',
         'strength': '17 + 2.2',
         'agility': '16 + 2.1',
         'intelligence': '27 + 2.5',
         'ms': '300',
         'tr': '0.6',
         'sr': '1800 / 800',
         'ar': '600',
         'miss_s': '1000',
         'ad': '0.5 + 0.5',
         'cd': '0.3 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/silencer.png'},

    76: {'name': 'Outworld Devourer',
         'role': 'Carry',
         'radiant': 'false',
         'class': 'Intelligence',
         'bio': '<strong>Harbinger</strong> the <strong>Outworld Devourer</strong> is a ranged intelligence hero who '
                'qualifies as a carry, though several weaknesses - primarily his inability to combat magic-immune '
                'targets - restrict him from true hard carry status. His damage output is entirely reliant on his '
                'intelligence attribute and the size of his mana pool, so he must focus more or less exclusively on '
                'items which augment them. Though extremely fragile (rendered even more so by his inability to build '
                'many significant durability items), he deals Pure damage which increases with his mana pool, meaning '
                'that if he gains an advantage in a match he deals constant, colossal damage which (because it is Pure '
                'damage) cannot be decreased or resisted except with total magic immunity. He and his allies enjoy '
                'more-or-less unlimited mana because of his Essence Aura, which gives them a chance to replenish a '
                'quarter of their mana upon casting a spell. With Astral Imprisonment, Harbinger can render himself '
                'or an ally invulnerable for a short period of time, or disable (and steal Intelligence from) the '
                'target enemy. His ultimate, Sanity\'s Eclipse, can instantly deal colossal area-of-effect damage '
                'against his enemies when his intelligence is higher than theirs.',
         'quote': 'Their sanity I\'ll shatter; their dreams of conquest I\'ll destroy.',
         'strength': '19 + 1.85',
         'agility': '24 + 2',
         'intelligence': '26 + 3.3',
         'ms': '315',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': '450',
         'miss_s': '900',
         'ad': '0.46 + 0.54',
         'cd': '0.25 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/obsidian_destroyer.png'
    },

    77: {'name': 'Lycan',
         'role': 'Carry, Jungler, Pusher, Durable',
         'radiant': 'false',
         'class': 'Strength',
         'bio': 'Banehallow the Lycan is a melee strength hero who is capable of immense physical damage and '
                'considerable movement speed, who also excels at pushing buildings and bolstering his team\'s damage. '
                'He is capable of summoning Wolves who make excellent sources of damage and objective control. His '
                'Howl gives a large boost to the attack damage of his allies, while Feral Impulse turns Lycan and his '
                'pack into prime fighters on their own. When the time is right, Shapeshift allows the Lycan himself '
                'to join in the hunt, overwhelming foes with deadly critical strikes and incredible movement speed.',
         'quote': 'Sheep may talk peace with a wolf, but the wolf always answers the same. No.',
         'strength': '22 + 2.75',
         'agility': '16 + 1.9',
         'intelligence': '17 + 1.55',
         'ms': '305',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.55 + 0.55',
         'cd': '0.3 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/lycan.png'
    },

    78: {'name': 'Brewmaster',
         'role': 'Carry, Durable, Initiator, Pusher',
         'radiant': 'true',
         'class': 'Strength',
         'bio': 'Mangix the Brewmaster is a melee strength hero that can fill almost any role, though he is primarily '
                'seen as a carry, ganker, tank or initiator. He fits well into any lane, but is very experience '
                'dependent, which means he is often seen on the offlane or the midlane. His core abilities make him a '
                'respectable physical damage dealer and an especially good duelist, since he has abilities that '
                'involve negating opposing auto-attacks while strengthening his own. However, his true power lies in '
                'his ultimate, Primal Split, which, if used properly, can by itself turn the tide of a team fight. '
                'Each of the three aspects of the Brewmaster are exceptionally powerful, with exceptional disables, '
                'survivability against magic and physical attacks, and damage; they are also able to charge recklessly '
                'into the enemy since the damage they take is not permanent, and very rarely will all three die '
                'before Primal Split ends. For this reason, Brewmaster is almost always built to fully maximize the '
                'potential of this ultimate, getting items such as Blink Dagger so that he can combo into his ultimate '
                'without risk of being initiated on, Heart of Tarrasque to ensure he can survive the first wave of '
                'stuns and burst in order to cast his ultimate, and of course Aghanim\'s Scepter to give his spirits '
                'his abilities, Thunder Clap to earth, Drunken Haze to Storm, and Drunken Brawler to Fire, all '
                'independent of the original brewmaster\'s cooldowns for his abilities.',
         'quote': 'Shall we call this off and have a friendly round?',
         'strength': '23 + 2.9',
         'agility': '22 + 1.95',
         'intelligence': '14 + 1.25',
         'ms': '300',
         'tr': '0.6',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.35 + 0.65',
         'cd': '0.4 + 0.5',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/brewmaster.png'},

    79: {'name': 'Shadow Demon',
         'role': 'Support, Disabler, Nuker',
         'radiant': 'false',
         'class': 'Intelligence',
         'bio': '<strong>Shadow Demon</strong> is a menacing ranged Intelligence hero who is most powerful in the '
                'early game for his strong set of spells. Disruption will take an enemy out of the fight, banishing '
                'them to a shadowy world and returning on the present world, along with two demonic illusions. Soul '
                'Catcher can curse his victim with vulnerability. The cursed target takes more damage from attacks '
                'and spells and his Shadow Poison can harass any unfortunate foe he encounters, slowly infecting them '
                'and dealing more when afflicted with the poison again and again, until the Shadow Demon chooses to '
                'take the poison to its full effect, bursting out the collected poison. Demonic Purge, his ultimate, '
                'is his key to a successful kill, the Shadow Demon greatly slows down his fleeing victim and removes '
                'all buffs of his enemy, crippling and weakening them. His spells also serve as a great support for '
                'his allies as well as a great way to gank. With a great start, the Shadow Demon will begin to '
                'dominate the battle. An ancient being of evil and darkness, Shadow Demon will soon rise again and '
                'conquer, bringing the world to despair and destruction.',
         'quote': 'Who toys with demons will find himself toyed with.',
         'strength': '17 + 1.9',
         'agility': '18 + 2.2',
         'intelligence': '23 + 2.7',
         'ms': '295',
         'tr': '0.6',
         'sr': '1800 / 800',
         'ar': '500',
         'miss_s': '900',
         'ad': '0.35 + 0.5',
         'cd': '0.3 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/shadow_demon.png'
    },

    80: {'name': 'Lone Druid',
         'role': 'Carry, Durable, Pusher, Jungler',
         'radiant': 'true',
         'class': 'Agility',
         'bio': '<strong>Sylla</strong> the <strong>Lone Druid</strong> is an adaptable and versatile ranged or melee '
                'agility Hero, who summons a Spirit Bear, who has a set of skills and can equip items, as his ally. '
                'With the help of his Spirit Bear, he can carry, jungle, and push lanes effectively. Because of these, '
                'technically speaking, the Spirit Bear and Lone Druid himself, are two available heroes at once. '
                'The Spirit Bear is mostly played as the tank and aura giver, while the Lone Druid is played as the '
                'support and the main damage dealer as the Druid is still capable of causing more damage than the '
                'Spirit Bear. When he activates his abilities, it will not only buff him but the Spirit Bear as well. '
                'Lone Druid is versatile as he can change from a fast ranged warrior to a tough and mighty melee bear '
                'himself. Together, they can push the lanes effectively, farm Neutrals in a cinch, and can take down '
                'Roshan by themselves if equipped with the right items. Due to the Spirit Bear, Lone Druid can have '
                'up to 12 items making him extremely formidable as he scales into the late game.',
         'quote': 'I wonder what awaits me at the end of everything...',
         'strength': '17 + 2.1',
         'agility': '24 + 2.7',
         'intelligence': '13 + 1.4',
         'ms': '325',
         'tr': '0.4',
         'sr': '1800 / 800',
         'ar': '550',
         'miss_s': '900',
         'ad': '0.33 + 0.53',
         'cd': '0.5 + 1.17',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/lone_druid.png'
    },

    81: {'name': 'Chaos Knight',
         'role': 'Carry, Disabler, Durable, Pusher',
         'radiant': 'false',
         'class': 'Strength',
         'bio': '<strong>Chaos Knight</strong> is a melee strength Hero with one of the highest physical damage '
                'outputs of all heroes. He is mostly played as a semi-carry and ganker. As his name implies, he has a '
                'theme based on randomness and uncertainty. His regular attack has an incredibly high thirty damage '
                'spread, making his last hitting ability somewhat unreliable. Chaos Bolt is his most notorious '
                'luck-based ability which, at max level, can stun a target anywhere between a mediocre 2 seconds to an '
                'effective 4 seconds that will almost certainly assure its death; it will also deal a variable amount '
                'of damage ranging from miniscule to moderate. Reality Rift pulls Chaos Knight and his target to a '
                'randomly chosen point along the line between the two and gives him bonus damage for one attack. Chaos '
                'Strike is a crit-based ability with one of the lowest proc chances, yet also one of the highest '
                'multipliers. His only non-random ability is his ultimate Phantasm, which produces the most powerful '
                'illusions in the game. These illusions, which retain his full damage and only take double damage, '
                'benefit from his Chaos Strike and can teleport alongside him to attack the target whenever he uses '
                'Reality Rift. With three illusions being produced at Phantasm\'s highest level, Chaos Knight\'s '
                'damage output is effectively quadrupled during teamfights later in the game, and it is not uncommon '
                'to see enemy heroes being killed instantly after being Reality Rifted by the four apocalyptic '
                'horsemen. Thus, even though he is mostly played as a semi-carry who is extremely effective in the '
                'early to mid game, if the game drags on long enough and he is able to acquire enough strength-based '
                'and survivability items to ensure that his illusions can stay alive, he will be able to overpower '
                'most hard carries.',
         'quote': 'The light shall be blackened, and chaos shall reign.',
         'strength': '20 + 2.9',
         'agility': '14 + 2.1',
         'intelligence': '16 + 1.2',
         'ms': '325',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.5 + 0.5',
         'cd': '0.4 + 0.2',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/chaos_knight.png'},

    82: {'name': 'Meepo',
         'role': 'Carry, Disabler, Initiator',
         'radiant': 'false',
         'class': 'Agility',
         'bio': 'Meepo the Geomancer is a melee agility hero who is notorious for being the hardest hero in the game '
                'to play effectively due to his heavy reliance on micromanagement. Meepo\'s defining ultimate, Divided '
                'We Stand, makes Meepo four individual clones of himself. The clones cannot use any items besides the '
                'boots that the main Meepo himself wears, but each come with their own individual spells and spell '
                'cooldowns. As well, they all gain experience and gold additively with the original Meepo. This means '
                'that a well-played Meepo can gain experience faster than any other hero, capable of reaching maximum '
                'level extremely early into the game and overpowering his unsuspecting opponents. With Earthbind, '
                'enough Meepos can permanently root someone in place while the clone army pummels them. Poof allows '
                'any Meepo to globally teleport to any other Meepo, as well as deal significant area of effect damage '
                'when cast enough times. Geostrike is Meepo\'s passive, which slows and deals damage on attack, as '
                'well as stack with each individual Meepo, permanently bringing them to dust. With this skill set, '
                'Meepo can be everywhere on the map at once, and can group up on an unsuspecting victim in a moment\'s '
                'notice. Meepo redefines the power of numbers and is played mostly as a carry.',
         'quote': 'All these fancy knights and scary monsters. Pff! What do they got that '
                  'I ain\'t got? Nothing, that\'s what.',
         'strength': '23 + 1.6',
         'agility': '23 + 1.9',
         'intelligence': '20 + 1.6',
         'ms': '305',
         'tr': '0.65',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.38 + 0.6',
         'cd': '0.5 + 0.5',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/meepo.png'
    },

    83: {'name': 'Treant Protector',
         'role': 'Durable, Initiator, Lane Support, Disabler',
         'radiant': 'true',
         'class': 'Strength',
         'bio': 'Rooftrellen the Treant Protector is a melee strength hero who excels in supporting and strengthening '
                'his allies with his beneficial set of spells using the power of nature. He is a natural tank, '
                'offensively and defensively, having both the highest natural attack damage, and the second highest '
                'overall Strength in the game. Manipulating the power of the plants to his will, he can grant '
                'invisibility and stealth to himself and his allies with Nature\'s Guise, provided that they remain '
                'within close proximity to a tree. He can also use Leech Seed against a target, dealing moderate '
                'damage over time to it and slowing it whilst nearby allies are replenished by the same amount. His '
                'signature Living Armor makes him truly live up his title, as he is able to provide allies and even '
                'friendly buildings increased health regeneration and a massive damage block from anywhere on the map. '
                'Finally his ultimate Overgrowth affects enemies in a respectable area of effect and entangles enemies '
                'with vines, branches, and roots; though it does not deal any damage, it will immobilize them and '
                'render them unable to attack for several crucial seconds. Although Treant Protector is not able to '
                'dish out much damage outside of his regular attacks, he is able to provide an enormous amount of '
                'defensive utility and survivability to himself and his teammates, thereby rooting a path to victory.',
         'quote': 'Life becomes death becomes new life. As it should be.',
         'strength': '25 + 3.3',
         'agility': '15 + 2',
         'intelligence': '17 + 1.8',
         'ms': '300',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.6 + 0.4',
         'cd': '0.5 + 0.51',
         'bat': '1.9',
         'avatar': 'img/dota/heroes/treant.png'
    },

    84: {'name': 'Ogre Magi',
         'role': 'Nuker, Disabler, Durable',
         'radiant': 'true',
         'class': 'Intelligence',
         'bio': '<strong>Aggron Stonebreak</strong> the <strong>Ogre Magi</strong> is a melee intelligence hero famous '
                'for his random potential for extreme burst damage and his enormous health pool for an intelligence '
                'Hero. He has good base attributes, and some of the best attributes gain in the game. He is a powerful '
                'ganker and disabler, eliminating his opponents in mere seconds if his ultimate Multicast successfully '
                'occurs with Fireblast. Later in the game he takes on the role of a buffer/debuffer with his powerful '
                'Bloodlust buff and his AoE Ignite.',
         'quote': 'Once is not enough! It\'s just as high as we can count.',
         'strength': '23 + 3.2',
         'agility': '14 + 1.55',
         'intelligence': '17 + 2.4',
         'ms': '295',
         'tr': '0.6',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.3 + 0.3',
         'cd': '0.56 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/ogre_magi.png'
    },

    85: {'name': 'Undying',
         'role': 'Durable, Pusher, Disabler, Initiator',
         'radiant': 'false',
         'class': 'Strength',
         'bio': 'Undying the Almighty Dirge is a melee Strength Hero who serves as a formidable tank and a dangerous '
                'spellcaster. His abilities force opponents to either kill him or suffer powerful debuffs in a '
                'teamfight. Decay is a spammable skill that steals enemies Strength in an area, making them more '
                'fragile and Undying himself more durable as the fight goes on. Soul Rip can act as both a powerful '
                'heal or nuke, redirecting the flow of living energy to a target. By ripping some of the health of '
                'his ally or enemy in an area, the target can be healed if an ally, or damaged if an enemy. This is '
                'empowered by Tombstone, which acts as a static tank by summoning Zombies to slow Undying\'s foes '
                'while active. With the Zombies summoned, Soul Rip can perform to its fullest, while Decay weakens '
                'Undying\'s foes. Finally, Undying can transform into a horrific Flesh Golem. This transformation '
                'increases all allied damage by a significant percentage, and helps keep him alive as his team kills '
                'the enemy. Monstrous and truly sadomasochistic, Undying finds great pleasure in keeping himself '
                'alive and vital, while his adversaries suffer as he delivers death to the field. With powerful '
                'abilities that scale well into late game, the Dirge may never cease.',
         'quote': 'Again and again, I live and die.',
         'strength': '22 + 2.1',
         'agility': '10 + 0.8',
         'intelligence': '27 + 2.0',
         'ms': '310',
         'tr': '0.6',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.3 + 0.3',
         'cd': '0.45 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/undying.png'
    },

    86: {'name': 'Rubick',
         'role': 'Disabler, Pusher, Support, Line Support',
         'radiant': 'true',
         'class': 'Intelligence',
         'bio': '<strong>Rubick</strong> the <strong>Grand Magus</strong> is a ranged Intelligence hero best known for '
                'his ability to copy the spells of his enemies and use them as his own. Although he is mostly played '
                'as a support and is extremely fragile the entire length of the game, he can still prove to be one of '
                'the most influential heroes if he utilizes good positioning and well-timed usage of his ultimate, '
                'Spell Steal, correctly. Spell Steal allows Rubick to cast an enemy hero\'s most recently used spell, '
                'giving him supreme versatility throughout the game. By stealing the right abilities, the Grand Magus '
                'can aid himself and allies by casting crippling disables, applying curses, unleashing powerful nukes, '
                'disorienting the enemy team, supporting his allies with buffs, escaping from rough situations, or '
                'even enhancing his own physical attacks. His other abilities are just as worthy of a Magus: '
                'Telekinesis lets Rubick magically lift an enemy into the air, rendering the target helpless and '
                'vulnerable, before hurling the lifted enemy to the ground up to a short distance away and stunning '
                'nearby foes on impact. Fade Bolt blasts enemies with a stream of arcane energy which bounces to all '
                'enemies nearby, dealing damage and reducing their attack damage. Null Field is a passive aura, which '
                'grants himself and nearby allied heroes bonus magic resistance to shrug off magical assaults. '
                'Rubick\'s versatile skill-set and his infamous Spell Steal make him a flexible and powerful hero '
                'that can work in any lineup.',
         'quote': 'I am no thief. I merely borrow.',
         'strength': '19 + 1.5',
         'agility': '14 + 1.6',
         'intelligence': '27 + 2.4',
         'ms': '290',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': '600',
         'miss_s': '1125',
         'ad': '0.4 + 0.77',
         'cd': '0.1 + 1.17',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/rubick.png'},

    87: {'name': 'Disruptor',
         'role': 'Nuker, Support, Initiator, Disabler',
         'radiant': 'true',
         'class': 'Intelligence',
         'bio': 'Disruptor the Stormcrafter is a supportive ranged intelligence Hero. His signature ability is Kinetic '
                'Field, a pseudo-disable that traps enemies within a small area for a long duration. Combined with his '
                'Static Storm, Disruptor can act as the initiator for a teamfight, or supplement his teammates '
                'initiation very well. Glimpse is another powerful spell that forces enemies to watch their movements, '
                'as Disruptor can easily drag them back to a previous location to be focused down. Thunder Strike '
                'provides Disruptor with some reliable single-target damage, but more importantly grants vision on the '
                'target to prevent jukes and escapes.',
         'quote': 'The forecast calls for blood.',
         'strength': '19 + 1.9',
         'agility': '15 + 1.4',
         'intelligence': '22 + 2.5',
         'ms': '300',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': '600',
         'miss_s': '1200',
         'ad': '0.4 + 0.5',
         'cd': '0.05 + 1.0',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/disruptor.png'},

    88: {'name': 'Nyx Assassin',
         'bio': '<strong>Nyx Assassin</strong> is a melee Agility Hero who is a dedicated ganker until the end. '
                'Rather than focusing on enhancing his physical attacks like most Agility carry Heroes, Nyx Assassin '
                'specializes in killing lone and fragile victims with his high burst damage and various disables. '
                'Unfarmed carries, supports and many Intelligence spellcasting heroes with a low healthpool are easy '
                'prey for Nyx; he can open with a devastating backstab attack, followed by a painful stun and mana '
                'burn to deal even more damage and prevent retaliation. The Nyx Assassin also has a fantastic defense '
                'mechanism that not only blocks damage for a small amount of time, but reflects it back onto the '
                'enemy with a stun effect to boot. With his short cooldowns, the Nyx Assassin can continually '
                'dispatch key enemy targets, removing their ability and will to fight.',
         'quote': 'The blessing of Nyx gives me all the purpose I require.',
         'role': 'Disabler, Nuker',
         'class': 'Agility',
         'radiant': 'false',
         'strength': '18 + 2',
         'agility': '19 + 2.2',
         'intelligence': '18 + 2.1',
         'ms': '300',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.46 + 0.54',
         'cd': '0.4 + 1.1',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/nyx_assassin.png'
    },

    89: {'name': 'Naga Siren',
         'role': ' Carry, Disabler, Pusher, Escape',
         'radiant': 'true',
         'class': 'Agility',
         'bio': 'Slithice the Naga Siren is a melee Agility hero who can be played both as a late-game carry and an '
                'early/mid-game support. Slithice is an item dependent hero and with the right style and inventory '
                'choices she can overpower many other heroes that deal strong physical damage while casting her all '
                'four active skills to handle her enemies altogether and turn the tides. Mirror Image creates three '
                'illusions to wreak havoc upon her enemies. Ensnare is a very useful spell with several unique '
                'features. It not only holds an enemy in a place, but also prevents them from blinking and going '
                'invisible. Even if the enemy is magic immune, Ensnare can still target the enemy unit. Rip Tide calls '
                'the forces of the seas, allowing the Siren and her illusions to unleash a wave of magical water to '
                'wash away foes and degrade their armor. The Song of the Siren is the ultimate skill for team battles, '
                'the Naga Siren performs a mystical song to put her enemies to sleep in an area around her. Song of '
                'the Siren is her tool for initiation, as while her enemies are under her slumber her allies can come '
                'forth and prepare to unleash their attacks after the song wears off. Slithice is a mighty single '
                'target huntress and a great team fighter, using her powerful water magic, skills in combat, and her '
                'enchanting voice.',
         'quote': 'I sing the Siren song of war',
         'strength': '21 + 2.3',
         'agility': '21 + 2.75',
         'intelligence': '18 + 1.95',
         'ms': '320',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.5 + 0.5',
         'cd': '0.65 + 0.7',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/naga_siren.png'},

    90: {'name': 'Keeper of the Light',
         'role': 'Pusher, Support',
         'radiant': 'true',
         'class': 'Intelligence',
         'bio': 'Ezalor the Keeper of the Light is a ranged Intelligence Hero famous for his reputation as a one-man '
                'support team. Supporting his allies in need, and pushing unguarded lanes with ease, Ezalor is a very '
                'valuable ally for any team. Having a variety of useful abilities, he can channel a powerful globe of '
                'intense light that can heavily damage an army of enemy creeps in the lane, allowing for an easy push; '
                'and manipulate the mana around him, restoring mana for himself and his allies or draining the mana '
                'of his enemy. His Ultimate allows him to gain his full power, giving Ezalor access to 2 sub-skills '
                'and an improved existing ability, giving him six different abilities in total. Keeper of the Light '
                'requires patience, confidence and selfless behavior to play him well, as he is played as a support '
                'instead of a killer caster like most Intelligence gankers. His wide set of skills also require good '
                'timing, reflexes, and knowledge to use well.',
         'quote': 'They say twas I who carried the first light into the universe. They might be right, '
                  'I can\'t quite recall',
         'strength': '14 + 1.8',
         'agility': '15 + 1.6',
         'intelligence': '22 + 2.8',
         'ms': '315',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': '600',
         'miss_s': '900',
         'ad': '0.3 + 0.85',
         'cd': '0.3 + 2.4',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/keeper_of_the_light.png'},

    91: {'name': 'Io',
         'role': 'Support, Lane Support, Nuker',
         'radiant': 'true',
         'class': 'Strength',
         'bio': '<strong>Io</strong> the <strong>Guardian Wisp</strong> is a highly unique ranged strength hero who '
                'works best as part of a '
                'communicative team. With its support-oriented skill set, Io is able to share its strength through '
                'Tether and Overcharge, harass enemy heroes out of the lane with Spirits, and materialize itself and '
                'an ally anywhere on the map with Relocate. Gank enemy Heroes, push undefended lanes, save teammates '
                'from deep within enemy territory - the possibilities are endless, and Io features one of the highest '
                'skill ceilings in the game.',
         'strength': '17 + 1.9',
         'agility': '14 + 1.6',
         'intelligence': '23 + 1.7',
         'ms': '295',
         'tr': '0.7',
         'sr': '1800 / 800',
         'ar': '575',
         'miss_s': '1200',
         'ad': '0.15 + 0.4',
         'cd': '0.001 + 0',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/wisp.png'},

    92: {'name': 'Visage',
         'role': 'Nuker, Durable, Disabler',
         'radiant': 'false',
         'class': 'Intelligence',
         'bio': '<strong>Visage</strong>, the bound form of <strong>Necro\'lic</strong>, is a ranged intelligence Hero '
                'whose traits are unusual when compared to most Intelligence heroes; he can be a Ganker, Tank, or '
                'Nuker. Resilient and ruthless, Visage is a highly aggressive hero thanks to his great Strength and '
                'Gravekeeper\'s Cloak which allow him to soak up surprising amounts of damage. This is especially '
                'true from attacks mounted by Heroes who try to chip at his health with spells and burst damage '
                'without committing to a protracted engagement. This unholy gargoyle thrives in the midst of large '
                'battles, where the abundant pain and suffering in the air charges his Soul Assumption: allowing him '
                'to fire off huge bursts of magical damage in rapid succession. Additionally, Visage\'s proficiency '
                'with auto-attacks is augmented by his ability to absorb the attack and movement speed of his foes '
                'with Grave Chill. Finally, his versatile ultimate, Familiars, is arguably one of the best scouting '
                'utilities in the game while also being excellent sources of damage and AOE disables. Utilizing his '
                'Familiars to their fullest requires constant split attention and good positioning to avoid feeding '
                'their large bounties to an enemy Hero. With a legion of ghostly gargoyles, incredible toughness and '
                'fast attacks, Visage sows terror and agony; relentlessly hunting poor souls and leading them in the '
                'shackles of death to the gates of the Underscape. Unlike most other heroes in Dota 2, Visage has a '
                'base 10% magic resistance instead of 25%.',
         'quote': 'It is one thing to animate a corpse from beneath the ground. It is another to rip a '
                  'soul from beyond the veil.',
         'strength': '22 + 2.4',
         'agility': '11 + 1.3',
         'intelligence': '24 + 2.5',
         'ms': '290',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': '600',
         'miss_s': '900',
         'ad': '0.46 + 0.54',
         'cd': '0.4 + 1.1',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/visage.png'},


    93: {'name': 'Slark',
         'role': 'Escape',
         'radiant': 'false',
         'class': 'Agility',
         'bio': '<strong>Slark</strong> the <strong>Nightcrawler</strong> is a melee agility hero that utilises his '
                'skills to spring onto enemy heroes and slip out unhindered. He is a very mobile ganker, but remains '
                'statwise below most other carries unless he is able to steal away stats with his abilities. Once he '
                'does, though, only a few heroes can hope to be as fearsome as the Nightcrawler - extremely mobile to '
                'the point of ever-presence; his strikes only hitting harder and faster. Slark can quickly leap forward '
                'onto enemies with Pounce to leash them and bind them from escaping. His Dark Pact releases a delayed '
                'purge that breaks even the most powerful disables. This gives him one of the most flexible abilities '
                'to start and end fights in the game. He is also capable of stealing stats on auto-attacks to boost '
                'his own damage temporarily with Essence Shift which can rapidly shift engagements in his favor, even '
                'when merely performing hit-and-run maneuvers. Slark\'s ultimate, Shadow Dance, allows him to remain '
                'unseen even while attacking for a short duration and allows him to move quicker when not under the '
                'watch of enemy eyes to strike in and out of enemy ranks unhindered.',
         'quote': 'If I\'d known I\'d end up here, I\'d have stayed in Dark Reef Prison.',
         'strength': '21 + 1.8',
         'agility': '21 + 1.5',
         'intelligence': '16 + 1.9',
         'ms': '305',
         'tr': '0.5',
         'sr': '1800 / 1800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.5 + 0.3',
         'cd': '0.001 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/slark.png'
    },

    94: {'name': 'Medusa',
         'role': 'Carry',
         'radiant': 'false',
         'class': 'Agility',
         'bio': '<strong>Medusa</strong> the <strong>Gorgon</strong> is a ranged agility Hero. Highly item-dependent, '
                'she acts as a carry who can potentially strike down entire teams at once while protected by tank-like '
                'survivability. Split Shot allows her attacks to hit multiple targets, greatly increasing the potency '
                'of damage-granting items. Mystic Snake grants Medusa some presence in the lane and skirmishes, and '
                'its mana stealing refunds part of the cost to boot, making it an excellent farming and harrassing '
                'tool. Mana Shield protects her from the opening damage of teamfights, and if supplemented with items '
                'makes killing Medusa a fatally time-consuming process. Stone Gaze acts as a fantastic defensive '
                'mechanism against ganks and initiations alike, '
                'with crippling effects on all who dare face the Gorgon.',
         'quote': 'The only real beauty is power.',
         'strength': '14 + 1.65',
         'agility': '20 + 2.5',
         'intelligence': '19 + 1.85',
         'ms': '290',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': '600',
         'miss_s': '1200',
         'ad': '0.5 + 0.6',
         'cd': '0.4 + 0.5',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/medusa.png'
    },

    95: {'name': 'Troll Warlord',
         'role': 'Carry',
         'radiant': 'true',
         'class': 'Agility',
         'bio': '<strong>Jah\'rakal</strong>, the <strong>Troll Warlord</strong>, is a ranged Agility hero able to '
                'output mighty damage competitively at range and in melee. His Berserker\'s Rage gives him the unique '
                'ability to change his attack position, from ranged to melee and back at will, as the situation '
                'prefers. When in close combat, his stats are increased accordingly, he gains bonus damage, armor, '
                'movement speed, health, reduced base attack time, and the ability to Bash. Not only does this '
                'greatly improve the Troll Warlord, but it allows him to survive and match on other melee fighters. '
                'The Troll Warlord is an axe specialist, using them in his unique Whirling Axes, Whirling Axes has '
                'two variations, the first is available to his ranged form where he throws five axes in a cone '
                'formation to damage and slow them down, the second is when he is in melee form, unleashing swirling '
                'axes to damage and blind nearby enemies. To keep up with his gruff and savage nature, Fervor builds '
                'up the Warlord\'s momentum, with each continuous hit on the same target, he gains more and more '
                'attack speed. Battle Trance not only massively enhances his own attack speed, but it also enhances '
                'his allies for a short period of time. The Troll Warlord capitalizes on the power and speed of his '
                'attacks, notorious for his superbly fast attack speed that can be matched by few. He is truly an '
                'ill-tempered troll and his rampaging might is unstoppable, bashing and crippling his foes with his '
                'axes quickly. If he acquires the right items to improve his fighting prowess, there aren\'t many '
                'fighters who can take him down.',
         'quote': 'The strong shall eat the weak.',
         'strength': '17 + 2.2',
         'agility': '21 + 2.75',
         'intelligence': '13 + 1',
         'ms': '300',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': '500',
         'miss_s': '1200',
         'ad': '0.3 + 0.3',
         'cd': '0.51 + 0.3',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/troll_warlord.png'
    },

    96: {'name': 'Centaur Warrunner',
         'role': 'Durable, Disabler, Initiator',
         'radiant': 'true',
         'class': 'Strength',
         'bio': '<strong>Bradwarden</strong> the <strong>Centaur Warrunner</strong> is a melee strength hero whose '
                'natural place in combat is right in the center of battle. His abilities stop enemies around him in '
                'their tracks and inflict heavy damage, making him an excellent initiator. He is also a powerful tank, '
                'having the highest strength gain in the game. Bradwarden has immense natural health, and his skills '
                'area of effect mean that he can charge into combat and incapacitate groups of enemies at a time. Hoof '
                'Stomp and Double Edge make a great combo of stunning and burst damage on short cooldowns and his '
                'Return means instant retaliation on enemies who try attack him. His ultimate, Stampede effectively '
                'turns the entire team into initiators, granting them high speed and the ability to flatten enemies '
                'under as they pass over them. Although he is usually not played as a carry, he can scale powerfully '
                'with items, becoming a hard-hitting semi-carry that is nearly impossible to kill.',
         'quote': 'It is not pride I take in my own power, it is passion.',
         'strength': '23 + 3.8',
         'agility': '15 + 2',
         'intelligence': '15 + 1.6',
         'ms': '300',
         'tr': '0.5',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.3 + 0.3',
         'cd': '0.5 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/centaur.png'
    },

    97: {'name': 'Magnus',
         'role': 'Initiator, Disabler, Nuker, Carry',
         'radiant': 'false',
         'class': 'Strength',
         'bio': '<strong>Magnus</strong> the <strong>Magnoceros</strong> is a monstrous melee strength hero who is '
                'usually played as a ganker, initiator, or semi-carry. His ability to battle multiple heroes at once '
                'gives him an excellent presence in team fights. In addition to his teamfight presence, he can buff '
                'allies or himself with bonus damage and cleave, capitalizing on his ability to group up multiple '
                'enemies. As a hero who possesses multiple area-of-effect abilities with a manageable mana cost, '
                'and a very powerful ultimate that serves as both a team fight and initiation ability, Magnus is '
                'truly a force to be reckoned with.',
         'quote': 'No, I blame no one who covets my horn. But to desire more than sight of it is a guarantee of death.',
         'strength': '21 + 2.75',
         'agility': '15 + 2.5',
         'intelligence': '17 + 1.65',
         'ms': '315',
         'tr': '0.8',
         'sr': '1800 + 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.5 + 0.84',
         'cd': '0.3 + 0.6',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/magnataur.png'
    },

    98: {'name': 'Timbersaw',
         'role': 'Ganker, Initiator, Durable',
         'radiant': 'true',
         'class': 'Strength',
         'bio': '<strong>Rizzrack</strong> the <strong>Timbersaw</strong> is a melee Strength hero that excels in '
                'dealing damage and causing destruction in large areas. His effectiveness is improved by having trees '
                'around him, as they can amplify the damage of his spells and allow him to escape easily. He is not '
                'naturally very durable, but can be surprisingly resilient when he is attacked due to Reactive Armor, '
                'and when surrounded by favorable terrain he can be extremely hard to pin down and kill. In addition '
                'to this, most of his spells deal pure damage, unreduced by magic resistance or armor. With proper '
                'positioning and timing, he can cause massive damage to multiple enemies while also decreasing their '
                'movement speed and attributes.',
         'quote': 'I\'m not a lumberjack. This. This is personal.',
         'strength': '25 + 2.1',
         'agility': '16 + 1.3',
         'intelligence': '21 + 2.4',
         'ms': '290',
         'tr': '0.6',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.36 + 0.64',
         'cd': '0.3 + 0.6',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/shredder.png'
    },

    99: {'name': 'Bristleback',
         'role': 'Durable, Initiator, Disabler',
         'radiant': 'true',
         'class': 'Strength',
         'bio': '<strong>Rigwarl</strong> the <strong>Bristleback</strong> is a melee Strength hero famous for his '
                'array of synergistic spells with low mana cost and cooldown. He is able to slow his enemies down and '
                'reduce their armor with Viscous Nasal Goo, then hit them with a barrage of Quill Sprays, making him '
                'an effective chaser when ganking enemies. His low strength gain makes him less tanky than most '
                'strength heroes, but he becomes substantially more durable when he turns around due to his passive '
                'Bristleback, which reduces damage taken from behind. In the right hands, Bristleback is a powerful '
                'ganker in the early stages of the game, and a powerful semi-carry in the later stages depending on '
                'how much farm he gets.',
         'quote': 'It was a barkeep that got me into this mess. Yeah, I think I\'ll pay em a visit when this is done.',
         'strength': '22 + 2.2',
         'agility': '17 + 1.8',
         'intelligence': '14 + 2.8',
         'ms': '295',
         'tr': '1.0',
         'sr': '1800 / 800',
         'ar': 'Melee',
         'miss_s': 'Instant',
         'ad': '0.3 + 0.3',
         'cd': '0.3 + 0.51',
         'bat': '1.7',
         'avatar': 'img/dota/heroes/bristleback.png'
    },

    100: {'name': 'Tusk',
          'role': 'Initiator, Durable',
          'radiant': 'true',
          'class': 'Strength',
          'bio': '<strong>Ymir</strong> the <strong>Tusk</strong> is a melee Strength hero whose array of icy spells '
                 'pack great potential to grant the advantage in a gank. Tusk is both an effective team fight hero '
                 'and initiator, who has the unique ability to bring along teammates into the fight. Though he is '
                 'usually played as a support, one can in fact benefit reasonably well from additional attributes '
                 'and farm, and can be a great semi-carry as well. Equipping damage-boosting items can greatly '
                 'increase the critical damage brought by Walrus PUNCH!, allowing him to fight on his own in the '
                 'later stages.',
          'quote': 'After a bar brawl it\'s customary, as a courtesy, '
                   'to buy everyone who\'s still standing a round of drinks.',
          'strength': '23 + 2.3',
          'agility': '23 + 2.1',
          'intelligence': '18 + 1.7',
          'ms': '305',
          'tr': '0.5',
          'sr': '1800 / 800',
          'ar': 'Melee',
          'miss_s': 'Instant',
          'ad': '0.36 + 0.64',
          'cd': '0.1 + 1',
          'bat': '1.7',
          'avatar': 'img/dota/heroes/tusk.png'
    },

    101: {'name': 'Skywrath Mage',
          'role': 'Nuker, Support',
          'radiant': 'true',
          'class': 'Intelligence ',
          'bio': '<strong>Dragonus</strong> the <strong>Skywrath Mage</strong> is a ranged Intelligence hero equipped '
                 'with tremendously powerful nukes, able to enhance magical damage and thus scales well into late '
                 'game. However, he is a proverbial glass cannon; while he can bring superb amounts of damage, he is '
                 'dangerously vulnerable and will most likely meet a swift end if the player isn\'t careful. Arcane '
                 'Bolt is his main spell; its damage is based on his current Intelligence level. Concussive Shot '
                 'blasts the nearest enemy hero, along with nearby units around the foe, slowing them down. The '
                 'Ancient Seal marks the target with magic amplification and silence, leaving the target vulnerable '
                 'to magic and unable to cast spells. Skywrath Mage\'s ultimate Mystic Flare is one of the most '
                 'dangerous nukes in the game. Its power is split equally among enemy heroes within its radius. '
                 'Enemy heroes caught in this field will suffer damage; if it is used on a single hero, it will '
                 'deal its full damage potential. His spells are most effective when targeted on a lone hero and '
                 'thus suffer decreased effectiveness when used on groups.',
          'quote': 'Those who tangle with the Skywrath risk a fall from starry heights.',
          'strength': '19 + 1.5',
          'agility': '18 + 0.8',
          'intelligence': '27 + 3.6',
          'ms': '315',
          'tr': '0.5',
          'sr': '1800 / 800',
          'ar': '600',
          'miss_s': '1000',
          'ad': '0.4 + 0.78',
          'cd': '0.1 + 1.08',
          'bat': '1.7',
          'avatar': 'img/dota/heroes/skywrath_mage.png'
    },

    102: {'name': 'Abaddon',
          'role': 'Durable, Support, Escape',
          'radiant': 'false',
          'class': 'Strength',
          'bio': '<strong>Abaddon</strong> the <strong>Lord of Avernus</strong> is a melee strength Hero known as '
                 'one of the most versatile characters in Dota due to his rather low mana dependence, short spell '
                 'cooldowns and a large number of viable item choices. His ability to help sustain his allies and '
                 'himself plus his strong tower diving capacity give him solid lane presence. Many of his abilities '
                 'offer a large sum of utility, which makes him a strong support Hero. Mist Coil serves as both a '
                 'single target nuke and heal that helps shift the sustainability of both allied and enemy heroes '
                 'in a lane at his will, though sacrificing a portion of his own health. Aphotic Shield holds as '
                 'one of the most useful abilities in the game, able to shield a target from some damage while also '
                 'able to reflect said damage to a huge area. The most important aspect is how it is able to dispel '
                 'many status effects such as slows and stuns. His other abilities allow him to become a mix between '
                 'a semi-carry and tank. Abaddon\'s passive, Curse of Avernus, allows his attacks to not only slow '
                 'down his enemy, but also increase the attack and movement speed of any ally attacking the same '
                 'target. With his ultimate, Borrowed Time, Abaddon is able to shift all non-HP removal damage he '
                 'receives into health. When not on cooldown, Borrowed Time may activate passively when his health '
                 'falls under a certain threshold, even under the most dire situations. Due to his powerful spells '
                 'and versatility, Abaddon is an excellent addition to any team.',
          'quote': 'The fog of war is no match for the mist of fate.',
          'strength': '23 + 2.7',
          'agility': '17 + 1.5',
          'intelligence': '21 + 2',
          'ms': '310',
          'tr': '0.6',
          'sr': '1800 / 800',
          'ar': 'Melee',
          'miss_s': 'Instant',
          'ad': '0.56 + 0.41',
          'cd': '0.452 + 1.008',
          'bat': '1.7',
          'avatar': 'img/dota/heroes/abaddon.png'
    },

    103: {'name': 'Elder Titan',
          'role': 'Initiator, Durable',
          'radiant': 'true',
          'class': 'Strength',
          'bio': 'The <strong>Elder Titan</strong> is a durable melee strength hero who plays the role of initiator. '
                 'His Astral Spirit and Echo Stomp abilities allow him to disable large groups of enemies from afar, '
                 'making him one of the few initiators that does not require a Blink Dagger. This combination creates '
                 'a perfect setup for his powerful ultimate Earth Splitter, which damages enemies based on their '
                 'maximum HP. This, along with his ability to lower his enemies physical and magical resistance, '
                 'makes Elder Titan scale well through his abilities and be effective at all stages of the game. '
                 'As the progenitor of this world, Elder Titan reshapes the battlefield on a whim and can turn any '
                 'teamfight in his favor.',
          'quote': 'It is only right that I am cast into this world, for I had a hand in breaking it.',
          'strength': '24 + 2.3',
          'agility': '14 + 1.5',
          'intelligence': '23 + 1.6',
          'ms': '315',
          'tr': '0.4',
          'sr': '1800 / 800',
          'ar': 'Melee',
          'miss_s': 'Instant',
          'ad': '0.35 + 0.97',
          'cd': '0.4 + 0.8',
          'bat': '1.7',
          'avatar': 'img/dota/heroes/elder_titan.png'},

    104: {'name': 'Legion Commander',
          'role': 'Carry, Durable',
          'radiant': 'true',
          'class': 'Strength',
          'bio': '<strong>Legion Commander</strong> universal strenght melee melee. This character may well manifest '
                 'itself in the role of a Carry hero and help its allies in the battle. Its first ability - '
                 'Overwhelming Odds let out hail of arrows at enemies, dealing damage and reducing movement speed. '
                 'The second ability hero - Press the Attack - good ability to help allies in the battle, as it '
                 'removes the negative effects increases health regeneration and attack speed for a short period of '
                 'time. Moment of Courage gives the hero passive chance to strike back at being attacked. In other '
                 'words, the hero during the attack can damage the effect of Vampirism. Duel - main ability of the '
                 'hero, which allows cause an opponent to a duel. You and the enemy will not be able to use other '
                 'abilities, or item, until the duel did not complete. The winner of the duel forever will receive '
                 'permanent damage bonus. In General, the Legion Commander, due to the ability to survive and kill, '
                 'it is recommended to players with an average level of the game.',
          'quote': 'If they want war, then we shall give it to them!',
          'strength': '26 + 2.6',
          'agility': '18 + 1.7',
          'intelligence': '20 + 2.2',
          'ms': '320',
          'tr': '0.6',
          'sr': '1800 / 800',
          'ar': 'Melee',
          'miss_s': 'Instant',
          'ad': '0.46 + 0.64',
          'cd': '0.3 + 0.6',
          'bat': '1.7',
          'avatar': 'img/dota/heroes/legion_commander.png'
    },

    106: {'name': 'Ember Spirit',
          'role': 'Carry, Nuker, Disabler, Durable',
          'radiant': 'true',
          'class': 'Agility',
          'bio': '<strong>Xin</strong>, the <strong>Ember Spirit</strong> is a highly mobile melee Agility carry, '
                 'whose abilities enable him to also play as an initiator or ganker. His skillset allows for '
                 'incredibly aggressive assaults on other heroes, dealing extraordinary amounts of damage in a '
                 'relatively small window of time, and then escaping to safety. Despite a good HP pool early on, '
                 'he lacks armor and a sizable mana pool, and as such may be unable to escape quickly enough if '
                 'caught out of position. However, with good item choices and proper judgement, Ember Spirit can '
                 'quickly snowball out of control, dominating the battlefield with blinding speed as he cheats '
                 'death. While he has only a limited presence in the early and mid game, in time Xin becomes a '
                 'dangerous opponent even on his own, proving to friend and foe alike that for them, there is '
                 'still much to be learnt.',
          'quote': 'Xin\'s teachings shall endure.',
          'strength': '19 + 2.0',
          'agility': '22 + 1.8',
          'intelligence': '20 + 1.8',
          'ms': '310',
          'tr':'0.6',
          'sr':'1800 / 800',
          'ar':'Melee',
          'miss_s':'Instant',
          'ad':'0.4 + 0.3',
          'cd':'0.00 + 0.51',
          'bat':'1.7',
          'avatar': 'img/dota/heroes/ember_spirit.png'
    },

    107: {'name': 'Earth Spirit',
          'role': 'Initiator',
          'radiant': 'true',
          'class': 'Strength',
          'bio': '<p><strong>Kaolin</strong>, the <strong>Earth Spirit</strong> a hero with the middle type of attack, '
                 'the main characteristic of which is the strength. The hero is a very versatile and useful to the '
                 'whole team. Can help to kill the enemies on the lines and be ганкером, is also very useful in the '
                 'mass battles, because of its ability to affect the region. He can act in a role of the initiator, as '
                 'his abilities can neutralize the entire enemy team. Also can act out the role of a semi-Kerry with '
                 'the proper assembling objects and lead your team to victory.</p><p>However, the ability of Kaolin '
                 'require good control and positioning, therefore it is recommended for players with an advanced '
                 'level of the game, and in any case not advisable for beginners.</p>',
          'quote': 'Through conflict, one\'s nature is revealed.',
          'strength': '21 + 2.9',
          'agility': '17 + 1.5',
          'intelligence': '18 + 2.4',
          'ms': '305',
          'tr': '0.6',
          'sr': '1800 / 800',
          'ar': 'Melee',
          'miss_s': 'Instant',
          'ad': '0.35 + 0.65',
          'cd': '0.01 + 0',
          'bat': '1.7',
          'avatar': 'img/dota/heroes/earth_spirit.png'
    },

    109: {'name': 'Terrorblade',
          'role': 'Carry',
          'radiant': 'false',
          'class': 'Agility',
          'bio': '<strong>Terrorblade</strong> is a melee Agility Carry with a focus on a limited but powerful amount '
                 'of illusions. As '
                 'any illusion based hero he requires stats-based items to make his illusions as strong as possible. '
                 'His unique ultimate allows him to swap his health bar with another hero making ganks on him '
                 'dangerous without extended lockdown to keep him from casting it. He can create long duration '
                 'illusions of himself that deal a significant amount of his own base damage and a powerful slow that '
                 'creates an unattackable illusion of target enemy hero that deals a significant amount of their base '
                 'damage. His third ability is a potent long duration transformation spell that makes him a powerful '
                 'ranged damage dealer. He has low starting health but high starting armor making him particularly '
                 'vulnerable to early game spell damage.',
          'quote': 'The self-righteous shall choke on their sanctimony.',
          'strength': '15 + 1.9',
          'agility': '22 + 3.2',
          'intelligence': '19 + 1.75',
          'ms': '315',
          'tr': '0.5',
          'sr': '1800 / 800',
          'ar': 'Melee',
          'miss_s': 'Instant',
          'ad': '0.3 + 0.6',
          'cd': '0.5 + 0.51',
          'bat': '1.5',
          'avatar': 'img/dota/heroes/terrorblade.png'
    },

    110: {'name': 'Phoenix',
          'role': 'Initiator, Disabler, Nuker',
          'radiant': 'true',
          'class': 'Strength',
          'bio': '<p>Alone across an untouched darkness gleamed the Keeper\'s first sun, a singular point of conscious '
                 'light fated to spread warmth into the empty void. Through aeons beyond count this blinding beacon '
                 'set to coalescing its incalculable energy before bursting forth the cataclysmic flare of supernova. '
                 'From this inferno raced new beacons, star progeny identical to its parent, who journeyed an unlit '
                 'ocean and settled in constellatory array. In time, they too would be made to propagate through '
                 'supernova flame. So would this dazzling cycle of birth and rebirth repeat until all skies hewn of '
                 'Titan toil deigned to twinkle and shine.</p><p>By this ageless crucible the star that mortals would '
                 'come to call Phoenix collapsed into being, and like its ancestors was thrust into an endless cosmos '
                 'to find a place among its stellar brethren. Yet curiosity toward that which the dimming elders '
                 'comfort in the darkness consumed the fledgling, and so over long cycles it inquired and studied. It '
                 'learned that among worlds both whole and broken would soon stir a nexus of remarkable variety locked '
                 'in an enduring conflict of cosmic consequence, a plane which would find itself in need of more '
                 'influence than a dying sun\'s distant rays could provide. Thus this infant son of suns took '
                 'terrestrial form, eagerly travelling to shine its warmth upon those who may need it most, and '
                 'perhaps seize upon its solar destiny.</p>',
          'strength': '17 + 2.9',
          'agility': '12 + 1.3',
          'intelligence': '18 + 1.8',
          'ms': '285',
          'tr': '1',
          'sr': '1800 / 800',
          'ar': '500',
          'miss_s': '1100',
          'ad': '0.35 + 0.633',
          'cd': '0.01 + 0.5',
          'bat': '1.7',
          'avatar': 'img/dota/heroes/phoenix.png'
    }

}