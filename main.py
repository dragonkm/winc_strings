# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

"""
Gullit Goal 32
Van Basten Goal 54
answer = 42
qa = f'The answer is.. {answer}'
"""
# Add your code after this line

speler2 = 'Marco van Basten'
speler1 = 'Ruud Gullit'

goal_0 = 32 
goal_1 = 54

scorers = speler1 + ' ' +  str(goal_0) + ', ' + speler2 + ' ' + str(goal_1)
report = f'{speler1} scored in the {goal_0}nd minute\n' + f'{speler2} scored in the {goal_1}th minute'

player = 'John van \'t Schip' #Escape teken om de ' te kunnen gebruiken
first_name = player[:player.find(' ')] # Zoek vanaf begin naar spatie, alles ervoor is voornaam 
last_name_len = len (player[player.find(' ')+1:]) # Incl. tussenvoegsels
name_short = player[0] + '. ' + player[player.find(' ')+1:] #Eerste letter voornaam gevolg door punt en daar tussenveogsel en achternaam
chant =  ( first_name + '! ') * (len(first_name) -1) + ( first_name + '!') # De laatste keer apart toegevoegd ivm eind spatie

good_chant = chant[-1] != ' '
print(chant)
