from django.db import models

class Track(models.Model):
    """
    A single track in an album
    """
    name = models.CharField(max_length=200)
    composer = models.CharField(max_length=200, null=True)
    milliseconds = models.IntegerField('Duration (ms)')
    bytes = models.IntegerField('Size (bytes)')
    unitPrice = models.FloatField('Unit Price (EUR)') 
    # unitPrice: a DecimalField(max_digits=3, decimal_places=2) would also work
    album = models.ForeignKey('Album', on_delete=models.CASCADE)

    def ms_as_mins_secs(self):
        """Human friendly duration label for milliseconds field

        Returns:
            string: 3:40 for a 3 mins 40 secs duration
        """
        minutes = self.milliseconds / 60000
        seconds = (self.milliseconds % 60000) / 1000
        return '%d:%02d' % (minutes, seconds)

    def __str__(self):
        return self.name


class Album(models.Model):
    """
    An album, by a single artist, with several tracks
    """
    title = models.CharField(max_length=200)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Artist(models.Model):
    """
    An artist, that may have many albums
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    