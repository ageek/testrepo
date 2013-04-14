import solr

# create a connection to a solr server
s = solr.SolrConnection('http://x.x.x.x:8983/solr/posts')

# add a document to the index
s.add(id='twitter_288536056058490880', author_name='harpreet2013', source='twitter',post_id='288536056058490880' )
s.commit()

# do a search
response = s.query('title:harpreet2013')
for hit in response.results:
    print hit['title']
