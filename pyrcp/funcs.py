# -*- coding: utf-8 -*-
import pyrcp.db as pydb
def get_class_name(classid):
    classes = {
        0: 'Novice',
        7: 'Knight',
        14: 'Crusader',
        1: 'Swordman',
        8: 'Priest',
        15: 'Monk',
        2: 'Mage',
        9: 'Wizard',
        16: 'Sage',
        23: 'Super Novice',
        3: 'Archer',
        10: 'Blacksmith',
        17: 'Rogue',
        24: 'Gunslinger',
        4: 'Acolyte',
        11: 'Hunter',
        18: 'Alchemist',
        25: 'Ninja',
        5: 'Merchant',
        12: 'Assassin',
        19: 'Bard',
        6: 'Thief',
        20: 'Dancer',
        4001: 'Novice High',
        4008: 'Lord Knight',
        4015: 'Paladin',
        4002: 'Swordman High',
        4009: 'High Priest',
        4016: 'Champion',
        4003: 'Mage High',
        4010: 'High Wizard',
        4017: 'Professor',
        4004: 'Archer High',
        4011: 'Whitesmith',
        4018: 'Stalker',
        4005: 'Acolyte High',
        4012: 'Sniper',
        4019: 'Creator',
        4006: 'Merchant High',
        4013: 'Assassin Cross',
        4020: 'Clown',
        4007: 'Thief High',
        4021: 'Gypsy',
        4023: 'Baby Novice',
        4030: 'Baby Knight',
        4037: 'Baby Crusader',
        4024: 'Baby Swordsman',
        4031: 'Baby Priest',
        4038: 'Baby Monk',
        4045: 'Super Baby',
        4025: 'Baby Mage',
        4032: 'Baby Wizard',
        4039: 'Baby Sage',
        4046: 'Taekwon Kid',
        4026: 'Baby Archer',
        4033: 'Baby Blacksmith',
        4040: 'Baby Rogue',
        4047: 'Taekwon Master',
        4027: 'Baby Acolyte',
        4034: 'Baby Hunter',
        4041: 'Baby Alchemist',
        4028: 'Baby Merchant',
        4035: 'Baby Assassin',
        4042: 'Baby Bard',
        4049: 'Soul Linker',
        4029: 'Baby Thief',
        4043: 'Baby Dancer',
        4054: 'Rune Knight',
        4055: 'Warlock',
        4056: 'Ranger',
        4057: 'Arch Bishop',
        4058: 'Mechanic',
        4059: 'Guillotine Cross',
        4060: 'Rune Knight (Trans)',
        4061: 'Warlock (Trans)',
        4062: 'Ranger (Trans)',
        4063: 'Arch Bishop (Trans)',
        4064: 'Mechanic (Trans)',
        4065: 'Guillotine Cross (Trans)',
        4066: 'Royal Guard (Trans)',
        4067: 'Sorcerer',
        4068: 'Minstrel',
        4069: 'Wanderer',
        4070: 'Sura',
        4071: 'Genetic',
        4072: 'Shadow Chaser',
        4073: 'Royal Guard (Trans)',
        4074: 'Sorcerer (Trans)',
        4075: 'Minstrel (Trans)',
        4076: 'Wanderer (Trans)',
        4077: 'Sura (Trans)',
        4078: 'Genetic (Trans)',
        4079: 'Shadow Chaser (Trans)',
        4080: 'Rune Knight Mount',
        4081: 'Rune Knight Mount (Trans)',
        4082: 'Royal Guard Mount',
        4083: 'Royal Guard Mount (Trans)',
        4084: 'Ranger Mount',
        4085: 'Ranger Mount (Trans)',
        4086: 'Mechanic Mount',
        4087: 'Mechanic Mount (Trans)',
        4088: 'Rune Knight Mount',
        4089: 'Rune Knight Mount (Trans)',
        4090: 'Rune Knight Mount',
        4091: 'Rune Knight Mount (Trans)',
        4092: 'Rune Knight Mount',
        4093: 'Rune Knight Mount (Trans)',
        4094: 'Rune Knight Mount',
        4095: 'Rune Knight Mount (Trans)',
        4211: 'Kagerou',
        4212: 'Oboro'
    }
    try:
        result = classes[classid]
    except:
        result = "Undefined (" + str(classid) + ")"
    return result

def get_party_name(party_id):
    db = pydb.get_db()
    cursor = db.cursor()
    sql = "SELECT `name` FROM `party` WHERE `party_id` = '%s' "
    cur = cursor.execute(sql % (party_id))
    if cur == 1:
        party = cursor.fetchone()
        name = party[0]
    else:
        name = "None"
    return name
