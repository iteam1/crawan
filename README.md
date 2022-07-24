<img src="https://img.shields.io/badge/license-MIT-green" /><img src="https://img.shields.io/badge/version-v0.1-lightgrey" />

<p align="center">
<a href="https://fontmeme.com/graffiti-creator/"><img src="https://fontmeme.com/permalink/220718/cf83fc275ade5340b6aa24c10b4d879f.png" alt="graffiti-creator" border="0"></a>
</p>

### crawan

crawler and analyzer informations from internet

### intro

Do you ever have these questions?

*Should i be a backend or frontend developer to get more money ?* 

*What skills i need to get for apply data scientist ?*

*Which things related to 'UI/UX'?*

*How much do i desired ?*
  
crawan will give you these answer by crawl data from many sources and analyze them.

### references

[1] [docs/elements-of-python-style.md](https://github.com/amontalenti/elements-of-python-style)

[2] [docs/codestyle.md](https://github.com/updog/codestyle)

### tools

|No|name|descript|
|---|---|---|
|01|[Graffiti Font](https://fontmeme.com/graffiti-creator/)|auto generate graffiti font|
|02|[diagrameditor](https://www.diagrameditor.com/)|drawing UML diagram|
|03|[codebeautify](https://codebeautify.org/htmlviewer)|prettify html|

### libraries

Each time you install new lib, please note.there are 2 os-system using for this repo `linux-ubuntu` and `windows`

    requests
    requests-html
    beautifulsoup4
    selenium
    lxml
    html5lib
    prettytable
    tqdm
    time
    argparse

**windows**
- create virtual environment: `virtualenv env`
- activate virtual environment: `cd env/Script` + `activate`
- install libraries follow the requirements: `pip install -r windows-requirements.txt`
- deactivate: `deactivate`

**ubuntu**
- create virtual environment: `virtualenv env`
- activate virtual environment: `source env/bin/activate`
- install libraries follow the requirements: `pip install -r ubuntu-requirements.txt`
- deactivate: `deactivate` 
