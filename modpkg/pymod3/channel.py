from channeltype.movies import *

# import channeltype.movies
# with this channeltype.movies.Movie will work

#from channeltype import movies
# with this movies.Movie will work
# from channeltype.movies import Movie


class TopLevelClass:

    def toplevelmethod(self):
        print('From the top level class')

# mv1 and mv2 are class level variables- can be referred using the class name
    mv1 = Movie('The Hateful Eight',
                ['Samuel Jackson', 'Kurt Russel',
                 'Jennifer Jason Leigh'], 234000, 350)

    mv2 = Movie('The Man Who Knew Infinity',
                ['Dev Patel', 'Jeremy Irons'], 110000, 320)

    def printMovieCollections(self):
        print(self.mv1.movieCollections())
        print(self.mv2.movieCollections())

    def printMovieCast(self):
        print('The lead cast for ' +
              TopLevelClass.mv1.movie_title + ' is ' +
              str(self.mv1.movie_cast))
        print('The lead cast for ' +
              TopLevelClass.mv2.movie_title + ' is ' +
              str(self.mv2.movie_cast))


def main():
    atlc = TopLevelClass()
    atlc.printMovieCollections()
    atlc.printMovieCast()
    atlc.toplevelmethod()


if __name__ == '__main__':
    main()
