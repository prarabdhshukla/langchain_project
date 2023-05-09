import wikipediaapi


def downloader(pages, generic_pages,file_path):
    wiki=wikipediaapi.Wikipedia(language='en',
                            extract_format=wikipediaapi.ExtractFormat.WIKI)
    print('Downloading Relevant pages......')

    for page in pages:
        page_py=wiki.page(page)
        if page_py.exists():
            page_text=page_py.text
            with open(f'{file_path}/relevant/{page}.txt', 'w') as file:
                file.write(page_text)
        else:
            print(f'Wikipedia Page: {page} not found :( Terminating...')
            return

    print('Downloading generic pages.....')

    for page in generic_pages:
        page_py=wiki.page(page)
        if page_py.exists():
            page_text=page_py.text
            with open(f'{file_path}/generic/{page}.txt', 'w') as file:
                file.write(page_text)
        else:
            print(f'Wikipedia Page: {page} not found :( Terminating...')
            return

    print("Finished downloading pages :) ")
    


if __name__=="__main__":
    pages=['William Shakespeare', 'Life of William Shakespeare','Shakespeare\'s Plays','William Shakespeare\'s collaborations', 'Shakespeare bibliography', 'Shakespeare\'s Sonnets', 'Shakespeare\'s writing style', 'Shakespeare\'s influence', 'Reputation of William Shakespeare', 'Timeline of Shakespeare criticism','Shakespeare authorship question', 'Religious views of William Shakespeare', 'Sexuality of William Shakespeare', 'Merchant of Venice', 'Twelfth Night']

    generic_pages=['Universe', 'Cricket', 'Astrology', 'Hollywood', 'White House']

    file_path='./data'

    downloader(pages,generic_pages,file_path)



