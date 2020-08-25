from django.db import models


# Create your models here.
class Todo(models.Model):
    content = models.TextField()


class NBI(models.Model):
    no = models.TextField()
    mda = models.TextField()
    mda_site = models.TextField()
    location = models.TextField()
    district = models.TextField()
    period_of_nbi_extension = models.TextField()
    status = models.TextField()
    internet = models.TextField()
    leased_mda = models.TextField()
    leased_ifms = models.TextField()
    dark_fibre = models.TextField()
    fy_period_of_connectivity = models.TextField()
    date_of_connection_internet_bandwidth = models.TextField()
    date_of_connection_ifms = models.TextField()
    date_of_connection_leased_lines = models.TextField()
    date_of_connection_dark_fibre = models.TextField()
    internet_capacity = models.TextField()
    leased_mda_capacity = models.TextField()
    leased_ifms_capacity = models.TextField()
    dark_fibre_quantity = models.TextField()
    fibre_done = models.TextField()
    odf_installed = models.TextField()
    latitude = models.TextField()
    longitude = models.TextField()
    comments = models.TextField()

    def __str__(self):
        return self.mda_site

    # class MovieInfo_test(models.Model):
    #     movie_test = models.CharField(max_length=200)
    #
    #     def __str__(self):
    #         return self.movie_test
