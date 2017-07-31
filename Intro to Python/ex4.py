# SOLUTIONS Ex. 4

kings = ['charles', 'louis', 'napoleon', 'henry']


def show_kings(king_list):
    for king in king_list:
        print(king.title())


def make_great(king_list):
    for index in range(len(king_list)):
        king_list[index] += " the Great"

show_kings(kings)
make_great(kings)
show_kings(kings)
