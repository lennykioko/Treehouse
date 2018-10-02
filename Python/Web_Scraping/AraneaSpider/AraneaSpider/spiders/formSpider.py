from scrapy.http import FormRequest
from scrapy.spiders import Spider


class FormSpider(Spider):
    name = "horseform"
    start_urls = ["https://treehouse-projects.github.io/horse-land/form.html"]

    def parse(self, response):
        formdata = {
            "firstname": "lenny",
            "lastname": "kioko",
            "jobtitle": "developer"
        }

        return FormRequest.from_response(
            response,
            formnumber=0,
            formdata=formdata,
            callback=self.after_post)

    def after_post(self, response):
        print(
            "\n***********\n\n Form processed \n\n***********\n\n {}\n\n***********\n"
            .format(response))
