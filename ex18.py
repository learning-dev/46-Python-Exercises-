def beer_song():
    for i in range(99,-0,-1):
      # print "%d bottles of beer on the wall, %d bottles of beer."% (i, i )
      # print "Take one down, pass it around, %d bottles of beer on the wall." % (i-1)
      print "{} bottles of beer on the wall, {} bottles of beer." .format (i, i)
      print "Take one down, pass it around, {} bottles of beer on the wall." .format(i-1)



beer_song()