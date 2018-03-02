from googletrans import Translator
from six.moves import reload_module
import csv
import io
import sys
reload_module(sys)

datafile = 'raw_in.csv'
translator = Translator()


# put your value from which to start
min = 0


if __name__ == '__main__':

    with open('error_log.txt', 'w') as logfile:
        errorWriter = csv.writer(logfile)
        with open(min.__str__() + '_{}_facebook_statuses.csv'.format("translated"), 'w') as file:
            w = csv.writer(file)
            with io.open(datafile, 'r', encoding='utf8') as csvfile:
                reader = csv.reader((line.replace('\0','') for line in csvfile),csvfile,delimiter=",")
                for i, row in enumerate(reader):
                    if i < min:
                        continue
                    try:
                        print("Translating line " + i.__str__() + ' len: ' + row[1].__len__().__str__())
                        tr = translator.translate(text=row[1], dest='En')
                        data = [row[0], tr, row[2]]
                        w.writerow(data)
                    except Exception as error:
                        print("ERROR: in line " + i.__str__() + ': ' + error.__str__())
                        errorWriter.writerow(row)
                        continue
                        # make #continue and uncomment raise to translate in portion
                        # raise
