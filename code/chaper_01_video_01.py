import pandas as pd

link = "https://3083218.youcanlearnit.net/geographytables.html"

area_data = pd.read_html(link)

area_data = area_data.pop()

print(area_data)
