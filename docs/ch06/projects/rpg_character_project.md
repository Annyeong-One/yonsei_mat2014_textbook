# RPG Character System Project


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

## Overview
Build a complete RPG (Role-Playing Game) character system using inheritance and polymorphism.

## Objectives
- Design a class hierarchy for different character types
- Implement combat mechanics using polymorphism
- Create character abilities and skills
- Manage character stats and leveling

## Requirements

### 1. Base Character Class
Create an abstract `Character` class with:
- Attributes: name, level, health, max_health, attack, defense, experience
- Methods:
  - `take_damage(amount)` - reduce health, check if alive
  - `heal(amount)` - restore health (max = max_health)
  - `is_alive()` - return True if health > 0
  - `gain_experience(amount)` - add XP, level up if threshold reached
  - `level_up()` - increase stats when leveling up
  - `get_stats()` - return character statistics
  - Abstract method: `special_ability()` - unique to each character type

### 2. Character Classes
Implement these character types:

**Warrior**
- High health and defense
- Moderate attack
- Special ability: "Power Strike" - deals 2x attack damage
- Gains +10 health, +3 attack, +2 defense per level

**Mage**
- Low health and defense
- High attack (magical)
- Special ability: "Fireball" - deals 3x attack damage but costs health
- Gains +5 health, +5 attack, +1 defense per level

**Rogue**
- Moderate health
- High attack
- Low defense
- Special ability: "Backstab" - deals 2.5x attack damage, 30% chance to dodge next attack
- Gains +7 health, +4 attack, +1 defense per level

**Healer**
- Moderate health
- Low attack
- Moderate defense
- Special ability: "Holy Light" - heals self for 50% max health
- Gains +8 health, +2 attack, +3 defense per level

### 3. Combat System
Create a `Battle` class that:
- Manages turn-based combat between two characters
- Allows characters to attack or use special abilities
- Displays combat log
- Determines winner
- Awards experience to winner

### 4. Character Party
Create a `Party` class that:
- Stores multiple characters
- Has methods to add/remove characters
- Calculate total party stats
- Find character by name
- Display all party members

## Sample Combat Flow
```
=== BATTLE START ===
Warrior (HP: 100/100) vs Mage (HP: 60/60)

Turn 1:
Warrior attacks Mage for 15 damage!
Mage HP: 45/60

Turn 2:
Mage uses Fireball! Deals 45 damage!
Warrior HP: 55/100

... combat continues ...

=== BATTLE END ===
Winner: Warrior
Experience gained: 150
```

## Bonus Features
- Add status effects (poison, stun, etc.)
- Implement equipment system
- Add character skills tree
- Create AI for computer-controlled characters
- Add multiplayer party battles

## Testing Requirements
Your implementation should:
1. Create one of each character type
2. Display their initial stats
3. Simulate a battle between two characters
4. Show leveling up
5. Demonstrate all special abilities
6. Test party management

## Files to Create
- `characters.py` - All character classes
- `battle.py` - Combat system
- `party.py` - Party management
- `main.py` - Demo program
- `README.md` - This file

Good luck, adventurer! 🗡️
