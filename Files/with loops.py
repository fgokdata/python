sea = open("fishes.txt", 'r')   

for line in sea:
    print(line)

sea.close()

#output

Orca is a kind of Dolphin.

Blue Whale is the largest animal known on earth.

Sharks are the sister group to the Rays (batoids).

The Tuna Fish can weigh up to 260 kg.

Squid and Octopus are in the same class.


#######

sea = open("fishes.txt", 'r')   

for line in sea.readlines():
    print(line)

sea.close()

#output

Orca is a kind of Dolphin.

Blue Whale is the largest animal known on earth.

Sharks are the sister group to the Rays (batoids).

The Tuna Fish can weigh up to 260 kg.

Squid and Octopus are in the same class.