import math
ag= int(input('Digite o angulo que você deseja?'))
seno = math.sin(math.radians(ag))
print(' O angulo de {} tem o SENO DE {:.2f}'.format(ag,seno))
cos = math.cos(math.radians(ag))
print(' O angulo de {} tem o COSSENO DE {:.2f}'.format(ag,cos))
tang= math.tan(math.radians(ag))
print(' O angulo de {} tem o TANGENTE DE {:.2f}'.format(ag,tang))
