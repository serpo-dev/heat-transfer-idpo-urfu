import requests
from bs4 import BeautifulSoup as bs4

def density():
    url = "https://www.freechemistry.ru/sprav/pl-h2o.htm"
    page = requests.get(url)

    if (page.status_code == 200):
        soup = bs4(page.text, "lxml")
        tables = soup.findAll("table", attrs={"id": "datatable"})

        def parse_table(table):
            values = []
            for x in table:
                cell = x.text.replace("\n", "").replace(",", ".")
                values.append(cell)
            values = values[2:]
            t = []
            d = []
            for i, x in enumerate(values):
                print(x)
                if (i % 2 == 0):
                    t.append(int(x))
                else:
                    d.append(float(x))
            
            return (t, d)
        
        t_all = []
        d_all = []
        for table in tables:
            td = table.findAll("td")
            t, d = parse_table(td)
            t_all += t
            d_all += d

        if (len(t_all) == len(d_all)):
            print("SUCCESS")
            print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
            print("ALl temperatures:")
            print(t_all)
            print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
            print("All density values:")
            print(d_all)

def specific_heat():
    url = "https://dpva.ru/Guide/GuideMedias/GuideWater/GuideWater1bar0to100deg/"
    page = requests.get(url)

    if (page.status_code == 200):
        soup = bs4(page.text, "lxml")
        table = soup.find("table", attrs={"border": "2"})
        all_rows = table.findAll("tr")
        rows = []
     
        for tr in all_rows:
            if not tr.has_attr("bgcolor"):
                rows.append(tr)
            elif tr.attrs["bgcolor"] == "#cccccc":
                continue
            rows.append(tr)
        t = []
        ch = []
        for i, row in enumerate(rows):
            if (i % 2) != 0:
                td = row.findAll("td")
                t.append(int(float((td[0].text))))
                ch.append(float(td[5].text))

        if (len(t) == len(ch)):
            print("SUCCESS")
            print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
            print("ALl temperatures:")
            print(t)
            print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
            print("All density values:")
            print(ch)


# density()
# specific_heat()