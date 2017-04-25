inv = {'tomato': 5, 'meat': 6, 'potato': 7}
loot = {'coin': 1, 'torch': 3, 'dagger': 4, 'meat' : 5}

for k, v in loot.items():
	inv.setdefault(k, v)


for k, v in inv.items():
	if k not in loot.items():
		print(str(v) +' '+ str(k))
	else:
		v = v + v

