# Get CSV from Url and write to local file.
# @author Matthieu SCARSET
# @see https://matthieuscarset.com
import os
import sys

import requests

url = 'https://www.data.gouv.fr/fr/datasets/r/4388ede9-aa01-4942-a3cf-cf88dd024d4a'

def main():
    try:
        # Get and write data.
        f = open('data.csv', 'w')
        r = requests.get(url)
        d = r.content.decode(r.encoding)
        f.write(d)
    except:
      print("Unexpected error:", sys.exc_info()[0])
      raise
    finally:
        # Read your file now.
        f = open('data.csv', 'r')
        print(f)
        print('Done: %s' % (os.getcwd() + '/' + __file__))


if __name__ == "__main__":
    main()
