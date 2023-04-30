"Here we have our class with the callable functions"

import requests


class Works:
    "creates the self variables"

    def __init__(self, oaid):
        "creates the self variables"
        self.oaid = oaid
        self.req = requests.get(f"https://api.openalex.org/works/{oaid}")
        self.data = self.req.json()

    def bibtex(self):
        "gets and parses data from OpenAlex and returns the reference in the bibtex format"
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

        reference = (
            f"@article{{{authors[0]}{year},\nauthor = {{{authors}}},\njournal ="
            f"{{{journal}}},\ntitle = {{{title}}},\nvolume = {{{volume}}},\nissue ="
            f"{{{issue1}}},\npages = {{{pages}}},\nyear = {{{year}}}\n}}"
        )

        return reference

    def ris(self):
        "gets and parses data from OpenAlex and returns the reference in the bibtex format"
        fields = []
        if self.data["type"] == "journal-article":
            fields += ["TY  - JOUR"]
        else:
            raise Exception("Unsupported type {self.data['type']}")

        for author in self.data["authorships"]:
            fields += [f'AU  - {author["author"]["display_name"]}']

        fields += [f'PY  - {self.data["publication_year"]}']
        fields += [f'TI  - {self.data["title"]}']
        fields += [f'JO  - {self.data["host_venue"]["display_name"]}']
        fields += [f'VL  - {self.data["biblio"]["volume"]}']

        if self.data["biblio"]["issue"]:
            fields += [f'IS  - {self.data["biblio"]["issue"]}']

        fields += [f'SP  - {self.data["biblio"]["first_page"]}']
        fields += [f'EP  - {self.data["biblio"]["last_page"]}']
        fields += [f'DO  - {self.data["doi"]}']
        fields += ["ER  -"]

        ris = "\n".join(fields)

        return ris

