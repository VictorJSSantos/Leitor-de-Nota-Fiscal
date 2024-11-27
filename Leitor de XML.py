import xml.etree.ElementTree as ET
import pandas as pd
import glob
from datetime import datetime

directory = r"path_to_files/*.xml"

xml_file = glob.glob(directory)


def parse_XML(xml_file):
    qtd = []
    pesob = []
    pesol = []
    nf = []
    dh = []
    rows = []
    ordem = []
    destino = []
    df_cols = ["Data", "Destino", "Ordem", "NF", "Vol #", "Peso Bruto", "Peso Líquido"]

    for file in xml_file:
        xml_file = file
        tree = ET.parse(xml_file)
        root = tree.getroot()
        sub = root[0][0]
        qtd = []
        pesob = []
        pesol = []
        nf = []
        dh = []
        ordem = []
        destino = []

        for child in sub.iter():
            # print(child)
            if child.tag == "{http://www.portalfiscal.inf.br/nfe}qVol":
                qtd = float(child.text)

            if child.tag == "{http://www.portalfiscal.inf.br/nfe}pesoB":
                pesob = float(child.text)

            if child.tag == "{http://www.portalfiscal.inf.br/nfe}pesoL":
                pesol = float(child.text)

            if child.tag == "{http://www.portalfiscal.inf.br/nfe}nNF":
                nf = float(child.text)

            if child.tag == "{http://www.portalfiscal.inf.br/nfe}dhEmi":
                dh = child.text[:10]
                dh = datetime.strptime(dh, "%Y-%m-%d").date()

            if child.tag == "{http://www.portalfiscal.inf.br/nfe}dest":
                destino = child[1].text

            if child.tag == "{http://www.portalfiscal.inf.br/nfe}infCpl":
                ordem = child.text.split("\\n\\n")
                ordem = ordem[1][-5:]
                ordem = int(ordem)

        rows.append(
            {
                "Destino": destino,
                "NF": nf,
                "Vol #": qtd,
                "Peso Bruto": pesob,
                "Peso Líquido": pesol,
                "Data": dh,
                "Ordem": ordem,
            }
        )

        df_cols = [
            "Data",
            "Destino",
            "Ordem",
            "NF",
            "Vol #",
            "Peso Bruto",
            "Peso Líquido",
        ]

    out_df = pd.DataFrame(rows, columns=df_cols)
    out_df.to_excel(
        r"Results.xlsx",
        index=False,
        header=True,
    )
    return print(out_df)


parse_XML(xml_file)
