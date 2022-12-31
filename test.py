import pandas as pd
import numpy as np

output = [['a','u','j','v','d','ha','s','d','t','r'],
          ['a','u','j','v','d','ha','s','d','t','r'],
          ['a','u','j','v','d','ha','s','d','t','r'],
          ['a','u','j','v','d','ha','s','d','t','r'],
          ['a','u','j','v','d','ha','s','d','t','r'],
          ['a','u','j','v','d','ha','s','d','t','r']]

df = pd.DataFrame(output)

cls = df[:, 6]

print(cls)
