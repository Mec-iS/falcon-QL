__author__ = 'Lorenzo'



from lib.graphql.parser import GraphQLParser


def parse_graphql():
    parser = GraphQLParser()
    ast = parser.parse("""
    {
      user(id: 4) {
        id
        name
        profilePic
        avatar: profilePic(width: 30, height: 30)
      }
    }
    """)
    print(ast)
    return ast
