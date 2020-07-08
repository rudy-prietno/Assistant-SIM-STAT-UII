import falcon

class HelloWorldResource(object):
    def on_get(self, request, response):
        response.status= falcon.HTTP_200
        response.body= "Hello Wolrd main1"

class HelloWorldJson(object):
    def on_get(self, request, response):
        response.media= {'response':'Hello World main1'}

# entrypoint
app = falcon.API()

HelloWorld= HelloWorldResource()
app.add_route('/', HelloWorld)

HelloWorldJ= HelloWorldJson()
app.add_route('/json', HelloWorldJ)