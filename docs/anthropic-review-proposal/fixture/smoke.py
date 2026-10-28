from quota import can_reserve, restore
assert can_reserve(2, 3, 10)
assert not can_reserve(8, 3, 10)
assert restore({"used": 4}, 10) == 4
try:
    restore({"used": -1}, 10)
except ValueError:
    pass
else:
    raise AssertionError("negative import accepted")
print("4 smoke checks passed")
