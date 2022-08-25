def recite(start, take=1):
    song = []
    left = start
    
    for _ in range(0,take):
        if left < 1:
            break
        song.append(
            '{count} {grammar} of beer on the wall, {count} {grammar} of beer.'.format(
                count= left,
                grammar= "bottles" if left > 1 else "bottle"
            )
        )
        left -= 1
        song.append(
            'Take {subject} down and pass it around, {count} {grammar} of beer on the wall.'.format(
                subject = "it" if left == 0 else "one",
                count= "no more" if left == 0 else left,
                grammar= "bottles" if left > 1 or left == 0 else "bottle"
            )
        )
        song.append('')
        
    if song != []:
        del song[-1]
        
    if start == 1:
        return song
    
    if left == 0:
        if take > start and start != 0:
            song.append('')
        song.append('No more bottles of beer on the wall, no more bottles of beer.')
        song.append('Go to the store and buy some more, 99 bottles of beer on the wall.')
    return song