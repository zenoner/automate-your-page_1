TopHTML = '''<!DOCTYPE HTML>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title> Udacity Nanodegree </title>
    <link href="css/style.css" rel="stylesheet" type="text/css"/>
</head>
<body>
   <h1>Udacity Nanodegree: Intro to Programming</h1>
  <div class="lesson"> 
    <h2>Stage 1: Web Development</h2>
  <h3>Unti 1: Basics of the Web</h3>'''

print TopHTML

def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)

EXAMPLE_LIST_OF_CONCEPTS = [ ['The Web', 'HTML (Hyper Text Markup Language)is a basic for the web. The computer program that operates on the computer  display HTML files that is found on the web, to link to the internet, then it connects to the servers where the host carries the files that make up the websites. '],
                             ['HTML', 'an create the text content, markup, and references to other documents, such as images & videos, link to another web page. '],
                             ['More information about HTML', 'HTML Whitespacecan turn everything into one line. Using br tag can seperate the content into multiple lines. Using <i>p tag</i> is another option but it is great for paragraphy.'] ]


def make_HTML_for_many_concepts(list_of_concepts):
    HTML = ""
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML


Unit2 = "<h3>Unit 2: Creating a Structured Document with HTMl</h3>"

print Unit2

def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)

EXAMPLE_LIST_OF_CONCEPTS = [ ['The Page Structure ', 'The website is alike building : The HTML is the structure, CSS isthe styling, and Javascript is the functional objects. '],
                             ['HTML, CSS, and DOM','HTML is a language with syntax , CSS is a language that uses syntax to change and design how elements look on the page. '],
                             ['More information about HTML', 'HTML Whitespacecan turn everything into one line. Using br tag can seperate the content into multiple lines. Using <i>p tag</i> is another option but it is great for paragraphy.'] ]


def make_HTML_for_many_concepts(list_of_concepts):
    HTML = ""
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML

def main():
    print make_HTML_for_many_concepts(EXAMPLE_LIST_OF_CONCEPTS)
    print Unit2
    print make_HTML_for_many_concepts(EXAMPLE_LIST_OF_CONCEPTS)
    
main()
