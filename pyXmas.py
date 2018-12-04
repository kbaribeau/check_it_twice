import random

def xmas(family):
  matches = []
  for giver in family:
    matches.append((giver, family[(family.index(giver)+1) % (len(family))]))
  return matches

if __name__ =='__main__':
  family = ['Mike', 'Muriel', 'Steph', 'James', 'Kevin', 'Laurier', 'Cameron']
  random.shuffle(family)
  matches = xmas(family)
  for (x,y) in matches:
    print "%s gives to %s" % (x, y)
