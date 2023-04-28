"creates the self variables"

# import base64
import requests
# from IPython.display import HTML


class Works:
    "creates the self variables"
    def __init__(self, oaid):
        "creates the self variables"
        self.oaid = oaid
        self.req = requests.get(f"https://api.openalex.org/works/{oaid}")
        self.data = self.req.json()

    # @property
    def ris(self):
        "creates the self variables"
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
                
        # ris = '\n'.join(fields)
        # return ris
        for field in fields:
            print(field)

    def __repr__(self):
        "creates the self variables"
        _authors = [au["author"]["display_name"] for au in self.data["authorships"]]

        if len(_authors) == 1:
            authors = _authors[0]
        elif len(_authors) > 1:
            authors = ", ".join(_authors[0:-1]) + " and " + _authors[-1]

        else:
            authors = "No authors reported on database."

        title = self.data["title"]

        journal = self.data["host_venue"]["display_name"]
        volume = self.data["biblio"]["volume"]

        issue_ = self.data["biblio"]["issue"]
        if issue_ is None:
            issue1 = "-"
        else:
            issue1 = issue_

        pages = "-".join(
            [
                self.data["biblio"].get("first_page", "") or "",
                self.data["biblio"].get("last_page", "") or "",
            ]
        )
        year = self.data["publication_year"]

        reference = (f'author = {{{authors}}},\njournal = {{{journal}}},\ntitle = {{{title}}},'
        f'\nvolume = {{{volume}}},\nissue  = {{{issue1}}},'
        f'\npages = {{{pages}}},\nyear = {{{year}}}')

        return reference

    def bibtex(self):
        "creates the self variables"
        rworks = Works(self.data["id"])
        return rworks
