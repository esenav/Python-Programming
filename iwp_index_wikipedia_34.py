#******************************************************************************

#                        iwp_index_wikipedia_34.py

#******************************************************************************

from whoosh.index import *
from whoosh.fields import *
from whoosh import scoring

import xml.etree.ElementTree as ET

#------------------------------------------------------------------------------
#
# Create an initial index from files in a directory.

def iwp_create_index():

    schema = Schema( title=TEXT( stored=True ), 
        path=ID( stored=True ), content=TEXT )
    ix = create_in( "indexdir2", schema )
    writer = ix.writer()
    
    import glob
    files = glob.glob( 'c:\\wikipedia\\resources\\wikipedia\\processed\\*\\*.xml' )

    for file in files:

        if file.find( 'part-60000\\1166530' ) == -1:
            tree = ET.parse( file )
            doc_elem = tree.getroot()
            doc_text = ''.join( doc_elem.itertext() )
            print( file )
            writer.add_document( path=file, content=doc_text )

    writer.commit()

#------------------------------------------------------------------------------
#
# Query an existing index using standard BM25 OKAPI weighting function.

def iwp_query_index_bm25( query ):

    ix = open_dir("indexdir2")
    from whoosh.qparser import QueryParser
    with ix.searcher() as searcher:
        query = QueryParser("content", ix.schema).parse( query )
        results = searcher.search( query, limit=20 )
        print( len( results ) )

        for result in range( 0, results.scored_length() ):

            print( results[ result ] )

#------------------------------------------------------------------------------
#
# Query an existing index using TF_IDF weighting function.

def iwp_query_index_tf_idf( query ):

    ix = open_dir("indexdir2")
    from whoosh.qparser import QueryParser
    with ix.searcher( weighting=scoring.TF_IDF() ) as searcher:
        query = QueryParser("content", ix.schema).parse( query )
        results = searcher.search( query, limit=20 )
        print( len( results ) )

        for result in range( 0, results.scored_length() ):

            print( results[ result ] )
