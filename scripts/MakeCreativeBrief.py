
from docx import *

if __name__ == '__main__':
    # Default set of relationshipships - the minimum components of a document
    relationships = relationshiplist()

    # Make a new document tree - this is the main part of a Word document
    document = newdocument()

    # This xpath location is where most interesting content lives
    body = document.xpath('/w:document/w:body', namespaces=nsprefixes)[0]

    # Append two headings and a paragraph
    body.append(heading("Creative Brief - ", 1))
    body.append(heading('Personnel', 2))
    body.append(paragraph('Producer: '))
    body.append(paragraph('Researcher:'))
    body.append(paragraph('Scriptwriter:'))
    body.append(paragraph('Video Editor:'))

    body.append(heading('Project Location', 2))
    
    # Append a table
    tbl_rows = [ ['File Type', 'File Name', 'Link', 'Credit', 'On-Screen Credit']
               , ['Image', '', '', '', '']
               , ['Image', '', '', '', '']
               , ['Image', '', '', '', '']
               , ['Image', '', '', '', '']
               , ['Image', '', '', '', '']
               , ['Image', '', '', '', '']
               , ['Image', '', '', '', '']
               , ['Image', '', '', '', '']
               , ['Image', '', '', '', '']
               , ['Image', '', '', '', '']
               , ['Image', '', '', '', '']
               , ['Image', '', '', '', '']
               , ['Image', '', '', '', '']
               , ['Image', '', '', '', '']
               , ['Image', '', '', '', '']
               , ['Image', '', '', '', '']
               , ['Image', '', '', '', '']
               , ['Image', '', '', '', '']
               , ['Image', '', '', '', '']
               , ['Image', '', '', '', '']
               ]
    body.append(table(tbl_rows))

    # Create our properties, contenttypes, and other support files
    title    = 'Studies Weekly Creative Brief'
    subject  = 'Template to be used for all POD projects'
    creator  = 'Producer'
    keywords = ['studies weekly', 'POD', 'Video']

    coreprops = coreproperties(title=title, subject=subject, creator=creator,
                               keywords=keywords)
    appprops = appproperties()
    contenttypes = contenttypes()
    websettings = websettings()
    wordrelationships = wordrelationships(relationships)

    # Save our document
    print 'saving file...'
    savedocx(document, coreprops, appprops, contenttypes, websettings,
             wordrelationships, '/Users/chrissmith/Desktop/POD_Workflow_Files/Google Drive/CreativeBrief.docx')

