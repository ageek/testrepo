import urllib
from urllib2 import *
import json
import solr



doc2  = {'id'= 'twitter_288536056058490880','application_name'= '<a href="http=//www.snsanalytics.com">SNS Analytics</a>',
         'no_of_reshares'= '0', 'original_post_id'= '-1', 'gender_guessed'= 'True',
         'text'= 'COCA-COLA ENTER = Coca-Cola Enterprises, Inc. to Webcast Fourth-Quarter ... - 4 http=//t.co/lmm9VN8R',
         'author_display_name'= 'Coca-Cola 24x7', 'author_name'= 'CocaCola24x7', 'post_id'= '288536056058490880',
         'author_gender'= 'unknown', 'no_of_likes'= '0', 'author_location'= 'San Francisco', 'no_of_comments'= '0',
         'user_id'= '11', 'language'= 'es', 'sentiment'= 'neg', 'link_url'= "[u'http=//sns.mx/1riTy7']",
         'profile_update_status'= 'done', 'to_author_id'= '0', 'no_of_ratings'= '0',
         'created_at'= '2013-01-08T06=42=11Z', 'source'= 'twitter', 'sentiment_score'= '-12.6163801146',
         'avatar'= 'http=//a0.twimg.com/profile_images/1159285674/Coca-Cola_normal.jpg', 'rating_average'= '0.0',
         'no_of_dislikes'= '0', '_version_'= '1424489826740076544', 'author_id'= '190136337', 'no_of_views'= '0',
         'search_id'= '908', 'crawl_time'= '1358273679052'}

s = solr.SolrConnection('http=//x.x.x.x:8983/solr/posts')

s.add(doc2)
s.commit()
s.close()


