
import re
points = re.compile(r'0\...')
scores = "[BodyPart:1-(0.50, 0.30) score=0.50 BodyPart:2-(0.45, 0.28) score=0.48 BodyPart:3-(0.39, 0.30) score=0.26 BodyPart:4-(0.54, 0.26) score=0.12 BodyPart:5-(0.56, 0.30) score=0.39 BodyPart:6-(0.62, 0.30) score=0.60 BodyPart:7-(0.59, 0.31) score=0.56 BodyPart:8-(0.44, 0.44) score=0.44 BodyPart:9-(0.45, 0.64) score=0.66 BodyPart:10-(0.45, 0.82) score=0.82 BodyPart:11-(0.54, 0.45) score=0.47 BodyPart:12-(0.52, 0.63) score=0.66 BodyPart:13-(0.52, 0.81) score=0.83 BodyPart:16-(0.52, 0.28) score=0.09"
f = points.findall(scores)
points, scores = [float(f[i]) for i in range(len(f)) if i%3!=2], [float(f[i]) for i in range(len(f)) if i%3==2]
print(f'points = {points}',f'scores = {scores}', sep='\n')