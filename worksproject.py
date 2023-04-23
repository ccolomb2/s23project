import time
import requests
import base64
import matplotlib.pyplot as plt
from IPython.core.pylabtools import print_figure

class Works:
    def __init__(self, oaid):
        self.oaid = oaid
        self.req = requests.get(f'https://api.openalex.org/works/{oaid}')
        self.data = self.req.json()

    def __str__(self):
        return 'str'
        
    def __repr__(self):
        _authors = [au['author']['display_name'] for au in self.data['authorships']]
        
        if len(_authors) == 1:
            authors = _authors[0]
        elif len(_authors) > 1:
            authors = ', '.join(_authors[0:-1]) + ' and' + _authors[-1]
            
        else: 
            authors = 'No authors reported on database.'
            
        title = self.data['title']
        
        journal = self.data['host_venue']['display_name']
        volume = self.data['biblio']['volume']
        
        issue = self.data['biblio']['issue']
        if issue is None:
            issue = ', '
        else:
            issue = issue

        pages = '-'.join([self.data['biblio'].get('first_page', '') or '',
                          self.data['biblio'].get('last_page', '') or ''])
        year = self.data['publication_year']
        citedby = self.data['cited_by_count']
        
        oa = self.data['id']
        s = f'author = {{{authors}}}, \n journal = {{{journal}}}, \n title = {{{title}}}, \n volume  ={{{volume}}}, \n issue  = {{{issue}}},  \n pages = {{{pages}}}, \n year = {{{year}}}'
        return s
             
    
    def bibtex(self):
        rworks = Works(self.data['id'])
        return rworks
    
     @property 
    def ris(self):
        fields = []
        if self.data['type'] == 'journal-article':
            fields += ['TY  - JOUR']
        else:
            raise Exception("Unsupported type {self.data['type']}") #raise...
        
        for author in self.data['authorships']: #for each author, do a line
            fields += [f'AU  - {author["author"]["display_name"]}']
            
        fields += [f'PY  - {self.data["publication_year"]}']
        fields += [f'TI  - {self.data["title"]}']
        fields += [f'JO  - {self.data["host_venue"]["display_name"]}']
        fields += [f'VL  - {self.data["biblio"]["volume"]}']
        
        if self.data['biblio']['issue']:
            fields += [f'IS  - {self.data["biblio"]["issue"]}']
        
        
        fields += [f'SP  - {self.data["biblio"]["first_page"]}']
        fields += [f'EP  - {self.data["biblio"]["last_page"]}']
        fields += [f'DO  - {self.data["doi"]}']
        fields += ['ER  -']
                
        ris = '\n'.join(fields)
        ris64 = base64.b64encode(ris.encode('utf-8')).decode('utf8')
        uri = f'<pre>{ris}<pre><br><a href="data:text/plain;base64,{ris64}" download="ris">Download RIS</a>' #<pre> makes it appear in different lines
        from IPython.display import HTML
        return HTML(uri) #so as a link- html is making hyperlink
        
