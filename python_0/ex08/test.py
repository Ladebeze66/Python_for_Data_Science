from tqdm import tqdm
import time

for i in tqdm(range(100)):
    time.sleep(0.01)
# Affiche : 100%|██████████| 100/100 [00:01<00:00, 99.00it/s]