class Musica:

    def __init__(self, titulo, artista, album, nroFaixa):
        self.__titulo = titulo
        self.__artista = artista
        self.__album = album
        self.__nroFaixa = nroFaixa

        artista.addMusica(self)

    def getTitulo(self):
        return self.__titulo

    def getArtista(self):
        return self.__artista

    def getAlbum(self):
        return self.__album

    def getNroFaixa(self):
        return self.__nroFaixa

class Album:

    def __init__(self, titulo, artista, ano):
        self.__titulo = titulo
        self.__artista = artista
        self.__ano = ano

        self.__faixas = []

        artista.addAlbum(self)

    def getTitulo(self):
        return self.__titulo

    def getArtista(self):
        return self.__artista

    def getAno(self):
        return self.__ano

    def getFaixas(self):
        return self.__faixas

    def addFaixa(self, titulo, artista=None):
        if artista is None:
            artista = self.__artista
        nroFaixa = len(self.__faixas)
        musica = Musica(titulo, artista, self, nroFaixa)
        self.__faixas.append(musica)

class Artista:

    def __init__(self, nome):
        self.__nome = nome

        self.__albuns = []
        self.__musicas = []

    def getNome(self):
        return self.__nome

    def getAlbuns(self):
        return self.__albuns

    def getMusicas(self):
        return self.__musicas

    def addAlbum(self, album):
        self.__albuns.append(album)

    def addMusica(self, musica):
        self.__musicas.append(musica)

class Playlist:

    def __init__(self, nome):
        self.__nome = nome

        self.__musicas = []

    def getNome(self):
        return self.__nome

    def getMusicas(self):
        return self.__musicas

    def addMusica(self, musica):
        self.__musicas.append(musica)    

art1 = Artista('Coldplay')
album1 = Album('Mylo Xyloto', art1, 2011)
album1.addFaixa('Paradise')
album1.addFaixa('Hurts Like Heaven')
album1.addFaixa('Charlie Brown')

playlist1 = Playlist('pl-Coldplay')

for musica in album1.getFaixas():
    playlist1.addMusica(musica)

for musica in playlist1.getMusicas():
    print (musica.getTitulo())

for album in art1.getAlbuns():
    print (album.getTitulo())