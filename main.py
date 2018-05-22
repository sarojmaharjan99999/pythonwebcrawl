import crawlUrlLibrary
import fileHandlerLibrary
import emailLibrary
import json
import schedule
import time


class MainClass:
    def __init__(self):
        self.file_name = 'movieDataStorage'
        crawl_cinema = crawlUrlLibrary.CrawlCinema()
        crawl_data_object = crawl_cinema.trade_spider()
        file_handler = fileHandlerLibrary.FileHaldler(self.file_name)
        file_data_object = file_handler.open_file()

        if type(file_data_object) is str:
            file_data_object = json.loads(file_data_object)
            #file_data_object = {'3D: Avengers: Infinity War': True, 'Damaru Ko Dandibiyo': True, 'Kohalpur Express': True, 'Shatru Gate': True, '3D: Rampage': True, 'Avengers: Infinity War': True, 'Lamphoo': True, 'Raazi': True, 'The Past': True, 'To Kill a Mockingbird': True, 'Deadpool 2': False}

        for key, value in file_data_object.items():
            if crawl_data_object.get(key) == value:
                pass
            else:
                print('break')
                if crawl_data_object.get(key) is None:
                    file_handler = fileHandlerLibrary.FileHaldler(self.file_name)
                    file_handler.file_fill(json.dumps(crawl_data_object))
                    break
                else:
                    email_library = emailLibrary.EmailLibrary(key)
                    email_library.send_email()
                    file_handler = fileHandlerLibrary.FileHaldler(self.file_name)
                    file_handler.file_fill(json.dumps(crawl_data_object))
                    break


schedule.every(5).seconds.do(MainClass)


while True:
    schedule.run_pending()
    time.sleep(1)


