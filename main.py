from swapi import swapi


def get_film_info():
    film = swapi.get_film(1)
    print(f"Фільм: {film.title}")


if __name__ == '__main__':
    film_id = input("введіть ідентефікатор фільму: ")
    get_film_info()
