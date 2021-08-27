from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort
from scrape import Scraper
app = Flask(__name__)
api = Api(app)

search_args = reqparse.RequestParser()
search_args.add_argument(
    "query", type=str, help="Arama yapılacak kelime(ler) lazım", required=True)
search_args.add_argument(
    "website", help="Arama yapılacak site(ler) lazım. Ör: ['hepsiburada','amazon']", action="append")
search_args.add_argument(
    "page", type=int, help="Sonuçların kaçıncı sayfasını istiyorsunuz?")
search_args.add_argument("low_limit", type=int,
                         help="Sonuçların parası en az ne kadar olsun?")
search_args.add_argument("high_limit", type=int,
                         help="Sonuçların parası en fazla ne kadar olsun?")
search_args.add_argument("ascending", type=bool, choices=(True, False),
                         help="Küçükten büyüğe (true), büyükten küçüğe (false)")


class HelloWorld(Resource):
    def __init__(self):
        self.item_count_in_page = 10

    def get(self):
        return {"data": "Hello world"}

    def post(self):
        print(request.form)
        args = search_args.parse_args()
        if args["low_limit"] != None and args["high_limit"] != None and args["high_limit"] < args["low_limit"]:
            return abort(417, description="low_limit high_limit ten küçük olmalı")
        scraper = Scraper(args["query"])

        items = scraper.runThread(args["website"])
        # price'a göre sortla (küçükten büyüğe)
        items = sorted(items, key=lambda k: k['price'])

        # price'a göre büyükten küçüğe
        if args["ascending"] != None and args["ascending"] == False:
            items = sorted(items, key=lambda k: k['price'], reverse=True)

        # low_limitten büyükleri tut
        if args["low_limit"] != None:
            items = [item for item in items if item["price"]
                     >= args["low_limit"]]
        # high_limitten düşükleri tut
        if args["high_limit"] != None:
            items = [item for item in items if item["price"]
                     <= args["high_limit"]]

        # items listesini 10 item olacak şekilde sayfalara ayır
        items = [items[i:i + self.item_count_in_page]
                 for i in range(0, len(items), self.item_count_in_page)]
        if args["page"] != None:
            if args["page"] > len(items) or args["page"] <= 0:
                return {"total_page_count": len(items), "page": []}
            return {"total_page_count": len(items), "page": items[args["page"]-1]}

        return {"total_page_count": len(items), "page": items[0]}


api.add_resource(HelloWorld, "/helloworld")


@app.route('/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)
