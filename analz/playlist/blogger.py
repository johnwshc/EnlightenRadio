import requests
from jinja2 import Environment, select_autoescape, FileSystemLoader


class erBlogger:
    blogger_api_key = 'AIzaSyBfVB6vTPwTBrWcCLi_NK4kPxOcBh_xjNI'
    blogger_client_id = '946832198726-eub0q1jk1b46emlsqdrbsj3aupsij1ue.apps.googleusercontent.com'
    client_secret = 'kDiIp5JzdDVOeQrhdfGveiZ1'
    blogger_client_id2 = '946832198726-eub0q1jk1b46emlsqdrbsj3aupsij1ue.apps.googleusercontent.com'
    bloger_api_key2 = 'AIzaSyD862XP1RJesWfqiGwTMQW3p47A3wgw-dk'
    er_player_blogID = '7248995940539759558'
    params = {'installed':
                     {'client_id':
                          '946832198726-eub0q1jk1b46emlsqdrbsj3aupsij1ue.apps.googleusercontent.com',
                      'project_id':'bloggertools-170622',
                      'auth_uri':'https://accounts.google.com/o/oauth2/auth',
                      'token_uri':'https://oauth2.googleapis.com/token',
                      'auth_provider_x509_cert_url':'https://www.googleapis.com/oauth2/v1/certs',
                      'client_secret':'kDiIp5JzdDVOeQrhdfGveiZ1',
                      'redirect_uris':['http://localhost']
                      }
                 }

    @staticmethod
    def get_er_player_blog():
        req = f'https://www.googleapis.com/blogger/v3/blogs/{erBlogger.er_player_blogID}'
        payload = {'key': erBlogger.blogger_api_key}
        r = requests.get(req, params=payload)

        return r.text

    @staticmethod
    def get_blogger_info(argv=''):
        from oauth2client import client
        from googleapiclient import sample_tools
        service, flags = sample_tools.init(
            argv, 'blogger', 'v3', __doc__, __file__,
            scope='https://www.googleapis.com/auth/blogger')

        try:
            blogs = service.blogs()
            jblog = blogs.get(blogId=erBlogger.er_player_blogID)
            return jblog.execute()

        except client.AccessTokenRefreshError:
            print('The credentials have been revoked or expired, please re-run'
                  'the application to re-authorize')


    @staticmethod
    def _getBody(m3u):


        jf = {
          "author": { # The author of this Post.
            "displayName": "The Red Caboose", # The display name.
            "id": "jcase", # The identifier of the creator.
            "image": { # The creator's avatar.
              "url": "https://www.enlightenradio.org", # The creator's avatar URL.
            },
            "url": "http://www.enlightenradio.org" # The URL of the creator's Profile page.
          },
          "blog": { # Data about the blog containing this Post.
            "id": f"{erBlogger.er_player_blogID}", # The identifier of the Blog that contains this Post.
          },
          "content": f"{m3u.simple_html}", # The content of the Post. May contain HTML markup.
          "kind": "blogger#post",  # The kind of this entity. Always blogger#post.

        }
        return jf
    @staticmethod
    def insert_playlist(bdy):
        from oauth2client import client
        from googleapiclient import sample_tools
        service, flags = sample_tools.init(
            '', 'blogger', 'v3', __doc__, __file__,
            scope='https://www.googleapis.com/auth/blogger')
        body = erBlogger._getBody(bdy)

        try:
            posts = service.blogs()
            jpost = posts.insert(erBlogger.er_player_blogID, body=bdy)
            return jpost.execute()

        except client.AccessTokenRefreshError:
            print('The credentials have been revoked or expired, please re-run'
                  'the application to re-authorize')

class XBody:
    def __init__(self,m3u):
        env = Environment(
            loader=FileSystemLoader("templates"),
            # autoescape=select_autoescape()
        )
        template = env.get_template("er_blogger.html")
        self.pl_htm = template.render(m3u=m3u)

