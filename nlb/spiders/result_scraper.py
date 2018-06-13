from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from ..items import NlbItem


class Result_Spider(CrawlSpider):
    name = "results"
    allowed_domains = ["https://www.nlb.lk/"]
    start_urls = [
        'https://www.nlb.lk/results/govisetha',
        'https://www.nlb.lk/results/dhana-nidhanaya',
        'https://www.nlb.lk/results/mega-power',
        'https://www.nlb.lk/results/mahajana-sampatha',
        'https://www.nlb.lk/results/jathika-sampatha',
        'https://www.nlb.lk/results/delakshapathi',
        'https://www.nlb.lk/results/sampath-rekha',
        'https://www.nlb.lk/results/supiri-vasana',
        'https://www.nlb.lk/results/vasana-sampatha',
        'https://www.nlb.lk/results/sevana',
        'https://www.nlb.lk/results/airport-super-draw',
        'https://www.nlb.lk/results/special',
        'https://www.nlb.lk/results/power-lotto',
        'https://www.nlb.lk/results/sevana-scratch-lottery',
        'https://www.nlb.lk/results/samurdhi-scratch-lottery',
        'https://www.nlb.lk/results/dollar-fortune',
        'https://www.nlb.lk/results/double-bonus-',
        'https://www.nlb.lk/results/super-fifty',
        'https://www.nlb.lk/results/manusath-mehewara',
        'https://www.nlb.lk/results/neeroga'
    ]

    def parse(self, response):
        # Extracting the content using css selectors
        Lottery_name = str(response.request.url).split('/')[-1]
        # print(Lottery_name)

        # table = response.css("table[class='w0 tbl']").extract()
        # print(table)
        # for table in response.css("table[class='w0 tbl']")[1:]:
        #     print('new row')
        #     scraped_info = {
        #         'Lottery_name': str(response.request.url).split('/')[-1],
        #         'draw_no': table.css('td:nth-child(1)::text').extract_first(),
        #         'date': table.css('td:nth-child(1)::text').extract_first(),
        #         'result': table.css('td:nth-child(2)::text').extract_first(),
        #     }
        #     print( scraped_info)
        #     # item = NlbItem()
        #     # item['Lottery_name'] =  str(response.request.url).split('/')[-1]
        #     # item['draw_no'] = table.css('td:nth-child(1)::text').extract_first()
        #     # item['date'] = table.css('td:nth-child(1)::text').extract_first()
        #     # item['result'] = table.css('td:nth-child(2)::text').extract_first()
        #     yield scraped_info
        table = response.xpath('//table[@class="w0 tbl"]')
        table_rows = table.xpath('.//tr')
        for row in table_rows[1:-1]:
            tds = row.xpath('.//td//text()')
            index = 0
            draw_no = 0
            date = ''
            result = ''
            for td in tds:
                if index == 0 :
                    draw_no = int(td.extract())
                elif index == 1 :
                    date = str(td.extract())
                elif index != len(tds)-1:
                    # print(td.extract())
                    result+=td.extract()+' '
                index+=1

            scraped_info = {
                'Lottery_name': str(response.request.url).split('/')[-1],
                'draw_no': draw_no,
                'date': date,
                'result': result,
            }
            # print( scraped_info)
            # item = NlbItem()
            # item['Lottery_name'] =  str(response.request.url).split('/')[-1]
            # item['draw_no'] = table.css('td:nth-child(1)::text').extract_first()
            # item['date'] = table.css('td:nth-child(1)::text').extract_first()
            # item['result'] = table.css('td:nth-child(2)::text').extract_first()
            yield scraped_info