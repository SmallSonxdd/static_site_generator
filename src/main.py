import os
import sys
import shutil
from generate_page import *


def main():
    source_to_destination('static', 'public')
    generate_pages_recursive('content', 'template.html', 'public')

if __name__ == "__main__":
    main()
