from channeltype.tmod import test_adder
print(test_adder(20,10))

# preferably one should load a module
# as in both cases the loading of the module will take place
# in a large code file it would be simple to know hat function came from what module in the style below
# and a reload would reload function definitioins also whereas that would not happen in the
# single function import case above

# import channeltype.tmod
# print(channeltype.tmod.test_adder(3,4))
