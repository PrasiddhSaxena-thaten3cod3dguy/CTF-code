from lxml import etree

def parse_xml(xmlstring):
    if "file://" in xmlstring:
        return {}
        
    parser = etree.XMLParser(load_dtd=True, no_network=False)
    root = etree.fromstring(xmlstring, parser=parser)

    title = root.xpath('title/text()')[0]
    desc = root.xpath('desc/text()')[0]

    return {"title": title, "desc": desc}