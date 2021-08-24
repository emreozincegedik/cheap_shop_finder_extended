from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from scrape import Scraper
app = Flask(__name__)
api = Api(app)

search_args = reqparse.RequestParser()
search_args.add_argument(
    "query", type=str, help="Arama yapılacak kelime(ler) lazım", required=True)
search_args.add_argument(
    "website", help="Arama yapılacak site(ler) lazım. Ör: ['hepsiburada','amazon']", action="append", required=True)


class HelloWorld(Resource):
    def get(self):
        return {"data": "Hello world"}

    def post(self):
        print(request.form)
        args = search_args.parse_args()
        scraper = Scraper(args["query"])
        items = scraper.runThread(args["website"])

        return items


api.add_resource(HelloWorld, "/helloworld")


@app.route('/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)
