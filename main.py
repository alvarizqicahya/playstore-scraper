from google_play_scraper import app, Sort, reviews_all
import csv


class App:
    reviews = []

    def __init__(self, appName, language, country, fileName):
        self.appName = appName
        self.language = language
        self.country = country
        self.fileName = fileName

    def appDetail(self):
        details = app(
            self.appName,
            lang=self.language,
            country=self.country
        )

        del details['comments']

        print('\n-----detail-----')

        for d in details:
            print('{}: {}'.format(d, details[d]))

    def appReview(self):
        review = reviews_all(
            self.appName,
            lang=self.language,
            country=self.country,
            sleep_milliseconds=0,
            sort=Sort.MOST_RELEVANT,
            filter_score_with=None
        )

        print('\n-----ulasan-----')

        for rev in review:
            nama = rev['userName']
            tanggal = rev['at']
            skor = rev['score']
            komentar = rev['content']

            self.reviews.append([nama, tanggal, skor, komentar])

            print('Nama: {}\nTanggal: {}\nSkor: {}\nKomentar: {}\n'.format(
                nama, tanggal, skor, komentar))

    def writeCsv(self):
        csv_file = open(self.fileName+'.csv', 'w')
        csv_write = csv.writer(csv_file)
        csv_write.writerow(['nama', 'tanggal', 'skor', 'komentar'])

        for rev in self.reviews:
            csv_write.writerow([rev[i] for i in range(4)])

            
if __name__ == '__main__':
    #app_id, language, country, file_name
    a = App('com.baraciptalaksana.espktkdrkotv2',
            'id', 'id', 'espkt_polres_kediri')
    a.appDetail()
    a.appReview()
    a.writeCsv()
