import scrapy


class EpltoptenSpiderSpider(scrapy.Spider):
    name = "epltopten_spider"
    allowed_domains = ["1xbet.whoscored.com"]
    start_urls = ["https://1xbet.whoscored.com/regions/252/tournaments/2/seasons/10316/stages/23400/playerstatistics/england-premier-league-2024-2025s"]

    def parse(self, response):
        players = response.css("tbody#player-table-statistics-body")

        for player in players:
            yield {
                "name": player.css('td:nth-child(1)::text').get(),
                "Games": player.css('td:nth-child(3)::text').get(),
                'Goals': player.css("td.goal::text").get(),
                'Asts': player.css("td.assistTotal::text").get(),
                "Rating": player.css("td.rating::text").get()
            }
