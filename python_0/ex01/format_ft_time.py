import time
from datetime import datetime

# Obtenir le timestamp actuel
timestamp = time.time()

# Formatage du timestamp avec virgules
formatted_timestamp = f"{timestamp:,.4f}"

# Notation scientifiques
scientific = f"{timestamp:.2e}"

# Date lisible
readable_date = datetime.now().strftime("%b %d %Y")

# Affichage
print(f"Seconds since January 1, 1970: {formatted_timestamp} or {scientific} in scientific notation")
print(readable_date)