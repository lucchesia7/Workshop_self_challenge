"""
att_roll + bonus >= armor_class

Damage
More description of combat rolls
Crits

"""
import random


def roll_d20():
    return random.randint(1, 20)


class CombatUnit:

    def __init__(self, name, attack_bonus, armor_class):
        self.name = name
        self.attack_bonus = attack_bonus
        self.armor_class = armor_class


def combat_turn(attacker: CombatUnit, defender: CombatUnit):
    att_roll = roll_d20() + attacker.attack_bonus
    if att_roll >= defender.armor_class:
        return f"{attacker} Hit {defender}"
    else:
        return f"{attacker} Miss {defender}"


def combat_round(unit_1, unit_2):
    c1 = combat_turn(unit_1, unit_2)
    c2 = combat_turn(unit_2, unit_1)


if __name__ == '__main__':
    unit_1 = CombatUnit("Wizard", attack_bonus=3, armor_class=14)
    unit_2 = CombatUnit("Dragon", attack_bonus=5, armor_class=18)


""" Details
Wizard 20 vs Dragon 13
Damage Delt, per round?
Health <= 0 Death?
Who Won?

Do we need every stat in the training data?

- Every training input requires input for predictions!!!
"""
