import python_avatars as pa

for i in range(1000):
    # Completely random avatar
    random_avatar = pa.Avatar.random(background_color='rgba(0,0,0,0.0')
    # Save to a file
    random_avatar.render("avatar_" + str(i) + ".svg")