'''
    Ranking functions
'''
def get_guilds_ranks():
    db = pydb.get_db()
    cursor = db.cursor()
    '''
        guilds[0] - Guild ID
        guilds[1] - Guild Name
        guilds[2] - Guildmaster ID
        guilds[3] - Guildmaster Name
        guilds[4] - Guild LVL
        guilds[5] - Guildmembers's average level
        guilds[6] - Guild Exp
        guilds[7] - Guild Exp
    '''
    sql = "SELECT `guild_id`, `name`, `char_id`, `master`, `guild_lv`, `average_lv`, `exp`, `emblem_len` FROM `guild` ORDER BY `guild_lv` DESC LIMIT 0, 20 "
    cur = cursor.execute(sql)
    guilds = cursor.fetchall()
    return guilds

def get_guild_members_count(guild_id):
    db = pydb.get_db()
    cursor = db.cursor()
    sql = "SELECT COUNT(`char_id`) FROM `char` WHERE `guild_id`='%s' "
    cur = cursor.execute(sql % (guild_id))
    if cur:
        count = cursor.fetchone()
    return count[0]

def get_guild_members(guild_id):
    db = pydb.get_db()
    cursor = db.cursor()
    '''
        chars[0] - Char ID
        chars[1] - Char Name
        chars[2] - Class #
        chars[3] - Base Level
        chars[4] - Job Level
        chars[5] - Online state
    '''
    sql = "SELECT `char_id`, `name`, `class`, `base_level`, `job_level`, `online`  FROM `char` WHERE `guild_id`='%s' "
    cur = cursor.execute(sql % (guild_id))
    if cur:
        chars = cursor.fetchall()
    return chars

def get_guild_info(guild_id):
    db = pydb.get_db()
    cursor = db.cursor()
    '''
        guild[0] - Guild ID
        guild[1] - Guild Name
        guild[2] - Guildmaster ID
        guild[3] - Guildmaster Name
        guild[4] - Guild LVL
        guild[5] - Guildmembers's average level
        guild[6] - Guild Exp
        guild[6] - Emblem Length
    '''
    sql = "SELECT `guild_id`, `name`, `char_id`, `master`, `guild_lv`, `average_lv`, `exp`, `emblem_len` FROM `guild` WHERE `guild_id`=%s"
    cur = cursor.execute(sql % (guild_id))
    guild = cursor.fetchone()
    return guild

def check_guild_icon(guild_id):
    db = pydb.get_db()
    cursor = db.cursor()
    '''
        guild[0] - Guild ID
        guild[1] - Guild Name
        guild[2] - Guildmaster ID
        guild[3] - Guildmaster Name
        guild[4] - Guild LVL
        guild[5] - Guildmembers's average level
        guild[6] - Guild Exp
    '''
    sql = "SELECT `emblem_len` FROM `guild` WHERE `guild_id`=%s "
    cur = cursor.execute(sql % (guild_id))
    guild = cursor.fetchone()
    if guild[0] > 0:
        return True
    else:
        return False

def get_guild_name(guild_id):
    db = pydb.get_db()
    cursor = db.cursor()
    sql = "SELECT `name` FROM `guild` WHERE `guild_id` = '%s' "
    cur = cursor.execute(sql % (guild_id))
    if cur == 1:
        guildd = cursor.fetchone()
        guild = guildd[0]
    else:
        guild = "None"
    return guild

def get_chars_ranks(start=0,count=20, order='`base_level`'):
    db = pydb.get_db()
    cursor = db.cursor()
    '''
        chars[0] - Char ID
        chars[1] - Char Name
        chars[2] - Class #
        chars[3] - Guild ID
        chars[4] - Base Level
        chars[5] - Job Level
        chars[6] - Online state
        chars[7] - Zeny amount
        chars[8] - Kills in PvP
        chars[9] - Deaths in PvP
        chars[10] - Kills on WoE
        chars[11] - Deaths on WoE
    '''
    sql = "SELECT `char_id`, `name`, `class`, `guild_id`, `base_level`, `job_level`, `online`, `zeny`, `pvp_kills`, `pvp_death`, `woe_kills`, `woe_death`  FROM `char` ORDER BY %s DESC LIMIT %s, %s "
    cur = cursor.execute(sql % (order, start, count))
    chars = cursor.fetchall()
    return chars

def get_char_info(char_id):
    db = pydb.get_db()
    cursor = db.cursor()
    '''
        chars[0] - Char ID
        chars[1] - Char Name
        chars[2] - Class #
        chars[3] - Guild ID
        chars[4] - Base Level
        chars[5] - Job Level
        chars[6] - Base Exp
        chars[7] - Job Exp
        chars[8] - Party ID
        chars[9] - Kills in PvP
        chars[10] - Deaths in PvP
        chars[11] - Kills on WoE
        chars[12] - Deaths on WoE
        chars[13] - Online state
    '''
    sql = "SELECT `char_id`, `name`, `class`, `guild_id`, `base_level`, `job_level`, `base_exp`, `job_exp`, `party_id`, `pvp_kills`, `pvp_death`, `woe_kills`, `woe_death`, `online`  FROM `char` WHERE `char_id`= '%s'"
    cur = cursor.execute(sql % (char_id))
    chars = cursor.fetchone()
    return chars